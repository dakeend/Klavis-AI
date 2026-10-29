# SOLUTION SUMMARY — completed flow run receives unresponsive-run action

## Diagnosis

The supplied incident is a proactive ("unresponsive run") automation:

- `after`: `prefect.flow-run.heartbeat`
- `expect`: `prefect.flow-run.*`
- `for_each`: `prefect.resource.id`, `threshold`: 1, `within`: 90 s

Recorded events (occurred times):

| # | event | occurred | received |
|---|-------|----------|----------|
| 1 | `prefect.flow-run.heartbeat` | 12:00:00 | +0.1 s |
| 2 | `prefect.flow-run.heartbeat` | 12:00:30 | +30.1 s |
| 3 | `prefect.flow-run.Completed` | 12:01:00 | +60.1 s |
| 4 | `prefect.flow-run.heartbeat` | 12:01:00 | +60.2 s |

The final proactive evaluation runs at +151 s and must produce zero actions.

The root causes are all in `src/prefect/server/events/triggers.py`:

1. **`ensure_bucket` discarded the satisfying event.** On every `after` event it
   overwrote the bucket's `last_event` with the incoming event before `evaluate`
   ran. By the time evaluation started, the `Completed` event that had just
   satisfied the window was no longer available for comparison.
2. **The proactive "same event in after and expect" special case re-armed
   unconditionally.** When a proactive bucket had reached its threshold, any
   event matching both `after` and `expect` removed the bucket and started a new
   window at `triggering_event.occurred`. The racing heartbeat (occurred
   12:01:00, not newer than the `Completed` event at 12:01:00) therefore reset
   the window to 12:01:00–12:02:30 with count 0. The proactive evaluation at
   12:02:31 then saw an expired window with no expected events and fired.
   `increment_bucket` could also move `last_event` backwards for out-of-order
   events, so comparisons could be anchored to an old event.
3. **The only persisted record of "this window was satisfied" was the bucket
   itself.** `remove_buckets_exceeding_threshold` deletes satisfied buckets on
   the next periodic proactive pass (the server runs one every 5 s). If that
   pass happens between the `Completed` event and the racing heartbeat, the
   bucket is gone and the heartbeat creates a brand-new window — the same false
   positive one tick later. Any fix that relies only on bucket state is
   therefore incomplete in a real deployment.

Baseline reproduction (`incident-observed.log`) showed `observed_actions: 1`.
The captured log confirmed the fired bucket had `start = 12:01:00` (the racing
heartbeat) and `count = 0`, i.e. the window had been re-armed by the heartbeat
after the terminal event.

## Repair

### 1. Persisted per-resource event watermark (primary fix)

A new internal model/table `automation_trigger_watermark` stores, per
`(automation_id, trigger_id, bucketing_key)`, the greatest event `occurred`
processed so far.

- ORM model: `AutomationTriggerWatermark` in
  `src/prefect/server/database/orm_models.py`, exposed as
  `db.AutomationTriggerWatermark` in `database/interface.py`.
- Migrations (additive only, existing tables/data untouched):
  - `.../migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py`
  - `.../migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py`
- `read_trigger_watermark`, `record_trigger_watermark`, and
  `sweep_expired_trigger_watermarks` in `triggers.py`. The watermark is
  upserted with an atomic `CASE … WHEN last_event_occurred < new` so older or
  out-of-order events can never lower it (works on SQLite and PostgreSQL; the
  same `on_conflict_do_update` construct already used for buckets).
- `reactive_evaluation` now, for proactive triggers with `after`:
  - records every covered event's occurrence, and
  - skips an `after` event that is **not strictly newer** than the watermark
    when it would either arm a *new* bucket or (for an after-only event)
    replace the bucket's `last_event`.
  This check does not depend on a bucket existing, so it still holds after
  eager/proactive bucket cleanup (the production race above) and after a
  server restart.
- `periodic_evaluation` sweeps watermarks untouched for
  `AUTOMATION_WATERMARK_RETENTION` (= `SEEN_EXPIRATION`, 30 minutes, the same
  horizon over which the triggers consumer remembers processed events), so
  storage stays bounded.

Only proactive triggers with `after` participate; reactive triggers and
triggers without `after` keep their previous event handling exactly.

### 2. Bucket-level hardening (defense in depth)

- `ensure_bucket` no longer overwrites `last_event` for events matching
  `expect`; those are recorded by `evaluate` after comparison.
- `increment_bucket` only advances `last_event` when the new event is newer,
  so counts still include out-of-order events but the "latest contributing
  event" never moves backwards.
- `evaluate`'s proactive re-arm special case now requires the triggering event
  to be strictly newer than `last_event`. This protects long-lived buckets
  (for example when a watermark row has already been swept) and keeps the
  correct `triggering_event` for a legitimate firing.

No thresholds, actions, public interfaces, or transaction/ locking behaviour
were changed.

### 3. Regression tests

`tests/events/server/triggers/test_incident_regressions.py` adds 8 tests:

- completed run + late heartbeat does not fire (the incident);
- a completion arriving before any bucket exists still suppresses the race;
- out-of-order heartbeats do not walk the watermark backwards;
- a genuinely unresponsive run still fires, and the `Firing` carries the
  correct `triggering_labels` (`prefect.resource.id`) and the latest heartbeat
  as `triggering_event`;
- a periodic proactive cleanup between the completion and the late heartbeat
  does not resurrect the window;
- a server restart (in-memory reset + reload) after bucket cleanup stays silent;
- watermarks are swept after the retention window (bounded storage);
- newer activity after a completion (`Running` + heartbeat) still re-arms and
  fires normally.

The provided `test_incident_completed_run.py` is unchanged.

## Commands actually executed and results

All Python commands used the locked interpreter
`$SANDBOX/.runtime/venv/Scripts/python.exe` from the
repository root (`prefect/`).

| Command | Result |
|---------|--------|
| `pytest tests/events/server/triggers/test_incident_completed_run.py -q -s` (before fix) | **FAILED**: `observed_actions: 1`, expected 0; fired bucket started at 12:01:00 with count 0 |
| same command, after fix | **1 passed**, `observed_actions: 0` |
| `pytest tests/events/server/triggers/ -q -p no:randomly` | **125 passed, 3 known xfail** (on the final run: 2 xfailed + 1 xpassed; the composite-trigger xfails are non-strict and intermittently xpass in this environment) |
| `pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly` | **8 passed** |
| `pytest tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations -q` | **2 passed** (one head per dialect) |
| standalone Alembic check on a fresh SQLite DB: upgrade head → inspect → downgrade -1 → upgrade | table, columns, unique index, `updated` index and CASCADE FK created; downgrade removed it; re-upgrade recreated it |
| standalone `PrefectDBInterface.drop_db()` → `create_db()` on a migrated SQLite DB | all tables dropped, then migrations recreated every table including `automation_trigger_watermark` |
| Alembic `compare_metadata` of ORM metadata vs. migration-built SQLite schema | no differences involving the new table |
| `pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py tests/events/server/models tests/events/server/test_in_memory_ordering.py tests/events/server/test_db_ordering.py -q` | 132 passed, 1 skipped, 1 failed: `test_read_automations_page` |
| `ruff format --check` on all changed files | clean |

The `test_read_automations_page` failure is unrelated to this change and
pre-existing in this environment: all four fixture automations are inserted
with the *same* `updated` timestamp, so `ORDER BY updated DESC` is a tie and
returns an arbitrary order. A debug run confirmed all four rows share
`updated = 2026-10-29 04:26:26.085167+00:00`; nothing in the repair touches
automation rows or that API path.

## Limits / notes

- PostgreSQL was not available in this environment, so the PostgreSQL migration
  was not executed against a live server. It mirrors the existing
  `automation_bucket` migration idioms (UUID/JSON/Timestamp types, conflict
  target on the unique index, `sa.case` upsert), and the per-dialect
  single-head migration test passes.
- Tests that invoke Alembic **from inside the pytest process**
  (`test_orion_full_migration_works_with_data_in_db`,
  `test_drop_db_removes_all_tables`) hang in this Windows environment inside
  `alembic_upgrade` (killed after several minutes). This is an
  environment/anyio limitation of running Alembic in-process here, not the
  migration content: the same upgrade runs fine during normal session setup
  (the whole triggers suite, including the new migration, passes), and the
  standalone-process checks below succeed. `drop_db`/`create_db` was also
  verified directly against the new table (drop removes every table, create
  re-runs migrations and recreates `automation_trigger_watermark`).
- Storage bound: one small watermark row per active trigger/bucketing key,
  removed after 30 minutes of inactivity; existing automation buckets are
  still swept as before.
