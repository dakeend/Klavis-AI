"""Replay the supplied synthetic incident through the server's event evaluator."""

import json
from datetime import timedelta
from pathlib import Path
from unittest.mock import AsyncMock

import pytest
from prefect.server.events import triggers
from prefect.server.events.models import automations
from prefect.server.events.schemas.automations import Automation
from prefect.server.events.schemas.events import Event
from prefect.types._datetime import parse_datetime

pytestmark = pytest.mark.clear_db


async def test_completed_run_incident(
    automations_session, cleared_buckets, cleared_automations, frozen_time, monkeypatch
):
    incident = json.loads(
        Path(__file__).with_name("incident_completed_run.json").read_text("utf-8")
    )
    action_sink = AsyncMock()
    monkeypatch.setattr(triggers, "act", action_sink)
    automation = await automations.create_automation(
        automations_session, Automation.model_validate(incident["automation"])
    )
    triggers.load_automation(automation)
    await automations_session.commit()

    # Shift the synthetic time anchor to the test clock, preserving all intervals.
    anchor = parse_datetime(incident["time_anchor"])
    for record in incident["records"]:
        payload = {key: record[key] for key in ("id", "occurred", "event", "resource")}
        payload["occurred"] = frozen_time + (
            parse_datetime(record["occurred"]) - anchor
        )
        event = Event.model_validate(payload).receive(
            received=frozen_time + timedelta(seconds=record["received_offset_seconds"])
        )
        print(
            json.dumps(
                {
                    "received_sequence": record["received_sequence"],
                    "event": record["event"],
                    "occurred": record["occurred"],
                }
            )
        )
        await triggers.reactive_evaluation(event)

    await triggers.proactive_evaluation(
        automation.trigger,
        frozen_time + timedelta(seconds=incident["evaluate_at_offset_seconds"]),
    )
    observed = action_sink.await_count
    print(
        json.dumps(
            {
                "incident_id": incident["incident_id"],
                "observed_actions": observed,
                "expected_actions": incident["expected_actions"],
            }
        )
    )
    assert observed == incident["expected_actions"], (
        f"Completed run received {observed} unresponsive-run action(s); expected zero"
    )
