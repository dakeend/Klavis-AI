# Completed-run monitoring repair

## Diagnosis

The supplied replay originally emitted one unresponsive-run action instead of
zero. A completion increments and satisfies the open proactive bucket. A
subsequently delivered heartbeat, with the same or an earlier event timestamp,
can then reset that satisfied bucket to an empty window. Periodic evaluation
later acts on that window. Removing satisfied buckets also discards the only
record that an earlier starting event has already been satisfied.

Separately, `ensure_bucket` overwrote `last_event` even when evaluation rejected
an old event. A legitimate later action could therefore identify the wrong
triggering event.

## Repair

- Added a durable watermark scoped by automation, trigger and bucketing key.
  An expect-only event that satisfies the threshold prevents equal-time or older
  starts from creating or restarting a monitoring window. Newer starts remain
  eligible. Multi-event thresholds still require their configured event count.
- The watermark upsert acquires the write lock before reading bucket state,
  serializing consumers for the same key without introducing a global lock.
- Watermarks survive bucket retirement and in-memory service resets. Existing
  satisfied buckets seed their watermark before proactive or periodic retirement,
  preserving information across upgrades.
- Added additive SQLite and PostgreSQL migrations. Existing automation and bucket
  tables are untouched. One row per key is retained for the trigger window plus
  the existing 15-minute causal-ordering lookback, then removed by the periodic
  sweep; automation deletion also removes its rows.
- Bucket creation no longer overwrites an existing bucket's event, and increments
  retain the latest event metadata. Public trigger/action schemas, monitoring
  thresholds, and deployment-concurrency implementation are unchanged.

## Commands and results

All commands ran from
`$SANDBOX/prefect`.
Every Python command first dot-sourced `../.runtime/environment.ps1` and used
`$TrialPython`. Database, temporary, home and cache state stayed in this trial's
`.runtime` directory. Output redirection is omitted below for readability.

1. Baseline incident:
   `& $TrialPython -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`
   — **1 failed**, observed actions **1**.
2. New ordering tests against the original implementation:
   `& $TrialPython -m pytest tests/events/server/triggers/test_proactive_event_ordering.py -q --tb=short`
   — **6 failed, 1 passed**. This demonstrated delivery-order, restart and
   triggering-event metadata failures before the repair.
3. Initial repair:
   `& $TrialPython -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_proactive_event_ordering.py -q --tb=short`
   — **8 passed** after correcting a timezone-binding issue exposed by the frozen
   test clock. The repair uses the existing datetime compatibility helper.
4. Additional upgrade-retirement coverage initially produced **1 failed,
   9 passed**; preserving legacy bucket state in the periodic sweep repaired it.
   A later threshold compatibility test initially produced **1 failed,
   2 passed**; threshold-aware watermark advancement repaired that case.
5. Full trigger suite, before the final multi-event-threshold refinement:
   `& $TrialPython -m pytest tests/events/server/triggers -q --tb=short`
   — **127 passed, 2 xfailed, 1 xpassed** in 397.37 seconds.
   Log: `.runtime/trigger-suite.log`.
6. Final regression batch:

   ```powershell
   & $TrialPython -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_proactive_event_ordering.py tests/events/server/triggers/test_regressions.py tests/server/database/test_migrations.py::test_automation_event_watermark_migration_preserves_existing_data tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations tests/events/server/models/test_automations.py tests/server/orchestration/test_validate_deployment_concurrency_at_running.py -q --tb=short
   ```

   — **71 passed, 5 xfailed** in 228.03 seconds. Includes all 13 new ordering,
   retention, threshold and restart cases; SQLite downgrade/upgrade with existing
   automation/bucket data; both migration-chain heads; automation models; and
   deployment-concurrency regressions. Log: `.runtime/final-regressions.log`.
7. Final supplied incident replay, same command as step 1:
   — **1 passed** in 27.56 seconds; printed
   `{"observed_actions": 0, "expected_actions": 0}`.
   Log: `.runtime/incident-repaired.log`.
8. PostgreSQL migration was executed through Alembic's offline PostgreSQL
   `MigrationContext` and `Operations` to compile both upgrade and downgrade.
   Assertions checked table creation, JSONB, cascade deletion, the unique scope
   index and table removal. Result: **passed**. Generated SQL:
   `.runtime/postgresql-watermark.sql`.
9. On the eight changed Python files,
   `& $TrialPython -m ruff check --select E4,E7,E9,F,I <files>` and
   `& $TrialPython -m ruff format --check <files>` — **passed**, all eight files
   formatted. Unfiltered Ruff reports **175 diagnostics** in existing portions
   of the touched files; these unrelated legacy style findings were not rewritten.
   Full diagnostics: `.runtime/lint-full.json`.

## Limits

PostgreSQL DDL and migration-chain structure were verified without a live
PostgreSQL service; runtime database tests used SQLite. The full repository
suite and TLA+ model were not run. The deployment-concurrency implementation and
its mapped protocol were not modified. Existing expected failures were retained.

Watermarks deliberately provide bounded ordering history using the existing
lookback horizon; they are not an indefinite event archive. Previously discarded
completion information from an already-corrupted old bucket cannot be
reconstructed by this additive schema migration.
