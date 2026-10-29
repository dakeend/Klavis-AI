# Completed-run automation repair

The supplied incident reproduced one action instead of zero. Its completion event
satisfied the proactive bucket, but a heartbeat with the same occurrence time then
incremented and restarted that bucket with count zero. Periodic removal of satisfied
buckets also erased the only evidence that a delayed heartbeat was obsolete.
`ensure_bucket` could replace `last_event` before an old event was rejected, causing
incorrect metadata on a legitimate timeout action.

The repair retains ordering state per automation, trigger and bucketing key in a new
`automation_bucket_state` table. Expect-only events take precedence over starting
events at the same or an earlier occurrence time. Later starting events still open
new monitoring windows. Counts for thresholds greater than one remain meaningful,
and stale events cannot replace the firing event. No flow-state names, monitoring
thresholds or action types are hard-coded or disabled.

State and bucket changes share database transactions and per-key write locks.
SQLite uses its supported immediate writer transaction; PostgreSQL uses the same
upsert protocol with row locks. Deployment concurrency code is unchanged.

Both database dialects have additive, reversible migrations. Existing automations
and buckets are preserved, and ordering information is recovered lazily from
pre-upgrade fulfilled buckets before removal. State is bounded to one row per recent
key and retained through its trigger window plus the existing ordering lookback
and bucket buffer. The periodic sweep prunes idle state and stores one monotonic
cutoff in Configuration, preventing very old starting events from resurrecting
expired windows after their per-key records have been pruned.

## Verification

All Python commands used `. ../.runtime/environment.ps1` from `prefect/` and
`& $TrialPython`, with the isolated SQLite database and test-generated homes.

- Baseline: `-m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`
  failed with `observed_actions: 1` and `expected_actions: 0`.
- Before implementation: `-m pytest tests/events/server/triggers/test_proactive_event_ordering.py -q --tb=short`
  produced 9 failures and 2 passes, including stale-start resurrection and incorrect
  triggering-event metadata.
- The initial broader trigger run produced 131 passes, 3 expected failures and one
  failing newly added higher-threshold test. That test now supplies its threshold in
  the persisted automation configuration rather than mutating an already loaded
  object.
- A focused sweep regression also demonstrated resurrection after ordering-state
  pruning; this motivated the durable sweep cutoff. Intermediate retention tests
  exposed Pendulum/ZoneInfo arithmetic dropping a timezone, fixed by normalizing
  through Prefect's datetime compatibility helper.
- `-m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_proactive_event_ordering.py -q -x --tb=short`
  passed 17 tests before the final concurrency regression was added.
- `-m pytest tests/server/database/test_migrations.py -q -k single_head --tb=short`
  passed 2 tests, covering both migration graphs.
- The changed Python files pass Ruff's `E4,E7,E9,F,I` checks and formatting checks.
  The new regression file and both migration files also pass the full default
  Ruff checks. A full default Ruff check of existing large source files reports
  pre-existing modernization/style findings; these unrelated files were not
  broadly rewritten.
- Final broad verification:
  `-m pytest tests/events/server/triggers tests/events/server/models/test_automations.py -q -n4 --tb=short`
  completed successfully: **166 passed, 2 xfailed, 1 xpassed** in 243.12 seconds.
  This includes the final concurrent-evaluation regression, pruning protection,
  long-window retention, action metadata, and SQLite upgrade preservation.
- Final standalone incident replay, using the original requested command,
  passed in 24.64 seconds and printed `observed_actions: 0`, `expected_actions: 0`.

## Limits

Verification uses real SQLite evaluation and migration paths, including a
downgrade/upgrade preserving an existing automation and completed bucket. PostgreSQL
migration graph validation is included, but no live PostgreSQL service was used.
An intermediate parallel run of an older implementation was interrupted after
worker termination; it is not reported as a successful suite run. No UI build,
external action execution, real flow worker, or external service was required.
An overlapping focused invocation timed out during hosted-API fixture setup before
running its tests; the final broad run above completed the same regressions.
