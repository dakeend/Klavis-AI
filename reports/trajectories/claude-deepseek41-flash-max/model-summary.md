# Solution summary: completed flow runs receive unresponsive-run actions

## Diagnosis

Reproduction before the repair:

```
python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s
...
{"incident_id": "completed-run-001", "observed_actions": 1, "expected_actions": 0}
AssertionError: Completed run received 1 unresponsive-run action(s); expected zero
```

Root cause is in the proactive-trigger bucket evaluation in
`prefect/src/prefect/server/events/triggers.py`.

For a proactive trigger whose `after` event also matches `expect` (the flow-run
heartbeat / unresponsive-run configuration), `evaluate()` has a special case: once a
bucket has reached its threshold (`not meets_threshold`, i.e. enough expected events
were seen), a further arming event removes the bucket and starts a fresh window at
that event's `occurred` time with `count=0` (the code around the "Special case of a
proactive trigger for which the same event satisfies both `after` and `expect`"
comment).

In the incident the recorded events are:

* heartbeat at 12:00:00
* heartbeat at 12:00:30
* `prefect.flow-run.Completed` at 12:01:00 (received first)
* heartbeat at 12:01:00 (received second, same `occurred` timestamp)

The completion event satisfies the 90 s window opened by the 12:00:30 heartbeat
(count becomes 1, the threshold). Then the final heartbeat, which carries the *same*
`occurred` timestamp but is received after the completion, hits the special case and
restarts the window at 12:01:00 with `count=0`. The restart discards the completion
observation, so proactive evaluation at 12:02:31 sees an apparently silent resource
and fires the unresponsive-run action.

Two existing behaviours combined to cause this:

1. `ensure_bucket()` unconditionally wrote the incoming event into the existing
   bucket's `last_event`, so the completion event that was already recorded at that
   instant was overwritten before evaluation.
2. The restart special case did not check whether the arming event was actually
   newer than events the bucket had already accounted for, so it could move/restart
   the window at or before an already-seen expected event.

## Repair

Changes in `prefect/src/prefect/server/events/triggers.py`:

* `ensure_bucket()` no longer updates `last_event` when the bucket already exists
  (it now matches its documented contract, "Will not modify the existing bucket").
  `last_event` is advanced only by `increment_bucket()`.
* `evaluate()` captures the bucket's `last_event` before mutating it and only records
  the triggering event as the new `last_event` when it is at least as recent. A
  distinct event with the same `occurred` timestamp does not replace one already
  recorded, and an expected event that does not arm the window (a "response", e.g. a
  terminal state event) takes precedence over an arming event at the same instant so
  the response cannot be lost depending on arrival order.
* The proactive-window restart is now guarded by
  `_can_restart_proactive_window()`: a window may only be restarted when the arming
  event is strictly newer than the last event the bucket accounted for. Repeated
  arming events at the same instant still restart the window (so duplicate
  heartbeats do not mask a real outage), and a different, same-event retry is still
  allowed.

The repair is entirely in the existing bucket state (`automation_bucket.last_event`,
already persisted as JSON for both SQLite and PostgreSQL):

* no schema change, no migration and no public API change;
* restart/upgrade safe: the state lives in the database and is re-read by proactive
  evaluation after a restart;
* storage remains bounded: one bucket row per (automation, trigger, bucketing key),
  cleaned up by the existing `remove_bucket` / `sweep_closed_buckets` paths;
* no monitoring thresholds, actions, or concurrency primitives were changed.

A genuinely unresponsive run still fires: its last heartbeat is newer than any event
already seen, so the window is still restarted and expires with a count below the
threshold. The `Firing` still gets `triggering_labels` from the bucketing key and
`triggering_event` from the recorded last event.

## Tests added

In `prefect/tests/events/server/triggers/test_regressions.py`:

* `test_zombie_flow_detection_ignores_heartbeat_that_predates_terminal_event` - the
  incident shape (completion received before a same-timestamp heartbeat) produces
  no action.
* `test_zombie_flow_detection_ignores_completion_received_after_heartbeat` - the
  same-instant events in the opposite receive order still produce no action.
* `test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat` - an
  out-of-order heartbeat older than a completion cannot move the window backwards.
* `test_zombie_flow_detection_fires_when_heartbeats_share_timestamp` - a run that
  stops responding after repeated same-timestamp heartbeats still fires, with the
  correct resource label and triggering event.

## Commands actually executed and results

Run from `$SANDBOX/prefect`
with the isolated interpreter
`$SANDBOX/.runtime/venv/Scripts/python.exe`.

Before the repair:

* `python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`
  -> 1 failed, `observed_actions: 1`.

After the repair:

* `python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`
  -> 1 passed, `{"incident_id": "completed-run-001", "observed_actions": 0,
  "expected_actions": 0}`.
* `python -m pytest tests/events/server/triggers/test_regressions.py -q`
  -> 16 passed.
* `python -m pytest tests/events/server/triggers/test_basics.py -q`
  -> 34 passed.
* `python -m pytest tests/events/server/triggers -q --ignore=tests/events/server/triggers/test_incident_completed_run.py`
  -> 120 passed, 3 xfailed.
* `python -m pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py -q`
  -> 61 passed, 1 failed (`test_read_automations_page`). This failure is unrelated to
  the repair: it is an ordering assumption on `automation.updated` in the API test,
  and it reproduces identically when the original trigger code is restored.
* `python -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py`
  -> both files already formatted. (The locally installed `ruff check` 0.16.2 with
  its default rule set already reports many pre-existing modernization/style
  findings across these files; the new code follows the surrounding conventions
  such as `Optional`/`Tuple` and adds no functional lint issues.)

## Limits

* The repair distinguishes ordering by the events' `occurred` timestamps and by the
  persisted bucket state. Events in this incident carry no payload/state, so it does
  not depend on flow-run-specific event names or payloads (also making it work for
  custom state names). If a heartbeat were emitted *after* a terminal state event's
  `occurred` timestamp (a narrow client/server race) it would be indistinguishable
  from a legitimate heartbeat at the trigger layer; the event fixture and the real
  recorded incident use same-instant timestamps, which are handled.
* No database migration is required; existing buckets keep working, but a bucket
  that was already persisted in the bad reset state before an upgrade is not
  retroactively repaired (it is indistinguishable from a genuine unresponsive
  state).
