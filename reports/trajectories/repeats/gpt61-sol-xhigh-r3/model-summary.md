# Completed-run automation repair

## Diagnosis

The incident reproduced on the original source: one unresponsive-run action,
where zero were expected. A heartbeat matching both `after` and `expect` could
restart a proactive bucket even when a later (or simultaneous) expected-only
event had satisfied it. `ensure_bucket` also overwrote `last_event` before the
evaluator rejected an older event. Deleting satisfied buckets discarded the
remaining ordering evidence, allowing the same problem after periodic evaluation
or a server restart.

## Repair

Implemented a durable satisfied-window watermark scoped by automation, trigger,
and bucketing key. Starting events at or before the watermark cannot rearm the
window. Closing events win timestamp ties. Out-of-order events still contribute
to higher thresholds, while restarts and action context use the newest relevant
event. The proactive action path rechecks the persisted watermark before acting.

SQLite and PostgreSQL have additive, reversible migrations for the new table.
Existing automations and buckets remain intact. Existing satisfied buckets seed
watermarks before either proactive or periodic cleanup removes them. There is
one row per key; expiry is indexed and normal periodic cleanup removes old rows.
Retention covers the trigger window plus the existing 15-minute causal-ordering
lookback, measured from the later closing-event occurrence/receipt time, plus
the normal expired-bucket cleanup buffer. Automation deletion cascades to its
watermarks.

Public schemas, monitoring thresholds, configured actions, and deployment
concurrency implementation were not changed. Source changes are under `prefect/`;
`prefect/MIGRATION-NOTES.md` describes the schema addition.

## Verification actually performed

All Python commands used the isolated runtime by first sourcing
`. ../.runtime/environment.ps1` from `prefect/`, then invoking `$TrialPython`.

Initial reproducer (failed with one action before the repair):

```powershell
& $TrialPython -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s
```

Regression tests were observed failing before their corresponding repairs:
9 initial ordering/context failures, 3 persisted higher-threshold failures, and
the legacy-bucket periodic-cleanup failure.

Final trigger verification:

```powershell
$env:PREFECT_UNIT_TEST_LOOP_DEBUG = 'false'
& $TrialPython -u -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_proactive_event_ordering.py tests/events/server/triggers/test_regressions.py tests/events/server/triggers/test_basics.py tests/events/server/triggers/test_flow_run_slas.py -q -s --tb=short --log-cli-level=ERROR
```

**78 passed in 55.68 seconds.** This includes zero actions for the incident,
genuine unresponsive-run actions with correct resource/event information,
restart persistence, event ordering, threshold handling, bounded cleanup, and
existing trigger/SLA behavior.

```powershell
& $TrialPython -u -m pytest tests/server/database/test_automation_bucket_watermark_migration.py tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations -q -s --tb=short --log-cli-level=ERROR
```

**3 passed in 23.90 seconds.** This exercises a real SQLite downgrade/upgrade with
pre-existing automation/bucket data and validates a single migration head for
both database dialects.

Ruff full checks passed for all five added Python files. On all eight changed
Python files, `ruff check --select E4,E7,E9,F,I` and `ruff format --check` passed.
Unrestricted Ruff checks on the existing modules reported legacy lint findings.

## Limits

No PostgreSQL service was available, so PostgreSQL execution was not verified.
The complete repository suite was not run. An exploratory wider run completed
81 tests without an assertion failure before timing out in an older migration;
some captured-output runs also timed out in hosted-API setup. The final isolated,
uncaptured commands above completed successfully. Ordering history is deliberately
finite: after watermark expiry and cleanup, arbitrarily old distinct events do
not retain indefinite completion history.
