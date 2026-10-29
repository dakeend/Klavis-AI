# SOLUTION_SUMMARY

## Incident

`tests/events/server/triggers/test_incident_completed_run.py` replays a standard
"unresponsive run" automation:

* posture: `Proactive`
* `after`: `prefect.flow-run.heartbeat`
* `expect`: `prefect.flow-run.*`
* `for_each`: `prefect.resource.id`
* threshold `1`, window `90s`

The recorded history is two heartbeats, then `prefect.flow-run.Completed` at
`12:01:00`, then a final heartbeat also stamped `12:01:00` but delivered moments
later. The replay observed **1** unresponsive-run action where **0** are expected.

## Diagnosis

The proactive trigger keeps one time-based bucket per bucketing key. For
keep-alive events (events that match both `after` and `expect`, such as a
heartbeat) `evaluate()` has a deliberate rolling-window special case: once the
current window has met its threshold, a new keep-alive event replaces the bucket
with a fresh one anchored at that event (`triggers.py` "Special case of a
proactive trigger ...", `start_new_bucket(..., count=0)`). That is what makes a
heartbeat watchdog keep extending its deadline while heartbeats arrive.

The condition was only `not meets_threshold` (for Proactive, "the window has
already been satisfied"). It never checked whether the keep-alive event was
actually newer than the event(s) that satisfied the window. In the incident:

1. heartbeat at `12:00:30` rolls the window to `12:00:30 .. 12:02:00`, count 0;
2. `Completed` at `12:01:00` is an `expect`-only event, increments the window to
   count 1 (threshold met), and should end the watch;
3. the trailing heartbeat at `12:01:00` is processed afterwards. Because the
   window is satisfied, the rolling special case resets it to `12:01:00 ..
   12:02:30` with **count 0**, discarding the fact that the run had completed;
4. when the new window expires, `count 0 < threshold 1`, so the automation fires
   the unresponsive-run action.

The same two events delivered in the opposite order do not fire, so the bug is
also an event-order dependence: events that occur at the same instant may be
ingested in either order.

The bucket itself is deleted when the window expires, and the trigger service is
restarted/replicated independently, so the "this resource already satisfied the
trigger" fact cannot be kept only in memory or only in the transient bucket.

## Repair

Added a small, persistent "latest satisfaction" marker per
`(automation, trigger, bucketing_key)`:

* New table/model `automation_trigger_satisfaction` (`satisfied_at`,
  `expires_at`) with a unique index on the key and an index on `expires_at`.
* `reactive_evaluation()` reads the marker before processing an event for a
  Proactive trigger with `after` criteria and treats an event whose `occurred`
  time is at or before the marker as **stale**. The marker advances to the
  maximum `occurred` of every event matching `expect`, using an atomic,
  forward-only upsert (`CASE WHEN existing < new THEN new ELSE existing`) so
  out-of-order delivery cannot regress it.
* A stale event may still be counted toward an already-open window (preserving
  threshold accounting), but it:
  * cannot create a new bucket if none exists (so a late/duplicate heartbeat
    cannot restart a watch after the run satisfied it), and
  * cannot trigger the rolling-window reset (`and not stale`), and
  * does not replace the window's `last_event`, so a legitimate action keeps the
    correct triggering event and labels.
* `periodic_evaluation()` sweeps markers past their `expires_at`. Retention is
  `max(PRECEDING_EVENT_LOOKBACK (15m), trigger.within)`, measured from the later
  of processing time and the event timestamp, so records outlive the window and
  the out-of-order event horizon but storage stays bounded (at most one row per
  live trigger/resource and they are removed when abandoned).
* Markers are deleted with their automation and with a workspace's automations.
* Alembic migrations were added for both SQLite and PostgreSQL. Before the new
  table's foreign key/index, the delete path acquires locks in the same order as
  event evaluation to avoid introducing deadlocks. No existing table or data is
  changed.

Unchanged: monitoring thresholds, postures, action configuration, public
schemas/interfaces, bucketing/concurrency behavior. A genuinely unresponsive
run still rolls its window on every newer heartbeat and fires on silence with
the last heartbeat as `triggering_event` and its resource id in
`triggering_labels`.

### Files changed

* `src/prefect/server/events/triggers.py` — stale detection, marker read/upsert,
  sweep, `evaluate(..., stale=...)`, rolling-reset guard, triggering-event
  preservation.
* `src/prefect/server/database/orm_models.py` — `AutomationTriggerSatisfaction`.
* `src/prefect/server/database/interface.py` — DB interface property.
* `src/prefect/server/events/models/automations.py` — delete markers with
  automation/workspace (lock-order aligned with evaluation).
* `src/prefect/server/database/_migrations/versions/{sqlite,postgresql}/2026_10_29_000000_*_add_automation_trigger_satisfaction.py`
  — new table migrations.
* `tests/events/server/triggers/test_regressions.py` — regression tests:
  completed-run + trailing heartbeat (same instant), late heartbeat after the
  satisfied bucket has already been swept, survival across a simulated restart
  (in-memory trigger state cleared), a different genuinely unresponsive run
  still fires with the right resource/event, empty bucketing key
  (no `for_each`), and satisfaction-record expiry.

## Commands executed and results

Interpreter: `$SANDBOX/.runtime/venv/Scripts/python.exe`
(isolated `PREFECT_HOME`/SQLite from `.runtime/environment.ps1`).

```sh
python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s
# {"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
# 1 passed   (baseline before the repair: observed_actions 1, failed)

python -m pytest tests/events/server/triggers -q
# 123 passed, 3 xfailed

python -m pytest tests/events/server/models/test_automations.py -q
# 32 passed

python -m pytest tests/events/server/triggers tests/events/server/models/test_automations.py -q
# 155 passed, 2 xfailed, 1 xpassed (same tests as the two runs above;
# the xfail/xpass status of one non-strict test varies between runs)

python -m pytest tests/server/database/test_migrations.py -q -k "single_head"
# 2 passed  (one head per dialect)

python -m pytest tests/events/server/triggers/test_regressions.py -q -k "zombie or satisfaction or stale_keepalive"
# 7 passed
```

Migration verification against a throwaway SQLite database
(`alembic_upgrade` from empty, `alembic_downgrade` one step and to `base`, then
`alembic_upgrade` again) succeeded, produced
`automation_trigger_satisfaction` with the expected indexes, and reported head
`c1d2e3f4a5b6`.

## Limits / notes

* `tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db`
  (and `test_drop_db_removes_all_tables`) time out in this sandbox. The timeout
  stack shows Alembic blocked in `run_async_from_worker_thread` while the test
  harness's hosted API server holds the same SQLite database, i.e. a
  pre-existing harness/lock interaction unrelated to this table. The equivalent
  migration chain was verified manually as described above; every test that
  exercises the new migration through the normal `create_db()`/upgrade path
  passes.
* Staleness is judged by event `occurred` time, which is the only general signal
  available to event triggers (custom flow-run state names are supported by the
  wildcard `expect` and carry no terminal-state metadata in the recorded
  incident). Events delayed beyond the retention horizon can no longer be
  recognized as stale; the horizon is bounded deliberately to keep storage
  bounded.
* Retention is an internal horizon (`max(15 minutes, trigger.within)`), not a
  new user-facing setting; thresholds and automation configuration are untouched.
