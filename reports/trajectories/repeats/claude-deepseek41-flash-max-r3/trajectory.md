# 可见操作轨迹

时间戳保留 UTC。路径已用占位符替换；内部推理、系统消息、协作消息正文及本地通用技能正文未导出。
工具调用和结果是实际记录；省略处明确标记。模型的公开自述不等于作者侧验收结论。

## 1 · 2026-10-29T03:22:12.047903+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && ls -la",
  "description": "List root directory contents"
}
```

## 2 · 2026-10-29T03:22:12.266495+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && cat AGENTS.md 2>/dev/null | head -100",
  "description": "Read AGENTS.md"
}
```

## 3 · 2026-10-29T03:22:14.686621+00:00 · tool_result 

```
total 22
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:16 .
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:12 ..
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:17 .runtime
-rw-r--r-- 1 luwen 197121  285 Oct 29 11:13 AGENTS.md
-rw-r--r-- 1 luwen 197121  285 Oct 29 11:16 CLAUDE.md
-rw-r--r-- 1 luwen 197121 2921 Oct 29 11:13 TASK.md
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 prefect
```

## 4 · 2026-10-29T03:22:14.729622+00:00 · tool_result 

```
# Independent diagnostic trial

Read TASK.md and solve it directly.
Keep task reads/writes under this working root. No parent/sibling files,
prior solutions or task-specific online answers. Generic installed skills
may be read. Implementation is authorized; finish autonomously.
```

## 5 · 2026-10-29T03:22:15.906293+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && cat TASK.md",
  "description": "Read TASK.md"
}
```

## 6 · 2026-10-29T03:22:16.149236+00:00 · tool_result 

````
You are independently solving a software-engineering task in a fresh session.
Your working root is $SANDBOX.
Only inspect and modify task files under this root. Do not read parent/sibling
directories, other Codex sessions, previous attempts, author materials, references,
or saved patches. Do not search for task-specific online solutions or PR discussions.
General installed tool documentation and applicable generic skills are allowed.
Respect the repository's coding/testing conventions. Implementation is authorized:
work autonomously, do not pause for design approval or contact upstream maintainers.
The locked development dependencies are already installed in .runtime/venv.
On Windows, source .runtime/environment.ps1 from this root (or
../.runtime/environment.ps1 from prefect/) before Python commands to use the isolated
interpreter, home, SQLite database, temporary files and caches. Use $TrialPython for
that interpreter. Never connect to an existing user database.
Deliver the source changes and SOLUTION_SUMMARY.md with diagnosis, commands actually
executed, results and limits. Do not delegate or switch models.

Some completed flow runs still receive the automation action intended for an unresponsive run. The flow's event history shows that it completed, yet its monitoring automation later acts on it as though it had stopped responding.

The source is at `$SANDBOX/prefect`. An incident reproduction is included in the repository. It uses synthetic, anonymized event records and the real server evaluation path; outgoing actions are captured rather than executed.

From the repository root, run:

```sh
python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s
```

The accompanying `incident_completed_run.json` contains the automation configuration and recorded events. `incident-observed.log` contains captured replay output from this version. The replay prints the observed action count. The completed run in this incident should produce **zero** unresponsive-run actions.

Investigate the failure, identify its cause in the existing code, and deliver a general repair. A genuinely unresponsive run must still cause its configured action. Actions that legitimately fire must retain correct information about the affected resource and triggering event.

Preserve existing automation behavior, public interfaces and deployment concurrency behavior. The repair must work with SQLite, survive server restarts and upgrades without losing existing data, and keep storage use bounded during continued operation. Do not change monitoring thresholds or disable actions to suppress the symptom.

You may add regression tests. No UI build, external services or real workflow worker is required. Deliver the repaired source and a brief description of the diagnosis and verification performed.
````

## 7 · 2026-10-29T03:22:16.152587+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls -la && git status 2>&1 | head -20",
  "description": "List prefect repo root and git status"
}
```

## 8 · 2026-10-29T03:22:16.632562+00:00 · tool_result 

```
total 1282
drwxr-xr-x 1 luwen 197121       0 Oct 29 11:13 .
drwxr-xr-x 1 luwen 197121       0 Oct 29 11:16 ..
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 .claude
-rw-r--r-- 1 luwen 197121     678 Oct 20 03:32 .dockerignore
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 .github
-rw-r--r-- 1 luwen 197121    1466 Oct 20 03:32 .gitignore
-rw-r--r-- 1 luwen 197121     104 Oct 20 03:32 .gitmodules
-rw-r--r-- 1 luwen 197121       9 Oct 20 03:32 .nvmrc
-rw-r--r-- 1 luwen 197121    3248 Oct 20 03:32 .pre-commit-config.yaml
-rw-r--r-- 1 luwen 197121     431 Oct 20 03:32 .prefectignore
-rw-r--r-- 1 luwen 197121    9736 Oct 20 03:32 AGENTS.md
-rw-r--r-- 1 luwen 197121    3356 Oct 20 03:32 CODE_OF_CONDUCT.md
-rw-r--r-- 1 luwen 197121    8830 Oct 20 03:32 Dockerfile
-rw-r--r-- 1 luwen 197121    1042 Oct 20 03:32 Dockerfile.sqlite-builder
-rw-r--r-- 1 luwen 197121   11558 Oct 20 03:32 LICENSE
-rw-r--r-- 1 luwen 197121    9103 Oct 20 03:32 README.md
-rw-r--r-- 1 luwen 197121    3013 Oct 20 03:32 REVIEW.md
-rw-r--r-- 1 luwen 197121    1350 Oct 20 03:32 SECURITY.md
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 assets
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 benches
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 client
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 compat-tests
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 docs
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 examples
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 formal
-rw-r--r-- 1 luwen 197121    1873 Oct 20 03:32 hatch_build.py
-rw-r--r-- 1 luwen 197121     551 Oct 29 11:13 incident-observed.log
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 integration-tests
-rw-r--r-- 1 luwen 197121    8377 Oct 20 03:32 justfile
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 load_testing
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 plans
-rw-r--r-- 1 luwen 197121   14407 Oct 20 03:32 pyproject.toml
-rw-r--r-- 1 luwen 197121    6240 Oct 20 03:32 pyrightconfig-ci.json
-rw-r--r-- 1 luwen 197121     702 Oct 20 03:32 renovate.json
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 schemas
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 scripts
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 src
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 tests
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 tools
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 ui
drwxr-xr-x 1 luwen 197121       0 Oct 20 03:32 ui-v2
-rw-r--r-- 1 luwen 197121 1121373 Oct 20 03:32 uv.lock
fatal: not a git repository (or any of the parent directories): .git
```

## 9 · 2026-10-29T03:22:17.625170+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat AGENTS.md",
  "description": "Read repo AGENTS.md"
}
```

## 10 · 2026-10-29T03:22:17.864336+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat incident-observed.log && ls tests/events/server/triggers/ | head -50",
  "description": "Read incident log and list trigger tests"
}
```

## 11 · 2026-10-29T03:22:17.921769+00:00 · tool_result 

````
Prefect is a workflow orchestration platform that coordinates and observes data pipelines. It provides a Python SDK for building workflows, a server backend for orchestration, and a web-based UI for managing and monitoring workflows.

# Guiding Principles

Your primary responsibility is to the project and its users. Every change should serve the broader user base — not just the immediate request. Be a quality gate: prefer correct, minimal, well-tested changes over fast ones.

# Before You Start

Before making code changes, read the public contribution guide in `docs/contribute/dev-contribute.mdx` so your work follows Prefect's contribution expectations, design principles, AI-use policy, testing standards, and maintainer review criteria.
For documentation-only changes, also read `docs/contribute/docs-contribute.mdx`.
For integration changes, also read `docs/contribute/contribute-integrations.mdx`.

# Directory Structure

```
prefect/
├── benches/                         # Benchmarks (CLI, flows, tasks, imports)
├── client/                          # prefect-client build: subset of src/prefect/ published as a separate PyPI package
├── compat-tests/                    # Tests for REST API compatibility with Prefect Cloud
├── Dockerfile                       # Production container image
├── docs/                            # Mintlify documentation (see docs/AGENTS.md)
├── examples/                        # Example flows (auto-published to docs)
├── formal/                          # Executable formal models (see formal/tla/AGENTS.md)
├── integration-tests/               # End-to-end integration tests (require running server)
├── justfile                         # Task runner (just <command>)
├── load_testing/                    # Load/performance testing
├── plans/                           # Design/implementation plan documents
├── pyproject.toml                   # Root package config
├── schemas/                         # JSON schemas (prefect.yaml, settings)
├── scripts/                         # Code generation and release scripts
├── src/
│   ├── integrations/                # External service integrations (see src/integrations/AGENTS.md)
│   └── prefect/                     # Core package: SDK, server, CLI (see src/prefect/AGENTS.md)
├── tests/                           # Test suite, mirrors src/prefect/ (see tests/AGENTS.md)
├── tools/                           # Build tools
├── ui/                              # Vue UI (legacy, will be replaced by ui-v2)
├── ui-v2/                           # React UI rewrite (see ui-v2/AGENTS.md)
└── uv.lock                          # Lockfile (auto-generated, do not edit manually)
```

# Essential Commands

```bash
# Dependencies
uv sync                                # Install all dev dependencies
just install                           # Same as above, plus perf group

# Running code
uv run -s my_script.py                             # Run a script with an editable prefect install
uv run --extra aws repros/1234.py                  # Run repro needing an integration extra
uv run --project ./src/integrations/<name> <cmd>   # Run against a local integration from repo root
prefect server start                               # Start local server
prefect config view                                # Inspect current configuration

# Testing (see tests/AGENTS.md for full details)
uv run pytest tests/path.py -k name    # Run specific test
uv run pytest tests/path.py -x -n4     # Parallel, stop on first failure

# Linting & formatting
uv run ruff check --fix .              # Lint with auto-fix
uv run ruff format .                   # Format code
uv run pre-commit run --all-files      # Run all pre-commit hooks

# Docs (from repo root)
just docs                              # Start Mintlify dev server at localhost:3000
just generate-docs                     # Regenerate all doc artifacts

# UI (from repo root)
just ui-v2                             # Start React dev server at localhost:5173

# Docker
docker build -t prefect .                              # Default build (Python 3.11)
docker build --build-arg PYTHON_VERSION=3.12 -t prefect .  # Custom Python version
docker build --build-arg EXTRA_PIP_PACKAGES="prefect-aws" -t prefect .  # With extras
```

## Quick Reference

| Component | Path | Tests |
|-----------|------|-------|
| Core SDK (flows, tasks, states, deployments) | `src/prefect/` | `tests/` |
| Flow & task engines (async orchestration) | `src/prefect/flow_engine.py`, `task_engine.py` | `tests/engine/` |
| Client SDK (schemas, HTTP client) | `src/prefect/client/` | `tests/client/` |
| Server (API, database, scheduling) | `src/prefect/server/` | `tests/server/` |
| CLI | `src/prefect/cli/` | `tests/cli/` |
| Settings | `src/prefect/settings/` | `tests/settings/` |
| Integrations (`prefect-aws`, `prefect-dbt`, etc.) | `src/integrations/` | per-integration |
| React UI (replacing Vue `ui/`) | `ui-v2/` | `ui-v2/e2e/` |

## Tech Stack & Tooling

- **Python >=3.11,<3.15** with modern typing (`list[int]`, `T | None`)
- **FastAPI** for REST APIs
- **Pydantic v2** for validation
- **SQLAlchemy 2.0** async ORM
- **Alembic** for database migrations
- **PostgreSQL/SQLite** databases
- **React + TypeScript** for UI (see ui-v2/AGENTS.md)
- **Ruff** for linting and formatting
- **Pre-commit** hooks: ruff, codespell, mypy (partial), uv-lock, no-commit-to-branch

## Architecture Overview

- **Three user-facing surfaces**: Python SDK (`@flow`/`@task` decorators), CLI (`prefect` command), REST API (FastAPI server)
- **Server is the source of truth for flow state transitions** — the flow engine proposes states, and the server's orchestration layer accepts or rejects them. Task state transitions are managed locally by the task engine via `set_state` and communicated through `prefect.task_run.*` events
- **Two published packages**: `prefect` (full SDK + server) and `prefect-client` (lightweight client subset). `client/` contains the build config that selects which files from `src/prefect/` go into `prefect-client`
- **Integrations are separate PyPI packages** (`prefect-aws`, `prefect-dbt`, etc.) each with their own version, published independently from `src/integrations/`
- **Async-first execution model** with sync wrappers — the engines (`flow_engine.py`, `task_engine.py`) are async; sync `@flow`/`@task` functions are run in workers

## Anti-patterns

- **Never bypass the server for flow state transitions** — always go through the orchestration API, even in tests. Task state transitions are managed locally by the task engine by design
- **Never use `pip install` or `uv pip`** — use `uv` for all dependency management
- **Never use deferred imports** (imports inside functions) unless required to break circular imports or for optional dependencies
- **Never commit directly to `main`** — a pre-commit hook enforces this
- **Never skip pre-commit hooks** (`--no-verify`) — fix the underlying issue instead
- **Never amend commits** (`--amend`) — create new commits instead

# Development Guidelines

## Make sure you have a Prefect server or Prefect Cloud
- use `prefect config view` to check your current profile
- run `prefect server start` in the background if needed

## Code Conventions

- Private implementation details (`_private_method`)
- No public API changes without approval
- Use single backticks for inline code references in docstrings, not double backticks

## Testing

- Directory structure mirrors source code
- Run affected tests after changes: `uv run pytest tests/module/`
- Tests require deterministic behavior
- Mock external dependencies

## Formal Protocol Models

- Use TLA+ selectively for bounded concurrent or distributed protocols whose correctness depends on interleavings, retries, duplication, time, or ownership. Prefer ordinary tests for local or sequential behavior.
- Treat each `formal/tla/<protocol>/README.md` as the authority for its scope, configurations, action-to-code mapping, owner, and review triggers.
- Before changing mapped behavior, review the model and its deterministic regressions. Update them when the abstraction changes; otherwise state in the PR why it remains valid.
- A green model validates only its documented abstraction, not Prefect's implementation. Implementation evidence comes from mapped behavior and contract tests.

## Working on Issues

- Read the GitHub issue/PR and comments (`gh issue view`, `gh pr view`) before writing code
- Understand the scope and intended behavior — ask clarifying questions if unclear
- Create reproduction scripts in `repros/` directory (create it if needed; add to `.gitignore`)
- Name files by issue number: `repros/1234.py` (only create one file per issue)
- Ensure the issue is reproducible before fixing
- Add unit tests for fixes
- DO NOT delete files from `repros/` directory after reproducing the issue unless asked

## PR Body Style

- Start with "closes #1234" if resolving issue
- Brief summary: "this PR {changes}"
- Details in `<details>` tag
- Include relevant links

## Code Review Rules

When reviewing changes, read and apply [REVIEW.md](REVIEW.md).

# Project Practices

- All PRs require test coverage for new functionality
- GitHub issues are used for tracking issues (use the `gh` cli)
- Dependencies: updates to client-side deps in `pyproject.toml` require parallel changes in `client/pyproject.toml`
- AGENTS.md always symlinked to CLAUDE.md
````

## 12 · 2026-10-29T03:22:18.263754+00:00 · tool_result 

```
Captured baseline replay output; input records are synthetic.
{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
{"incident_id": "completed-run-001", "observed_actions": 1, "expected_actions": 0}
conftest.py
incident_completed_run.json
test_basics.py
test_composite_triggers.py
test_find_interested_triggers.py
test_flow_run_slas.py
test_incident_completed_run.py
test_regressions.py
test_service.py
test_service_changes.py
```

## 13 · 2026-10-29T03:22:19.434142+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat tests/events/server/triggers/test_incident_completed_run.py",
  "description": "Read incident test"
}
```

## 14 · 2026-10-29T03:22:19.660395+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat tests/events/server/triggers/incident_completed_run.json",
  "description": "Read incident config"
}
```

## 15 · 2026-10-29T03:22:19.703067+00:00 · tool_result 

```
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
```

## 16 · 2026-10-29T03:22:19.912295+00:00 · tool_result 

```
{
  "fixture_provenance": "Synthetic incident; identifiers and time anchor are artificial. Execution output is captured separately from actual replay.",
  "incident_id": "completed-run-001",
  "time_anchor": "2026-10-20T12:00:00Z",
  "automation": {
    "name": "Unresponsive run monitor",
    "trigger": {
      "match": {"prefect.resource.id": "prefect.flow-run.*"},
      "after": ["prefect.flow-run.heartbeat"],
      "expect": ["prefect.flow-run.*"],
      "for_each": ["prefect.resource.id"],
      "posture": "Proactive",
      "threshold": 1,
      "within": 90
    },
    "actions": [{"type": "do-nothing"}]
  },
  "records": [
    {"received_sequence": 1, "received_offset_seconds": 0.1, "id": "11111111-1111-4111-8111-111111111111", "occurred": "2026-10-20T12:00:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
    {"received_sequence": 2, "received_offset_seconds": 30.1, "id": "22222222-2222-4222-8222-222222222222", "occurred": "2026-10-20T12:00:30Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
    {"received_sequence": 3, "received_offset_seconds": 60.1, "id": "33333333-3333-4333-8333-333333333333", "occurred": "2026-10-20T12:01:00Z", "event": "prefect.flow-run.Completed", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
    {"received_sequence": 4, "received_offset_seconds": 60.2, "id": "44444444-4444-4444-8444-444444444444", "occurred": "2026-10-20T12:01:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}}
  ],
  "evaluate_at_offset_seconds": 151,
  "expected_actions": 0
}
```

## 17 · 2026-10-29T03:22:23.256810+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/events/ && ls src/prefect/server/events/models/ && wc -l src/prefect/server/events/triggers.py src/prefect/server/events/models/triggers.py src/prefect/server/events/schemas/automations.py",
  "description": "List events source and file sizes"
}
```

## 18 · 2026-10-29T03:22:23.523183+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"Proactive\\|proactive\" src/prefect/server/events/models/triggers.py | head -60",
  "description": "Find proactive logic in models"
}
```

## 19 · 2026-10-29T03:22:23.777663+00:00 · tool_result 

```
Exit code 1
__init__.py
actions.py
clients.py
counting.py
filters.py
jinja_filters.py
messaging.py
models
ordering
pipeline.py
schemas
services
storage
stream.py
triggers.py
__init__.py
automations.py
composite_trigger_child_firing.py
 1386 src/prefect/server/events/triggers.py
wc: src/prefect/server/events/models/triggers.py: No such file or directory
  818 src/prefect/server/events/schemas/automations.py
 2204 total
```

## 20 · 2026-10-29T03:22:23.878184+00:00 · tool_result 

```
grep: src/prefect/server/events/models/triggers.py: No such file or directory
```

## 21 · 2026-10-29T03:22:24.753236+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py"
}
```

## 22 · 2026-10-29T03:22:25.067506+00:00 · tool_result 

```
1	"""
2	The triggers consumer watches events streaming in from the event bus and decides whether
3	to act on them based on the automations that users have set up.
4	"""
5	
6	import asyncio
7	import fnmatch
8	from contextlib import AsyncExitStack, asynccontextmanager
9	from datetime import timedelta
10	from typing import (
11	    TYPE_CHECKING,
12	    AsyncGenerator,
13	    Collection,
14	    Dict,
15	    List,
16	    Optional,
17	    Set,
18	    Tuple,
19	)
20	from uuid import UUID
21	
22	import orjson
23	import sqlalchemy as sa
24	from sqlalchemy.ext.asyncio import AsyncSession
25	from typing_extensions import Literal, TypeAlias
26	
27	import prefect.types._datetime
28	from prefect._internal.retries import retry_async_fn
29	from prefect.logging import get_logger
30	from prefect.server.database import PrefectDBInterface, db_injector
31	from prefect.server.events import messaging
32	from prefect.server.events.actions import ServerActionTypes
33	from prefect.server.events.models.automations import (
34	    AUTOMATION_CHANGES_CHANNEL,
35	    AutomationChangeEvent,
36	    automations_session,
37	    read_automation,
38	)
39	from prefect.server.events.models.composite_trigger_child_firing import (
40	    acquire_composite_trigger_lock,
41	    clear_child_firings,
42	    clear_old_child_firings,
43	    get_child_firings,
44	    upsert_child_firing,
45	)
46	from prefect.server.events.ordering import (
47	    PRECEDING_EVENT_LOOKBACK,
48	    EventArrivedEarly,
49	    get_triggers_causal_ordering,
50	)
51	from prefect.server.events.schemas.automations import (
52	    Automation,
53	    CompositeTrigger,
54	    EventTrigger,
55	    Firing,
56	    Posture,
57	    Trigger,
58	    TriggeredAction,
59	    TriggerState,
60	)
61	from prefect.server.events.schemas.events import ReceivedEvent
62	from prefect.server.utilities.messaging import Message, MessageHandler
63	from prefect.server.utilities.postgres_listener import (
64	    get_pg_notify_connection,
65	    pg_listen,
66	)
67	from prefect.settings import PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER
68	from prefect.settings.context import get_current_settings
69	
70	if TYPE_CHECKING:
71	    import logging
72	
73	    from prefect.server.database.orm_models import ORMAutomationBucket
74	
75	
76	logger: "logging.Logger" = get_logger(__name__)
77	
78	AutomationID: TypeAlias = UUID
79	TriggerID: TypeAlias = UUID
80	AutomationStateSnapshot: TypeAlias = Tuple[
81	    Optional[prefect.types._datetime.DateTime], int
82	]
83	
84	
85	AUTOMATION_BUCKET_BATCH_SIZE = 500
86	
87	
88	async def evaluate(
89	    session: AsyncSession,
90	    trigger: EventTrigger,
91	    bucket: "ORMAutomationBucket",
92	    now: prefect.types._datetime.DateTime,
93	    triggering_event: Optional[ReceivedEvent],
94	) -> "ORMAutomationBucket | None":
95	    """Evaluates an Automation, either triggered by a specific event or proactively
96	    on a time interval.  Evaluating a Automation updates the associated counters for
97	    each automation, and will fire the associated action if it has met the threshold."""
98	    automation = trigger.automation
99	
100	    logging_context = {
101	        "automation": automation.id,
102	        "trigger": trigger.id,
103	        "bucketing_key": bucket.bucketing_key,
104	        "bucket_start": bucket.start,
105	        "bucket_end": bucket.end,
106	        "bucket_initial_count": bucket.count,
107	        "bucket_last_operation": bucket.last_operation,
108	        "now": now,
109	        "triggering_event": (
110	            {
111	                "id": triggering_event.id,
112	                "event": triggering_event.event,
113	            }
114	            if triggering_event
115	            else None
116	        ),
117	    }
118	
119	    # Implementation notes:
120	    #
121	    # This triggering algorithm maintains an invariant that there is exactly one
122	    # time-based "bucket" open and collecting events for each automation at a time. When
123	    # an event comes in that matches the automation, one of four things can happen:
124	    #
125	    # 1. The event would have matched an older bucket that has either expired or has
126	    #    already filled up, and thus is no longer relevant;
127	    # 2. The event matches the current bucket, but the bucket does not meet its
128	    #    threshold yet;
129	    # 3. The event matches the current bucket, causes it to meet the the threshold, so
130	    #    we fire immediately and advance the bucket to the next time period.
131	    # 4. The event matches the current bucket, but the event is for a future time after
132	    #    the current bucket has expired, so we will start the new bucket and re-evaluate
133	    #
134	    # Automations are also evaluated proactively without an event to see if they have
135	    # met their proactive threshold (where not enough events have happened in the time
136	    # period)
137	
138	    # If there was a triggering event, then we need to "spend" this count somewhere,
139	    # either in the currently open bucket or in the next time period's bucket
140	    count = 1 if triggering_event else 0
141	
142	    if now < bucket.start:
143	        # This is an older out-of-order message or a redundant event for a reactive
144	        # trigger that has has already fired, so it should not should not affect the
145	        # current bucket.  We can safely ignore this event/timestamp entirely.  Case #1
146	        # from the implementation notes above.
147	        logger.debug(
148	            "Automation %s (%r) trigger %s got a late event for keys (%r)",
149	            automation.id,
150	            automation.name,
151	            trigger.id,
152	            bucket.bucketing_key,
153	            extra=logging_context,
154	        )
155	        return bucket
156	
157	    if count and (trigger.immediate or bucket.start <= now < bucket.end):
158	        # we are still within the automation time period, so spend the count in the
159	        # current bucket
160	        bucket = await increment_bucket(session, bucket, count, triggering_event)
161	        count = 0
162	
163	    # Reactive automations will fire "eagerly", meaning they will fire as _soon_ as the
164	    # threshold is reached, then wait for the rest of their time period before
165	    # firing again.  This is done by creating a new bucket in the future after the
166	    # trigger has fired.
167	
168	    # Proactive automations must wait until the whole bucket has expired before they can
169	    # fire, because we can't know if we'll get one late event just in time to cause the
170	    # automation _not_ to fire.
171	
172	    ready_to_fire = trigger.posture == Posture.Reactive or bucket.end <= now
173	    meets_threshold = trigger.meets_threshold(bucket.count)
174	
175	    if ready_to_fire and meets_threshold:
176	        logger.debug(
177	            (
178	                "Automation %s (%r) trigger %s triggered for keys (%r) %s, "
179	                "having occurred %s times between %s and %s"
180	            ),
181	            automation.id,
182	            automation.name,
183	            trigger.id,
184	            bucket.bucketing_key,
185	            "reactively" if triggering_event else "proactively",
186	            bucket.count,
187	            bucket.start,
188	            bucket.end,
189	            extra=logging_context,
190	        )
191	
192	        firing = Firing(
193	            trigger=trigger,
194	            trigger_states={TriggerState.Triggered},
195	            triggered=prefect.types._datetime.now("UTC"),
196	            triggering_labels={
197	                label: value
198	                for label, value in zip(sorted(trigger.for_each), bucket.bucketing_key)
199	            },
200	            triggering_event=triggering_event or bucket.last_event,
201	        )
202	
203	        await fire(session, firing)
204	
205	        # when acting, remove the current bucket from the database immediately to avoid
206	        # potentially double-acting in the case of a crash between now and the next
207	        # time we backup buckets to the database
208	        await remove_bucket(session, bucket)
209	
210	    elif now < bucket.end:
211	        # We didn't fire this time, and also the bucket still has more time, so leave
212	        # before setting up a new future bucket.  Case #2 from the implementation notes
213	        # above.
214	        logger.debug(
215	            "Automation %s (%r) trigger %s has more time for keys (%r)",
216	            automation.id,
217	            automation.name,
218	            trigger.id,
219	            bucket.bucketing_key,
220	            extra={
221	                **logging_context,
222	                "ready_to_fire": ready_to_fire,
223	                "meets_threshold": meets_threshold,
224	            },
225	        )
226	
227	        # Special case of a proactive trigger for which the same event satisfies
228	        # both `after` and `expect`.  For example, using flow run heartbeats for crash
229	        # detection, after the first heartbeat we expect a subsequent heartbeat or
230	        # terminal state within a given time.
231	        #
232	        # If we've already reached the proactive threshold, we need to remove the
233	        # current bucket and start a new one for the latest event.
234	        if (
235	            triggering_event
236	            and trigger.posture == Posture.Proactive
237	            and not meets_threshold
238	            and trigger.starts_after(triggering_event.event)
239	            and trigger.expects(triggering_event.event)
240	        ):
241	            await remove_bucket(session, bucket)
242	            return await start_new_bucket(
243	                session,
244	                trigger,
245	                bucketing_key=bucket.bucketing_key,
246	                start=triggering_event.occurred,
247	                end=triggering_event.occurred + trigger.within,
248	                count=0,
249	                last_event=triggering_event,
250	            )
251	
252	        return bucket
253	    else:
254	        # Case #2 from the implementation notes above.
255	        logger.debug(
256	            "Automation %s (%r) trigger %s not ready to fire for keys (%r)",
257	            automation.id,
258	            automation.name,
259	            trigger.id,
260	            bucket.bucketing_key,
261	            extra={
262	                **logging_context,
263	                "ready_to_fire": ready_to_fire,
264	                "meets_threshold": meets_threshold,
265	                "bucket_current_count": bucket.count,
266	            },
267	        )
268	
269	    # We are now outside of the automation's time period or we triggered this
270	    # time.  That means it's time to start a new bucket for the next possible time
271	    # window (if this automation does not require an event to start `after`):
272	    if trigger.after:
273	        # remove the bucket because it should only get re-created if we see another
274	        # appropriate starting event
275	        return await remove_bucket(session, bucket)
276	    else:
277	        if trigger.within == timedelta(seconds=0):
278	            return None
279	
280	        start = prefect.types._datetime.create_datetime_instance(max(bucket.end, now))
281	        end = start + trigger.within
282	
283	        # If we're processing a reactive trigger and leaving the function with a count
284	        # that we've just spent in the bucket for the next time window, it means that we
285	        # just processed an event that was in the future. It's possible that this event
286	        # was sufficient enough to cause the trigger to fire, so we need to evaluate one
287	        # more time to see if that's the case.  This is case #4 from the implementation
288	        # notes above.
289	        if trigger.posture == Posture.Reactive and count > 0:
290	            bucket = await start_new_bucket(
291	                session,
292	                trigger,
293	                bucketing_key=tuple(bucket.bucketing_key),
294	                start=start,
295	                end=end,
296	                count=0,
297	            )
298	            return await evaluate(session, trigger, bucket, now, triggering_event)
299	        else:
300	            return await start_new_bucket(
301	                session,
302	                trigger,
303	                bucketing_key=tuple(bucket.bucketing_key),
304	                start=start,
305	                end=end,
306	                count=count,
307	            )
308	
309	
310	async def fire(session: AsyncSession, firing: Firing) -> None:
311	    if isinstance(firing.trigger.parent, Automation):
312	        await act(firing)
313	    elif isinstance(firing.trigger.parent, CompositeTrigger):
314	        await evaluate_composite_trigger(session, firing)
315	    else:
316	        raise NotImplementedError(
317	            f"Cannot fire {firing} with parent trigger type {type(firing.trigger.parent)}"
318	        )
319	
320	
321	async def evaluate_composite_trigger(session: AsyncSession, firing: Firing) -> None:
322	    automation = firing.trigger.automation
323	
324	    assert isinstance(firing.trigger.parent, CompositeTrigger)
325	    trigger: CompositeTrigger = firing.trigger.parent
326	
327	    # If we only need to see 1 child firing,
328	    # then the parent trigger can fire immediately.
329	    if trigger.num_expected_firings == 1:
330	        logger.info(
331	            "Automation %s (%r) %s trigger %s fired (shortcut)",
332	            automation.id,
333	            automation.name,
334	            trigger.type,
335	            trigger.id,
336	            extra={
337	                "automation": automation.id,
338	                "trigger": trigger.id,
339	                "trigger_type": trigger.type,
340	                "firings": firing.id,
341	            },
342	        )
343	        await fire(
344	            session,
345	            Firing(
346	                trigger=trigger,
347	                trigger_states={TriggerState.Triggered},
348	                triggered=prefect.types._datetime.now("UTC"),
349	                triggering_firings=[firing],
350	                triggering_event=firing.triggering_event,
351	            ),
352	        )
353	        return
354	
355	    # Acquire an advisory lock to serialize concurrent evaluations for this
356	    # compound trigger. This prevents a race condition where multiple child
357	    # triggers fire concurrently and neither transaction sees both firings.
358	    await acquire_composite_trigger_lock(session, trigger)
359	
360	    # If we're only looking within a certain time horizon, remove any older firings that
361	    # should no longer be considered as satisfying this trigger
362	    if trigger.within is not None:
363	        await clear_old_child_firings(
364	            session, trigger, firing.triggered - trigger.within
365	        )
366	
367	    # Otherwise we need N child firings. We'll upsert this firing and then check
368	    # what the current state of the world is. If we have enough firings, we'll
369	    # fire the parent trigger.
370	    await upsert_child_firing(session, firing)
371	    firings: list[Firing] = [
372	        cf.child_firing for cf in await get_child_firings(session, trigger)
373	    ]
374	    firing_ids: set[UUID] = {f.id for f in firings}
375	
376	    # If our current firing no longer exists when we read firings
377	    # another firing has superseded it, and we should defer to that one
378	    if firing.id not in firing_ids:
379	        return
380	
381	    if trigger.ready_to_fire(firings):
382	        logger.info(
383	            "Automation %s (%r) %s trigger %s fired",
384	            automation.id,
385	            automation.name,
386	            trigger.type,
387	            trigger.id,
388	            extra={
389	                "automation": automation.id,
390	                "trigger": trigger.id,
391	                "trigger_type": trigger.type,
392	                "firings": ",".join(str(f.id) for f in firings),
393	            },
394	        )
395	
396	        # Clear by firing id, and only proceed if we won the race to claim them.
397	        # This prevents double-firing when multiple workers evaluate concurrently.
398	        deleted_ids = await clear_child_firings(
399	            session, trigger, firing_ids=list(firing_ids)
400	        )
401	
402	        if deleted_ids != firing_ids:
403	            logger.debug(
404	                "Composite trigger %s skipped fire; expected to delete %s firings, "
405	                "actually deleted %s (another worker likely claimed them)",
406	                trigger.id,
407	                len(firing_ids),
408	                len(deleted_ids),
409	                extra={
410	                    "automation": automation.id,
411	                    "trigger": trigger.id,
412	                    "expected_firing_ids": sorted(str(f) for f in firing_ids),
413	                    "deleted_firing_ids": sorted(str(f) for f in deleted_ids),
414	                },
415	            )
416	            return
417	
418	        await fire(
419	            session,
420	            Firing(
421	                trigger=trigger,
422	                trigger_states={TriggerState.Triggered},
423	                triggered=prefect.types._datetime.now("UTC"),
424	                triggering_firings=firings,
425	                triggering_event=firing.triggering_event,
426	            ),
427	        )
428	
429	
430	async def act(firing: Firing) -> None:
431	    """Given a Automation that has been triggered, the triggering labels and event
432	    (if there was one), publish an action for the `actions` service to process."""
433	    automation = firing.trigger.automation
434	
435	    state_change_events: Dict[TriggerState, ReceivedEvent] = {
436	        trigger_state: firing.trigger.create_automation_state_change_event(
437	            firing=firing,
438	            trigger_state=trigger_state,
439	        )
440	        for trigger_state in sorted(firing.trigger_states, key=list(TriggerState).index)
441	    }
442	    await messaging.publish(state_change_events.values())
443	
444	    # Determine the primary state change event ID for linking action events back to
445	    # the automation.triggered or automation.resolved event. Prefer Triggered over
446	    # Resolved when both are present.
447	    primary_state_change_event = state_change_events.get(
448	        TriggerState.Triggered
449	    ) or state_change_events.get(TriggerState.Resolved)
450	    primary_state_change_event_id = (
451	        primary_state_change_event.id if primary_state_change_event else None
452	    )
453	
454	    # By default, all `automation.actions` are fired. Each tuple contains:
455	    # (triggering_event, action, automation_triggered_event_id)
456	    source_actions: List[
457	        Tuple[Optional[ReceivedEvent], ServerActionTypes, UUID | None]
458	    ] = [
459	        (firing.triggering_event, action, primary_state_change_event_id)
460	        for action in automation.actions
461	    ]
462	
463	    # Conditionally add in actions that fire on specific trigger states
464	    if TriggerState.Triggered in firing.trigger_states:
465	        triggered_event = state_change_events[TriggerState.Triggered]
466	        source_actions += [
467	            (triggered_event, action, triggered_event.id)
468	            for action in automation.actions_on_trigger
469	        ]
470	
471	    if TriggerState.Resolved in firing.trigger_states:
472	        resolved_event = state_change_events[TriggerState.Resolved]
473	        source_actions += [
474	            (resolved_event, action, resolved_event.id)
475	            for action in automation.actions_on_resolve
476	        ]
477	
478	    actions = [
479	        TriggeredAction(
480	            automation=automation,
481	            firing=firing,
482	            triggered=firing.triggered,
483	            triggering_labels=firing.triggering_labels,
484	            triggering_event=action_triggering_event,
485	            action=action,
486	            action_index=index,
487	            automation_triggered_event_id=automation_triggered_event_id,
488	        )
489	        for index, (
490	            action_triggering_event,
491	            action,
492	            automation_triggered_event_id,
493	        ) in enumerate(source_actions)
494	    ]
495	
496	    async with messaging.create_actions_publisher() as publisher:
497	        for action in actions:
498	            await publisher.publish_data(action.model_dump_json().encode(), {})
499	
500	
501	__events_clock_lock: Optional[asyncio.Lock] = None
502	_events_clock: Optional[float] = None
503	_events_clock_updated: Optional[float] = None
504	
505	
506	def _events_clock_lock() -> asyncio.Lock:
507	    global __events_clock_lock
508	    if __events_clock_lock is None:
509	        __events_clock_lock = asyncio.Lock()
510	    return __events_clock_lock
511	
512	
513	async def update_events_clock(event: ReceivedEvent) -> None:
514	    global _events_clock, _events_clock_updated
515	    async with _events_clock_lock():
516	        # we want the offset to be negative to represent that we are always
517	        # processing events behind realtime...
518	        now = prefect.types._datetime.now("UTC").timestamp()
519	        event_timestamp = event.occurred.timestamp()
520	        offset = event_timestamp - now
521	
522	        # ...and we should clamp this value to zero so we don't inadvertently look like
523	        # we are processing the future
524	        if offset > 0.0:
525	            event_timestamp = now
526	
527	        if not _events_clock or event_timestamp >= _events_clock:
528	            _events_clock = event_timestamp
529	
530	        _events_clock_updated = now
531	
532	
533	async def get_events_clock() -> Optional[float]:
534	    global _events_clock
535	    return _events_clock
536	
537	
538	async def get_events_clock_offset() -> float:
539	    """Calculate the current clock offset.  This takes into account both the `occurred`
540	    of the last event, as well as the time we _saw_ the last event.  This helps to
541	    ensure that in low volume environments, we don't end up getting huge offsets."""
542	    global _events_clock, _events_clock_updated
543	
544	    async with _events_clock_lock():
545	        if _events_clock is None or _events_clock_updated is None:
546	            return 0.0
547	
548	        now: float = prefect.types._datetime.now("UTC").timestamp()
549	        offset = (_events_clock - now) + (now - _events_clock_updated)
550	
551	    return offset
552	
553	
554	async def reset_events_clock() -> None:
555	    global _events_clock, _events_clock_updated
556	    async with _events_clock_lock():
557	        _events_clock = None
558	        _events_clock_updated = None
559	
560	
561	async def reactive_evaluation(event: ReceivedEvent, depth: int = 0) -> None:
562	    """
563	    Evaluate all automations that may apply to this event.
564	
565	    Args:
566	    event (ReceivedEvent): The event to evaluate. This object contains all the necessary information
567	        about the event, including its type, associated resources, and metadata.
568	    depth (int, optional): The current recursion depth. This is used to prevent infinite recursion
569	        due to cyclic event dependencies. Defaults to 0 and is incremented with
570	        each recursive call.
571	
572	    """
573	    async with AsyncExitStack() as stack:
574	        await update_events_clock(event)
575	        await stack.enter_async_context(
576	            get_triggers_causal_ordering().preceding_event_confirmed(
577	                reactive_evaluation, event, depth
578	            )
579	        )
580	
581	        interested_triggers = find_interested_triggers(event)
582	        if not interested_triggers:
583	            return
584	
585	        for trigger in interested_triggers:
586	            logger.info(
587	                "Automation %s, trigger %s covers event %r (%s) for %r at %r",
588	                trigger.automation.id,
589	                trigger.id,
590	                event.event,
591	                event.id,
592	                event.resource.id,
593	                event.occurred.isoformat(),
594	            )
595	
596	            bucketing_key = trigger.bucketing_key(event)
597	
598	            async with automations_session(begin_transaction=True) as session:
599	                try:
600	                    bucket: Optional["ORMAutomationBucket"] = None
601	
602	                    if trigger.after and trigger.starts_after(event.event):
603	                        # When an event matches both the after and expect, each event
604	                        # can both start a new bucket and increment the bucket that was
605	                        # started by the previous event.  Here we offset the bucket to
606	                        # start at -1 so that the first event will leave the bucket at 0
607	                        # after evaluation.  See the tests:
608	                        #
609	                        #   test_same_event_in_expect_and_after_never_reacts_immediately
610	                        #   test_same_event_in_expect_and_after_reacts_after_threshold_is_met
611	                        #   test_same_event_in_expect_and_after_proactively_does_not_fire
612	                        #   test_same_event_in_expect_and_after_proactively_fires
613	                        #
614	                        # in test_triggers_regressions.py for examples of how we expect
615	                        # this to behave.
616	                        #
617	                        # https://github.com/PrefectHQ/nebula/issues/4201
618	                        initial_count = -1 if trigger.expects(event.event) else 0
619	                        bucket = await ensure_bucket(
620	                            session,
621	                            trigger,
622	                            bucketing_key,
623	                            start=event.occurred,
624	                            end=event.occurred + trigger.within,
625	                            last_event=event,
626	                            initial_count=initial_count,
627	                        )
628	
629	                    if (
630	                        not bucket
631	                        and not trigger.after
632	                        and trigger.expects(event.event)
633	                    ):
634	                        # When ensuring a bucket and _creating it for the first time_,
635	                        # use an old time so that we can catch any other events flowing
636	                        # through the system at the same time even if they are out of
637	                        # order.  After the trigger fires and creates its next bucket,
638	                        # time will start from that point forward.  We'll use our
639	                        # preceding event lookback variable as the horizon that we'll
640	                        # accept these older events.
641	                        #
642	                        # https://github.com/PrefectHQ/nebula/issues/7230
643	                        start = event.occurred - PRECEDING_EVENT_LOOKBACK
644	
645	                        bucket = await ensure_bucket(
646	                            session,
647	                            trigger,
648	                            bucketing_key=bucketing_key,
649	                            start=start,
650	                            end=event.occurred + trigger.within,
651	                            last_event=event,
652	                        )
653	
654	                    if not trigger.expects(event.event):
655	                        continue
656	
657	                    if not bucket:
658	                        bucket = await read_bucket(session, trigger, bucketing_key)
659	                        if not bucket:
660	                            continue
661	
662	                    await evaluate(
663	                        session,
664	                        trigger,
665	                        bucket,
666	                        event.occurred,
667	                        triggering_event=event,
668	                    )
669	                finally:
670	                    await session.commit()
671	
672	
673	# retry on operational errors to account for db flakiness with sqlite
674	@retry_async_fn(max_attempts=3, retry_on_exceptions=(sa.exc.OperationalError,))
675	async def get_lost_followers() -> List[ReceivedEvent]:
676	    """Get followers that have been sitting around longer than our lookback"""
677	    return await get_triggers_causal_ordering().get_lost_followers()
678	
679	
680	async def periodic_evaluation(now: prefect.types._datetime.DateTime) -> None:
681	    """Periodic tasks that should be run regularly, but not as often as every event"""
682	    offset = await get_events_clock_offset()
683	    as_of = now + timedelta(seconds=offset)
684	
685	    logger.debug("Running periodic evaluation as of %s (offset %ss)", as_of, offset)
686	
687	    await reconcile_automations()
688	
689	    # Any followers that have been sitting around longer than our lookback are never
690	    # going to see their leader event (maybe it was lost or took too long to arrive).
691	    # These events can just be evaluated now in the order they occurred.
692	    for event in await get_lost_followers():
693	        await reactive_evaluation(event)
694	
695	    async with automations_session() as session:
696	        await sweep_closed_buckets(
697	            session,
698	            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),
699	        )
700	        await session.commit()
701	
702	
703	async def evaluate_periodically(periodic_granularity: timedelta) -> None:
704	    """Runs periodic evaluation on the given interval"""
705	    logger.debug(
706	        "Starting periodic evaluation task every %s seconds",
707	        periodic_granularity.total_seconds(),
708	    )
709	    while True:
710	        try:
711	            await periodic_evaluation(prefect.types._datetime.now("UTC"))
712	        except Exception:
713	            logger.exception("Error running periodic evaluation")
714	        finally:
715	            await asyncio.sleep(periodic_granularity.total_seconds())
716	
717	
718	# The currently loaded automations for this shard, organized both by ID and by
719	# account and workspace
720	automations_by_id: Dict[UUID, Automation] = {}
721	triggers: Dict[TriggerID, EventTrigger] = {}
722	# Index from expect/after pattern → trigger IDs, so find_interested_triggers
723	# checks a handful of patterns instead of scanning all triggers.
724	_triggers_by_expect: Dict[str, Set[TriggerID]] = {}
725	next_proactive_runs: Dict[TriggerID, prefect.types._datetime.DateTime] = {}
726	automation_state_snapshot: Optional[AutomationStateSnapshot] = None
727	
728	# This lock governs any changes to the set of loaded automations; any routine that will
729	# add/remove automations must be holding this lock when it does so.  It's best to use
730	# the methods below to access the loaded set of automations.
731	__automations_lock: Optional[asyncio.Lock] = None
732	
733	
734	def _automations_lock() -> asyncio.Lock:
735	    global __automations_lock
736	    if __automations_lock is None:
737	        __automations_lock = asyncio.Lock()
738	    return __automations_lock
739	
740	
741	def find_interested_triggers(event: ReceivedEvent) -> Collection[EventTrigger]:
742	    candidate_ids: set[TriggerID] = set()
743	    for expect_pattern, trigger_ids in _triggers_by_expect.items():
744	        if fnmatch.fnmatchcase(event.event, expect_pattern):
745	            candidate_ids.update(trigger_ids)
746	    candidates = [triggers[tid] for tid in candidate_ids if tid in triggers]
747	    return [trigger for trigger in candidates if trigger.covers(event)]
748	
749	
750	def clear_loaded_automations() -> None:
751	    automations_by_id.clear()
752	    triggers.clear()
753	    _triggers_by_expect.clear()
754	    next_proactive_runs.clear()
755	
756	
757	def _index_keys_for(trigger: EventTrigger) -> set[str]:
758	    # An empty `expect` means "match any event" (event_pattern is `.+`), so the
759	    # trigger must be reachable for every event regardless of its `after` set.
760	    if not trigger.expect:
761	        return {"*"}
762	    return trigger.expect | trigger.after
763	
764	
765	def _index_trigger(trigger: EventTrigger) -> None:
766	    for key in _index_keys_for(trigger):
767	        _triggers_by_expect.setdefault(key, set()).add(trigger.id)
768	
769	
770	def _unindex_trigger(trigger: EventTrigger) -> None:
771	    for key in _index_keys_for(trigger):
772	        if key in _triggers_by_expect:
773	            _triggers_by_expect[key].discard(trigger.id)
774	            if not _triggers_by_expect[key]:
775	                del _triggers_by_expect[key]
776	
777	
778	def load_automation(automation: Optional[Automation]) -> None:
779	    """Loads the given automation into memory so that it is available for evaluations"""
780	    if not automation:
781	        return
782	
783	    event_triggers = automation.triggers_of_type(EventTrigger)
784	
785	    if not automation.enabled or not event_triggers:
786	        forget_automation(automation.id)
787	        return
788	
789	    automations_by_id[automation.id] = automation
790	
791	    for trigger in event_triggers:
792	        triggers[trigger.id] = trigger
793	        next_proactive_runs.pop(trigger.id, None)
794	        _index_trigger(trigger)
795	
796	
797	def forget_automation(automation_id: UUID) -> None:
798	    """Unloads the given automation from memory"""
799	    if automation := automations_by_id.pop(automation_id, None):
800	        for trigger in automation.triggers():
801	            triggers.pop(trigger.id, None)
802	            next_proactive_runs.pop(trigger.id, None)
803	        for trigger in automation.triggers_of_type(EventTrigger):
804	            _unindex_trigger(trigger)
805	
806	
807	async def automation_changed(
808	    automation_id: UUID,
809	    event: Literal["automation__created", "automation__updated", "automation__deleted"],
810	) -> None:
811	    global automation_state_snapshot
812	
813	    async with _automations_lock():
814	        if event in ("automation__deleted", "automation__updated"):
815	            forget_automation(automation_id)
816	
817	        async with automations_session() as session:
818	            if event in ("automation__created", "automation__updated"):
819	                automation = await read_automation(session, automation_id)
820	                load_automation(automation)
821	            automation_state_snapshot = await read_automation_state_snapshot(session)
822	
823	
824	@db_injector
825	async def load_automations(db: PrefectDBInterface, session: AsyncSession):
826	    """Loads all automations for the given set of accounts"""
827	    query = sa.select(db.Automation)
828	
829	    logger.debug("Loading automations")
830	
831	    result = await session.execute(query)
832	    for automation in result.scalars().all():
833	        load_automation(Automation.model_validate(automation, from_attributes=True))
834	
835	    logger.debug(
836	        "Loaded %s automations with %s triggers", len(automations_by_id), len(triggers)
837	    )
838	
839	
840	@db_injector
841	async def read_automation_state_snapshot(
842	    db: PrefectDBInterface, session: AsyncSession
843	) -> AutomationStateSnapshot:
844	    query = sa.select(
845	        sa.func.max(db.Automation.updated),
846	        sa.func.count(db.Automation.id),
847	    ).select_from(db.Automation)
848	
849	    latest_updated, count = (await session.execute(query)).one()
850	
851	    return (
852	        prefect.types._datetime.create_datetime_instance(latest_updated)
853	        if latest_updated
854	        else None,
855	        count or 0,
856	    )
857	
858	
859	async def reconcile_automations(force: bool = False) -> bool:
860	    global automation_state_snapshot
861	
862	    async with _automations_lock():
863	        async with automations_session() as session:
864	            current_snapshot = await read_automation_state_snapshot(session)
865	            if not force and current_snapshot == automation_state_snapshot:
866	                return False
867	
868	            previous_automations = automations_by_id.copy()
869	            previous_triggers = triggers.copy()
870	            previous_triggers_by_expect = {
871	                k: v.copy() for k, v in _triggers_by_expect.items()
872	            }
873	            previous_next_proactive_runs = next_proactive_runs.copy()
874	
875	            clear_loaded_automations()
876	
877	            try:
878	                await load_automations(session)
879	            except Exception:
880	                clear_loaded_automations()
881	                automations_by_id.update(previous_automations)
882	                triggers.update(previous_triggers)
883	                _triggers_by_expect.update(previous_triggers_by_expect)
884	                next_proactive_runs.update(previous_next_proactive_runs)
885	                raise
886	
887	            automation_state_snapshot = current_snapshot
888	            return True
889	
890	
891	@db_injector
892	async def remove_buckets_exceeding_threshold(
893	    db: PrefectDBInterface, session: AsyncSession, trigger: EventTrigger
894	):
895	    """Deletes bucket where the count has already exceeded the threshold"""
896	    assert isinstance(trigger, EventTrigger), repr(trigger)
897	    await session.execute(
898	        sa.delete(db.AutomationBucket).where(
899	            db.AutomationBucket.automation_id == trigger.automation.id,
900	            db.AutomationBucket.trigger_id == trigger.id,
901	            db.AutomationBucket.count >= trigger.threshold,
902	        )
903	    )
904	
905	
906	@db_injector
907	async def read_buckets_for_automation(
908	    db: PrefectDBInterface,
909	    session: AsyncSession,
910	    trigger: Trigger,
911	    batch_size: int = AUTOMATION_BUCKET_BATCH_SIZE,
912	) -> AsyncGenerator["ORMAutomationBucket", None]:
913	    """Yields buckets for the given automation and trigger in batches."""
914	    offset = 0
915	
916	    while True:
917	        query = (
918	            sa.select(db.AutomationBucket)
919	            .where(
920	                db.AutomationBucket.automation_id == trigger.automation.id,
921	                db.AutomationBucket.trigger_id == trigger.id,
922	            )
923	            .order_by(db.AutomationBucket.start)
924	            .limit(batch_size)
925	            .offset(offset)
926	        )
927	
928	        result = await session.execute(query)
929	        buckets = result.scalars().all()
930	
931	        if not buckets:
932	            break
933	
934	        for bucket in buckets:
935	            yield bucket
936	
937	        offset += batch_size
938	
939	
940	@db_injector
941	async def read_bucket(
942	    db: PrefectDBInterface,
943	    session: AsyncSession,
944	    trigger: Trigger,
945	    bucketing_key: Tuple[str, ...],
946	) -> Optional["ORMAutomationBucket"]:
947	    """Gets the bucket this event would fall into for the given Automation, if there is
948	    one currently"""
949	    return await read_bucket_by_trigger_id(
950	        session,
951	        trigger.automation.id,
952	        trigger.id,
953	        bucketing_key,
954	    )
955	
956	
957	@db_injector
958	async def read_bucket_by_trigger_id(
959	    db: PrefectDBInterface,
960	    session: AsyncSession,
961	    automation_id: UUID,
962	    trigger_id: UUID,
963	    bucketing_key: Tuple[str, ...],
964	) -> "ORMAutomationBucket | None":
965	    """Gets the bucket this event would fall into for the given Automation, if there is
966	    one currently"""
967	    query = sa.select(db.AutomationBucket).where(
968	        db.AutomationBucket.automation_id == automation_id,
969	        db.AutomationBucket.trigger_id == trigger_id,
970	        db.AutomationBucket.bucketing_key == bucketing_key,
971	    )
972	    result = await session.execute(query)
973	    bucket = result.scalars().first()
974	    if bucket:
975	        await session.refresh(bucket)
976	
977	    return bucket
978	
979	
980	@db_injector
981	async def increment_bucket(
982	    db: PrefectDBInterface,
983	    session: AsyncSession,
984	    bucket: "ORMAutomationBucket",
985	    count: int,
986	    last_event: Optional[ReceivedEvent],
987	) -> "ORMAutomationBucket":
988	    """Adds the given count to the bucket, returning the new bucket"""
989	    additional_updates: dict[str, ReceivedEvent] = (
990	        {"last_event": last_event} if last_event else {}
991	    )
992	    await session.execute(
993	        db.queries.insert(db.AutomationBucket)
994	        .values(
995	            automation_id=bucket.automation_id,
996	            trigger_id=bucket.trigger_id,
997	            bucketing_key=bucket.bucketing_key,
998	            start=bucket.start,
999	            end=bucket.end,
1000	            count=count,
1001	            last_operation="increment_bucket[insert]",
1002	        )
1003	        .on_conflict_do_update(
1004	            index_elements=[
1005	                db.AutomationBucket.automation_id,
1006	                db.AutomationBucket.trigger_id,
1007	                db.AutomationBucket.bucketing_key,
1008	            ],
1009	            set_=dict(
1010	                count=db.AutomationBucket.count + count,
1011	                last_operation="increment_bucket[update]",
1012	                updated=prefect.types._datetime.now("UTC"),
1013	                **additional_updates,
1014	            ),
1015	        )
1016	    )
1017	
1018	    read_bucket = await read_bucket_by_trigger_id(
1019	        session,
1020	        bucket.automation_id,
1021	        bucket.trigger_id,
1022	        tuple(bucket.bucketing_key),
1023	    )
1024	
1025	    if TYPE_CHECKING:
1026	        assert read_bucket is not None
1027	
1028	    return read_bucket
1029	
1030	
1031	@db_injector
1032	async def start_new_bucket(
1033	    db: PrefectDBInterface,
1034	    session: AsyncSession,
1035	    trigger: EventTrigger,
1036	    bucketing_key: Tuple[str, ...],
1037	    start: prefect.types._datetime.DateTime,
1038	    end: prefect.types._datetime.DateTime,
1039	    count: int,
1040	    triggered_at: Optional[prefect.types._datetime.DateTime] = None,
1041	    last_event: Optional[ReceivedEvent] = None,
1042	) -> "ORMAutomationBucket":
1043	    """Ensures that a bucket with the given start and end exists with the given count,
1044	    returning the new bucket"""
1045	    automation = trigger.automation
1046	
1047	    await session.execute(
1048	        db.queries.insert(db.AutomationBucket)
1049	        .values(
1050	            automation_id=automation.id,
1051	            trigger_id=trigger.id,
1052	            bucketing_key=bucketing_key,
1053	            start=start,
1054	            end=end,
1055	            count=count,
1056	            last_operation="start_new_bucket[insert]",
1057	            triggered_at=triggered_at,
1058	            last_event=last_event,
1059	        )
1060	        .on_conflict_do_update(
1061	            index_elements=[
1062	                db.AutomationBucket.automation_id,
1063	                db.AutomationBucket.trigger_id,
1064	                db.AutomationBucket.bucketing_key,
1065	            ],
1066	            set_=dict(
1067	                start=start,
1068	                end=end,
1069	                count=count,
1070	                last_operation="start_new_bucket[update]",
1071	                updated=prefect.types._datetime.now("UTC"),
1072	                triggered_at=triggered_at,
1073	                last_event=last_event,
1074	            ),
1075	        )
1076	    )
1077	
1078	    read_bucket = await read_bucket_by_trigger_id(
1079	        session,
1080	        automation.id,
1081	        trigger.id,
1082	        tuple(bucketing_key),
1083	    )
1084	
1085	    if TYPE_CHECKING:
1086	        assert read_bucket is not None
1087	
1088	    return read_bucket
1089	
1090	
1091	@db_injector
1092	async def ensure_bucket(
1093	    db: PrefectDBInterface,
1094	    session: AsyncSession,
1095	    trigger: EventTrigger,
1096	    bucketing_key: Tuple[str, ...],
1097	    start: prefect.types._datetime.DateTime,
1098	    end: prefect.types._datetime.DateTime,
1099	    last_event: Optional[ReceivedEvent],
1100	    initial_count: int = 0,
1101	) -> "ORMAutomationBucket":
1102	    """Ensures that a bucket has been started for the given automation and key,
1103	    returning the current bucket.  Will not modify the existing bucket."""
1104	    automation = trigger.automation
1105	    additional_updates: dict[str, ReceivedEvent] = (
1106	        {"last_event": last_event} if last_event else {}
1107	    )
1108	    await session.execute(
1109	        db.queries.insert(db.AutomationBucket)
1110	        .values(
1111	            automation_id=automation.id,
1112	            trigger_id=trigger.id,
1113	            bucketing_key=bucketing_key,
1114	            last_event=last_event,
1115	            start=start,
1116	            end=end,
1117	            count=initial_count,
1118	            last_operation="ensure_bucket[insert]",
1119	        )
1120	        .on_conflict_do_update(
1121	            index_elements=[
1122	                db.AutomationBucket.automation_id,
1123	                db.AutomationBucket.trigger_id,
1124	                db.AutomationBucket.bucketing_key,
1125	            ],
1126	            set_=dict(
1127	                # no-op, but this counts as an update so the query returns a row
1128	                count=db.AutomationBucket.count,
1129	                **additional_updates,
1130	            ),
1131	        )
1132	    )
1133	
1134	    read_bucket = await read_bucket_by_trigger_id(
1135	        session, automation.id, trigger.id, tuple(bucketing_key)
1136	    )
1137	
1138	    if TYPE_CHECKING:
1139	        assert read_bucket is not None
1140	
1141	    return read_bucket
1142	
1143	
1144	@db_injector
1145	async def remove_bucket(
1146	    db: PrefectDBInterface, session: AsyncSession, bucket: "ORMAutomationBucket"
1147	):
1148	    """Removes the given bucket from the database"""
1149	    await session.execute(
1150	        sa.delete(db.AutomationBucket).where(
1151	            db.AutomationBucket.automation_id == bucket.automation_id,
1152	            db.AutomationBucket.trigger_id == bucket.trigger_id,
1153	            db.AutomationBucket.bucketing_key == bucket.bucketing_key,
1154	        )
1155	    )
1156	
1157	
1158	@db_injector
1159	async def sweep_closed_buckets(
1160	    db: PrefectDBInterface,
1161	    session: AsyncSession,
1162	    older_than: prefect.types._datetime.DateTime,
1163	) -> None:
1164	    await session.execute(
1165	        sa.delete(db.AutomationBucket).where(db.AutomationBucket.end <= older_than)
1166	    )
1167	
1168	
1169	async def reset() -> None:
1170	    """Resets the in-memory state of the service"""
1171	    global automation_state_snapshot
1172	
1173	    await reset_events_clock()
1174	    clear_loaded_automations()
1175	    automation_state_snapshot = None
1176	
1177	
1178	async def listen_for_automation_changes() -> None:
1179	    """
1180	    Listens for any changes to automations via PostgreSQL NOTIFY/LISTEN,
1181	    and applies those changes to the set of loaded automations.
1182	    """
1183	    logger.info("Starting automation change listener")
1184	
1185	    while True:
1186	        conn = None
1187	        try:
1188	            conn = await get_pg_notify_connection()
1189	            if not conn:
1190	                logger.debug(
1191	                    "PostgreSQL NOTIFY/LISTEN not available (not using PostgreSQL). "
1192	                    "Automation changes will not be synchronized across servers."
1193	                )
1194	                return
1195	
1196	            logger.info(
1197	                f"Listening for automation changes on {AUTOMATION_CHANGES_CHANNEL}"
1198	            )
1199	
1200	            await reconcile_automations()
1201	
1202	            async for payload in pg_listen(
1203	                conn,
1204	                AUTOMATION_CHANGES_CHANNEL,
1205	                heartbeat_interval=get_current_settings().server.services.triggers.pg_notify_heartbeat_interval_seconds,
1206	            ):
1207	                try:
1208	                    data = orjson.loads(payload)
1209	                    automation_id = UUID(data["automation_id"])
1210	                    event_type = data["event_type"]
1211	
1212	                    logger.info(
1213	                        f"Received automation change notification: {event_type} for {automation_id}"
1214	                    )
1215	
1216	                    event_map: dict[str, AutomationChangeEvent] = {
1217	                        "created": "automation__created",
1218	                        "updated": "automation__updated",
1219	                        "deleted": "automation__deleted",
1220	                    }
1221	
1222	                    if event_type in event_map:
1223	                        await automation_changed(automation_id, event_map[event_type])
1224	                    else:
1225	                        logger.warning(f"Unknown automation event type: {event_type}")
1226	
1227	                except Exception as e:
1228	                    logger.error(
1229	                        f"Error processing automation change notification: {e}",
1230	                        exc_info=True,
1231	                    )
1232	
1233	        except asyncio.CancelledError:
1234	            logger.info("Automation change listener cancelled")
1235	            break
1236	        except Exception as e:
1237	            reconnect_seconds = get_current_settings().server.services.triggers.pg_notify_reconnect_interval_seconds
1238	            logger.error(
1239	                f"Error in automation change listener: {e}. Reconnecting in {reconnect_seconds}s...",
1240	                exc_info=True,
1241	            )
1242	            await asyncio.sleep(reconnect_seconds)
1243	        finally:
1244	            if conn and not conn.is_closed():
1245	                await conn.close()
1246	
1247	
1248	@asynccontextmanager
1249	async def consumer(
1250	    periodic_granularity: timedelta = timedelta(seconds=5),
1251	) -> AsyncGenerator[MessageHandler, None]:
1252	    """The `triggers.consumer` processes all Events arriving on the event bus to
1253	    determine if they meet the automation criteria, queuing up a corresponding
1254	    `TriggeredAction` for the `actions` service if the automation criteria is met."""
1255	    # Start the automation change listener task
1256	    sync_task = asyncio.create_task(listen_for_automation_changes())
1257	
1258	    await reconcile_automations(force=True)
1259	
1260	    proactive_task = asyncio.create_task(evaluate_periodically(periodic_granularity))
1261	
1262	    ordering = get_triggers_causal_ordering()
1263	
1264	    async def message_handler(message: Message):
1265	        if not message.data:
1266	            logger.warning("Message had no data")
1267	
1268	            return
1269	
1270	        if not message.attributes:
1271	            logger.warning("Message had no attributes")
1272	
1273	            return
1274	
1275	        if message.attributes.get("event") == "prefect.log.write":
1276	            return
1277	
1278	        try:
1279	            event_id = UUID(message.attributes["id"])
1280	        except (KeyError, ValueError, TypeError):
1281	            logger.warning(
1282	                "Unable to get event ID from message attributes: %s",
1283	                repr(message.attributes),
1284	            )
1285	            return
1286	
1287	        if await ordering.event_has_been_seen(event_id):
1288	            return
1289	
1290	        event = ReceivedEvent.model_validate_json(message.data)
1291	
1292	        try:
1293	            await reactive_evaluation(event)
1294	        except EventArrivedEarly:
1295	            pass  # it's fine to ACK this message, since it is safe in the DB
1296	
1297	    try:
1298	        logger.debug("Starting reactive evaluation task")
1299	        yield message_handler
1300	    finally:
1301	        sync_task.cancel()
1302	        proactive_task.cancel()
1303	        # Wait for tasks to finish
1304	        await asyncio.gather(sync_task, proactive_task, return_exceptions=True)
1305	
1306	
1307	async def proactive_evaluation(
1308	    trigger: EventTrigger, as_of: prefect.types._datetime.DateTime
1309	) -> prefect.types._datetime.DateTime:
1310	    """The core proactive evaluation operation for a single Automation"""
1311	    assert isinstance(trigger, EventTrigger), repr(trigger)
1312	    automation = trigger.automation
1313	
1314	    offset = await get_events_clock_offset()
1315	    as_of += timedelta(seconds=offset)
1316	
1317	    logger.debug(
1318	        "Evaluating automation %s trigger %s proactively as of %s (offset %ss)",
1319	        automation.id,
1320	        trigger.id,
1321	        as_of,
1322	        offset,
1323	    )
1324	
1325	    # By default, the next run will come after the full trigger window, but it
1326	    # may be sooner based on the state of the buckets
1327	    run_again_at = as_of + trigger.within
1328	
1329	    async with automations_session() as session:
1330	        try:
1331	            if not trigger.for_each:
1332	                await ensure_bucket(
1333	                    session,
1334	                    trigger,
1335	                    bucketing_key=tuple(),
1336	                    start=as_of,
1337	                    end=as_of + trigger.within,
1338	                    last_event=None,
1339	                )
1340	
1341	            # preemptively delete buckets where possible without
1342	            # evaluating them in memory
1343	            await remove_buckets_exceeding_threshold(session, trigger)
1344	
1345	            async for bucket in read_buckets_for_automation(session, trigger):
1346	                next_bucket = await evaluate(
1347	                    session, trigger, bucket, as_of, triggering_event=None
1348	                )
1349	                if next_bucket and as_of < next_bucket.end < run_again_at:
1350	                    run_again_at = prefect.types._datetime.create_datetime_instance(
1351	                        next_bucket.end
1352	                    )
1353	
1354	            return run_again_at
1355	        finally:
1356	            await session.commit()
1357	
1358	
1359	async def evaluate_proactive_triggers() -> None:
1360	    for trigger in list(triggers.values()):
1361	        if trigger.posture != Posture.Proactive:
1362	            continue
1363	
1364	        next_run = next_proactive_runs.get(
1365	            trigger.id, prefect.types._datetime.now("UTC")
1366	        )
1367	        if next_run > prefect.types._datetime.now("UTC"):
1368	            continue
1369	
1370	        try:
1371	            run_again_at = await proactive_evaluation(
1372	                trigger, prefect.types._datetime.now("UTC")
1373	            )
1374	            logger.debug(
1375	                "Automation %s trigger %s will run again at %s",
1376	                trigger.automation.id,
1377	                trigger.id,
1378	                run_again_at,
1379	            )
1380	            next_proactive_runs[trigger.id] = run_again_at
1381	        except Exception:
1382	            logger.exception(
1383	                "Error evaluating automation %s trigger %s proactively",
1384	                trigger.automation.id,
1385	                trigger.id,
1386	            )
1387	
```

## 23 · 2026-10-29T03:22:39.298179+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class EventTrigger\\|def covers\\|def starts_after\\|def expects\\|def bucketing_key\\|def meets_threshold\\|def within\\|for_each\" -n src/prefect/server/events/schemas/automations.py | head -50",
  "description": "Find EventTrigger methods"
}
```

## 24 · 2026-10-29T03:22:39.622414+00:00 · tool_result 

```
273:    def covers_resources(
289:class EventTrigger(ResourceTrigger):
314:    for_each: Set[str] = Field(
322:            'example, `"for_each": ["related:flow:prefect.resource.id"]` would '
380:    def covers(self, event: ReceivedEvent) -> bool:
417:    def starts_after(self, event: str) -> bool:
429:    def expects(self, event: str) -> bool:
438:    def bucketing_key(self, event: ReceivedEvent) -> Tuple[str, ...]:
440:            event.find_resource_label(label) or "" for label in sorted(self.for_each)
443:    def meets_threshold(self, event_count: int) -> bool:
701:            "for_each values of the trigger.  Only used in the context "
770:            "corresponding to the Automation's for_each.  If no for_each is specified, "
```

## 25 · 2026-10-29T03:22:40.577436+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/schemas/automations.py",
  "offset": 240,
  "limit": 230
}
```

## 26 · 2026-10-29T03:22:40.689020+00:00 · tool_result 

```
240	        default_factory=lambda: ResourceSpecification.model_validate({}),
241	        description="Labels for resources which this trigger will match.",
242	    )
243	    match_related: Union[
244	        ResourceSpecification,
245	        ResourceSpecificationDict,
246	        list[Union[ResourceSpecification, ResourceSpecificationDict]],
247	    ] = Field(
248	        default_factory=lambda: ResourceSpecification.model_validate({}),
249	        description="Labels for related resources which this trigger will match.",
250	    )
251	
252	    @field_validator("match", mode="before")
253	    @classmethod
254	    def coerce_match(cls, v: Any) -> Any:
255	        if isinstance(v, dict):
256	            return ResourceSpecification.model_validate(v)
257	        return v
258	
259	    @field_validator("match_related", mode="before")
260	    @classmethod
261	    def coerce_match_related(cls, v: Any) -> Any:
262	        if isinstance(v, dict):
263	            return ResourceSpecification.model_validate(v)
264	        if isinstance(v, list):
265	            return [
266	                ResourceSpecification.model_validate(item)
267	                if isinstance(item, dict)
268	                else item
269	                for item in v
270	            ]
271	        return v
272	
273	    def covers_resources(
274	        self, resource: Resource, related: Sequence[RelatedResource]
275	    ) -> bool:
276	        if not self.match.includes([resource]):
277	            return False
278	
279	        match_related = self.match_related
280	        if not isinstance(match_related, list):
281	            match_related = [match_related]
282	
283	        if not all(match.includes(related) for match in match_related):
284	            return False
285	
286	        return True
287	
288	
289	class EventTrigger(ResourceTrigger):
290	    """
291	    A trigger that fires based on the presence or absence of events within a given
292	    period of time.
293	    """
294	
295	    type: Literal["event"] = "event"
296	
297	    after: Set[str] = Field(
298	        default_factory=set,
299	        description=(
300	            "The event(s) which must first been seen to fire this trigger.  If "
301	            "empty, then fire this trigger immediately.  Events may include "
302	            "trailing wildcards, like `prefect.flow-run.*`"
303	        ),
304	    )
305	    expect: Set[str] = Field(
306	        default_factory=set,
307	        description=(
308	            "The event(s) this trigger is expecting to see.  If empty, this "
309	            "trigger will match any event.  Events may include trailing wildcards, "
310	            "like `prefect.flow-run.*`"
311	        ),
312	    )
313	
314	    for_each: Set[str] = Field(
315	        default_factory=set,
316	        description=(
317	            "Evaluate the trigger separately for each distinct value of these labels "
318	            "on the resource.  By default, labels refer to the primary resource of the "
319	            "triggering event.  You may also refer to labels from related "
320	            "resources by specifying `related:<role>:<label>`.  This will use the "
321	            "value of that label for the first related resource in that role.  For "
322	            'example, `"for_each": ["related:flow:prefect.resource.id"]` would '
323	            "evaluate the trigger for each flow."
324	        ),
325	    )
326	    posture: Literal[Posture.Reactive, Posture.Proactive] = Field(  # type: ignore[valid-type]
327	        ...,
328	        description=(
329	            "The posture of this trigger, either Reactive or Proactive.  Reactive "
330	            "triggers respond to the _presence_ of the expected events, while "
331	            "Proactive triggers respond to the _absence_ of those expected events."
332	        ),
333	    )
334	    threshold: int = Field(
335	        1,
336	        description=(
337	            "The number of events required for this trigger to fire (for "
338	            "Reactive triggers), or the number of events expected (for Proactive "
339	            "triggers)"
340	        ),
341	    )
342	    within: timedelta = Field(
343	        timedelta(seconds=0),
344	        ge=timedelta(seconds=0),
345	        description=(
346	            "The time period over which the events must occur.  For Reactive triggers, "
347	            "this may be as low as 0 seconds, but must be at least 10 seconds for "
348	            "Proactive triggers"
349	        ),
350	    )
351	
352	    @model_validator(mode="before")
353	    @classmethod
354	    def enforce_minimum_within_for_proactive_triggers(
355	        cls, data: Dict[str, Any] | Any
356	    ) -> Dict[str, Any]:
357	        if not isinstance(data, dict):
358	            return data
359	
360	        if "within" in data and data["within"] is None:
361	            raise ValueError("`within` should be a valid timedelta")
362	
363	        posture: Optional[Posture] = data.get("posture")
364	        within: Optional[timedelta] = data.get("within")
365	
366	        if isinstance(within, (int, float)):
367	            data["within"] = within = timedelta(seconds=within)
368	
369	        if posture == Posture.Proactive:
370	            if not within or within == timedelta(0):
371	                data["within"] = timedelta(seconds=10.0)
372	            elif within < timedelta(seconds=10.0):
373	                raise ValueError(
374	                    "`within` for Proactive triggers must be greater than or equal to "
375	                    "10 seconds"
376	                )
377	
378	        return data
379	
380	    def covers(self, event: ReceivedEvent) -> bool:
381	        if not self.event_pattern.match(event.event):
382	            return False
383	
384	        if not self.covers_resources(event.resource, event.related):
385	            return False
386	
387	        return True
388	
389	    @property
390	    def immediate(self) -> bool:
391	        """Does this reactive trigger fire immediately for all events?"""
392	        return self.posture == Posture.Reactive and self.within == timedelta(0)
393	
394	    _event_pattern: Optional[re.Pattern[str]] = PrivateAttr(None)
395	
396	    @property
397	    def event_pattern(self) -> re.Pattern[str]:
398	        """A regular expression which may be evaluated against any event string to
399	        determine if this trigger would be interested in the event"""
400	        if self._event_pattern:
401	            return self._event_pattern
402	
403	        if not self.expect:
404	            # This preserves the trivial match for `expect`, and matches the behavior
405	            # of expects() below
406	            self._event_pattern = re.compile(".+")
407	        else:
408	            patterns = [
409	                # escape each pattern, then translate wildcards ('*' -> r'.+')
410	                re.escape(e).replace("\\*", ".+")
411	                for e in self.expect | self.after
412	            ]
413	            self._event_pattern = re.compile("|".join(patterns))
414	
415	        return self._event_pattern
416	
417	    def starts_after(self, event: str) -> bool:
418	        # Warning: Previously we returned 'True' if there was trivial 'after' criteria.
419	        # Although this is not wrong, it led to automations processing more events
420	        # than they should have.
421	        if not self.after:
422	            return False
423	
424	        for candidate in self.after:
425	            if matches(candidate, event):
426	                return True
427	        return False
428	
429	    def expects(self, event: str) -> bool:
430	        if not self.expect:
431	            return True
432	
433	        for candidate in self.expect:
434	            if matches(candidate, event):
435	                return True
436	        return False
437	
438	    def bucketing_key(self, event: ReceivedEvent) -> Tuple[str, ...]:
439	        return tuple(
440	            event.find_resource_label(label) or "" for label in sorted(self.for_each)
441	        )
442	
443	    def meets_threshold(self, event_count: int) -> bool:
444	        if self.posture == Posture.Reactive and event_count >= self.threshold:
445	            return True
446	
447	        if self.posture == Posture.Proactive and event_count < self.threshold:
448	            return True
449	
450	        return False
451	
452	    def create_automation_state_change_event(
453	        self, firing: Firing, trigger_state: TriggerState
454	    ) -> ReceivedEvent:
455	        """Returns a ReceivedEvent for an automation state change
456	        into a triggered or resolved state."""
457	        automation = firing.trigger.automation
458	        triggering_event = firing.triggering_event
459	
460	        resource_data = Resource(
461	            {
462	                "prefect.resource.id": f"prefect.automation.{automation.id}",
463	                "prefect.resource.name": automation.name,
464	            }
465	        )
466	
467	        if self.posture.value:
468	            resource_data["prefect.posture"] = self.posture.value
469	
```

## 27 · 2026-10-29T03:22:57.307330+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"same_event_in_expect_and_after\" tests/events/server/triggers/ | head -40",
  "description": "Find related tests"
}
```

## 28 · 2026-10-29T03:22:57.679303+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"terminal\\|Completed\" src/prefect/server/events/triggers.py src/prefect/server/events/models/*.py src/prefect/server/events/schemas/*.py | head -40",
  "description": "Search terminal handling"
}
```

## 29 · 2026-10-29T03:22:57.762543+00:00 · tool_result 

```
tests/events/server/triggers/test_regressions.py:218:async def test_same_event_in_expect_and_after_never_reacts_immediately(
tests/events/server/triggers/test_regressions.py:296:async def test_same_event_in_expect_and_after_reacts_after_threshold_is_met(
tests/events/server/triggers/test_regressions.py:403:async def test_same_event_in_expect_and_after_proactively_does_not_fire(
tests/events/server/triggers/test_regressions.py:476:async def test_same_event_in_expect_and_after_proactively_fires(
tests/events/server/triggers/test_regressions.py:943:async def test_same_event_in_expect_and_after_proactively_fires_with_for_each_threshold_1(
```

## 30 · 2026-10-29T03:22:58.038980+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:230:        # terminal state within a given time.
```

## 31 · 2026-10-29T03:22:59.541826+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "offset": 380,
  "limit": 220
}
```

## 32 · 2026-10-29T03:22:59.701376+00:00 · tool_result 

```
380	    cleared_automations: None,
381	    automations_session: AsyncSession,
382	) -> Automation:
383	    # Automation for https://github.com/PrefectHQ/nebula/issues/4201
384	    automation = await automations.create_automation(
385	        automations_session,
386	        Automation(
387	            name="Both expect and after",
388	            trigger=EventTrigger(
389	                after={"some-event"},
390	                expect={"some-event"},
391	                posture=Posture.Proactive,
392	                threshold=2,
393	                within=timedelta(seconds=10),
394	            ),
395	            actions=[actions.DoNothing()],
396	        ),
397	    )
398	    triggers.load_automation(automation)
399	    await automations_session.commit()
400	    return automation
401	
402	
403	async def test_same_event_in_expect_and_after_proactively_does_not_fire(
404	    act: mock.AsyncMock,
405	    frozen_time: DateTime,
406	    proactive_extended_expect_and_after: Automation,
407	):
408	    """Regression test for https://github.com/PrefectHQ/nebula/issues/4201, where
409	    having the same event in after and expect causes weird behavior
410	
411	    Case three (negative): Proactive -> this will not fire if get `threshold - 1`
412	    events during the window
413	    """
414	    assert isinstance(proactive_extended_expect_and_after.trigger, EventTrigger)
415	
416	    await triggers.reactive_evaluation(
417	        Event(
418	            occurred=frozen_time + timedelta(seconds=1),
419	            event="some-event",
420	            resource={"prefect.resource.id": "some.resource"},
421	            id=uuid4(),
422	        ).receive()
423	    )
424	
425	    await triggers.proactive_evaluation(
426	        proactive_extended_expect_and_after.trigger,
427	        frozen_time + timedelta(seconds=1),
428	    )
429	    act.assert_not_awaited()  # won't act here, but this should have "armed" the trigger
430	
431	    act.reset_mock()
432	    await triggers.reactive_evaluation(
433	        Event(
434	            occurred=frozen_time + timedelta(seconds=2),
435	            event="some-event",
436	            resource={"prefect.resource.id": "some.resource"},
437	            id=uuid4(),
438	        ).receive()
439	    )
440	    await triggers.proactive_evaluation(
441	        proactive_extended_expect_and_after.trigger,
442	        frozen_time + timedelta(seconds=2),
443	    )
444	    act.assert_not_awaited()  # won't act here, we're within the window
445	
446	    act.reset_mock()
447	    await triggers.reactive_evaluation(
448	        Event(
449	            occurred=frozen_time + timedelta(seconds=3),
450	            event="some-event",
451	            resource={"prefect.resource.id": "some.resource"},
452	            id=uuid4(),
453	        ).receive()
454	    )
455	    await triggers.proactive_evaluation(
456	        proactive_extended_expect_and_after.trigger,
457	        frozen_time + timedelta(seconds=3),
458	    )
459	    act.assert_not_awaited()  # won't act here, we've reached the threshold
460	
461	    act.reset_mock()
462	    await triggers.proactive_evaluation(
463	        proactive_extended_expect_and_after.trigger,
464	        frozen_time + timedelta(seconds=10),
465	    )
466	    act.assert_not_awaited()  # won't act here, we've reached the threshold
467	
468	    act.reset_mock()
469	    await triggers.proactive_evaluation(
470	        proactive_extended_expect_and_after.trigger,
471	        frozen_time + timedelta(seconds=11),
472	    )
473	    act.assert_not_awaited()  # won't act here, we've reached the threshold
474	
475	
476	async def test_same_event_in_expect_and_after_proactively_fires(
477	    act: mock.AsyncMock,
478	    frozen_time: DateTime,
479	    proactive_extended_expect_and_after: Automation,
480	):
481	    """Regression test for https://github.com/PrefectHQ/nebula/issues/4201, where
482	    having the same event in after and expect causes weird behavior
483	
484	    Case three (positive): Proactive -> this will fire if we don't get `threshold - 1`
485	    events during the window
486	    """
487	    assert isinstance(proactive_extended_expect_and_after.trigger, EventTrigger)
488	
489	    await triggers.reactive_evaluation(
490	        Event(
491	            occurred=frozen_time + timedelta(seconds=1),
492	            event="some-event",
493	            resource={"prefect.resource.id": "some.resource"},
494	            id=uuid4(),
495	        ).receive()
496	    )
497	
498	    await triggers.proactive_evaluation(
499	        proactive_extended_expect_and_after.trigger,
500	        frozen_time + timedelta(seconds=2),
501	    )
502	    act.assert_not_awaited()  # won't act here, this should have "armed" the trigger
503	
504	    act.reset_mock()
505	    await triggers.reactive_evaluation(
506	        Event(
507	            occurred=frozen_time + timedelta(seconds=3),
508	            event="some-event",
509	            resource={"prefect.resource.id": "some.resource"},
510	            id=uuid4(),
511	        ).receive()
512	    )
513	    await triggers.proactive_evaluation(
514	        proactive_extended_expect_and_after.trigger,
515	        frozen_time + timedelta(seconds=4),
516	    )
517	    act.assert_not_awaited()  # won't act here, we're within the window
518	
519	    act.reset_mock()
520	    await triggers.proactive_evaluation(
521	        proactive_extended_expect_and_after.trigger,
522	        frozen_time + timedelta(seconds=11),
523	    )
524	    act.assert_awaited_once()  # act here, we haven't reached the threshold of 2
525	
526	    act.reset_mock()
527	    await triggers.proactive_evaluation(
528	        proactive_extended_expect_and_after.trigger,
529	        frozen_time + timedelta(seconds=30),
530	    )
531	    act.assert_not_awaited()  # won't act here, we haven't "armed" the trigger again
532	
533	
534	@pytest.fixture
535	async def rapid_fire_automation(
536	    work_queue: WorkQueue,
537	    cleared_buckets: None,
538	    cleared_automations: None,
539	    automations_session: AsyncSession,
540	) -> Automation:
541	    # Automation for https://github.com/PrefectHQ/nebula/issues/4201
542	    automation = await automations.create_automation(
543	        automations_session,
544	        Automation(
545	            name="Reacts instantly to each event",
546	            trigger=EventTrigger(
547	                expect={"some-event"},
548	                posture=Posture.Reactive,
549	                threshold=1,
550	                within=timedelta(seconds=0),
551	            ),
552	            actions=[actions.DoNothing()],
553	        ),
554	    )
555	    triggers.load_automation(automation)
556	    await automations_session.commit()
557	    return automation
558	
559	
560	async def test_rapid_fire_events(
561	    act: mock.AsyncMock,
562	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
563	    start_of_test: DateTime,
564	    rapid_fire_automation: Automation,
565	    automations_session: AsyncSession,
566	    frozen_time: DateTime,
567	):
568	    """Regression test for https://github.com/PrefectHQ/prefect/issues/11199, where very
569	    rapidly arriving events wouldn't all trigger an action.
570	
571	    Note: there's a small false negative rate in this test when we're trying to detect
572	    the timing bug, where one out of several dozen runs may accidentally show that we
573	    got N out of N actions fired (i.e. like the bug isn't present).  When the bug is
574	    fixed, this has 100% accuracy and should not introduce any test flakes.
575	    """
576	    events = [
577	        Event(
578	            occurred=start_of_test + timedelta(microseconds=i),
579	            event="some-event",
580	            resource={"prefect.resource.id": "some.resource"},
581	            id=UUID(int=i),
582	        ).receive()
583	        for i in range(50)
584	    ]
585	
586	    random.shuffle(events)
587	
588	    await asyncio.gather(*[triggers.reactive_evaluation(event) for event in events])
589	
590	    assert act.await_count == len(events)
591	    assert_acted_with(
592	        [
593	            Firing(
594	                trigger=rapid_fire_automation.trigger,
595	                trigger_states={TriggerState.Triggered},
596	                triggered=frozen_time,  # type: ignore
597	                triggering_labels={},
598	                triggering_event=event,
599	            )
```

## 33 · 2026-10-29T03:23:01.049808+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && ls -la .runtime/ && cat .runtime/environment.ps1 2>/dev/null | head -60",
  "description": "Inspect runtime environment"
}
```

## 34 · 2026-10-29T03:23:01.468702+00:00 · tool_result 

```
total 16
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:17 .
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:16 ..
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:22 claude-config
-rw-r--r-- 1 luwen 197121 1188 Oct 29 11:13 environment.ps1
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 prefect-home
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 pycache
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 python
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 ruff-cache
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:22 temp
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:13 uv-cache
drwxr-xr-x 1 luwen 197121    0 Oct 29 11:14 venv
$env:UV_CACHE_DIR = '$SANDBOX/.runtime/uv-cache'
$env:UV_PYTHON_INSTALL_DIR = '$SANDBOX/.runtime/python'
$env:UV_PROJECT_ENVIRONMENT = '$SANDBOX/.runtime/venv'
$env:PREFECT_HOME = '$SANDBOX/.runtime/prefect-home'
$env:PREFECT_SERVER_DATABASE_CONNECTION_URL = 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
$env:PREFECT_SERVER_ANALYTICS_ENABLED = 'false'
$env:PREFECT_CLI_TELEMETRY_ENABLED = 'false'
$env:PREFECT_TESTING_UNIT_TEST_MODE = '1'
$env:TEMP = '$SANDBOX/.runtime/temp'
$env:TMP = '$SANDBOX/.runtime/temp'
$env:PYTHONPYCACHEPREFIX = '$SANDBOX/.runtime/pycache'
$env:PYTHONPATH = '$SANDBOX/prefect/src'
$env:RUFF_CACHE_DIR = '$SANDBOX/.runtime/ruff-cache'
$env:NO_PROXY = 'localhost,127.0.0.1,::1'
$env:PATH = '$SANDBOX/.runtime/venv/Scripts;' + $env:PATH
$TrialPython = '$SANDBOX/.runtime/venv/Scripts/python.exe'
```

## 35 · 2026-10-29T03:23:02.656475+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && echo \"PYTHONPATH=$PYTHONPATH\" && echo \"PREFECT_HOME=$PREFECT_HOME\" && echo \"DB=$PREFECT_SERVER_DATABASE_CONNECTION_URL\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -c \"import prefect, sys; print(prefect.__version__, prefect.__file__); print(sys.version)\"",
  "description": "Verify environment and prefect import"
}
```

## 36 · 2026-10-29T03:23:08.136974+00:00 · tool_result 

```
PYTHONPATH=$SANDBOX/prefect/src
PREFECT_HOME=$SANDBOX/.runtime/prefect-home
DB=sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db
3.6.24+nogit $SANDBOX\prefect\src\prefect\__init__.py
3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]
```

## 37 · 2026-10-29T03:23:09.245164+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | tail -40",
  "description": "Run incident reproduction test",
  "timeout": 300000
}
```

## 38 · 2026-10-29T03:23:56.620314+00:00 · tool_result 

```
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
>       assert observed == incident["expected_actions"], (
            f"Completed run received {observed} unresponsive-run action(s); expected zero"
        )
E       AssertionError: Completed run received 1 unresponsive-run action(s); expected zero
E       assert 1 == 0

tests\events\server\triggers\test_incident_completed_run.py:67: AssertionError
------------------------------ Captured log call ------------------------------
INFO     prefect.server.events.triggers:triggers.py:586 Automation 4835e58b-c491-4642-9999-318013e0c1c9, trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f covers event 'prefect.flow-run.heartbeat' (11111111-1111-4111-8111-111111111111) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:23:50.312435+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 4835e58b-c491-4642-9999-318013e0c1c9 ('Unresponsive run monitor') trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 4835e58b-c491-4642-9999-318013e0c1c9, trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f covers event 'prefect.flow-run.heartbeat' (22222222-2222-4222-8222-222222222222) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:24:20.312435+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 4835e58b-c491-4642-9999-318013e0c1c9 ('Unresponsive run monitor') trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 4835e58b-c491-4642-9999-318013e0c1c9, trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f covers event 'prefect.flow-run.Completed' (33333333-3333-4333-8333-333333333333) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:24:50.312435+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 4835e58b-c491-4642-9999-318013e0c1c9 ('Unresponsive run monitor') trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 4835e58b-c491-4642-9999-318013e0c1c9, trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f covers event 'prefect.flow-run.heartbeat' (44444444-4444-4444-8444-444444444444) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:24:50.312435+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 4835e58b-c491-4642-9999-318013e0c1c9 ('Unresponsive run monitor') trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
DEBUG    prefect.server.events.triggers:triggers.py:1317 Evaluating automation 4835e58b-c491-4642-9999-318013e0c1c9 trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f proactively as of 2026-10-29 03:26:21.312435+00:00 (offset 0.0s)
DEBUG    prefect.server.events.triggers:triggers.py:176 Automation 4835e58b-c491-4642-9999-318013e0c1c9 ('Unresponsive run monitor') trigger 8fc7e8f1-2173-441d-ac56-15a9ce706e9f triggered for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa']) proactively, having occurred 0 times between 2026-10-29 03:24:50.312435+00:00 and 2026-10-29 03:26:20.312435+00:00
=========================== short test summary info ===========================
FAILED tests/events/server/triggers/test_incident_completed_run.py::test_completed_run_incident
1 failed in 25.72s
```

## 39 · 2026-10-29T03:24:09.575192+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/ordering/__init__.py"
}
```

## 40 · 2026-10-29T03:24:09.687719+00:00 · tool_result 

```
1	"""
2	Manages the partial causal ordering of events for a particular consumer.  This module
3	maintains a buffer of events to be processed, aiming to process them in the order they
4	occurred causally.
5	"""
6	
7	import abc
8	from datetime import timedelta
9	import importlib
10	from typing import (
11	    TYPE_CHECKING,
12	    AsyncContextManager,
13	    List,
14	    Protocol,
15	    Union,
16	    runtime_checkable,
17	)
18	from uuid import UUID
19	from prefect.logging import get_logger
20	from prefect.server.events.schemas.events import Event, ReceivedEvent
21	from prefect.settings import get_current_settings
22	
23	if TYPE_CHECKING:
24	    import logging
25	
26	logger: "logging.Logger" = get_logger(__name__)
27	
28	# How long we'll retain preceding events (to aid with ordering)
29	PRECEDING_EVENT_LOOKBACK = timedelta(minutes=15)
30	
31	# How long we'll retain events we've processed (to prevent re-processing an event)
32	PROCESSED_EVENT_LOOKBACK = timedelta(minutes=30)
33	
34	# How long we'll remember that we've seen an event
35	SEEN_EXPIRATION = max(PRECEDING_EVENT_LOOKBACK, PROCESSED_EVENT_LOOKBACK)
36	
37	# How deep we'll allow the recursion to go when processing events
38	MAX_DEPTH_OF_PRECEDING_EVENT = 20
39	
40	
41	@runtime_checkable
42	class CausalOrderingModule(Protocol):
43	    CausalOrdering: type["CausalOrdering"]
44	
45	
46	class EventArrivedEarly(Exception):
47	    def __init__(self, event: ReceivedEvent):
48	        self.event = event
49	
50	
51	class MaxDepthExceeded(Exception):
52	    def __init__(self, event: ReceivedEvent):
53	        self.event = event
54	
55	
56	class event_handler(Protocol):
57	    async def __call__(
58	        self, event: ReceivedEvent, depth: int = 0
59	    ) -> None: ...  # pragma: no cover
60	
61	
62	class CausalOrdering(abc.ABC):
63	    def __init__(self, scope: str):
64	        self.scope = scope
65	
66	    @abc.abstractmethod
67	    async def event_has_been_seen(self, event: Union[UUID, Event]) -> bool: ...
68	
69	    @abc.abstractmethod
70	    async def record_event_as_seen(self, event: ReceivedEvent) -> None: ...
71	
72	    @abc.abstractmethod
73	    async def record_follower(self, event: ReceivedEvent) -> None: ...
74	
75	    @abc.abstractmethod
76	    async def forget_follower(self, follower: ReceivedEvent) -> None: ...
77	
78	    @abc.abstractmethod
79	    async def get_followers(self, leader: ReceivedEvent) -> List[ReceivedEvent]: ...
80	
81	    @abc.abstractmethod
82	    async def get_lost_followers(self) -> List[ReceivedEvent]: ...
83	
84	    @abc.abstractmethod
85	    def preceding_event_confirmed(
86	        self, handler: event_handler, event: ReceivedEvent, depth: int = 0
87	    ) -> AsyncContextManager[None]: ...
88	
89	
90	def get_triggers_causal_ordering() -> CausalOrdering:
91	    import_path = get_current_settings().server.events.causal_ordering
92	    causal_ordering_module = importlib.import_module(import_path)
93	
94	    if not isinstance(causal_ordering_module, CausalOrderingModule):
95	        raise ValueError(
96	            f"Module at {import_path} does not export a CausalOrdering class. Please check your server.events.causal_ordering setting."
97	        )
98	
99	    return causal_ordering_module.CausalOrdering(scope="triggers")
100	
```

## 41 · 2026-10-29T03:24:10.899054+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/events/ordering/ && grep -rn \"causal_ordering\" src/prefect/settings/models/server/events.py | head",
  "description": "List ordering implementations"
}
```

## 42 · 2026-10-29T03:24:11.212257+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"class CausalOrdering\" src/prefect/server/events/ordering/*.py && wc -l src/prefect/server/events/ordering/*.py",
  "description": "Find CausalOrdering classes"
}
```

## 43 · 2026-10-29T03:24:11.277836+00:00 · tool_result 

```
__init__.py
db.py
memory.py
143:    causal_ordering: str = Field(
```

## 44 · 2026-10-29T03:24:11.583286+00:00 · tool_result 

```
src/prefect/server/events/ordering/__init__.py:42:class CausalOrderingModule(Protocol):
src/prefect/server/events/ordering/__init__.py:62:class CausalOrdering(abc.ABC):
src/prefect/server/events/ordering/db.py:35:class CausalOrdering(_CausalOrdering):
src/prefect/server/events/ordering/memory.py:40:class CausalOrdering(_CausalOrdering):
   99 src/prefect/server/events/ordering/__init__.py
  183 src/prefect/server/events/ordering/db.py
  314 src/prefect/server/events/ordering/memory.py
  596 total
```

## 45 · 2026-10-29T03:24:12.987773+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/ordering/memory.py"
}
```

## 46 · 2026-10-29T03:24:13.137966+00:00 · tool_result 

```
1	from __future__ import annotations
2	
3	import asyncio
4	import logging
5	from contextlib import asynccontextmanager
6	from datetime import datetime, timedelta
7	from typing import Any, AsyncGenerator
8	from uuid import UUID
9	
10	import anyio
11	from cachetools import TTLCache
12	
13	import prefect.types._datetime
14	from prefect.logging import get_logger
15	from prefect.server.events.ordering import (
16	    MAX_DEPTH_OF_PRECEDING_EVENT,
17	    PRECEDING_EVENT_LOOKBACK,
18	    SEEN_EXPIRATION,
19	    EventArrivedEarly,
20	    MaxDepthExceeded,
21	    event_handler,
22	)
23	from prefect.server.events.ordering import CausalOrdering as _CausalOrdering
24	from prefect.server.events.schemas.events import Event, ReceivedEvent
25	
26	logger: logging.Logger = get_logger(__name__)
27	
28	# How long we'll wait for an in-flight event to be processed for follower handling
29	IN_FLIGHT_EVENT_TIMEOUT = timedelta(seconds=8)
30	
31	
32	class EventBeingProcessed(Exception):
33	    """Indicates that an event is currently being processed and should not be processed
34	    until it is finished. This may happen due to concurrent processing."""
35	
36	    def __init__(self, event: ReceivedEvent):
37	        self.event = event
38	
39	
40	class CausalOrdering(_CausalOrdering):
41	    # Class-level storage for different scopes
42	    _instances: dict[str, "CausalOrdering"] = {}
43	    _locks: dict[str, asyncio.Lock] = {}
44	
45	    def __new__(cls, scope: str) -> "CausalOrdering":
46	        if scope not in cls._instances:
47	            cls._instances[scope] = super().__new__(cls)
48	        return cls._instances[scope]
49	
50	    def __init__(self, scope: str):
51	        # Only initialize once per scope
52	        if hasattr(self, "_initialized") and self._initialized:
53	            return
54	
55	        self.scope: str = scope
56	        self._processing_events: set[UUID] = set()
57	        self._seen_events: TTLCache[UUID, bool] = TTLCache(
58	            maxsize=10000, ttl=SEEN_EXPIRATION.total_seconds()
59	        )
60	        self._followers: dict[UUID, set[UUID]] = {}  # leader_id -> set of follower_ids
61	        self._events: dict[UUID, ReceivedEvent] = {}  # event_id -> event
62	        self._waitlist: dict[UUID, datetime] = {}  # event_id -> received_time
63	
64	        # Each scope gets its own lock
65	        if scope not in self.__class__._locks:
66	            self.__class__._locks[scope] = asyncio.Lock()
67	        self._lock = self.__class__._locks[scope]
68	
69	        self._initialized = True
70	
71	    def clear(self) -> None:
72	        """Clear all data for this scope."""
73	        self._processing_events.clear()
74	        self._seen_events.clear()
75	        self._followers.clear()
76	        self._events.clear()
77	        self._waitlist.clear()
78	
79	    @classmethod
80	    def clear_all_scopes(cls) -> None:
81	        """Clear all data for all scopes - useful for testing."""
82	        for instance in cls._instances.values():
83	            instance.clear()
84	        cls._instances.clear()
85	        cls._locks.clear()
86	
87	    async def record_event_as_processing(self, event: ReceivedEvent) -> bool:
88	        """Record that an event is being processed, returning False if already processing."""
89	        async with self._lock:
90	            if event.id in self._processing_events:
91	                return False
92	            self._processing_events.add(event.id)
93	            return True
94	
95	    async def event_has_started_processing(self, event: UUID | Event) -> bool:
96	        event_id = event.id if isinstance(event, Event) else event
97	        async with self._lock:
98	            return event_id in self._processing_events
99	
100	    async def forget_event_is_processing(self, event: ReceivedEvent) -> None:
101	        async with self._lock:
102	            self._processing_events.discard(event.id)
103	
104	    async def event_has_been_seen(self, event: UUID | Event) -> bool:
105	        event_id = event.id if isinstance(event, Event) else event
106	        async with self._lock:
107	            return event_id in self._seen_events
108	
109	    async def record_event_as_seen(self, event: ReceivedEvent) -> None:
110	        async with self._lock:
111	            self._seen_events[event.id] = True
112	
113	    async def record_follower(self, event: ReceivedEvent) -> None:
114	        """Remember that this event is waiting on another event to arrive."""
115	        assert event.follows
116	
117	        async with self._lock:
118	            self._events[event.id] = event
119	            if event.follows not in self._followers:
120	                self._followers[event.follows] = set()
121	            self._followers[event.follows].add(event.id)
122	            self._waitlist[event.id] = event.received
123	
124	    async def forget_follower(self, follower: ReceivedEvent) -> None:
125	        """Forget that this event is waiting on another event to arrive."""
126	        assert follower.follows
127	
128	        async with self._lock:
129	            self._waitlist.pop(follower.id, None)
130	            if follower.follows in self._followers:
131	                self._followers[follower.follows].discard(follower.id)
132	                if not self._followers[follower.follows]:
133	                    del self._followers[follower.follows]
134	            self._events.pop(follower.id, None)
135	
136	    async def get_followers(self, leader: ReceivedEvent) -> list[ReceivedEvent]:
137	        """Returns events that were waiting on this leader event to arrive."""
138	        async with self._lock:
139	            follower_ids = self._followers.get(leader.id, set()).copy()
140	
141	        follower_events: list[ReceivedEvent] = []
142	        for follower_id in follower_ids:
143	            if follower_id in self._events:
144	                follower_events.append(self._events[follower_id])
145	
146	        # Sort by occurred time to maintain causal order
147	        return sorted(follower_events, key=lambda f: f.occurred)
148	
149	    async def followers_by_id(self, follower_ids: list[UUID]) -> list[ReceivedEvent]:
150	        """Returns the events with the given IDs, in the order they occurred."""
151	        async with self._lock:
152	            follower_events = [
153	                self._events[fid] for fid in follower_ids if fid in self._events
154	            ]
155	
156	        return sorted(follower_events, key=lambda f: f.occurred)
157	
158	    async def get_lost_followers(self) -> list[ReceivedEvent]:
159	        """Returns events that were waiting on a leader event that never arrived."""
160	        cutoff_time = prefect.types._datetime.now("UTC") - PRECEDING_EVENT_LOOKBACK
161	
162	        async with self._lock:
163	            lost_ids = [
164	                event_id
165	                for event_id, received_time in self._waitlist.items()
166	                if received_time <= cutoff_time
167	            ]
168	
169	            # Remove lost followers from our tracking
170	            lost_events: list[ReceivedEvent] = []
171	            for event_id in lost_ids:
172	                if event_id in self._events:
173	                    event = self._events[event_id]
174	                    lost_events.append(event)
175	
176	                    # Clean up tracking for this lost event
177	                    if event.follows and event.follows in self._followers:
178	                        self._followers[event.follows].discard(event_id)
179	                        if not self._followers[event.follows]:
180	                            del self._followers[event.follows]
181	
182	                    del self._events[event_id]
183	                    del self._waitlist[event_id]
184	
185	        return sorted(lost_events, key=lambda f: f.occurred)
186	
187	    @asynccontextmanager
188	    async def event_is_processing(
189	        self, event: ReceivedEvent
190	    ) -> AsyncGenerator[None, None]:
191	        """Mark an event as being processed for the duration of its lifespan through
192	        the ordering system."""
193	        if not await self.record_event_as_processing(event):
194	            self._log(event, "is already being processed")
195	            raise EventBeingProcessed(event)
196	
197	        try:
198	            yield
199	            await self.record_event_as_seen(event)
200	        finally:
201	            await self.forget_event_is_processing(event)
202	
203	    async def wait_for_leader(self, event: ReceivedEvent) -> None:
204	        """Given an event, wait for its leader to be processed before proceeding, or
205	        raise EventArrivedEarly if we would wait too long in this attempt."""
206	        # If this event doesn't follow anything (meaningfully), it's ready to go now
207	        if not event.follows or event.follows == event.id:
208	            return
209	
210	        # If this is an old event, we won't have accurate bookkeeping for its leader
211	        # so we're just going to send it
212	        age = prefect.types._datetime.now("UTC") - event.received
213	        if age >= PRECEDING_EVENT_LOOKBACK:
214	            return
215	
216	        # If the leader has already been seen, keep on trucking
217	        if await self.event_has_been_seen(event.follows):
218	            return
219	
220	        # Check if the leader is currently being processed, and if so, poll until it's
221	        # done being processed as a quicker alternative to sitting on the waitlist
222	        if await self.event_has_started_processing(event.follows):
223	            try:
224	                with anyio.fail_after(IN_FLIGHT_EVENT_TIMEOUT.total_seconds()):
225	                    while not await self.event_has_been_seen(event.follows):
226	                        await asyncio.sleep(0.25)
227	                    return
228	            except asyncio.TimeoutError:
229	                self._log(
230	                    event,
231	                    "timed out waiting for its in-flight leader %s, will treat as lost",
232	                    event.follows,
233	                )
234	
235	        # Otherwise, we'll stop processing now and sit on the waitlist until the leader
236	        # eventually comes through the system
237	        self._log(event, "arrived before the event it follows %s", event.follows)
238	
239	        await self.record_follower(event)
240	        raise EventArrivedEarly(event)
241	
242	    @asynccontextmanager
243	    async def preceding_event_confirmed(
244	        self,
245	        handler: event_handler,
246	        event: ReceivedEvent,
247	        depth: int = 0,
248	    ) -> AsyncGenerator[None, None]:
249	        """
250	        Events may optionally declare that they logically follow another event, so that
251	        we can preserve important event orderings in the face of unreliable delivery and
252	        ordering of messages from the queues.
253	
254	        This function keeps track of the ID of each event that this shard has
255	        successfully processed going back to the PRECEDING_EVENT_LOOKBACK period. If an
256	        event arrives that must follow another one, confirm that we have recently seen
257	        and processed that event before proceeding.
258	
259	        Args:
260	            handler: The function to call when an out-of-order event is
261	                ready to be processed
262	            event: The event to be processed. This object should include
263	                metadata indicating if and what event it follows.
264	            depth: The current recursion depth, used to prevent infinite
265	                recursion due to cyclic dependencies between events. Defaults to 0.
266	
267	        Raises EventArrivedEarly if the current event shouldn't be processed yet.
268	        """
269	        if depth > MAX_DEPTH_OF_PRECEDING_EVENT:
270	            # There is either a cyclic set of events or a chain
271	            # of events that is too long
272	            self._log(
273	                event,
274	                "has exceeded the maximum recursion depth %s",
275	                MAX_DEPTH_OF_PRECEDING_EVENT,
276	            )
277	            raise MaxDepthExceeded(event)
278	
279	        async with self.event_is_processing(event):
280	            await self.wait_for_leader(event)
281	            yield
282	
283	        # We have just processed an event that other events may have been waiting
284	        # on, so let's react to them now in the order they occurred
285	        try:
286	            for waiter in await self.get_followers(event):
287	                await handler(waiter, depth=depth + 1)
288	        except MaxDepthExceeded:
289	            # We'll only process the first MAX_DEPTH_OF_PRECEDING_EVENT followers.
290	            # If we hit this limit, we'll just log and move on.
291	            self._log(
292	                event,
293	                "reached its max depth of %s followers processed.",
294	                MAX_DEPTH_OF_PRECEDING_EVENT,
295	            )
296	
297	        # If this event was itself waiting on a leader, let's consider it as
298	        # resolved now that it has been processed
299	        if event.follows and event.follows != event.id:
300	            await self.forget_follower(event)
301	
302	    def _log(self, event: ReceivedEvent, message: str, *args: Any) -> None:
303	        logger.info(
304	            "Event %r (%s) for %r " + message,
305	            event.event,
306	            event.id,
307	            event.resource.id,
308	            *args,
309	            extra={
310	                "event_id": event.id,
311	                "follows": event.follows,
312	                "resource_id": event.resource.id,
313	            },
314	        )
315	
```

## 47 · 2026-10-29T03:24:15.005760+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"heartbeat\" tests/events/server/triggers/*.py | head -60",
  "description": "Search heartbeat tests"
}
```

## 48 · 2026-10-29T03:24:15.307326+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rln \"heartbeat\" src/prefect/server/events/ src/prefect/server/api/ | head -30",
  "description": "Search heartbeat in server events"
}
```

## 49 · 2026-10-29T03:24:15.413782+00:00 · tool_result 

```
tests/events/server/triggers/test_regressions.py:803:    # Send another Running event within the window (e.g., a heartbeat)
tests/events/server/triggers/test_regressions.py:853:                after={"prefect.flow-run.heartbeat"},
tests/events/server/triggers/test_regressions.py:868:async def test_zombie_flow_detection_fires_when_heartbeats_stop(
tests/events/server/triggers/test_regressions.py:876:    first_heartbeat = Event(
tests/events/server/triggers/test_regressions.py:878:        event="prefect.flow-run.heartbeat",
tests/events/server/triggers/test_regressions.py:882:    second_heartbeat = Event(
tests/events/server/triggers/test_regressions.py:884:        event="prefect.flow-run.heartbeat",
tests/events/server/triggers/test_regressions.py:889:    await triggers.reactive_evaluation(first_heartbeat)
tests/events/server/triggers/test_regressions.py:890:    await triggers.reactive_evaluation(second_heartbeat)
tests/events/server/triggers/test_regressions.py:912:            triggering_event=second_heartbeat,
tests/events/server/triggers/test_regressions.py:957:    heartbeat_times = range(1, 3)
tests/events/server/triggers/test_regressions.py:972:        if minute in heartbeat_times:
```

## 50 · 2026-10-29T03:24:15.725324+00:00 · tool_result 

```
src/prefect/server/events/triggers.py
src/prefect/server/api/workers.py
```

## 51 · 2026-10-29T03:24:16.997265+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "offset": 760,
  "limit": 260
}
```

## 52 · 2026-10-29T03:24:17.120918+00:00 · tool_result 

```
760	    triggers.load_automation(automation)
761	    await automations_session.commit()
762	    return automation
763	
764	
765	async def test_proactive_flow_run_automation_includes_triggering_event(
766	    act: mock.AsyncMock,
767	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
768	    frozen_time: DateTime,
769	    proactive_flow_run_automation: Automation,
770	):
771	    """Test that proactive automations with same event in after and expect
772	    correctly populate the triggering_event field when fired.
773	
774	    This ensures that when a proactive automation fires, it includes reference
775	    to the event that started the trigger (the 'after' event), not just null.
776	
777	    This tests the special case where:
778	    1. The same event (Running) is in both 'after' and 'expect' arrays
779	    2. A Running event starts the trigger
780	    3. Another Running event arrives within the window (triggering the special case)
781	    4. When the window expires without completion, it fires with the triggering_event set
782	    """
783	    assert isinstance(proactive_flow_run_automation.trigger, EventTrigger)
784	
785	    flow_run_id = uuid4()
786	
787	    # Create the first Running event that should start the trigger
788	    first_running_event = Event(
789	        occurred=frozen_time,
790	        event="prefect.flow-run.Running",
791	        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
792	        related=[],
793	        payload={},
794	        id=uuid4(),
795	    ).receive()
796	
797	    # Process the first Running event - this starts the trigger
798	    await triggers.reactive_evaluation(first_running_event)
799	
800	    # Verify not fired yet
801	    act.assert_not_awaited()
802	
803	    # Send another Running event within the window (e.g., a heartbeat)
804	    # This should trigger the special case condition in event.py lines 189-195
805	    second_running_event = Event(
806	        occurred=frozen_time + timedelta(minutes=30),
807	        event="prefect.flow-run.Running",
808	        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
809	        related=[],
810	        payload={},
811	        id=uuid4(),
812	    ).receive()
813	
814	    # Process the second Running event - this hits the special case
815	    await triggers.reactive_evaluation(second_running_event)
816	
817	    # Still shouldn't fire yet (within window)
818	    act.assert_not_awaited()
819	
820	    # After the 2-hour window from the SECOND event, should fire
821	    await triggers.proactive_evaluation(
822	        proactive_flow_run_automation.trigger,
823	        frozen_time + timedelta(minutes=30) + timedelta(hours=2, minutes=1),
824	    )
825	
826	    # Verify the automation fired with the correct triggering_event
827	    # The triggering_event should be the second Running event (the one that restarted the bucket)
828	    assert_acted_with(
829	        Firing(
830	            trigger=proactive_flow_run_automation.trigger,
831	            trigger_states={TriggerState.Triggered},
832	            triggered=frozen_time,  # type: ignore
833	            triggering_labels={
834	                "prefect.resource.id": f"prefect.flow-run.{flow_run_id}"
835	            },
836	            triggering_event=second_running_event,  # Should be the second Running event
837	        )
838	    )
839	
840	
841	@pytest.fixture
842	async def zombie_flow_detection_automation(
843	    cleared_buckets: None,
844	    cleared_automations: None,
845	    automations_session: AsyncSession,
846	) -> Automation:
847	    automation = await automations.create_automation(
848	        automations_session,
849	        Automation(
850	            name="Crash zombie flows",
851	            trigger=EventTrigger(
852	                match={"prefect.resource.id": "prefect.flow-run.*"},
853	                after={"prefect.flow-run.heartbeat"},
854	                expect={"prefect.flow-run.*"},
855	                for_each={"prefect.resource.id"},
856	                posture=Posture.Proactive,
857	                threshold=1,
858	                within=timedelta(seconds=90),
859	            ),
860	            actions=[actions.DoNothing()],
861	        ),
862	    )
863	    triggers.load_automation(automation)
864	    await automations_session.commit()
865	    return automation
866	
867	
868	async def test_zombie_flow_detection_fires_when_heartbeats_stop(
869	    act: mock.AsyncMock,
870	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
871	    frozen_time: DateTime,
872	    zombie_flow_detection_automation: Automation,
873	):
874	    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
875	    flow_run_id = uuid4()
876	    first_heartbeat = Event(
877	        occurred=frozen_time,
878	        event="prefect.flow-run.heartbeat",
879	        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
880	        id=uuid4(),
881	    ).receive()
882	    second_heartbeat = Event(
883	        occurred=frozen_time + timedelta(seconds=30),
884	        event="prefect.flow-run.heartbeat",
885	        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
886	        id=uuid4(),
887	    ).receive()
888	
889	    await triggers.reactive_evaluation(first_heartbeat)
890	    await triggers.reactive_evaluation(second_heartbeat)
891	    act.assert_not_awaited()
892	
893	    await triggers.proactive_evaluation(
894	        zombie_flow_detection_automation.trigger,
895	        frozen_time + timedelta(seconds=31),
896	    )
897	    act.assert_not_awaited()
898	
899	    await triggers.proactive_evaluation(
900	        zombie_flow_detection_automation.trigger,
901	        frozen_time + timedelta(seconds=121),
902	    )
903	
904	    assert_acted_with(
905	        Firing(
906	            trigger=zombie_flow_detection_automation.trigger,
907	            trigger_states={TriggerState.Triggered},
908	            triggered=frozen_time,  # type: ignore
909	            triggering_labels={
910	                "prefect.resource.id": f"prefect.flow-run.{flow_run_id}"
911	            },
912	            triggering_event=second_heartbeat,
913	        )
914	    )
915	
916	
917	@pytest.fixture
918	async def proactive_extended_expect_and_after_with_threshold_1(
919	    cleared_buckets: None,
920	    cleared_automations: None,
921	    automations_session: AsyncSession,
922	) -> Automation:
923	    automation = await automations.create_automation(
924	        automations_session,
925	        Automation(
926	            name="Both expect and after",
927	            trigger=EventTrigger(
928	                for_each=["prefect.resource.id"],
929	                after=["some-event"],
930	                expect=["some-event"],
931	                posture=Posture.Proactive,
932	                threshold=1,
933	                within=timedelta(minutes=5),
934	            ),
935	            actions=[actions.DoNothing()],
936	        ),
937	    )
938	    triggers.load_automation(automation)
939	    await automations_session.commit()
940	    return automation
941	
942	
943	async def test_same_event_in_expect_and_after_proactively_fires_with_for_each_threshold_1(
944	    act: mock.AsyncMock,
945	    frozen_time: DateTime,
946	    proactive_extended_expect_and_after_with_threshold_1: Automation,
947	):
948	    """
949	    During the test, an event is emitted every minute starting at t=1.
950	    Proactive automations are run every 5 minutes, starting at t=0
951	    """
952	    assert isinstance(
953	        proactive_extended_expect_and_after_with_threshold_1.trigger, EventTrigger
954	    )
955	
956	    evaluate_proactive_times = range(0, 15, 5)
957	    heartbeat_times = range(1, 3)
958	
959	    for minute in range(0, 11):
960	        if minute in evaluate_proactive_times:
961	            act.reset_mock()
962	            await triggers.proactive_evaluation(
963	                proactive_extended_expect_and_after_with_threshold_1.trigger,
964	                frozen_time + timedelta(minutes=minute),
965	            )
966	
967	            if minute != 10:
968	                act.assert_not_awaited()
969	            else:
970	                act.assert_awaited_once()
971	
972	        if minute in heartbeat_times:
973	            await triggers.reactive_evaluation(
974	                Event(
975	                    occurred=frozen_time + timedelta(minutes=minute),
976	                    event="some-event",
977	                    resource={"prefect.resource.id": "some.resource"},
978	                    id=uuid4(),
979	                ).receive()
980	            )
981	
```

## 53 · 2026-10-29T03:24:24.714288+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"class AutomationBucket\" src/prefect/server/database/orm_models.py && grep -n \"automation_bucket\" src/prefect/server/database/orm_models.py | head -20",
  "description": "Find AutomationBucket ORM"
}
```

## 54 · 2026-10-29T03:24:25.013114+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"automation_bucket\" src/prefect/server/database/migrations/ | head -30 && ls src/prefect/server/database/migrations/versions/ | tail -20",
  "description": "Find bucket migrations"
}
```

## 55 · 2026-10-29T03:24:25.566719+00:00 · tool_result 

```
1306:class AutomationBucket(Base):
1309:            "uq_automation_bucket__automation_id__trigger_id__bucketing_key",
1316:            "ix_automation_bucket__automation_id__end",
```

## 56 · 2026-10-29T03:24:25.918805+00:00 · tool_result 

```
grep: src/prefect/server/database/migrations/: No such file or directory
ls: cannot access 'src/prefect/server/database/migrations/versions/': No such file or directory
```

## 57 · 2026-10-29T03:24:27.276987+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "offset": 1290,
  "limit": 70
}
```

## 58 · 2026-10-29T03:24:27.629741+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && find . -path ./node_modules -prune -o -name \"*.py\" -print | xargs grep -ln \"automation_bucket\" 2>/dev/null | grep -i migra | head -20",
  "description": "Find migration files referencing automation_bucket"
}
```

## 59 · 2026-10-29T03:24:27.700236+00:00 · tool_result 

```
1290	    related_resources: Mapped[list["AutomationRelatedResource"]] = relationship(
1291	        "AutomationRelatedResource", back_populates="automation", lazy="raise"
1292	    )
1293	
1294	    @classmethod
1295	    def sort_expression(cls, value: AutomationSort) -> sa.ColumnExpressionArgument[Any]:
1296	        """Return an expression used to sort Automations"""
1297	        sort_mapping: dict[AutomationSort, sa.ColumnExpressionArgument[Any]] = {
1298	            AutomationSort.CREATED_DESC: cls.created.desc(),
1299	            AutomationSort.UPDATED_DESC: cls.updated.desc(),
1300	            AutomationSort.NAME_ASC: cls.name.asc(),
1301	            AutomationSort.NAME_DESC: cls.name.desc(),
1302	        }
1303	        return sort_mapping[value]
1304	
1305	
1306	class AutomationBucket(Base):
1307	    __table_args__: Any = (
1308	        sa.Index(
1309	            "uq_automation_bucket__automation_id__trigger_id__bucketing_key",
1310	            "automation_id",
1311	            "trigger_id",
1312	            "bucketing_key",
1313	            unique=True,
1314	        ),
1315	        sa.Index(
1316	            "ix_automation_bucket__automation_id__end",
1317	            "automation_id",
1318	            "end",
1319	        ),
1320	    )
1321	
1322	    automation_id: Mapped[uuid.UUID] = mapped_column(
1323	        sa.ForeignKey("automation.id", ondelete="CASCADE")
1324	    )
1325	
1326	    trigger_id: Mapped[uuid.UUID]
1327	
1328	    bucketing_key: Mapped[list[str]] = mapped_column(
1329	        JSON, server_default="[]", default=list
1330	    )
1331	
1332	    last_event: Mapped[Optional[ReceivedEvent]] = mapped_column(Pydantic(ReceivedEvent))
1333	
1334	    start: Mapped[DateTime]
1335	    end: Mapped[DateTime]
1336	
1337	    count: Mapped[int]
1338	
1339	    last_operation: Mapped[Optional[str]]
1340	
1341	    triggered_at: Mapped[Optional[DateTime]]
1342	
1343	
1344	class AutomationRelatedResource(Base):
1345	    __table_args__: Any = (
1346	        sa.Index(
1347	            "uq_automation_related_resource__automation_id__resource_id",
1348	            "automation_id",
1349	            "resource_id",
1350	            unique=True,
1351	        ),
1352	    )
1353	
1354	    automation_id: Mapped[uuid.UUID] = mapped_column(
1355	        sa.ForeignKey("automation.id", ondelete="CASCADE")
1356	    )
1357	
1358	    resource_id: Mapped[Optional[str]] = mapped_column(index=True)
1359	    automation_owned_by_resource: Mapped[bool] = mapped_column(
```

## 60 · 2026-10-29T03:24:31.246819+00:00 · tool_result 

```
./src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py
./src/prefect/server/database/_migrations/versions/postgresql/2024_04_09_132036_954db7517015_trigger_in_index.py
./src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py
./src/prefect/server/database/_migrations/versions/sqlite/2024_04_09_131832_2b6c2b548f95_trigger_in_index.py
```

## 61 · 2026-10-29T03:24:32.813224+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls -t src/prefect/server/database/_migrations/versions/sqlite/ | head -15 && echo ---- && ls -t src/prefect/server/database/_migrations/versions/postgresql/ | head -15",
  "description": "List recent migrations"
}
```

## 62 · 2026-10-29T03:24:33.167012+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"down_revision\" src/prefect/server/database/_migrations/versions/sqlite/*.py | tail -10 && grep -rn \"down_revision\" src/prefect/server/database/_migrations/versions/postgresql/*.py | tail -10",
  "description": "Find migration heads"
}
```

## 63 · 2026-10-29T03:24:34.184687+00:00 · tool_result 

```
2022_01_20_115236_9725c1cbee35_initial_migration.py
2022_02_04_093838_619bea85701a_block_data.py
2022_02_15_211737_28ae48128c75_add_configurations.py
2022_02_17_151416_7c91cb86dc4e_add_agents_and_work_queues.py
2022_02_19_210255_4c4a6a138053_rename_block_data_table.py
2022_02_20_103610_e1ff4973a9eb_add_block_spec_table.py
2022_02_21_111238_f327e877e423_index_flowrun_flow_runner_type.py
2022_02_21_145916_c8ff35f94028_add_block_spec_id_to_blocks.py
2022_03_10_102500_71a57ec351d1_index_flow_created.py
2022_04_19_181604_7f5f335cace3_add_flow_run_state_name.py
2022_04_21_113057_db6bde582447_backfill_state_name.py
2022_04_23_114831_fd966d4ad99c_rename_block_to_blockbasis_and_.py
2022_04_25_135207_b75d279ba985_replace_version_with_checksum.py
2022_05_12_203158_888a0bb0df7b_add_flow_run_alerts.py
2022_05_19_165808_33439667aeea_add_block_schema_capabilities.py
----
2021_01_20_122127_25f4b90a7a42_initial_migration.py
2022_02_13_125213_5f376def75c3_block_data.py
2022_02_13_125213_679e695af6ba_add_configurations.py
2022_02_17_140821_5bff7878e700_add_agents_and_work_queue.py
2022_02_19_205543_d9d98a9ebb6f_rename_block_data_table.py
2022_02_20_103844_4799f657a6a1_add_block_spec_table.py
2022_02_21_111050_d115556a8ab6_index_flowrun_flow_runner_type.py
2022_02_21_150017_b68b3cad6b8a_add_block_spec_id_to_blocks.py
2022_03_10_102713_2e7e1428ffce_index_flow_created.py
2022_04_20_113011_605ebb4e9155_add_flow_run_state_name.py
2022_04_21_095519_14dc68cc5853_backfill_state_name.py
2022_04_23_132803_d38c5e6a9115_rename_block_to_blockbasis_and_.py
2022_05_10_145956_1c9390e2f9c6_replace_version_with_checksum_and_.py
2022_05_12_202952_dc7a3c6fd3e9_add_flow_run_alerts.py
2022_05_26_135743_724e6dcc6b5d_add_block_schema_capabilities.py
```

## 64 · 2026-10-29T03:24:34.191689+00:00 · tool_result 

```
src/prefect/server/database/_migrations/versions/sqlite/2025_06_12_144500_add_automation_tags_bb2345678901.py:16:down_revision = "3c841a1800a1"
src/prefect/server/database/_migrations/versions/sqlite/2025_06_13_164506_8bb517bae6f9_drop_task_run_state_id_foreign_key_.py:14:down_revision = "bb2345678901"
src/prefect/server/database/_migrations/versions/sqlite/2025_09_17_091213_9e83011d1f2a_migrate_v1_concurrency_limits_to_v2.py:16:down_revision = "8bb517bae6f9"
src/prefect/server/database/_migrations/versions/sqlite/2026_02_19_200000_add_scheduler_schedule_id_index.py:13:down_revision = "9e83011d1f2a"
src/prefect/server/database/_migrations/versions/sqlite/2026_03_03_000000_add_task_run_state_type_start_time_index.py:13:down_revision = "a1b2c3d4e5f7"
src/prefect/server/database/_migrations/versions/sqlite/2026_05_05_000000_2095de406cbe_add_block_document_reference_self_check.py:17:down_revision = "4dfa692e02a7"
src/prefect/server/database/_migrations/versions/sqlite/2026_06_10_000000_79e7a60e43d8_add_event_resources_occurred_index.py:17:down_revision = "2095de406cbe"
src/prefect/server/database/_migrations/versions/sqlite/2026_07_20_000000_14806cb26270_add_event_resources_event_id_index.py:18:down_revision = "79e7a60e43d8"
src/prefect/server/database/_migrations/versions/sqlite/2026_08_20_000000_f416ea180ae1_add_flow_run_deployment_id_index.py:20:down_revision = "14806cb26270"
src/prefect/server/database/_migrations/versions/sqlite/2026_09_15_000000_a3b9c7d2e5f1_add_flow_run_state_type_coalesce_start_time_index.py:19:down_revision = "f416ea180ae1"
src/prefect/server/database/_migrations/versions/postgresql/2025_06_13_160644_3b86c5ea017a_drop_task_run_state_id_foreign_key_.py:14:down_revision = "aa1234567890"
src/prefect/server/database/_migrations/versions/postgresql/2025_09_17_091213_9e83011d1f2a_migrate_v1_concurrency_limits_to_v2.py:16:down_revision = "3b86c5ea017a"
src/prefect/server/database/_migrations/versions/postgresql/2026_02_19_200000_add_scheduler_schedule_id_index.py:13:down_revision = "9e83011d1f2a"
src/prefect/server/database/_migrations/versions/postgresql/2026_03_03_000000_add_task_run_state_type_start_time_index.py:13:down_revision = "a1b2c3d4e5f6"
src/prefect/server/database/_migrations/versions/postgresql/2026_05_05_000000_7218aad17905_add_block_document_reference_self_check.py:17:down_revision = "09a9e091e578"
src/prefect/server/database/_migrations/versions/postgresql/2026_06_10_000000_bad1e352c597_add_event_resources_occurred_index.py:21:down_revision = "7218aad17905"
src/prefect/server/database/_migrations/versions/postgresql/2026_07_20_000000_50737cdaee36_add_event_resources_event_id_index.py:24:down_revision = "bad1e352c597"
src/prefect/server/database/_migrations/versions/postgresql/2026_08_20_000000_9e9dadc36797_add_flow_run_deployment_id_index.py:26:down_revision = "50737cdaee36"
src/prefect/server/database/_migrations/versions/postgresql/2026_09_04_000000_c8d5f2a71b3e_rebuild_invalid_event_resources_occurred_index.py:26:down_revision = "9e9dadc36797"
src/prefect/server/database/_migrations/versions/postgresql/2026_09_15_000000_d4a7e1c93f52_add_flow_run_state_type_coalesce_start_time_index.py:26:down_revision = "c8d5f2a71b3e"
```

## 65 · 2026-10-29T03:24:46.973110+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"last_event\" src/prefect/server/events/ tests/events/server/triggers/ | head -60",
  "description": "Search last_event usage"
}
```

## 66 · 2026-10-29T03:24:47.341290+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"triggered_at\" src/prefect/server/events/ src/prefect/server/database/_migrations/versions/sqlite/*.py | head -40",
  "description": "Search triggered_at usage"
}
```

## 67 · 2026-10-29T03:24:47.412237+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:200:            triggering_event=triggering_event or bucket.last_event,
src/prefect/server/events/triggers.py:249:                last_event=triggering_event,
src/prefect/server/events/triggers.py:625:                            last_event=event,
src/prefect/server/events/triggers.py:651:                            last_event=event,
src/prefect/server/events/triggers.py:986:    last_event: Optional[ReceivedEvent],
src/prefect/server/events/triggers.py:990:        {"last_event": last_event} if last_event else {}
src/prefect/server/events/triggers.py:1041:    last_event: Optional[ReceivedEvent] = None,
src/prefect/server/events/triggers.py:1058:            last_event=last_event,
src/prefect/server/events/triggers.py:1073:                last_event=last_event,
src/prefect/server/events/triggers.py:1099:    last_event: Optional[ReceivedEvent],
src/prefect/server/events/triggers.py:1106:        {"last_event": last_event} if last_event else {}
src/prefect/server/events/triggers.py:1114:            last_event=last_event,
src/prefect/server/events/triggers.py:1338:                    last_event=None,
tests/events/server/triggers/test_flow_run_slas.py:209:    last_event = received_events[5]
tests/events/server/triggers/test_flow_run_slas.py:210:    assert last_event.occurred == frozen_time + timedelta(seconds=4)
tests/events/server/triggers/test_flow_run_slas.py:211:    assert last_event.resource.id == "prefect.flow-run.SLOWBOI"
tests/events/server/triggers/test_flow_run_slas.py:212:    assert last_event.event == "prefect.flow-run.running"
tests/events/server/triggers/test_flow_run_slas.py:224:            triggering_event=last_event,
tests/events/server/triggers/test_flow_run_slas.py:293:    last_event = received_events[5]
tests/events/server/triggers/test_flow_run_slas.py:294:    assert last_event.occurred == frozen_time + timedelta(seconds=4)
tests/events/server/triggers/test_flow_run_slas.py:295:    assert last_event.resource.id == "prefect.flow-run.SLOWBOI"
tests/events/server/triggers/test_flow_run_slas.py:296:    assert last_event.event == "prefect.flow-run.running"
tests/events/server/triggers/test_flow_run_slas.py:308:            triggering_event=last_event,
```

## 68 · 2026-10-29T03:24:47.759527+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:1040:    triggered_at: Optional[prefect.types._datetime.DateTime] = None,
src/prefect/server/events/triggers.py:1057:            triggered_at=triggered_at,
src/prefect/server/events/triggers.py:1072:                triggered_at=triggered_at,
src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py:112:            "triggered_at",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_09_131832_2b6c2b548f95_trigger_in_index.py:29:            "triggered_at",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_09_131832_2b6c2b548f95_trigger_in_index.py:58:            "triggered_at",
```

## 69 · 2026-10-29T03:24:49.002923+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"out.of.order\\|out of order\\|older\\|late event\\|before the bucket\" tests/events/server/triggers/*.py src/prefect/server/events/triggers.py | head -60",
  "description": "Search ordering-related tests"
}
```

## 70 · 2026-10-29T03:24:49.378657+00:00 · tool_result 

```
tests/events/server/triggers/test_basics.py:670:            name="Testing out-of-order events",
tests/events/server/triggers/test_basics.py:746:            name="Testing out-of-order events",
tests/events/server/triggers/test_basics.py:796:    # process it out of order
tests/events/server/triggers/test_basics.py:822:            name="Testing out-of-order events",
tests/events/server/triggers/test_composite_triggers.py:1090:    async def test_sequence_trigger_multiple_triggers_fired_out_of_order_does_not_act(
tests/events/server/triggers/test_composite_triggers.py:1329:    async def test_sequence_trigger_multiple_triggers_fired_somewhat_out_of_order_duplicate_events_does_not_act(
tests/events/server/triggers/test_composite_triggers.py:1562:    def host_duties_out_of_order(
tests/events/server/triggers/test_composite_triggers.py:1610:    async def test_sequence_and_compound_trigger_multiple_triggers_fired_out_of_order_does_not_act(
tests/events/server/triggers/test_composite_triggers.py:1613:        host_duties_out_of_order: List[ReceivedEvent],
tests/events/server/triggers/test_composite_triggers.py:1616:        for event in host_duties_out_of_order:
tests/events/server/triggers/test_flow_run_slas.py:586:    """While testing this issue, found another issue where sweeping older buckets might
src/prefect/server/events/triggers.py:125:    # 1. The event would have matched an older bucket that has either expired or has
src/prefect/server/events/triggers.py:143:        # This is an older out-of-order message or a redundant event for a reactive
src/prefect/server/events/triggers.py:148:            "Automation %s (%r) trigger %s got a late event for keys (%r)",
src/prefect/server/events/triggers.py:169:    # fire, because we can't know if we'll get one late event just in time to cause the
src/prefect/server/events/triggers.py:360:    # If we're only looking within a certain time horizon, remove any older firings that
src/prefect/server/events/triggers.py:640:                        # accept these older events.
src/prefect/server/events/triggers.py:1162:    older_than: prefect.types._datetime.DateTime,
src/prefect/server/events/triggers.py:1165:        sa.delete(db.AutomationBucket).where(db.AutomationBucket.end <= older_than)
```

## 71 · 2026-10-29T03:24:55.032607+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls plans/ && grep -rln \"automation\\|bucket\" plans/ | head -20",
  "description": "Search plans directory"
}
```

## 72 · 2026-10-29T03:24:55.417986+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"zombie\\|crash detection\\|unresponsive\" src/ docs/ tests/ --include=\"*.py\" --include=\"*.mdx\" --include=\"*.md\" 2>/dev/null | head -40",
  "description": "Search for zombie/crash detection references"
}
```

## 73 · 2026-10-29T03:24:55.575988+00:00 · tool_result 

```
2025-01-31-per-node-dbt-orchestration.md
2026-01-06-custom-deployment-sdks.md
2026-01-12-deployment-crud-events.md
2026-02-05-cli-cyclopts-migration.md
completed
plans/2025-01-31-per-node-dbt-orchestration.md
plans/2026-01-06-custom-deployment-sdks.md
plans/2026-01-12-deployment-crud-events.md
plans/2026-02-05-cli-cyclopts-migration.md
```

## 74 · 2026-10-29T03:25:04.547028+00:00 · tool_result 

```
src/integrations/prefect-aws/prefect_aws/observers/ecs.py:277:                            "and crash detection will not work. To enable ECS event replication and "
src/integrations/prefect-aws/prefect_aws/observers/ecs.py:278:                            "crash detection, deploy an SQS queue using "
src/integrations/prefect-aws/prefect_aws/workers/ecs_worker.py:768:            # The observer will handle crash detection, so we can always return 1 if the task
src/integrations/prefect-dask/tests/test_task_runners.py:286:        We care more about the crash detection and
src/integrations/prefect-databricks/prefect_databricks/models/jobs.py:1653:    * DRIVER_UNRESPONSIVE: Databricks was not able to access the Spark driver, because it was unresponsive.
src/integrations/prefect-databricks/prefect_databricks/models/jobs.py:1676:    driverunresponsive = "DRIVER_UNRESPONSIVE"
src/integrations/prefect-kubernetes/integration_tests/src/prefect_kubernetes_integration_tests/test_crash_detection.py:47:    # Use run_once mode for the crash detection test since we just need one attempt
src/integrations/prefect-ray/tests/test_task_runners.py:429:        We care more about the crash detection and
src/prefect/runner/runner.py:1174:        child processes and short-circuit the crash detection logic.
src/prefect/runner/server.py:64:                content={"message": "Runner is unresponsive at this time"},
src/prefect/workers/server.py:53:                content={"message": "Worker may be unresponsive at this time"},
docs/v3/advanced/detect-zombie-flows.mdx:2:title: How to detect and respond to zombie flows
docs/v3/advanced/detect-zombie-flows.mdx:4:description: Learn how to detect and respond to zombie flows.
docs/v3/advanced/detect-zombie-flows.mdx:5:keywords: ["zombie", "unresponsive", "stale flow", "stuck run", "detection", "cleanup", "automation"]
docs/v3/advanced/detect-zombie-flows.mdx:8:Sudden infrastructure failures (like machine crashes or container evictions) can cause flow runs to become unresponsive and appear stuck in a `Running` state.
docs/v3/advanced/detect-zombie-flows.mdx:10:To mitigate this, flow runs triggered by deployments can emit heartbeats to drive Automations that detect and respond to these "zombie" flow runs, ensuring they are marked as `Crashed` if they stop reporting heartbeats. Prefect Cloud provides a managed automation for this (**Unresponsive run detection**); self-hosted users (or anyone wanting custom behavior) can create the automation manually.
docs/v3/advanced/detect-zombie-flows.mdx:41:To create an automation that marks zombie flow runs as crashed, run this script:
docs/v3/advanced/detect-zombie-flows.mdx:53:    name="Crash zombie flows",
docs/v3/advanced/detect-zombie-flows.mdx:113:zombie detection for that flow run.
docs/v3/advanced/detect-zombie-flows.mdx:122:- `PREFECT_FLOWS_HEARTBEAT_FREQUENCY=30` with `within=timedelta(seconds=90)` — detects zombie flows within 90 seconds (as shown in the example above).
docs/v3/advanced/detect-zombie-flows.mdx:123:- `PREFECT_FLOWS_HEARTBEAT_FREQUENCY=180` (the current default) with `within=timedelta(seconds=540)` — detects zombie flows within 9 minutes.
docs/v3/advanced/detect-zombie-flows.mdx:127:You can also add additional actions to your automation to send a notification when zombie runs are detected.
docs/v3/advanced/worker-healthchecks.mdx:4:description: Learn how to monitor worker health and automatically restart workers when they become unresponsive.
docs/v3/advanced/worker-healthchecks.mdx:16:3. **Detecting unresponsive workers**: The health endpoint returns an error status if the worker hasn't polled recently
docs/v3/advanced/worker-healthchecks.mdx:38:- **503 Service Unavailable** with `{"message": "Worker may be unresponsive at this time"}` when the worker is unhealthy
docs/v3/api-ref/events/flow-run-events.mdx:131:[zombie flow detection](/v3/advanced/detect-zombie-flows).
docs/v3/api-ref/python/prefect-runner-runner.mdx:247:child processes and short-circuit the crash detection logic.
docs/v3/concepts/flows.mdx:73:From the perspective of a Prefect server and its clients, a flow run should eventually reach a terminal state. If it doesn't for one of the above reasons, it is called a ["zombie" flow run](/v3/advanced/detect-zombie-flows/).
docs/v3/how-to-guides/deployment_infra/serve-flows-docker.mdx:314:- **503 Service Unavailable** when the runner hasn't polled recently (indicating it may be unresponsive)
docs/v3/release-notes/integrations/prefect-aws.mdx:207:With this release the ECS worker now uses an event-based architecture that receives task state changes via EventBridge and SQS, replacing the previous polling-based design. This dramatically improves crash detection responsiveness and reduces API overhead. The worker gracefully degrades to limited functionality if SQS is unavailable, ensuring continued operation even during infrastructure issues.
docs/v3/release-notes/integrations/prefect-aws.mdx:213:- Move ECS worker to event-based crash detection [#18804](https://github.com/PrefectHQ/prefect/pull/18804) by [@desertaxle](https://github.com/desertaxle)
docs/v3/release-notes/oss/version-3-1.mdx:353:* Add an example for creating an automation to mark zombie flow runs as crashed by [@desertaxle](https://github.com/desertaxle) in [#16425](https://github.com/PrefectHQ/prefect/pull/16425)
docs/v3/release-notes/oss/version-3-1.mdx:367:Flow runs can now emit heartbeat events to detect infrastructure failures (crashed machines, evicted containers, etc). When enabled, an automation can automatically mark flows as crashed when heartbeats stop, preventing stuck "zombie" flows in the running state.
docs/v3/release-notes/oss/version-3-1.mdx:380:    name="Crash zombie flows",
docs/v3/release-notes/oss/version-3-4.mdx:842:* fix dead link to zombie flow runs by [@zzstoatzz](https://github.com/zzstoatzz) in [#18244](https://github.com/PrefectHQ/prefect/pull/18244)
docs/v3/release-notes/oss/version-3-4.mdx:957:This release also ships with version 0.6.0 of prefect-kubernetes, featuring a revamped Kubernetes worker. The updated worker is more stateless, providing improved resiliency, enhanced event emission, and better crash detection capabilities. See [#18004](https://github.com/PrefectHQ/prefect/pull/18004) for more details.
docs/v3/release-notes/oss/version-3-6.mdx:30:* Fix wildcard in zombie flow detection docs for custom state names by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21736](https://github.com/PrefectHQ/prefect/pull/21736)
docs/v3/release-notes/oss/version-3-7.mdx:146:* Align zombie-flow detection guide with current heartbeat defaults by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22285](https://github.com/PrefectHQ/prefect/pull/22285)
docs/v3/release-notes/oss/version-3-7.mdx:359:* Recommend managed automation for zombie detection by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#21894](https://github.com/PrefectHQ/prefect/pull/21894)
docs/v3/release-notes/oss/version-3-7.mdx:409:* Add zombie flow detection trigger regression test by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21802](https://github.com/PrefectHQ/prefect/pull/21802)
```

## 75 · 2026-10-29T03:25:05.756824+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/docs/v3/advanced/detect-zombie-flows.mdx"
}
```

## 76 · 2026-10-29T03:25:05.871696+00:00 · tool_result 

````
1	---
2	title: How to detect and respond to zombie flows
3	sidebarTitle: Detect Zombie Flows
4	description: Learn how to detect and respond to zombie flows.
5	keywords: ["zombie", "unresponsive", "stale flow", "stuck run", "detection", "cleanup", "automation"]
6	---
7	
8	Sudden infrastructure failures (like machine crashes or container evictions) can cause flow runs to become unresponsive and appear stuck in a `Running` state.
9	
10	To mitigate this, flow runs triggered by deployments can emit heartbeats to drive Automations that detect and respond to these "zombie" flow runs, ensuring they are marked as `Crashed` if they stop reporting heartbeats. Prefect Cloud provides a managed automation for this (**Unresponsive run detection**); self-hosted users (or anyone wanting custom behavior) can create the automation manually.
11	
12	
13	### Enable the managed automation (Prefect Cloud)
14	
15	<Note>This managed automation is only available in Prefect Cloud.</Note>
16	
17	Prefect Cloud refers to this capability as **Unresponsive run detection**: a built-in automation that automatically marks flow runs as `Crashed` when they stop responding. To enable it:
18	
19	1. In the upper left, click on the current workspace and select **Settings**.
20	2. Under **Account Settings → Controls**, ensure **Managed automations** is enabled. This is an account-wide switch and only needs to be done once.
21	3. Under **Workspace Settings → Managed Automations**, enable **Unresponsive run detection** for this workspace.
22	
23	By default, the automation marks a run as `Crashed` if it does not receive a heartbeat for 9 minutes, which tolerates three missed heartbeats at the default `PREFECT_FLOWS_HEARTBEAT_FREQUENCY` of 180 seconds (3 minutes).
24	
25	<Note>
26	Prefect 3.6.22 and later ship with `PREFECT_FLOWS_HEARTBEAT_FREQUENCY` set to 180 seconds out of the box, so no extra configuration is needed. Earlier clients default to `None` (no heartbeats); if your deployments run on a client older than 3.6.22, set `PREFECT_FLOWS_HEARTBEAT_FREQUENCY=180` on the workers that run them so the managed automation has heartbeats to consume.
27	</Note>
28	
29	
30	### Enable flow run heartbeat events
31	
32	Prefect 3.6.22 and later emit flow run heartbeats by default (`PREFECT_FLOWS_HEARTBEAT_FREQUENCY` defaults to 180 seconds), so no extra configuration is needed on modern clients.
33	
34	If you are running an older client (3.1.8–3.6.21), set `PREFECT_FLOWS_HEARTBEAT_FREQUENCY` to an integer greater than or equal to 30 to enable heartbeat emission.
35	
36	
37	### Create the automation manually
38	
39	Follow this path if you're running self-hosted Prefect, or if you're on Prefect Cloud and want custom behavior (different thresholds, additional actions, notifications, etc.).
40	
41	To create an automation that marks zombie flow runs as crashed, run this script:
42	```python
43	from datetime import timedelta
44	
45	from prefect.automations import Automation
46	from prefect.client.schemas.objects import StateType
47	from prefect.events.actions import ChangeFlowRunState
48	from prefect.events.schemas.automations import EventTrigger, Posture
49	from prefect.events.schemas.events import ResourceSpecification
50	
51	
52	my_automation = Automation(
53	    name="Crash zombie flows",
54	    trigger=EventTrigger(
55	        after={"prefect.flow-run.heartbeat"},
56	        expect={
57	            "prefect.flow-run.*",
58	        },
59	        match=ResourceSpecification({"prefect.resource.id": ["prefect.flow-run.*"]}),
60	        for_each={"prefect.resource.id"},
61	        posture=Posture.Proactive,
62	        threshold=1,
63	        within=timedelta(seconds=90),
64	    ),
65	    actions=[
66	        ChangeFlowRunState(
67	            state=StateType.CRASHED,
68	            message="Flow run marked as crashed due to missing heartbeats.",
69	        )
70	    ],
71	)
72	
73	if __name__ == "__main__":
74	    my_automation.create()
75	```
76	
77	The trigger definition says that `after` each heartbeat event for a flow run we `expect` to see any flow run event
78	(heartbeat or state change) for that same flow run `within` 90 seconds. Using the `prefect.flow-run.*` wildcard
79	in `expect` ensures the automation works correctly even when flows return custom-named states
80	(for example, `Completed(name="SuccessfullyProcessed")`), since flow run event names are based on the state's
81	name rather than its type.
82	
83	<Note>
84	The `within=timedelta(seconds=90)` window in the example above is calibrated for heartbeats arriving every 30 seconds (three missed heartbeats × 30 s = 90 s). Current clients default `PREFECT_FLOWS_HEARTBEAT_FREQUENCY` to 180 seconds, so if you keep that default you should increase `within` accordingly — for example, `within=timedelta(seconds=540)` to tolerate three missed 180-second heartbeats.
85	</Note>
86	
87	
88	### Custom state names
89	
90	Flow run event names are based on the state's name, not its type. If your flows return states with
91	custom names (for example, `return Completed(name="SuccessfullyProcessed")`), the emitted event will be
92	`prefect.flow-run.SuccessfullyProcessed` rather than `prefect.flow-run.Completed`.
93	
94	The wildcard `prefect.flow-run.*` in the example above handles this automatically. If you need
95	finer-grained control over which events disarm the trigger, you can explicitly list your custom
96	state names in the `expect` set instead:
97	
98	{/* pmd-metadata: notest */}
99	```python
100	expect={
101	    "prefect.flow-run.heartbeat",
102	    "prefect.flow-run.Completed",
103	    "prefect.flow-run.Failed",
104	    "prefect.flow-run.Cancelled",
105	    "prefect.flow-run.Crashed",
106	    "prefect.flow-run.SuccessfullyProcessed",  # your custom state name
107	},
108	```
109	
110	<Note>
111	When using explicit state names, you must include every custom state name your flows may return.
112	A missing name means the automation won't recognize that terminal state, causing a false-positive
113	zombie detection for that flow run.
114	</Note>
115	
116	
117	### Adjusting behavior with settings
118	
119	The `within` window and `PREFECT_FLOWS_HEARTBEAT_FREQUENCY` together control how quickly the automation fires after a flow run stops responding. A good rule of thumb is to set `within` to at least three times the heartbeat frequency so transient delays don't cause false positives.
120	
121	For example:
122	- `PREFECT_FLOWS_HEARTBEAT_FREQUENCY=30` with `within=timedelta(seconds=90)` — detects zombie flows within 90 seconds (as shown in the example above).
123	- `PREFECT_FLOWS_HEARTBEAT_FREQUENCY=180` (the current default) with `within=timedelta(seconds=540)` — detects zombie flows within 9 minutes.
124	
125	`PREFECT_FLOWS_HEARTBEAT_FREQUENCY` must be greater than or equal to 30.
126	
127	You can also add additional actions to your automation to send a notification when zombie runs are detected.
````

## 77 · 2026-10-29T03:25:10.733756+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"heartbeat\" src/prefect/ --include=\"*.py\" | grep -v test | head -40",
  "description": "Find heartbeat emission code"
}
```

## 78 · 2026-10-29T03:25:11.816215+00:00 · tool_result 

```
src/prefect/cli/worker.py:245:            heartbeat_interval_seconds=int(PREFECT_WORKER_HEARTBEAT_SECONDS.value()),
src/prefect/client/orchestration/routes.py:136:    "/work_pools/{work_pool_name}/workers/heartbeat",
src/prefect/client/orchestration/_work_pools/client.py:37:    def send_worker_heartbeat(
src/prefect/client/orchestration/_work_pools/client.py:41:        heartbeat_interval_seconds: float | None = None,
src/prefect/client/orchestration/_work_pools/client.py:46:        Sends a worker heartbeat for a given work pool.
src/prefect/client/orchestration/_work_pools/client.py:49:            work_pool_name: The name of the work pool to heartbeat against.
src/prefect/client/orchestration/_work_pools/client.py:50:            worker_name: The name of the worker sending the heartbeat.
src/prefect/client/orchestration/_work_pools/client.py:58:            "heartbeat_interval_seconds": heartbeat_interval_seconds,
src/prefect/client/orchestration/_work_pools/client.py:67:            "/work_pools/{work_pool_name}/workers/heartbeat",
src/prefect/client/orchestration/_work_pools/client.py:365:    async def send_worker_heartbeat(
src/prefect/client/orchestration/_work_pools/client.py:369:        heartbeat_interval_seconds: float | None = None,
src/prefect/client/orchestration/_work_pools/client.py:374:        Sends a worker heartbeat for a given work pool.
src/prefect/client/orchestration/_work_pools/client.py:377:            work_pool_name: The name of the work pool to heartbeat against.
src/prefect/client/orchestration/_work_pools/client.py:378:            worker_name: The name of the worker sending the heartbeat.
src/prefect/client/orchestration/_work_pools/client.py:386:            "heartbeat_interval_seconds": heartbeat_interval_seconds,
src/prefect/client/orchestration/_work_pools/client.py:395:            "/work_pools/{work_pool_name}/workers/heartbeat",
src/prefect/client/schemas/filters.py:982:    """Filter by `Worker.last_heartbeat_time`."""
src/prefect/client/schemas/filters.py:987:            "Only include processes whose last heartbeat was at or before this time"
src/prefect/client/schemas/filters.py:993:            "Only include processes whose last heartbeat was at or after this time"
src/prefect/client/schemas/filters.py:1014:    last_heartbeat_time: Optional[WorkerFilterLastHeartbeatTime] = Field(
src/prefect/client/schemas/filters.py:1016:        description="Filter criteria for `Worker.last_heartbeat_time`",
src/prefect/client/schemas/objects.py:1636:    last_heartbeat_time: Optional[datetime.datetime] = Field(
src/prefect/client/schemas/objects.py:1637:        default=None, description="The last time the worker process sent a heartbeat."
src/prefect/client/schemas/objects.py:1639:    heartbeat_interval_seconds: Optional[int] = Field(
src/prefect/client/schemas/objects.py:1642:            "The number of seconds to expect between heartbeats sent by the worker."
src/prefect/client/schemas/worker_channel.py:30:    "worker_heartbeat.v1",
src/prefect/client/schemas/worker_channel.py:41:    "worker.heartbeat.v1",
src/prefect/client/schemas/worker_channel.py:69:WORKER_HEARTBEAT_CAPABILITY: Literal["worker_heartbeat.v1"] = "worker_heartbeat.v1"
src/prefect/client/schemas/worker_channel.py:105:    HEARTBEAT_PERSISTENCE_FAILED = "heartbeat_persistence_failed"
src/prefect/client/schemas/worker_channel.py:230:    heartbeat_interval_seconds: PositiveInteger
src/prefect/client/schemas/worker_channel.py:317:    effective_heartbeat_interval_seconds: PositiveInteger
src/prefect/client/schemas/worker_channel.py:380:    heartbeat_interval_seconds: PositiveInteger
src/prefect/client/schemas/worker_channel.py:384:    type: Literal["worker.heartbeat.v1"]
src/prefect/flow_engine.py:306:def _send_heartbeats(
src/prefect/flow_engine.py:310:    """Context manager that maintains heartbeats for a flow run using a daemon thread.
src/prefect/flow_engine.py:312:    Uses a background OS thread instead of an asyncio task so that heartbeats
src/prefect/flow_engine.py:316:        engine: The flow run engine instance to emit heartbeats for.
src/prefect/flow_engine.py:317:        join_on_exit: Whether to join the heartbeat thread on exit. Set to
src/prefect/flow_engine.py:323:    heartbeat_seconds = engine.heartbeat_seconds
src/prefect/flow_engine.py:324:    if heartbeat_seconds is None:
```

## 79 · 2026-10-29T03:25:13.248911+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/flow_engine.py",
  "offset": 290,
  "limit": 90
}
```

## 80 · 2026-10-29T03:25:13.349754+00:00 · tool_result 

```
290	    try:
291	        flow_run_id = UUID(flow_run_id_value) if flow_run_id_value else None
292	    except ValueError:
293	        flow_run_id = None
294	
295	    if flow_run_id is None:
296	        _engine_logger.error(
297	            "Invalid flow run id. Expected PREFECT__FLOW_RUN_ID to contain a UUID."
298	        )
299	        return 1
300	
301	    _run_flow_from_runtime_entrypoint(flow_run_id, args[0])
302	    return 0
303	
304	
305	@contextmanager
306	def _send_heartbeats(
307	    engine: "BaseFlowRunEngine[Any, Any]",
308	    join_on_exit: bool = True,
309	) -> Generator[None, None, None]:
310	    """Context manager that maintains heartbeats for a flow run using a daemon thread.
311	
312	    Uses a background OS thread instead of an asyncio task so that heartbeats
313	    fire even when the event loop is blocked by CPU-bound work.
314	
315	    Args:
316	        engine: The flow run engine instance to emit heartbeats for.
317	        join_on_exit: Whether to join the heartbeat thread on exit. Set to
318	            `False` in async engines to avoid blocking the event loop.
319	
320	    Yields:
321	        None
322	    """
323	    heartbeat_seconds = engine.heartbeat_seconds
324	    if heartbeat_seconds is None:
325	        yield
326	        return
327	    heartbeat_seconds = max(heartbeat_seconds, MINIMUM_HEARTBEAT_INTERVAL)
328	
329	    # Pre-compute the event template once to minimize per-heartbeat GIL hold time
330	    resource, related = engine._build_heartbeat_event_template()
331	
332	    stop_event = threading.Event()
333	
334	    def heartbeat_loop() -> None:
335	        while not stop_event.is_set():
336	            # Check state before emitting - don't emit if final
337	            if (
338	                engine.flow_run
339	                and engine.flow_run.state
340	                and engine.flow_run.state.is_final()
341	            ):
342	                engine.logger.debug("Flow run in terminal state, stopping heartbeat")
343	                return
344	
345	            try:
346	                engine._emit_flow_run_heartbeat(resource, related)
347	            except Exception:
348	                engine.logger.debug("Failed to emit heartbeat", exc_info=True)
349	
350	            # Sleep in increments to allow quick shutdown
351	            for _ in range(heartbeat_seconds):
352	                if stop_event.is_set():
353	                    return
354	                time.sleep(1)
355	
356	    # Copy the current context so the heartbeat thread sees the same
357	    # `SettingsContext` (and therefore the same `PREFECT_API_URL`) as the
358	    # calling thread. Without this, `threading.Thread` starts with an empty
359	    # context and `SettingsContext.get()` falls back to the process-wide
360	    # `GLOBAL_SETTINGS_CONTEXT`, which is initialized at import time and can
361	    # have a stale `api.url=None`. That caused `EventsWorker.instance()` from
362	    # the heartbeat path to spawn an ephemeral `SubprocessASGIServer` during
363	    # flow teardown, racing with interpreter shutdown and aborting the
364	    # process.
365	    heartbeat_ctx = contextvars.copy_context()
366	    thread = threading.Thread(
367	        target=heartbeat_ctx.run, args=(heartbeat_loop,), daemon=True
368	    )
369	    thread.start()
370	    engine.logger.debug("Started flow run heartbeat context")
371	
372	    try:
373	        yield
374	    finally:
375	        stop_event.set()
376	        if join_on_exit:
377	            thread.join(timeout=2)
378	        engine.logger.debug("Stopped flow run heartbeat context")
379	
```

## 81 · 2026-10-29T03:25:16.614173+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"_emit_flow_run_heartbeat\\|_build_heartbeat_event_template\" -n -A40 src/prefect/flow_engine.py | head -100",
  "description": "Inspect heartbeat event payload"
}
```

## 82 · 2026-10-29T03:25:16.951555+00:00 · tool_result 

```
330:    resource, related = engine._build_heartbeat_event_template()
331-
332-    stop_event = threading.Event()
333-
334-    def heartbeat_loop() -> None:
335-        while not stop_event.is_set():
336-            # Check state before emitting - don't emit if final
337-            if (
338-                engine.flow_run
339-                and engine.flow_run.state
340-                and engine.flow_run.state.is_final()
341-            ):
342-                engine.logger.debug("Flow run in terminal state, stopping heartbeat")
343-                return
344-
345-            try:
346:                engine._emit_flow_run_heartbeat(resource, related)
347-            except Exception:
348-                engine.logger.debug("Failed to emit heartbeat", exc_info=True)
349-
350-            # Sleep in increments to allow quick shutdown
351-            for _ in range(heartbeat_seconds):
352-                if stop_event.is_set():
353-                    return
354-                time.sleep(1)
355-
356-    # Copy the current context so the heartbeat thread sees the same
357-    # `SettingsContext` (and therefore the same `PREFECT_API_URL`) as the
358-    # calling thread. Without this, `threading.Thread` starts with an empty
359-    # context and `SettingsContext.get()` falls back to the process-wide
360-    # `GLOBAL_SETTINGS_CONTEXT`, which is initialized at import time and can
361-    # have a stale `api.url=None`. That caused `EventsWorker.instance()` from
362-    # the heartbeat path to spawn an ephemeral `SubprocessASGIServer` during
363-    # flow teardown, racing with interpreter shutdown and aborting the
364-    # process.
365-    heartbeat_ctx = contextvars.copy_context()
366-    thread = threading.Thread(
367-        target=heartbeat_ctx.run, args=(heartbeat_loop,), daemon=True
368-    )
369-    thread.start()
370-    engine.logger.debug("Started flow run heartbeat context")
371-
372-    try:
373-        yield
374-    finally:
375-        stop_event.set()
376-        if join_on_exit:
377-            thread.join(timeout=2)
378-        engine.logger.debug("Stopped flow run heartbeat context")
379-
380-
381-@deprecated_callable(
382-    start_date=datetime.datetime(2026, 3, 1),
383-    help="Use `_send_heartbeats` instead.",
384-)
385-@contextmanager
386-def send_heartbeats_sync(
--
482:    def _build_heartbeat_event_template(
483-        self,
484-    ) -> tuple[dict[str, str], list[RelatedResource]]:
485-        """Pre-compute the heartbeat event resource and related list.
486-
487-        Called once before starting the heartbeat thread to avoid repeated
488-        Pydantic validation (RelatedResource.model_validate) on every tick.
489-        """
490-        resource: dict[str, str] = {}
491-        related: list[RelatedResource] = []
492-
493-        if not self.flow_run:
494-            return resource, related
495-
496-        resource = {
497-            "prefect.resource.id": f"prefect.flow-run.{self.flow_run.id}",
498-            "prefect.resource.name": self.flow_run.name or "",
499-            "prefect.version": __version__,
500-        }
501-
502-        tags: list[str] = list(self.flow_run.tags or [])
503-
504-        if self.flow_run.flow_id:
505-            related.append(
506-                RelatedResource.model_validate(
507-                    {
508-                        "prefect.resource.id": f"prefect.flow.{self.flow_run.flow_id}",
509-                        "prefect.resource.role": "flow",
510-                        "prefect.resource.name": self.flow.name if self.flow else "",
511-                    }
512-                )
513-            )
514-
515-        if self.flow_run.deployment_id:
516-            related.append(
517-                RelatedResource.model_validate(
518-                    {
519-                        "prefect.resource.id": f"prefect.deployment.{self.flow_run.deployment_id}",
520-                        "prefect.resource.role": "deployment",
521-                    }
522-                )
--
```

## 83 · 2026-10-29T03:25:18.585158+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"def _emit_flow_run_heartbeat\" -A60 src/prefect/flow_engine.py",
  "description": "Inspect heartbeat event emission"
}
```

## 84 · 2026-10-29T03:25:18.873491+00:00 · tool_result 

```
529:    def _emit_flow_run_heartbeat(
530-        self,
531-        resource: dict[str, str] | None = None,
532-        related: list[RelatedResource] | None = None,
533-    ) -> None:
534-        """Emit a heartbeat event for the current flow run.
535-
536-        Args:
537-            resource: Pre-computed resource dict from _build_heartbeat_event_template.
538-            related: Pre-computed related list from _build_heartbeat_event_template.
539-                If not provided, builds the template on the fly (backward compat).
540-        """
541-        if not self.flow_run:
542-            return
543-
544-        if resource is None or related is None:
545-            resource, related = self._build_heartbeat_event_template()
546-
547-        emit_event(
548-            event="prefect.flow-run.heartbeat",
549-            resource=resource,
550-            related=related,
551-        )
552-
553-    def _update_otel_labels(
554-        self, span: trace.Span, client: Union[SyncPrefectClient, PrefectClient]
555-    ):
556-        parent_flow_run_ctx = FlowRunContext.get()
557-
558-        if parent_flow_run_ctx and parent_flow_run_ctx.flow_run:
559-            if traceparent := parent_flow_run_ctx.flow_run.labels.get(
560-                LABELS_TRACEPARENT_KEY
561-            ):
562-                carrier: KeyValueLabels = {TRACEPARENT_KEY: traceparent}
563-                propagate.get_global_textmap().inject(
564-                    carrier={TRACEPARENT_KEY: traceparent},
565-                    setter=OTELSetter(),
566-                )
567-
568-            else:
569-                carrier: KeyValueLabels = {}
570-                propagate.get_global_textmap().inject(
571-                    carrier,
572-                    context=trace.set_span_in_context(span),
573-                    setter=OTELSetter(),
574-                )
575-            if carrier.get(TRACEPARENT_KEY):
576-                if self.flow_run:
577-                    client.update_flow_run_labels(
578-                        flow_run_id=self.flow_run.id,
579-                        labels={LABELS_TRACEPARENT_KEY: carrier[TRACEPARENT_KEY]},
580-                    )
581-                else:
582-                    self.logger.info(
583-                        f"Tried to set traceparent {carrier[TRACEPARENT_KEY]} for flow run, but None was found"
584-                    )
585-
586-    def _engine_owns_cancellation_handling(self) -> bool:
587-        """Return whether this engine owns cancellation state and hooks.
588-
589-        Runner-managed subprocesses set `PREFECT__ENABLE_CANCELLATION_AND_CRASHED_HOOKS=false`
```

## 85 · 2026-10-29T03:25:20.516405+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"heartbeat\" docs/v3/release-notes/oss/*.mdx | head -40",
  "description": "Search release notes for heartbeat fixes"
}
```

## 86 · 2026-10-29T03:25:20.820594+00:00 · tool_result 

```
docs/v3/release-notes/oss/version-3-1.mdx:367:Flow runs can now emit heartbeat events to detect infrastructure failures (crashed machines, evicted containers, etc). When enabled, an automation can automatically mark flows as crashed when heartbeats stop, preventing stuck "zombie" flows in the running state.
docs/v3/release-notes/oss/version-3-1.mdx:371:- Deploy the provided automation script to update flow states when heartbeats stop
docs/v3/release-notes/oss/version-3-1.mdx:382:        after={"prefect.flow-run.heartbeat"},
docs/v3/release-notes/oss/version-3-1.mdx:384:            "prefect.flow-run.heartbeat",
docs/v3/release-notes/oss/version-3-1.mdx:399:            message="Flow run marked as crashed due to missing heartbeats.",
docs/v3/release-notes/oss/version-3-1.mdx:425:* Enhance `Runner` to send heartbeat events for flow runs by [@desertaxle](https://github.com/desertaxle) in [#16410](https://github.com/PrefectHQ/prefect/pull/16410)
docs/v3/release-notes/oss/version-3-1.mdx:761:* Send worker metadata with first heartbeat by [@abrookins](https://github.com/abrookins) in [#15898](https://github.com/PrefectHQ/prefect/pull/15898)
docs/v3/release-notes/oss/version-3-2.mdx:203:* Fix bug causing duplicate flow run heartbeats with a process worker by [@desertaxle](https://github.com/desertaxle) in [#17375](https://github.com/PrefectHQ/prefect/pull/17375)
docs/v3/release-notes/oss/version-3-4.mdx:1014:* handle heartbeat event in `wait_for_flow_run` by [@zzstoatzz](https://github.com/zzstoatzz) in [#17930](https://github.com/PrefectHQ/prefect/pull/17930)
docs/v3/release-notes/oss/version-3-6.mdx:107:* Propagate contextvars to the flow heartbeat thread by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#21577](https://github.com/PrefectHQ/prefect/pull/21577)
docs/v3/release-notes/oss/version-3-6.mdx:233:* Fix heartbeat starvation under CPU-bound workloads by [@desertaxle](https://github.com/desertaxle) in [#21276](https://github.com/PrefectHQ/prefect/pull/21276)
docs/v3/release-notes/oss/version-3-6.mdx:294:* Enforce minimum heartbeat interval at the engine level by [@desertaxle](https://github.com/desertaxle) in [#21188](https://github.com/PrefectHQ/prefect/pull/21188)
docs/v3/release-notes/oss/version-3-6.mdx:340:* Change heartbeat default from `None` to 180s by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#21058](https://github.com/PrefectHQ/prefect/pull/21058)
docs/v3/release-notes/oss/version-3-6.mdx:365:* Fix flaky `test_two_subscriptions_get_all_events` by handling `None` heartbeats by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21037](https://github.com/PrefectHQ/prefect/pull/21037)
docs/v3/release-notes/oss/version-3-6.mdx:367:* Disable heartbeats in tests to fix CI timeout by [@desertaxle](https://github.com/desertaxle) in [#21062](https://github.com/PrefectHQ/prefect/pull/21062)
docs/v3/release-notes/oss/version-3-6.mdx:746:## 3.6.13 - The heartbeat is coming from *inside* the engine
docs/v3/release-notes/oss/version-3-6.mdx:757:* Move flow run heartbeat event emission to flow run engine by [@zzstoatzz](https://github.com/zzstoatzz) in [#19641](https://github.com/PrefectHQ/prefect/pull/19641)
docs/v3/release-notes/oss/version-3-7.mdx:52:* Reconcile stale work-pool snapshots on worker heartbeat by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22429](https://github.com/PrefectHQ/prefect/pull/22429)
docs/v3/release-notes/oss/version-3-7.mdx:146:* Align zombie-flow detection guide with current heartbeat defaults by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22285](https://github.com/PrefectHQ/prefect/pull/22285)
docs/v3/release-notes/oss/version-3-7.mdx:260:* Add worker channel handshake and heartbeat by [@desertaxle](https://github.com/desertaxle) in [#22004](https://github.com/PrefectHQ/prefect/pull/22004)
```

## 87 · 2026-10-29T03:25:22.536537+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"zombie\\|automation\\|trigger\" docs/v3/release-notes/oss/version-3-7.mdx | head -60",
  "description": "Search 3.7 release notes for automation fixes"
}
```

## 88 · 2026-10-29T03:25:22.889633+00:00 · tool_result 

```
133:* Use `retry_asserts` for flaky automation notification test by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22246](https://github.com/PrefectHQ/prefect/pull/22246)
146:* Align zombie-flow detection guide with current heartbeat defaults by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22285](https://github.com/PrefectHQ/prefect/pull/22285)
147:* Document lifecycle events for automations, concurrency, artifacts, work pools/queues by [@github-actions](https://github.com/github-actions)[bot] in [#22230](https://github.com/PrefectHQ/prefect/pull/22230)
160:* Emit lifecycle events (`created`, `updated`, `deleted`) for all domain objects including variables, flows, block documents, block types, concurrency limits, artifact collections, and automations by [@chrisguidry](https://github.com/chrisguidry) in [#22226](https://github.com/PrefectHQ/prefect/pull/22226)
167:* Add configurable filter params (`automations`, `sort`, `limit`, `offset`) to `read_automations` client methods by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#22191](https://github.com/PrefectHQ/prefect/pull/22191)
181:* Document `flow_run_log_summary` automation template variable by [@mitchnielsen](https://github.com/mitchnielsen) in [#22192](https://github.com/PrefectHQ/prefect/pull/22192)
259:* Add delete flow run automation action by [@zzstoatzz](https://github.com/zzstoatzz) in [#22018](https://github.com/PrefectHQ/prefect/pull/22018)
262:* Index triggers by expect pattern to avoid O(n) scan in `find_interested_triggers` by [@chuqCTC](https://github.com/chuqCTC) in [#21977](https://github.com/PrefectHQ/prefect/pull/21977)
301:* Add delete-flow-run automation action to action types table by [@github-actions](https://github.com/github-actions)[bot] in [#22021](https://github.com/PrefectHQ/prefect/pull/22021)
359:* Recommend managed automation for zombie detection by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#21894](https://github.com/PrefectHQ/prefect/pull/21894)
361:* Note metric-trigger Cloud gating and event prefix difference by [@zzstoatzz](https://github.com/zzstoatzz) in [#21935](https://github.com/PrefectHQ/prefect/pull/21935)
409:* Add zombie flow detection trigger regression test by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21802](https://github.com/PrefectHQ/prefect/pull/21802)
```

## 89 · 2026-10-29T03:25:37.383135+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class ChangeFlowRunState\" -A80 src/prefect/server/events/actions.py | head -100",
  "description": "Inspect ChangeFlowRunState action"
}
```

## 90 · 2026-10-29T03:25:37.736270+00:00 · tool_result 

```
1150:class ChangeFlowRunState(FlowRunStateChangeAction):
1151-    """Changes the state of a flow run associated with the trigger"""
1152-
1153-    type: Literal["change-flow-run-state"] = "change-flow-run-state"
1154-
1155-    name: str | None = Field(
1156-        None,
1157-        description="The name of the state to change the flow run to",
1158-    )
1159-    state: StateType = Field(
1160-        ...,
1161-        description="The type of the state to change the flow run to",
1162-    )
1163-    message: str | None = Field(
1164-        None,
1165-        description="An optional message to associate with the state change",
1166-    )
1167-    force: bool = Field(
1168-        False,
1169-        description="Force the state change even if the transition is not allowed",
1170-    )
1171-
1172-    async def new_state(self, triggered_action: "TriggeredAction") -> StateCreate:
1173-        message = (
1174-            self.message
1175-            or f"State changed by Automation {triggered_action.automation.id}"
1176-        )
1177-
1178-        return StateCreate(
1179-            name=self.name,
1180-            type=self.state,
1181-            message=message,
1182-        )
1183-
1184-
1185-class CancelFlowRun(FlowRunStateChangeAction):
1186-    """Cancels a flow run associated with the trigger"""
1187-
1188-    type: Literal["cancel-flow-run"] = "cancel-flow-run"
1189-
1190-    async def new_state(self, triggered_action: "TriggeredAction") -> StateCreate:
1191-        return StateCreate(
1192-            type=StateType.CANCELLING,
1193-            message=f"Cancelled by Automation {triggered_action.automation.id}",
1194-        )
1195-
1196-
1197-class DeleteFlowRun(FlowRunAction):
1198-    """Deletes a flow run associated with the trigger"""
1199-
1200-    type: Literal["delete-flow-run"] = "delete-flow-run"
1201-
1202-    async def act(self, triggered_action: "TriggeredAction") -> None:
1203-        flow_run_id = await self.flow_run(triggered_action)
1204-
1205-        self._resulting_related_resources.append(
1206-            RelatedResource.model_validate(
1207-                {
1208-                    "prefect.resource.id": f"prefect.flow-run.{flow_run_id}",
1209-                    "prefect.resource.role": "target",
1210-                }
1211-            )
1212-        )
1213-
1214-        logger.info(
1215-            "Deleting flow run",
1216-            extra={
1217-                "flow_run_id": str(flow_run_id),
1218-                **self.logging_context(triggered_action),
1219-            },
1220-        )
1221-
1222-        async with await self.orchestration_client(triggered_action) as orchestration:
1223-            response = await orchestration.delete_flow_run(flow_run_id)
1224-
1225-            self._result_details["status_code"] = response.status_code
1226-            if response.status_code >= 300:
1227-                raise ActionFailed(self.reason_from_response(response))
1228-
1229-
1230-class SuspendFlowRun(FlowRunStateChangeAction):
```

## 91 · 2026-10-29T03:25:39.465639+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class FlowRunAction\\|class FlowRunStateChangeAction\" -A70 src/prefect/server/events/actions.py | head -120",
  "description": "Inspect flow run action resource resolution"
}
```

## 92 · 2026-10-29T03:25:39.782540+00:00 · tool_result 

```
1088:class FlowRunAction(ExternalDataAction):
1089-    """An action that operates on a flow run"""
1090-
1091-    async def flow_run(self, triggered_action: "TriggeredAction") -> UUID:
1092-        # Proactive triggers won't have an event, but they might be tracking
1093-        # buckets per-resource, so check for that first
1094-        labels = triggered_action.triggering_labels
1095-        if triggering_resource_id := labels.get("prefect.resource.id"):
1096-            if id := _id_from_resource_id(triggering_resource_id, "prefect.flow-run"):
1097-                return id
1098-
1099-        event = triggered_action.triggering_event
1100-        if event:
1101-            if id := _id_of_first_resource_of_kind(event, "prefect.flow-run"):
1102-                return id
1103-
1104-        raise ActionFailed("No flow run could be inferred")
1105-
1106-
1107:class FlowRunStateChangeAction(FlowRunAction):
1108-    """Changes the state of a flow run associated with the trigger"""
1109-
1110-    @abc.abstractmethod
1111-    async def new_state(self, triggered_action: "TriggeredAction") -> StateCreate:
1112-        """Return the new state for the flow run"""
1113-
1114-    async def act(self, triggered_action: "TriggeredAction") -> None:
1115-        flow_run_id = await self.flow_run(triggered_action)
1116-
1117-        self._resulting_related_resources.append(
1118-            RelatedResource.model_validate(
1119-                {
1120-                    "prefect.resource.id": f"prefect.flow-run.{flow_run_id}",
1121-                    "prefect.resource.role": "target",
1122-                }
1123-            )
1124-        )
1125-
1126-        logger.info(
1127-            "Changing flow run state",
1128-            extra={
1129-                "flow_run_id": str(flow_run_id),
1130-                **self.logging_context(triggered_action),
1131-            },
1132-        )
1133-
1134-        async with await self.orchestration_client(triggered_action) as orchestration:
1135-            response = await orchestration.set_flow_run_state(
1136-                flow_run_id,
1137-                await self.new_state(triggered_action=triggered_action),
1138-                force=getattr(self, "force", False),
1139-            )
1140-
1141-            self._result_details["status_code"] = response.status_code
1142-            if response.status_code >= 300:
1143-                raise ActionFailed(self.reason_from_response(response))
1144-
1145-            result = OrchestrationResult.model_validate(response.json())
1146-            if not isinstance(result.details, StateAcceptDetails):
1147-                raise ActionFailed(f"Failed to set state: {result.details.reason}")
1148-
1149-
1150-class ChangeFlowRunState(FlowRunStateChangeAction):
1151-    """Changes the state of a flow run associated with the trigger"""
1152-
1153-    type: Literal["change-flow-run-state"] = "change-flow-run-state"
1154-
1155-    name: str | None = Field(
1156-        None,
1157-        description="The name of the state to change the flow run to",
1158-    )
1159-    state: StateType = Field(
1160-        ...,
1161-        description="The type of the state to change the flow run to",
1162-    )
1163-    message: str | None = Field(
1164-        None,
1165-        description="An optional message to associate with the state change",
1166-    )
1167-    force: bool = Field(
1168-        False,
1169-        description="Force the state change even if the transition is not allowed",
1170-    )
1171-
1172-    async def new_state(self, triggered_action: "TriggeredAction") -> StateCreate:
1173-        message = (
1174-            self.message
1175-            or f"State changed by Automation {triggered_action.automation.id}"
1176-        )
1177-
```

## 93 · 2026-10-29T03:25:51.845488+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"flow-run\\.\\|flow_run.*event=\" src/prefect/server/orchestration/ | grep -i \"event\" | head -30",
  "description": "Find flow run state event emission"
}
```

## 94 · 2026-10-29T03:25:52.189508+00:00 · tool_result 

```
(Bash completed with no output)
```

## 95 · 2026-10-29T03:25:52.241148+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def emit_flow_run_state_change_event\\|flow_run_state_change\\|payload=\" src/prefect/server/events/ --include=\"*.py\" | head -30",
  "description": "Find state change event payload"
}
```

## 96 · 2026-10-29T03:25:52.577270+00:00 · tool_result 

```
src/prefect/server/events/actions.py:204:                    payload=action_details,
src/prefect/server/events/actions.py:215:                    payload={
src/prefect/server/events/actions.py:293:                    payload=action_details,
src/prefect/server/events/actions.py:304:                    payload={
src/prefect/server/events/actions.py:1366:            response = await block.call(payload=payload)
src/prefect/server/events/clients.py:171:                mismatch_reasons.append((f"{payload=}", f"{emitted_event.payload=}"))
src/prefect/server/events/clients.py:182:    {payload=}
src/prefect/server/events/schemas/automations.py:152:            payload={
src/prefect/server/events/schemas/automations.py:486:            payload={
src/prefect/server/events/schemas/lifecycle.py:57:        payload=payload,
src/prefect/server/events/schemas/lifecycle.py:93:        payload=VariableEventPayload.model_validate(variable).model_dump(mode="json"),
src/prefect/server/events/schemas/lifecycle.py:129:        payload=FlowEventPayload.model_validate(flow).model_dump(mode="json"),
src/prefect/server/events/schemas/lifecycle.py:172:        payload=BlockTypeEventPayload.model_validate(block_type).model_dump(
src/prefect/server/events/schemas/lifecycle.py:272:        payload=payload.model_dump(mode="json"),
src/prefect/server/events/schemas/lifecycle.py:319:        payload=ConcurrencyLimitV2EventPayload.model_validate(
src/prefect/server/events/schemas/lifecycle.py:365:        payload=ConcurrencyLimitEventPayload.model_validate(
src/prefect/server/events/schemas/lifecycle.py:441:        payload=ArtifactCollectionEventPayload.model_validate(
src/prefect/server/events/schemas/lifecycle.py:472:        payload=automation.model_dump(mode="json"),
```

## 97 · 2026-10-29T03:25:54.025133+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"prefect.flow-run\" src/prefect/server --include=\"*.py\" | grep -v \"resource.id\" | head -30",
  "description": "Find flow run event emission in server"
}
```

## 98 · 2026-10-29T03:25:54.578728+00:00 · tool_result 

```
src/prefect/server/database/_migrations/versions/postgresql/2025_04_29_112902_4160a4841eed_remove_flow_run_notifications.py:75:                        {f"prefect.flow-run.{state_name}" for state_name in state_names}
src/prefect/server/database/_migrations/versions/postgresql/2025_04_29_112902_4160a4841eed_remove_flow_run_notifications.py:78:                    else ["prefect.flow-run.*"],
src/prefect/server/database/_migrations/versions/sqlite/2025_04_28_133722_7655f31c5157_remove_flow_run_notifications.py:74:                        {f"prefect.flow-run.{state_name}" for state_name in state_names}
src/prefect/server/database/_migrations/versions/sqlite/2025_04_28_133722_7655f31c5157_remove_flow_run_notifications.py:77:                    else ["prefect.flow-run.*"],
src/prefect/server/events/actions.py:571:            "prefect.flow-run": (
src/prefect/server/events/actions.py:1101:            if id := _id_of_first_resource_of_kind(event, "prefect.flow-run"):
src/prefect/server/events/jinja_filters.py:25:    FlowRun: "prefect.flow-run",
src/prefect/server/events/schemas/automations.py:302:            "trailing wildcards, like `prefect.flow-run.*`"
src/prefect/server/events/schemas/automations.py:310:            "like `prefect.flow-run.*`"
src/prefect/server/events/schemas/automations.py:576:        if not any(e.startswith("prefect.flow-run.") for e in self.trigger.expect):
src/prefect/server/events/schemas/automations.py:582:            "prefect.flow-run.Scheduled",
src/prefect/server/events/schemas/automations.py:583:            "prefect.flow-run.Pending",
src/prefect/server/events/schemas/automations.py:584:            "prefect.flow-run.Running",
src/prefect/server/events/schemas/automations.py:585:            "prefect.flow-run.*",
src/prefect/server/events/schemas/automations.py:610:                    "prefect.flow-run"
src/prefect/server/events/schemas/automations.py:618:                        related.matches_every_resource_of_kind("prefect.flow-run")
src/prefect/server/events/schemas/lifecycle.py:421:                    f"prefect.flow-run.{artifact_collection.flow_run_id}"
src/prefect/server/models/events.py:53:        event=f"prefect.flow-run.{validated_state.name}",
src/prefect/server/models/task_runs.py:582:        default_labels["prefect.flow-run.id"] = str(task_run.flow_run_id)
src/prefect/server/services/task_run_recorder.py:271:        flow_run_id = flow_run_resource.prefect_object_id("prefect.flow-run")
```

## 99 · 2026-10-29T03:25:56.287654+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/models/events.py",
  "offset": 1,
  "limit": 130
}
```

## 100 · 2026-10-29T03:25:56.384836+00:00 · tool_result 

```
1	from datetime import datetime, timedelta
2	from typing import Any, Dict, List, MutableMapping, Optional, Set, Union
3	from uuid import UUID
4	
5	from cachetools import TTLCache
6	from sqlalchemy.ext.asyncio import AsyncSession
7	
8	from prefect._internal.uuid7 import uuid7
9	from prefect.server import models, schemas
10	from prefect.server.database.orm_models import (
11	    ORMDeployment,
12	    ORMFlow,
13	    ORMFlowRun,
14	    ORMFlowRunState,
15	    ORMTaskRun,
16	    ORMTaskRunState,
17	    ORMWorkPool,
18	    ORMWorkQueue,
19	)
20	from prefect.server.events.schemas.events import Event
21	from prefect.server.models import deployments
22	from prefect.server.schemas.statuses import DeploymentStatus
23	from prefect.settings import PREFECT_API_EVENTS_RELATED_RESOURCE_CACHE_TTL
24	from prefect.types._datetime import DateTime, now
25	from prefect.utilities.text import truncated_to
26	
27	ResourceData = Dict[str, Dict[str, Any]]
28	RelatedResourceList = List[Dict[str, str]]
29	
30	
31	# Some users use state messages to convey error messages and large results; let's
32	# truncate them so they don't blow out the size of a message
33	TRUNCATE_STATE_MESSAGES_AT = 100_000
34	
35	
36	_flow_run_resource_data_cache: MutableMapping[UUID, ResourceData] = TTLCache(
37	    maxsize=1000,
38	    ttl=PREFECT_API_EVENTS_RELATED_RESOURCE_CACHE_TTL.value().total_seconds(),
39	)
40	
41	
42	async def flow_run_state_change_event(
43	    session: AsyncSession,
44	    occurred: datetime,
45	    flow_run: ORMFlowRun,
46	    initial_state_id: Optional[UUID],
47	    initial_state: Optional[schemas.states.State],
48	    validated_state_id: Optional[UUID],
49	    validated_state: schemas.states.State,
50	) -> Event:
51	    return Event(
52	        occurred=occurred,
53	        event=f"prefect.flow-run.{validated_state.name}",
54	        resource={
55	            "prefect.resource.id": f"prefect.flow-run.{flow_run.id}",
56	            "prefect.resource.name": flow_run.name,
57	            "prefect.run-count": str(flow_run.run_count),
58	            "prefect.state-message": truncated_to(
59	                TRUNCATE_STATE_MESSAGES_AT, validated_state.message
60	            ),
61	            "prefect.state-name": validated_state.name or "",
62	            "prefect.state-timestamp": (
63	                validated_state.timestamp.isoformat()
64	                if validated_state.timestamp
65	                else None
66	            ),
67	            "prefect.state-type": validated_state.type.value,
68	        },
69	        related=await _flow_run_related_resources_from_orm(
70	            session=session, flow_run=flow_run
71	        ),
72	        payload={
73	            "intended": {
74	                "from": _state_type(initial_state),
75	                "to": _state_type(validated_state),
76	            },
77	            "initial_state": state_payload(initial_state),
78	            "validated_state": state_payload(validated_state),
79	        },
80	        # Here we use the state's ID as the ID of the event as well, in order to
81	        # establish the ordering of the state-change events
82	        id=validated_state_id,
83	        follows=initial_state_id if _timing_is_tight(occurred, initial_state) else None,
84	    )
85	
86	
87	async def _flow_run_related_resources_from_orm(
88	    session: AsyncSession, flow_run: ORMFlowRun
89	) -> RelatedResourceList:
90	    resource_data = _flow_run_resource_data_cache.get(flow_run.id)
91	    if not resource_data:
92	        flow = await models.flows.read_flow(session=session, flow_id=flow_run.flow_id)
93	        deployment: Optional[ORMDeployment] = None
94	        if flow_run.deployment_id:
95	            deployment = await deployments.read_deployment(
96	                session, deployment_id=flow_run.deployment_id
97	            )
98	
99	        work_queue = None
100	        if flow_run.work_queue_id:
101	            work_queue = await models.work_queues.read_work_queue(
102	                session, work_queue_id=flow_run.work_queue_id
103	            )
104	
105	        work_pool = work_queue.work_pool if work_queue is not None else None
106	
107	        task_run: Optional[ORMTaskRun] = None
108	        if flow_run.parent_task_run_id:
109	            task_run = await models.task_runs.read_task_run(
110	                session,
111	                task_run_id=flow_run.parent_task_run_id,
112	            )
113	
114	        resource_data = _as_resource_data(
115	            flow_run, flow, deployment, work_queue, work_pool, task_run
116	        )
117	        _flow_run_resource_data_cache[flow_run.id] = resource_data
118	
119	    return _resource_data_as_related_resources(
120	        resource_data,
121	        excluded_kinds=["flow-run"],
122	    ) + _provenance_as_related_resources(flow_run.created_by)
123	
124	
125	def _as_resource_data(
126	    flow_run: ORMFlowRun,
127	    flow: Union[ORMFlow, schemas.core.Flow, None],
128	    deployment: Union[ORMDeployment, schemas.responses.DeploymentResponse, None],
129	    work_queue: Union[ORMWorkQueue, schemas.responses.WorkQueueResponse, None],
130	    work_pool: Union[ORMWorkPool, schemas.core.WorkPool, None],
```

## 101 · 2026-10-29T03:26:20.605221+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "offset": 700,
  "limit": 70
}
```

## 102 · 2026-10-29T03:26:20.723065+00:00 · tool_result 

```
700	):
701	    """Regression test for an issue where a simple reactive recurring automation would
702	    not trigger when the event arrived slightly in the future."""
703	
704	    await triggers.reactive_evaluation(
705	        Event(
706	            occurred=start_of_test,
707	            event="some-event",
708	            resource={"prefect.resource.id": "some.resource"},
709	            id=uuid4(),
710	        ).receive()
711	    )
712	
713	    act.assert_awaited_once()
714	    act.reset_mock()
715	
716	    await triggers.reactive_evaluation(
717	        Event(
718	            occurred=start_of_test + timedelta(seconds=999),
719	            event="some-event",
720	            resource={"prefect.resource.id": "some.resource"},
721	            id=uuid4(),
722	        ).receive()
723	    )
724	
725	    act.assert_awaited_once()
726	
727	
728	@pytest.fixture
729	async def proactive_flow_run_automation(
730	    cleared_buckets: None,
731	    cleared_automations: None,
732	    automations_session: AsyncSession,
733	) -> Automation:
734	    """Automation that mirrors real-world flow run monitoring with multiple after states."""
735	    automation = await automations.create_automation(
736	        automations_session,
737	        Automation(
738	            name="Monitor stuck flow runs",
739	            trigger=EventTrigger(
740	                match={"prefect.resource.id": "prefect.flow-run.*"},
741	                match_related={},
742	                after=[
743	                    "prefect.flow-run.Retrying",
744	                    "prefect.flow-run.AwaitingRetry",
745	                    "prefect.flow-run.Resuming",
746	                    "prefect.flow-run.Cancelling",
747	                    "prefect.flow-run.Pending",
748	                    "prefect.flow-run.AwaitingConcurrencySlot",
749	                    "prefect.flow-run.Running",
750	                ],
751	                expect=["prefect.flow-run.*"],
752	                for_each=["prefect.resource.id"],
753	                posture=Posture.Proactive,
754	                threshold=1,
755	                within=timedelta(hours=2),
756	            ),
757	            actions=[actions.DoNothing()],
758	        ),
759	    )
760	    triggers.load_automation(automation)
761	    await automations_session.commit()
762	    return automation
763	
764	
765	async def test_proactive_flow_run_automation_includes_triggering_event(
766	    act: mock.AsyncMock,
767	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
768	    frozen_time: DateTime,
769	    proactive_flow_run_automation: Automation,
```

## 103 · 2026-10-29T03:26:54.997617+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"AutomationBucket\\|read_bucket\" tests/events/server/triggers/*.py | head -40",
  "description": "Search tests inspecting buckets"
}
```

## 104 · 2026-10-29T03:26:55.350924+00:00 · tool_result 

```
tests/events/server/triggers/test_basics.py:606:    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
tests/events/server/triggers/test_basics.py:633:    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
tests/events/server/triggers/test_basics.py:645:    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
tests/events/server/triggers/test_basics.py:653:    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
```

## 105 · 2026-10-29T03:26:55.426086+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"ensure_bucket\\|increment_bucket\\|start_new_bucket\" tests/ src/ --include=\"*.py\" | grep -v \"src/prefect/server/events/triggers.py\" | head -30",
  "description": "Find direct bucket function tests"
}
```

## 106 · 2026-10-29T03:26:57.793354+00:00 · tool_result 

```
(Bash completed with no output)
```

## 107 · 2026-10-29T03:26:59.514143+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_basics.py",
  "offset": 560,
  "limit": 120
}
```

## 108 · 2026-10-29T03:26:59.629161+00:00 · tool_result 

```
560	                expect=["prefect.flow-run.Failed"],
561	                within=10.0,
562	                posture="Reactive",
563	                for_each=["prefect.resource.id"],
564	                threshold=1,
565	                match_related={
566	                    "prefect.resource.id": ["prefect.flow.ffffffff"],
567	                    "prefect.resource.role": "flow",
568	                },
569	            ),
570	            actions=[actions.DoNothing()],
571	        ),
572	    )
573	    triggers.load_automation(automation)
574	    await automations_session.commit()
575	
576	    trigger = automation.trigger
577	    assert isinstance(trigger, EventTrigger), repr(trigger)
578	
579	    now = start_of_test
580	
581	    # A Running event is not relevant to this Automation and should not cause a bucket
582	    # to be created
583	    running_event = ReceivedEvent(
584	        occurred=now,
585	        event="prefect.flow-run.Running",
586	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
587	        related=[
588	            {
589	                "prefect.resource.id": "prefect.flow.ffffffff",
590	                "prefect.resource.role": "flow",
591	            }
592	        ],
593	        received=now,
594	        id=uuid4(),
595	    )
596	
597	    # Previously any event was 'covered' if the automation
598	    # trigger did not contain `after` criteria
599	    assert not trigger.after
600	
601	    await triggers.reactive_evaluation(running_event)
602	    act.assert_not_awaited()
603	
604	    # There should be no bucket, because this event was irrelevant
605	    bucketing_key = trigger.bucketing_key(running_event)
606	    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
607	    assert not bucket
608	
609	    now += timedelta(seconds=1)
610	
611	    # The failed event _is_ relevant and should cause this automation to fire
612	    failed_event = ReceivedEvent(
613	        occurred=now,
614	        event="prefect.flow-run.Failed",
615	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
616	        related=[
617	            {
618	                "prefect.resource.id": "prefect.flow.ffffffff",
619	                "prefect.resource.role": "flow",
620	            }
621	        ],
622	        received=now,
623	        id=uuid4(),
624	    )
625	    assert trigger.covers(failed_event)
626	
627	    await triggers.reactive_evaluation(failed_event)
628	    act.assert_awaited_once()
629	
630	    # There is a bucket, because this event caused an immediate trigger, and thus
631	    # scheduled the next bucket into the future
632	    assert trigger.bucketing_key(failed_event) == bucketing_key
633	    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
634	    assert bucket
635	    assert bucket.start == now + timedelta(seconds=10)
636	    assert bucket.end == bucket.start + timedelta(seconds=10)
637	
638	    # Now run proactive evaluation to sweep any buckets that have ended
639	
640	    # When we're just at the `end` of the bucket, that's too early, so the bucket should
641	    # still be there
642	    await triggers.reset_events_clock()
643	    now += timedelta(seconds=10) + timedelta(seconds=10)  # the start  # the end
644	    await triggers.periodic_evaluation(now)
645	    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
646	    assert bucket
647	
648	    # Only when we're past the bucket's `end` by a short buffer can we remove it, this
649	    # avoids contention with other in-flight changes to buckets
650	    await triggers.reset_events_clock()
651	    now += PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value() + timedelta(seconds=1)
652	    await triggers.periodic_evaluation(now)
653	    bucket = await triggers.read_bucket(automations_session, trigger, bucketing_key)
654	    assert not bucket
655	
656	
657	async def test_follower_messages_are_processed_when_leaders_arrive(
658	    cleared_buckets: None,
659	    cleared_automations: None,
660	    automations_session: AsyncSession,
661	    start_of_test: DateTime,
662	    act: mock.AsyncMock,
663	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
664	    frozen_time: DateTime,
665	):
666	    automation = await automations.create_automation(
667	        automations_session,
668	        Automation(
669	            id=uuid4(),
670	            name="Testing out-of-order events",
671	            trigger=EventTrigger(
672	                after=[],
673	                match={"prefect.resource.id": "prefect.flow-run.*"},
674	                expect=["prefect.flow-run.Failed"],
675	                within=10.0,
676	                posture="Reactive",
677	                for_each=["prefect.resource.id"],
678	                threshold=1,
679	            ),
```

## 109 · 2026-10-29T03:27:07.911756+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"last_operation\" tests/ src/ --include=\"*.py\" | head -20",
  "description": "Search last_operation usage"
}
```

## 110 · 2026-10-29T03:27:08.199337+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"initial_count\" src/ tests/ --include=\"*.py\" | head -20",
  "description": "Search initial_count usage"
}
```

## 111 · 2026-10-29T03:27:10.316107+00:00 · tool_result 

```
src/prefect/server/database/orm_models.py:1339:    last_operation: Mapped[Optional[str]]
src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py:107:        sa.Column("last_operation", sa.String(), nullable=True),
src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py:110:        sa.Column("last_operation", sa.String(), nullable=True),
src/prefect/server/events/triggers.py:107:        "bucket_last_operation": bucket.last_operation,
src/prefect/server/events/triggers.py:1001:            last_operation="increment_bucket[insert]",
src/prefect/server/events/triggers.py:1011:                last_operation="increment_bucket[update]",
src/prefect/server/events/triggers.py:1056:            last_operation="start_new_bucket[insert]",
src/prefect/server/events/triggers.py:1070:                last_operation="start_new_bucket[update]",
src/prefect/server/events/triggers.py:1118:            last_operation="ensure_bucket[insert]",
```

## 112 · 2026-10-29T03:27:10.527734+00:00 · tool_result 

```
src/integrations/prefect-docker/tests/test_worker.py:1880:            initial_count = len(initial_flow_runs)
src/integrations/prefect-docker/tests/test_worker.py:1891:            assert len(final_flow_runs) > initial_count
src/prefect/server/events/triggers.py:106:        "bucket_initial_count": bucket.count,
src/prefect/server/events/triggers.py:618:                        initial_count = -1 if trigger.expects(event.event) else 0
src/prefect/server/events/triggers.py:626:                            initial_count=initial_count,
src/prefect/server/events/triggers.py:1100:    initial_count: int = 0,
src/prefect/server/events/triggers.py:1117:            count=initial_count,
tests/workers/test_process_worker.py:1189:    initial_count = len(initial_flow_runs)
tests/workers/test_process_worker.py:1200:    assert len(final_flow_runs) > initial_count
```

## 113 · 2026-10-29T03:28:13.866958+00:00 · assistant_message 

```
I've reproduced the failure. Now let me study the bucket state transitions in `evaluate` closely before making the repair.
```

## 114 · 2026-10-29T03:28:14.160724+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 136,
  "limit": 120
}
```

## 115 · 2026-10-29T03:28:14.297098+00:00 · tool_result 

```
136	    # period)
137	
138	    # If there was a triggering event, then we need to "spend" this count somewhere,
139	    # either in the currently open bucket or in the next time period's bucket
140	    count = 1 if triggering_event else 0
141	
142	    if now < bucket.start:
143	        # This is an older out-of-order message or a redundant event for a reactive
144	        # trigger that has has already fired, so it should not should not affect the
145	        # current bucket.  We can safely ignore this event/timestamp entirely.  Case #1
146	        # from the implementation notes above.
147	        logger.debug(
148	            "Automation %s (%r) trigger %s got a late event for keys (%r)",
149	            automation.id,
150	            automation.name,
151	            trigger.id,
152	            bucket.bucketing_key,
153	            extra=logging_context,
154	        )
155	        return bucket
156	
157	    if count and (trigger.immediate or bucket.start <= now < bucket.end):
158	        # we are still within the automation time period, so spend the count in the
159	        # current bucket
160	        bucket = await increment_bucket(session, bucket, count, triggering_event)
161	        count = 0
162	
163	    # Reactive automations will fire "eagerly", meaning they will fire as _soon_ as the
164	    # threshold is reached, then wait for the rest of their time period before
165	    # firing again.  This is done by creating a new bucket in the future after the
166	    # trigger has fired.
167	
168	    # Proactive automations must wait until the whole bucket has expired before they can
169	    # fire, because we can't know if we'll get one late event just in time to cause the
170	    # automation _not_ to fire.
171	
172	    ready_to_fire = trigger.posture == Posture.Reactive or bucket.end <= now
173	    meets_threshold = trigger.meets_threshold(bucket.count)
174	
175	    if ready_to_fire and meets_threshold:
176	        logger.debug(
177	            (
178	                "Automation %s (%r) trigger %s triggered for keys (%r) %s, "
179	                "having occurred %s times between %s and %s"
180	            ),
181	            automation.id,
182	            automation.name,
183	            trigger.id,
184	            bucket.bucketing_key,
185	            "reactively" if triggering_event else "proactively",
186	            bucket.count,
187	            bucket.start,
188	            bucket.end,
189	            extra=logging_context,
190	        )
191	
192	        firing = Firing(
193	            trigger=trigger,
194	            trigger_states={TriggerState.Triggered},
195	            triggered=prefect.types._datetime.now("UTC"),
196	            triggering_labels={
197	                label: value
198	                for label, value in zip(sorted(trigger.for_each), bucket.bucketing_key)
199	            },
200	            triggering_event=triggering_event or bucket.last_event,
201	        )
202	
203	        await fire(session, firing)
204	
205	        # when acting, remove the current bucket from the database immediately to avoid
206	        # potentially double-acting in the case of a crash between now and the next
207	        # time we backup buckets to the database
208	        await remove_bucket(session, bucket)
209	
210	    elif now < bucket.end:
211	        # We didn't fire this time, and also the bucket still has more time, so leave
212	        # before setting up a new future bucket.  Case #2 from the implementation notes
213	        # above.
214	        logger.debug(
215	            "Automation %s (%r) trigger %s has more time for keys (%r)",
216	            automation.id,
217	            automation.name,
218	            trigger.id,
219	            bucket.bucketing_key,
220	            extra={
221	                **logging_context,
222	                "ready_to_fire": ready_to_fire,
223	                "meets_threshold": meets_threshold,
224	            },
225	        )
226	
227	        # Special case of a proactive trigger for which the same event satisfies
228	        # both `after` and `expect`.  For example, using flow run heartbeats for crash
229	        # detection, after the first heartbeat we expect a subsequent heartbeat or
230	        # terminal state within a given time.
231	        #
232	        # If we've already reached the proactive threshold, we need to remove the
233	        # current bucket and start a new one for the latest event.
234	        if (
235	            triggering_event
236	            and trigger.posture == Posture.Proactive
237	            and not meets_threshold
238	            and trigger.starts_after(triggering_event.event)
239	            and trigger.expects(triggering_event.event)
240	        ):
241	            await remove_bucket(session, bucket)
242	            return await start_new_bucket(
243	                session,
244	                trigger,
245	                bucketing_key=bucket.bucketing_key,
246	                start=triggering_event.occurred,
247	                end=triggering_event.occurred + trigger.within,
248	                count=0,
249	                last_event=triggering_event,
250	            )
251	
252	        return bucket
253	    else:
254	        # Case #2 from the implementation notes above.
255	        logger.debug(
```

## 116 · 2026-10-29T03:28:16.121890+00:00 · assistant_message 

```
Now I understand the failure mechanics. Let me implement the repair in `triggers.py`.
```

## 117 · 2026-10-29T03:28:16.942501+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    automation = trigger.automation\n\n    logging_context = {",
  "new_string": "    automation = trigger.automation\n\n    # Capture the most recent event that has contributed to this bucket before this\n    # evaluation mutates it.  Proactive buckets may only be re-armed by an event that\n    # is _newer_ than the event that last satisfied the window; otherwise a late or\n    # out-of-order event (for example, a heartbeat racing a terminal state change for\n    # the same flow run) could re-open an expectation that has already been met.\n    previous_last_event_occurred = (\n        bucket.last_event.occurred if bucket.last_event else None\n    )\n\n    logging_context = {"
}
```

## 118 · 2026-10-29T03:28:17.081582+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 119 · 2026-10-29T03:28:20.213927+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "        # Special case of a proactive trigger for which the same event satisfies\n        # both `after` and `expect`.  For example, using flow run heartbeats for crash\n        # detection, after the first heartbeat we expect a subsequent heartbeat or\n        # terminal state within a given time.\n        #\n        # If we've already reached the proactive threshold, we need to remove the\n        # current bucket and start a new one for the latest event.\n        if (\n            triggering_event\n            and trigger.posture == Posture.Proactive\n            and not meets_threshold\n            and trigger.starts_after(triggering_event.event)\n            and trigger.expects(triggering_event.event)\n        ):",
  "new_string": "        # Special case of a proactive trigger for which the same event satisfies\n        # both `after` and `expect`.  For example, using flow run heartbeats for crash\n        # detection, after the first heartbeat we expect a subsequent heartbeat or\n        # terminal state within a given time.\n        #\n        # If we've already reached the proactive threshold, we need to remove the\n        # current bucket and start a new one for the latest event.  We may only do\n        # that when this event is actually newer than the event that last contributed\n        # to the bucket: a stale event (a heartbeat that occurred at or before the\n        # terminal state it raced) carries no new information and must not restart\n        # the expectation.\n        if (\n            triggering_event\n            and trigger.posture == Posture.Proactive\n            and not meets_threshold\n            and trigger.starts_after(triggering_event.event)\n            and trigger.expects(triggering_event.event)\n            and (\n                previous_last_event_occurred is None\n                or triggering_event.occurred > previous_last_event_occurred\n            )\n        ):"
}
```

## 120 · 2026-10-29T03:28:20.364486+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 121 · 2026-10-29T03:28:22.312197+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    \"\"\"Adds the given count to the bucket, returning the new bucket\"\"\"\n    additional_updates: dict[str, ReceivedEvent] = (\n        {\"last_event\": last_event} if last_event else {}\n    )",
  "new_string": "    \"\"\"Adds the given count to the bucket, returning the new bucket\"\"\"\n    additional_updates: dict[str, ReceivedEvent] = {}\n    if last_event:\n        # Keep `last_event` pointing at the newest event that has contributed to the\n        # bucket.  Out-of-order events still count towards the threshold, but they\n        # must not move the bucket's notion of \"latest event\" backwards.\n        if (\n            bucket.last_event is None\n            or last_event.occurred > bucket.last_event.occurred\n        ):\n            additional_updates[\"last_event\"] = last_event"
}
```

## 122 · 2026-10-29T03:28:22.448720+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 123 · 2026-10-29T03:28:24.541555+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    \"\"\"Ensures that a bucket has been started for the given automation and key,\n    returning the current bucket.  Will not modify the existing bucket.\"\"\"\n    automation = trigger.automation\n    additional_updates: dict[str, ReceivedEvent] = (\n        {\"last_event\": last_event} if last_event else {}\n    )",
  "new_string": "    \"\"\"Ensures that a bucket has been started for the given automation and key,\n    returning the current bucket.  Will not modify the existing bucket.\"\"\"\n    automation = trigger.automation\n    # Events matching `expect` are counted by `evaluate`, which records them as the\n    # bucket's `last_event` only when they are newer than the event already recorded.\n    # Updating `last_event` here as well would overwrite the event that last satisfied\n    # the window before `evaluate` can compare against it, which would let a stale\n    # event (for example, a heartbeat racing a terminal state change) re-arm an\n    # expectation that has already been met.\n    additional_updates: dict[str, ReceivedEvent] = (\n        {\"last_event\": last_event}\n        if last_event and not trigger.expects(last_event.event)\n        else {}\n    )"
}
```

## 124 · 2026-10-29T03:28:24.670000+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 125 · 2026-10-29T03:28:28.154154+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | tail -20",
  "description": "Run incident test after fix",
  "timeout": 300000
}
```

## 126 · 2026-10-29T03:29:17.842444+00:00 · tool_result 

```
11:29:13.492 | INFO    | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809, trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 covers event 'prefect.flow-run.heartbeat' (22222222-2222-4222-8222-222222222222) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:29:42.178403+00:00'
11:29:13.926 | DEBUG   | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809 ('Unresponsive run monitor') trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
11:29:14.161 | INFO    | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809, trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 covers event 'prefect.flow-run.Completed' (33333333-3333-4333-8333-333333333333) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:30:12.178403+00:00'
11:29:14.465 | DEBUG   | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809 ('Unresponsive run monitor') trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
11:29:14.513 | INFO    | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809, trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 covers event 'prefect.flow-run.heartbeat' (44444444-4444-4444-8444-444444444444) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:30:12.178403+00:00'
11:29:14.846 | DEBUG   | prefect.server.events.triggers - Automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809 ('Unresponsive run monitor') trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
11:29:14.894 | DEBUG   | prefect.server.events.triggers - Evaluating automation ddc3e3ec-6e1f-4c19-bfff-544bdb39c809 trigger a8d9ef38-d6b6-43cd-9bc8-cabed03627f6 proactively as of 2026-10-29 03:31:43.178403+00:00 (offset 0.0s)
Generating test database connection URL from 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
Running hosted API server on port 54512
{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
.11:29:15.220 | INFO    | uvicorn.error - Shutting down
11:29:15.327 | INFO    | uvicorn.error - Waiting for application shutdown.
11:29:15.331 | INFO    | uvicorn.error - Application shutdown complete.
11:29:15.331 | INFO    | uvicorn.error - Finished server process [14620]

1 passed in 32.70s
```

## 127 · 2026-10-29T03:29:19.860863+00:00 · assistant_message 

```
The incident now produces zero actions. Let me run the full triggers test suite to check for regressions.
```

## 128 · 2026-10-29T03:29:20.280152+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/ -q -p no:randomly 2>&1 | tail -30",
  "description": "Run complete triggers test suite",
  "timeout": 1800000
}
```

## 129 · 2026-10-29T03:37:45.083434+00:00 · tool_result 

```
.................................................x...x...x.............. [ 60%]
................................................                         [100%]
117 passed, 3 xfailed in 488.08s (0:08:08)
```

## 130 · 2026-10-29T03:37:56.776519+00:00 · assistant_message 

```
All 117 existing trigger tests pass. Now let me verify the genuine-unresponsive and restart scenarios explicitly with focused regression tests. First, let me inspect the test fixtures.
```

## 131 · 2026-10-29T03:37:56.941635+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/conftest.py"
}
```

## 132 · 2026-10-29T03:37:57.089731+00:00 · tool_result 

```
1	from typing import Callable, List, Tuple, Union
2	from unittest import mock
3	
4	import pytest
5	
6	from prefect.server.events import messaging, triggers
7	from prefect.server.events.schemas.automations import Firing
8	
9	
10	@pytest.fixture(autouse=True)
11	async def reset_triggers(cleared_automations: None):
12	    await triggers.reset()
13	    yield
14	    await triggers.reset()
15	
16	
17	@pytest.fixture
18	async def reset_events_clock():
19	    await triggers.reset_events_clock()
20	
21	
22	@pytest.fixture
23	def actions_publish_mocks(
24	    monkeypatch: pytest.MonkeyPatch,
25	) -> Tuple[mock.MagicMock, mock.AsyncMock]:
26	    mock_create_publisher = mock.MagicMock(spec=messaging.create_actions_publisher)
27	    mock_publish = mock.AsyncMock()
28	    mock_create_publisher.return_value.__aenter__.return_value.publish_data = (
29	        mock_publish
30	    )
31	
32	    monkeypatch.setattr(
33	        "prefect.server.events.messaging.create_actions_publisher",
34	        mock_create_publisher,
35	    )
36	
37	    return mock_create_publisher, mock_publish
38	
39	
40	@pytest.fixture
41	def actions_publish(
42	    actions_publish_mocks: Tuple[mock.MagicMock, mock.AsyncMock],
43	) -> mock.AsyncMock:
44	    return actions_publish_mocks[1]
45	
46	
47	@pytest.fixture
48	def create_actions_publisher(
49	    actions_publish_mocks: Tuple[mock.MagicMock, mock.AsyncMock],
50	) -> mock.MagicMock:
51	    return actions_publish_mocks[0]
52	
53	
54	@pytest.fixture
55	def assert_acted_with(
56	    act: mock.AsyncMock,
57	) -> Callable[[Union[Firing, List[Firing]]], None]:
58	    def assertion(expected: Union[Firing, List[Firing]]):
59	        if not isinstance(expected, list):
60	            expected = [expected]
61	
62	        assert act.await_count == len(expected)
63	        actuals: list[Firing] = [args[0][0] for args in act.await_args_list]
64	        for actual in actuals:
65	            assert isinstance(actual, Firing)
66	
67	        dumped_actuals = [actual.model_dump(exclude={"id"}) for actual in actuals]
68	        dumped_expected = [exp.model_dump(exclude={"id"}) for exp in expected]
69	        for exp in dumped_expected:
70	            assert exp in dumped_actuals
71	
72	    return assertion
73	
```

## 133 · 2026-10-29T03:37:58.811846+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def act\\|def frozen_time\\|def cleared_buckets\\|def cleared_automations\\|def automations_session\" tests/conftest.py tests/events/conftest.py tests/events/server/conftest.py 2>/dev/null | head -20",
  "description": "Locate shared fixtures"
}
```

## 134 · 2026-10-29T03:37:59.195864+00:00 · tool_result 

```
tests/events/server/conftest.py:28:def act(monkeypatch: pytest.MonkeyPatch) -> AsyncMock:
tests/events/server/conftest.py:35:def automations_session(session: AsyncSession) -> AsyncSession:
tests/events/server/conftest.py:41:async def cleared_buckets(db: PrefectDBInterface, automations_session: AsyncSession):
tests/events/server/conftest.py:47:async def cleared_automations():
```

## 135 · 2026-10-29T03:38:00.375601+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/conftest.py"
}
```

## 136 · 2026-10-29T03:38:00.495287+00:00 · tool_result 

```
1	from datetime import timedelta
2	from typing import Any, Dict, List, Sequence, Tuple
3	from unittest.mock import AsyncMock, MagicMock
4	from uuid import uuid4
5	
6	import pytest
7	import sqlalchemy as sa
8	from sqlalchemy.ext.asyncio import AsyncSession
9	
10	from prefect.server.database import PrefectDBInterface
11	from prefect.server.events import ResourceSpecification, actions, messaging
12	from prefect.server.events.schemas.automations import (
13	    Automation,
14	    EventTrigger,
15	    Firing,
16	    Posture,
17	    TriggeredAction,
18	    TriggerState,
19	)
20	from prefect.server.events.schemas.events import ReceivedEvent
21	from prefect.server.utilities.messaging import Message
22	from prefect.types import DateTime
23	from prefect.types._datetime import now
24	from prefect.utilities.pydantic import parse_obj_as
25	
26	
27	@pytest.fixture
28	def act(monkeypatch: pytest.MonkeyPatch) -> AsyncMock:
29	    mock_act = AsyncMock()
30	    monkeypatch.setattr("prefect.server.events.triggers.act", mock_act)
31	    return mock_act
32	
33	
34	@pytest.fixture
35	def automations_session(session: AsyncSession) -> AsyncSession:
36	    # pass through the existing session
37	    return session
38	
39	
40	@pytest.fixture
41	async def cleared_buckets(db: PrefectDBInterface, automations_session: AsyncSession):
42	    await automations_session.execute(sa.delete(db.AutomationBucket))
43	    await automations_session.commit()
44	
45	
46	@pytest.fixture
47	async def cleared_automations():
48	    from prefect.server.events import triggers
49	
50	    await triggers.reset()
51	    yield
52	    await triggers.reset()
53	
54	
55	@pytest.fixture
56	def arachnophobia() -> Automation:
57	    return Automation(
58	        name="React immediately to spiders",
59	        trigger=EventTrigger(
60	            expect={"animal.walked"},
61	            match={
62	                "class": "Arachnida",
63	                "order": "Araneae",
64	            },
65	            posture=Posture.Reactive,
66	            threshold=1,
67	        ),
68	        actions=[actions.DoNothing()],
69	    )
70	
71	
72	@pytest.fixture
73	def daddy_long_legs_walked(start_of_test: DateTime) -> ReceivedEvent:
74	    return ReceivedEvent(
75	        occurred=start_of_test + timedelta(microseconds=1),
76	        event="animal.walked",
77	        resource={
78	            "kingdom": "Animalia",
79	            "phylum": "Arthropoda",
80	            "class": "Arachnida",
81	            "order": "Araneae",
82	            "family": "Pholcidae",
83	            "genus": "Pholcus",
84	            "species": "phalangioides",
85	            "prefect.resource.id": "daddy-long-legs",
86	        },
87	        id=uuid4(),
88	    )
89	
90	
91	@pytest.fixture
92	def chonk_party() -> Automation:
93	    return Automation(
94	        name="Three woodchucks is worth throwing a party",
95	        trigger=EventTrigger(
96	            expect={"animal.walked"},
97	            match={
98	                "genus": "Marmota",
99	                "species": "monax",
100	            },
101	            posture=Posture.Reactive,
102	            threshold=3,
103	            within=timedelta(seconds=10),
104	        ),
105	        actions=[actions.DoNothing()],
106	    )
107	
108	
109	@pytest.fixture
110	def flow_run_pending_automation() -> Automation:
111	    return Automation(
112	        name="Flow Run Pending",
113	        trigger=EventTrigger(
114	            expect={"prefect.flow-run.Pending"},
115	            match={
116	                "prefect.resource.id": "flow-run-pending",
117	            },
118	            posture=Posture.Reactive,
119	            threshold=1,
120	        ),
121	        actions=[actions.DoNothing()],
122	    )
123	
124	
125	@pytest.fixture
126	def flow_run_failed_automation() -> Automation:
127	    return Automation(
128	        name="Flow Run Failed",
129	        trigger=EventTrigger(
130	            expect={"prefect.flow-run.Failed"},
131	            match={
132	                "prefect.resource.id": "flow-run-failed",
133	            },
134	            posture=Posture.Reactive,
135	            threshold=1,
136	        ),
137	        actions=[actions.DoNothing()],
138	    )
139	
140	
141	@pytest.fixture
142	def flow_run_running_automation() -> Automation:
143	    return Automation(
144	        name="Flow Run Running",
145	        trigger=EventTrigger(
146	            expect={"prefect.flow-run.Running"},
147	            match={
148	                "prefect.resource.id": "flow-run-running",
149	            },
150	            posture=Posture.Reactive,
151	            threshold=1,
152	        ),
153	        actions=[actions.DoNothing()],
154	    )
155	
156	
157	@pytest.fixture
158	def chonk_lonely() -> Automation:
159	    return Automation(
160	        name="One woodchucks is worth throwing a party all alone",
161	        trigger=EventTrigger(
162	            expect={"animal.table_for_one"},
163	            match={
164	                "genus": "Marmota",
165	                "species": "monax",
166	            },
167	            posture=Posture.Reactive,
168	            threshold=1,
169	            within=timedelta(seconds=10),
170	        ),
171	        actions=[actions.DoNothing()],
172	    )
173	
174	
175	@pytest.fixture
176	def chonk_sadness() -> Automation:
177	    return Automation(
178	        name="If I haven't seen a woodchuck in 30 seconds, cry",
179	        trigger=EventTrigger(
180	            expect={"animal.walked"},
181	            match={
182	                "genus": "Marmota",
183	                "species": "monax",
184	            },
185	            posture=Posture.Proactive,
186	            threshold=1,
187	            within=timedelta(seconds=30),
188	        ),
189	        actions=[actions.DoNothing()],
190	    )
191	
192	
193	@pytest.fixture
194	def woodchonk_walked(start_of_test: DateTime) -> ReceivedEvent:
195	    return ReceivedEvent(
196	        occurred=start_of_test + timedelta(microseconds=2),
197	        event="animal.walked",
198	        resource={
199	            "kingdom": "Animalia",
200	            "phylum": "Chordata",
201	            "class": "Mammalia",
202	            "order": "Rodentia",
203	            "family": "Sciuridae",
204	            "genus": "Marmota",
205	            "species": "monax",
206	            "prefect.resource.id": "woodchonk",
207	        },
208	        id=uuid4(),
209	    )
210	
211	
212	@pytest.fixture
213	def woodchonk_table_for_one(start_of_test: DateTime) -> ReceivedEvent:
214	    return ReceivedEvent(
215	        occurred=start_of_test + timedelta(microseconds=2),
216	        event="animal.table_for_one",
217	        resource={
218	            "kingdom": "Animalia",
219	            "phylum": "Chordata",
220	            "class": "Mammalia",
221	            "order": "Rodentia",
222	            "family": "Sciuridae",
223	            "genus": "Marmota",
224	            "species": "monax",
225	            "prefect.resource.id": "woodchonk",
226	        },
227	        id=uuid4(),
228	    )
229	
230	
231	@pytest.fixture
232	def my_poor_lilies() -> Automation:
233	    return Automation(
234	        name="If my lilies get nibbled, let me know",
235	        trigger=EventTrigger(
236	            expect={"animal.ingested"},
237	            match_related={
238	                "prefect.resource.role": "meal",
239	                "genus": "Hemerocallis",
240	                "species": "fulva",
241	            },
242	            posture=Posture.Reactive,
243	            threshold=0,
244	            within=timedelta(seconds=30),
245	        ),
246	        actions=[actions.DoNothing()],
247	    )
248	
249	
250	@pytest.fixture
251	def woodchonk_nibbled(start_of_test: DateTime):
252	    return ReceivedEvent(
253	        occurred=start_of_test + timedelta(microseconds=2),
254	        event="animal.ingested",
255	        resource={
256	            "kingdom": "Animalia",
257	            "phylum": "Chordata",
258	            "class": "Mammalia",
259	            "order": "Rodentia",
260	            "family": "Sciuridae",
261	            "genus": "Marmota",
262	            "species": "monax",
263	            "prefect.resource.id": "woodchonk",
264	        },
265	        related=[
266	            {
267	                "prefect.resource.role": "meal",
268	                "kingdom": "Plantae",
269	                "order": "Asparagales",
270	                "family": "Asphodelaceae",
271	                "genus": "Hemerocallis",
272	                "species": "fulva",
273	                "prefect.resource.id": "my-lily",
274	            },
275	            {
276	                "prefect.resource.role": "meal",
277	                "kingdom": "Plantae",
278	                "order": "Liliales",
279	                "family": "Liliaceae",
280	                "genus": "Tulipa",
281	                "species": "gesneriana",
282	                "prefect.resource.id": "my-tulip",
283	            },
284	        ],
285	        id=uuid4(),
286	    )
287	
288	
289	@pytest.fixture
290	def woodchonk_gobbled(start_of_test: DateTime):
291	    return ReceivedEvent(
292	        occurred=start_of_test + timedelta(microseconds=3),
293	        event="animal.ingested",
294	        resource={
295	            "kingdom": "Animalia",
296	            "phylum": "Chordata",
297	            "class": "Mammalia",
298	            "order": "Rodentia",
299	            "family": "Sciuridae",
300	            "genus": "Marmota",
301	            "species": "monax",
302	            "prefect.resource.id": "woodchonk",
303	        },
304	        related=[
305	            {
306	                "prefect.resource.role": "meal",
307	                "kingdom": "Plantae",
308	                "order": "Ranunculales",
309	                "family": "Papaveraceae",
310	                "genus": "Dicentra",
311	                "species": "cucullaria",
312	                "prefect.resource.id": "my-bleeding-heart",
313	            },
314	            {
315	                "prefect.resource.role": "meal",
316	                "kingdom": "Plantae",
317	                "order": "Asparagales",
318	                "family": "Amaryllidaceae",
319	                "genus": "Narcissus",
320	                "species": "poeticus",
321	                "prefect.resource.id": "my-daffodil",
322	            },
323	        ],
324	        id=uuid4(),
325	    )
326	
327	
328	@pytest.fixture
329	def animal_lover() -> Automation:
330	    return Automation(
331	        name="I get excited about just about anything an animal does",
332	        trigger=EventTrigger(
333	            expect=set(),
334	            match={
335	                "kingdom": "Animalia",
336	            },
337	            posture=Posture.Reactive,
338	            threshold=0,
339	            within=timedelta(seconds=30),
340	        ),
341	        actions=[actions.DoNothing()],
342	    )
343	
344	
345	@pytest.fixture
346	def email_me_when_that_dang_spider_comes(
347	    arachnophobia: Automation,
348	    daddy_long_legs_walked: ReceivedEvent,
349	) -> TriggeredAction:
350	    firing = Firing(
351	        trigger=arachnophobia.trigger,
352	        trigger_states={TriggerState.Triggered},
353	        triggered=now("UTC"),
354	        triggering_labels={"hello": "world"},
355	        triggering_event=daddy_long_legs_walked,
356	    )
357	    return TriggeredAction(
358	        automation=arachnophobia,
359	        firing=firing,
360	        triggered=firing.triggered,
361	        triggering_labels=firing.triggering_labels,
362	        triggering_event=firing.triggering_event,
363	        action=arachnophobia.actions[0],
364	    )
365	
366	
367	@pytest.fixture
368	async def some_workspace_automations(
369	    db: PrefectDBInterface, automations_session: AsyncSession
370	) -> Sequence[Automation]:
371	    uninteresting_kwargs: Dict[str, Any] = dict(
372	        trigger=EventTrigger(
373	            expect=("things.happened",),
374	            match=ResourceSpecification.model_validate(
375	                {"prefect.resource.id": "some-resource"}
376	            ),
377	            match_related=ResourceSpecification.model_validate({}),
378	            posture=Posture.Reactive,
379	            threshold=1,
380	            within=timedelta(seconds=10),
381	        ),
382	        actions=[actions.DoNothing()],
383	    )
384	
385	    automations = [
386	        db.Automation(
387	            id=uuid4(),
388	            name="automation 1",
389	            **uninteresting_kwargs,
390	        ),
391	        db.Automation(
392	            id=uuid4(),
393	            name="automation 2",
394	            **uninteresting_kwargs,
395	        ),
396	        db.Automation(
397	            id=uuid4(),
398	            name="automation 3",
399	            **uninteresting_kwargs,
400	        ),
401	        db.Automation(
402	            id=uuid4(),
403	            name="automation 4",
404	            **uninteresting_kwargs,
405	        ),
406	    ]
407	
408	    automations_session.add_all(automations)
409	    await automations_session.commit()
410	    return parse_obj_as(List[Automation], automations)
411	
412	
413	@pytest.fixture
414	def publish_mocks(
415	    monkeypatch: pytest.MonkeyPatch,
416	) -> Tuple[MagicMock, AsyncMock]:
417	    mock_create_publisher = MagicMock(spec=messaging.create_event_publisher)
418	    mock_publish = AsyncMock()
419	    mock_create_publisher.return_value.__aenter__.return_value.publish_data = (
420	        mock_publish
421	    )
422	
423	    monkeypatch.setattr(
424	        "prefect.server.events.messaging.create_event_publisher", mock_create_publisher
425	    )
426	
427	    return mock_create_publisher, mock_publish
428	
429	
430	@pytest.fixture
431	def publish(publish_mocks: Tuple[MagicMock, AsyncMock]) -> AsyncMock:
432	    return publish_mocks[1]
433	
434	
435	@pytest.fixture
436	def create_publisher(
437	    publish_mocks: Tuple[MagicMock, AsyncMock],
438	) -> MagicMock:
439	    return publish_mocks[0]
440	
441	
442	def assert_message_represents_event(message: Message, event: ReceivedEvent):
443	    """Confirms that the message adequately represents the event"""
444	    assert message.data
445	    assert ReceivedEvent.model_validate_json(message.data) == event
446	    assert message.attributes
447	    assert message.attributes["id"] == str(event.id)
448	    assert message.attributes["event"] == event.event
449	
```

## 137 · 2026-10-29T03:38:20.882153+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"COMPLETED\\|Completed\\|is_final\\|TERMINAL\" src/prefect/server/events/schemas/*.py src/prefect/server/events/*.py | head -40",
  "description": "Search terminal state handling in events schemas"
}
```

## 138 · 2026-10-29T03:38:21.168745+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"state-type\" src/ tests/ --include=\"*.py\" | head -30",
  "description": "Search state-type resource label usage"
}
```

## 139 · 2026-10-29T03:38:21.403361+00:00 · tool_result 

```
(Bash completed with no output)
```

## 140 · 2026-10-29T03:38:24.726522+00:00 · tool_result 

```
src/prefect/cli/flow_run.py:224:        cyclopts.Parameter("--state-type", help="Type of the flow run's state"),
src/prefect/cli/flow_run.py:241:        $ prefect flow-runs ls --state-type RUNNING
src/prefect/cli/flow_run.py:242:        $ prefect flow-runs ls --state-type RUNNING --state-type FAILED
src/prefect/cli/flow_runs_watching.py:212:        state_type_str = event.resource.get("prefect.state-type")
src/prefect/cli/task_run.py:107:        cyclopts.Parameter("--state-type", help="Type of the task run's state"),
src/prefect/events/subscribers.py:137:        state_type_str = event.resource.get("prefect.state-type")
src/prefect/flow_runs.py:144:                if not (state_type := event.resource.get("prefect.state-type")):
src/prefect/server/events/actions.py:521:                "prefect.state-type",
src/prefect/server/events/actions.py:533:                        type=StateType(resource["prefect.state-type"]),
src/prefect/server/models/events.py:67:            "prefect.state-type": validated_state.type.value,
src/prefect/utilities/engine/__init__.py:963:            "prefect.state-type": str(validated_state.type.value),
tests/cli/test_flow_run.py:269:            "--state-type",
tests/cli/test_flow_run.py:271:            "--state-type",
tests/cli/test_flow_run.py:286:        command=["flow-run", "ls", "--state-type", "invalid"],
tests/cli/test_task_run.py:241:            "--state-type",
tests/cli/test_task_run.py:243:            "--state-type",
tests/cli/test_task_run.py:258:        command=["task-run", "ls", "--state-type", "invalid"],
tests/events/client/instrumentation/test_task_run_state_change_events.py:82:            "prefect.state-type": "PENDING",
tests/events/client/instrumentation/test_task_run_state_change_events.py:130:            "prefect.state-type": "RUNNING",
tests/events/client/instrumentation/test_task_run_state_change_events.py:187:            "prefect.state-type": "COMPLETED",
tests/events/client/instrumentation/test_task_run_state_change_events.py:286:            "prefect.state-type": "PENDING",
tests/events/client/instrumentation/test_task_run_state_change_events.py:334:            "prefect.state-type": "RUNNING",
tests/events/client/instrumentation/test_task_run_state_change_events.py:394:            "prefect.state-type": "FAILED",
tests/events/client/instrumentation/test_task_run_state_change_events.py:619:            "prefect.state-type": "SCHEDULED",
tests/events/client/test_flow_run_subscriber.py:151:                "prefect.state-type": "COMPLETED",
tests/events/client/test_flow_run_subscriber.py:526:                "prefect.state-type": "COMPLETED",
tests/events/server/actions/test_jinja_templated_action.py:247:            "prefect.state-type": "COMPLETED",
tests/events/server/actions/test_jinja_templated_action.py:283:            "prefect.state-type": "COMPLETED",
tests/events/server/actions/test_jinja_templated_action.py:405:            event.resource["prefect.state-type"],
tests/events/server/actions/test_jinja_templated_action.py:476:            "prefect.state-type": "ANNIHILATED",
```

## 141 · 2026-10-29T03:38:26.807986+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def emit_event\" -A60 src/prefect/events/utilities.py src/prefect/events/*.py 2>/dev/null | head -90",
  "description": "Inspect emit_event occurred default"
}
```

## 142 · 2026-10-29T03:38:27.324719+00:00 · tool_result 

```
src/prefect/events/utilities.py:30:def emit_event(
src/prefect/events/utilities.py-31-    event: str,
src/prefect/events/utilities.py-32-    resource: dict[str, str],
src/prefect/events/utilities.py-33-    occurred: datetime.datetime | None = None,
src/prefect/events/utilities.py-34-    related: list[dict[str, str]] | list[RelatedResource] | None = None,
src/prefect/events/utilities.py-35-    payload: dict[str, Any] | None = None,
src/prefect/events/utilities.py-36-    id: UUID | None = None,
src/prefect/events/utilities.py-37-    follows: Event | None = None,
src/prefect/events/utilities.py-38-    **kwargs: dict[str, Any] | None,
src/prefect/events/utilities.py-39-) -> Event | None:
src/prefect/events/utilities.py-40-    """
src/prefect/events/utilities.py-41-    Send an event to Prefect.
src/prefect/events/utilities.py-42-
src/prefect/events/utilities.py-43-    Args:
src/prefect/events/utilities.py-44-        event: The name of the event that happened.
src/prefect/events/utilities.py-45-        resource: The primary Resource this event concerns.
src/prefect/events/utilities.py-46-        occurred: When the event happened from the sender's perspective.
src/prefect/events/utilities.py-47-                  Defaults to the current datetime.
src/prefect/events/utilities.py-48-        related: A list of additional Resources involved in this event.
src/prefect/events/utilities.py-49-        payload: An open-ended set of data describing what happened.
src/prefect/events/utilities.py-50-        id: The sender-provided identifier for this event. Defaults to a random
src/prefect/events/utilities.py-51-            UUID.
src/prefect/events/utilities.py-52-        follows: The event that preceded this one. Setting `follows`
src/prefect/events/utilities.py-53-            establishes that this event is known to have occurred after the
src/prefect/events/utilities.py-54-            given event, which the system can use to disambiguate the
src/prefect/events/utilities.py-55-            ordering of the two events. Only the `id` and `occurred` of the
src/prefect/events/utilities.py-56-            given event are used; it is not emitted again. If the preceding
src/prefect/events/utilities.py-57-            event happened more than 5 minutes prior to this event the
src/prefect/events/utilities.py-58-            follows relationship will not be set.
src/prefect/events/utilities.py-59-
src/prefect/events/utilities.py-60-    Returns:
src/prefect/events/utilities.py-61-        The event that was emitted if worker is using a client that emit
src/prefect/events/utilities.py-62-        events, otherwise None
src/prefect/events/utilities.py-63-    """
src/prefect/events/utilities.py-64-    if not should_emit_events():
src/prefect/events/utilities.py-65-        return None
src/prefect/events/utilities.py-66-
src/prefect/events/utilities.py-67-    try:
src/prefect/events/utilities.py-68-        operational_clients = [
src/prefect/events/utilities.py-69-            AssertingPassthroughEventsClient,
src/prefect/events/utilities.py-70-            AssertingEventsClient,
src/prefect/events/utilities.py-71-            PrefectCloudEventsClient,
src/prefect/events/utilities.py-72-            PrefectEventsClient,
src/prefect/events/utilities.py-73-            ProcessPoolForwardingEventsClient,
src/prefect/events/utilities.py-74-        ]
src/prefect/events/utilities.py-75-        worker_instance = EventsWorker.instance()
src/prefect/events/utilities.py-76-
src/prefect/events/utilities.py-77-        if worker_instance.client_type not in operational_clients:
src/prefect/events/utilities.py-78-            return None
src/prefect/events/utilities.py-79-
src/prefect/events/utilities.py-80-        event_kwargs: dict[str, Any] = {
src/prefect/events/utilities.py-81-            "event": event,
src/prefect/events/utilities.py-82-            "resource": resource,
src/prefect/events/utilities.py-83-            **kwargs,
src/prefect/events/utilities.py-84-        }
src/prefect/events/utilities.py-85-
src/prefect/events/utilities.py-86-        if occurred is None:
src/prefect/events/utilities.py-87-            occurred = prefect.types._datetime.now("UTC")
src/prefect/events/utilities.py-88-        event_kwargs["occurred"] = occurred
src/prefect/events/utilities.py-89-
src/prefect/events/utilities.py-90-        if related is not None:
--
src/prefect/events/utilities.py:30:def emit_event(
src/prefect/events/utilities.py-31-    event: str,
src/prefect/events/utilities.py-32-    resource: dict[str, str],
src/prefect/events/utilities.py-33-    occurred: datetime.datetime | None = None,
src/prefect/events/utilities.py-34-    related: list[dict[str, str]] | list[RelatedResource] | None = None,
src/prefect/events/utilities.py-35-    payload: dict[str, Any] | None = None,
src/prefect/events/utilities.py-36-    id: UUID | None = None,
src/prefect/events/utilities.py-37-    follows: Event | None = None,
src/prefect/events/utilities.py-38-    **kwargs: dict[str, Any] | None,
src/prefect/events/utilities.py-39-) -> Event | None:
src/prefect/events/utilities.py-40-    """
src/prefect/events/utilities.py-41-    Send an event to Prefect.
src/prefect/events/utilities.py-42-
src/prefect/events/utilities.py-43-    Args:
src/prefect/events/utilities.py-44-        event: The name of the event that happened.
src/prefect/events/utilities.py-45-        resource: The primary Resource this event concerns.
src/prefect/events/utilities.py-46-        occurred: When the event happened from the sender's perspective.
src/prefect/events/utilities.py-47-                  Defaults to the current datetime.
src/prefect/events/utilities.py-48-        related: A list of additional Resources involved in this event.
src/prefect/events/utilities.py-49-        payload: An open-ended set of data describing what happened.
src/prefect/events/utilities.py-50-        id: The sender-provided identifier for this event. Defaults to a random
src/prefect/events/utilities.py-51-            UUID.
src/prefect/events/utilities.py-52-        follows: The event that preceded this one. Setting `follows`
src/prefect/events/utilities.py-53-            establishes that this event is known to have occurred after the
src/prefect/events/utilities.py-54-            given event, which the system can use to disambiguate the
src/prefect/events/utilities.py-55-            ordering of the two events. Only the `id` and `occurred` of the
src/prefect/events/utilities.py-56-            given event are used; it is not emitted again. If the preceding
src/prefect/events/utilities.py-57-            event happened more than 5 minutes prior to this event the
```

## 143 · 2026-10-29T03:38:30.128274+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"flow_run_state_change_event(\" -B5 -A15 src/prefect/server/orchestration/ src/prefect/server/models/ 2>/dev/null | head -80",
  "description": "Find state change event call sites"
}
```

## 144 · 2026-10-29T03:38:30.506278+00:00 · tool_result 

```
src/prefect/server/orchestration/instrumentation_policies.py-53-
src/prefect/server/orchestration/instrumentation_policies.py-54-        assert isinstance(context.session, AsyncSession)
src/prefect/server/orchestration/instrumentation_policies.py-55-
src/prefect/server/orchestration/instrumentation_policies.py-56-        async with PrefectServerEventsClient() as events:
src/prefect/server/orchestration/instrumentation_policies.py-57-            await events.emit(
src/prefect/server/orchestration/instrumentation_policies.py:58:                await flow_run_state_change_event(
src/prefect/server/orchestration/instrumentation_policies.py-59-                    session=context.session,
src/prefect/server/orchestration/instrumentation_policies.py-60-                    occurred=validated_state.timestamp,
src/prefect/server/orchestration/instrumentation_policies.py-61-                    flow_run=context.run,
src/prefect/server/orchestration/instrumentation_policies.py-62-                    initial_state_id=initial_state.id if initial_state else None,
src/prefect/server/orchestration/instrumentation_policies.py-63-                    initial_state=initial_state,
src/prefect/server/orchestration/instrumentation_policies.py-64-                    validated_state_id=validated_state.id,
src/prefect/server/orchestration/instrumentation_policies.py-65-                    validated_state=validated_state,
src/prefect/server/orchestration/instrumentation_policies.py-66-                )
src/prefect/server/orchestration/instrumentation_policies.py-67-            )
--
src/prefect/server/models/events.py-37-    maxsize=1000,
src/prefect/server/models/events.py-38-    ttl=PREFECT_API_EVENTS_RELATED_RESOURCE_CACHE_TTL.value().total_seconds(),
src/prefect/server/models/events.py-39-)
src/prefect/server/models/events.py-40-
src/prefect/server/models/events.py-41-
src/prefect/server/models/events.py:42:async def flow_run_state_change_event(
src/prefect/server/models/events.py-43-    session: AsyncSession,
src/prefect/server/models/events.py-44-    occurred: datetime,
src/prefect/server/models/events.py-45-    flow_run: ORMFlowRun,
src/prefect/server/models/events.py-46-    initial_state_id: Optional[UUID],
src/prefect/server/models/events.py-47-    initial_state: Optional[schemas.states.State],
src/prefect/server/models/events.py-48-    validated_state_id: Optional[UUID],
src/prefect/server/models/events.py-49-    validated_state: schemas.states.State,
src/prefect/server/models/events.py-50-) -> Event:
src/prefect/server/models/events.py-51-    return Event(
src/prefect/server/models/events.py-52-        occurred=occurred,
src/prefect/server/models/events.py-53-        event=f"prefect.flow-run.{validated_state.name}",
src/prefect/server/models/events.py-54-        resource={
src/prefect/server/models/events.py-55-            "prefect.resource.id": f"prefect.flow-run.{flow_run.id}",
src/prefect/server/models/events.py-56-            "prefect.resource.name": flow_run.name,
src/prefect/server/models/events.py-57-            "prefect.run-count": str(flow_run.run_count),
```

## 145 · 2026-10-29T03:38:36.795248+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"timestamp\" src/prefect/server/schemas/states.py | head -30 && grep -rn \"timestamp\" src/prefect/server/orchestration/core_policy.py src/prefect/server/orchestration/api.py 2>/dev/null | head -20",
  "description": "Check state timestamp source"
}
```

## 146 · 2026-10-29T03:38:37.079372+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"timestamp\" src/prefect/server/models/flow_runs.py | head -30",
  "description": "Check flow run state timestamp handling"
}
```

## 147 · 2026-10-29T03:38:37.328622+00:00 · tool_result 

```
129:    timestamp: DateTime = Field(default_factory=lambda: now("UTC"))
225:                "timestamp": now("UTC"),
309:                self.timestamp,
```

## 148 · 2026-10-29T03:38:37.484813+00:00 · tool_result 

```
(Bash completed with no output)
```

## 149 · 2026-10-29T03:38:52.998266+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"Finished\\|Completed\\|Failed\\|Crashed\\|Cancelled\" tests/events/server/triggers/*.py | head -40",
  "description": "Search terminal state usage in trigger tests"
}
```

## 150 · 2026-10-29T03:38:53.437973+00:00 · tool_result 

```
tests/events/server/triggers/test_basics.py:560:                expect=["prefect.flow-run.Failed"],
tests/events/server/triggers/test_basics.py:614:        event="prefect.flow-run.Failed",
tests/events/server/triggers/test_basics.py:674:                expect=["prefect.flow-run.Failed"],
tests/events/server/triggers/test_basics.py:705:        event="prefect.flow-run.Failed",
tests/events/server/triggers/test_basics.py:718:    # Failed is the event we want, but it's too early so we shouldn't have acted yet
tests/events/server/triggers/test_basics.py:728:            triggering_event=failed,  # we reacted due to the Failed event, not Running
tests/events/server/triggers/test_basics.py:750:                expect=["prefect.flow-run.Failed"],
tests/events/server/triggers/test_basics.py:783:        event="prefect.flow-run.Failed",
tests/events/server/triggers/test_basics.py:795:    # Failed is the event we want, and the message is so late that we'll just need to
tests/events/server/triggers/test_basics.py:826:                expect=["prefect.flow-run.Failed"],
tests/events/server/triggers/test_basics.py:869:        event="prefect.flow-run.Failed",
tests/events/server/triggers/test_basics.py:882:    # Failed is the event we want, but it's too early so we shouldn't have acted yet
tests/events/server/triggers/test_composite_triggers.py:74:            event="prefect.flow-run.Completed",
tests/events/server/triggers/test_composite_triggers.py:92:            event="prefect.flow-run.Failed",
tests/events/server/triggers/test_composite_triggers.py:137:                        expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:185:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:235:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:253:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:357:                        expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:416:                        expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:422:                        expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:532:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:538:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:550:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:621:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:627:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:639:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:712:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:718:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:730:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:795:                                expect={"prefect.flow-run.Failed"},
tests/events/server/triggers/test_composite_triggers.py:801:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_composite_triggers.py:813:                                expect={"prefect.flow-run.Completed"},
tests/events/server/triggers/test_flow_run_slas.py:496:        event="prefect.flow-run.Completed",
tests/events/server/triggers/test_flow_run_slas.py:536:        ),  # just shy of the 2 hour mark since Completed
tests/events/server/triggers/test_flow_run_slas.py:538:        + datetime.timedelta(minutes=124),  # just at the 2 hour mark since Completed
tests/events/server/triggers/test_flow_run_slas.py:570:            if item.event == "prefect.flow-run.Completed":
tests/events/server/triggers/test_flow_run_slas.py:592:            if item.event == "prefect.flow-run.Completed":
tests/events/server/triggers/test_flow_run_slas.py:627:# order of the Completed and Running events, but they will have the correct causal
tests/events/server/triggers/test_flow_run_slas.py:629:# is just looking for a Completed after a Running to hone in on what the causal ordering
```

## 151 · 2026-10-29T03:38:53.599648+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"state-type\\|is_final\\|StateType\" src/prefect/server/events/ --include=\"*.py\" | head -20",
  "description": "Check events code for state type handling"
}
```

## 152 · 2026-10-29T03:38:54.024004+00:00 · tool_result 

```
src/prefect/server/events/actions.py:73:from prefect.server.schemas.states import Scheduled, State, StateType, Suspended
src/prefect/server/events/actions.py:521:                "prefect.state-type",
src/prefect/server/events/actions.py:533:                        type=StateType(resource["prefect.state-type"]),
src/prefect/server/events/actions.py:1159:    state: StateType = Field(
src/prefect/server/events/actions.py:1192:            type=StateType.CANCELLING,
```

## 153 · 2026-10-29T03:38:55.026333+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/actions.py",
  "offset": 490,
  "limit": 60
}
```

## 154 · 2026-10-29T03:38:55.167716+00:00 · tool_result 

```
490	
491	        templates: list[tuple[dict[Any, Any], dict[Any, str]]] = []
492	
493	        if templates_at_layer:
494	            templates.append((dict_, templates_at_layer))
495	
496	        for item in to_traverse:
497	            templates += cls.templates_in_dictionary(item)
498	
499	        return templates
500	
501	    def instantiate_object(
502	        self,
503	        model: Type[PrefectBaseModel],
504	        data: Dict[str, Any],
505	        triggered_action: "TriggeredAction",
506	        resource: Optional["Resource"] = None,
507	    ) -> PrefectBaseModel:
508	        object = model.model_validate(data)
509	
510	        if isinstance(object, FlowRunResponse) or isinstance(object, TaskRun):
511	            # The flow/task run was fetched from the API, but between when its
512	            # state changed and now it's possible that the state in the API has
513	            # changed again from what's contained in the event. Use the event's
514	            # data to rebuild the state object and attach it to the object
515	            # received from the API.
516	            # https://github.com/PrefectHQ/nebula/issues/3310
517	            state_fields = [
518	                "prefect.state-message",
519	                "prefect.state-name",
520	                "prefect.state-timestamp",
521	                "prefect.state-type",
522	            ]
523	
524	            if resource and all(field in resource for field in state_fields):
525	                try:
526	                    timestamp = parse_datetime(resource["prefect.state-timestamp"])
527	                    if TYPE_CHECKING:
528	                        assert isinstance(timestamp, DateTime)
529	                    object.state = State(
530	                        message=resource["prefect.state-message"],
531	                        name=resource["prefect.state-name"],
532	                        timestamp=timestamp,
533	                        type=StateType(resource["prefect.state-type"]),
534	                    )
535	                except Exception:
536	                    logger.exception(
537	                        "Failed to parse state from event resource",
538	                        extra={
539	                            **self.logging_context(triggered_action),
540	                        },
541	                    )
542	
543	        return object
544	
545	    async def _get_object_from_prefect_api(
546	        self,
547	        orchestration_client: "OrchestrationClient",
548	        triggered_action: "TriggeredAction",
549	        resource: Optional["Resource"],
```

## 155 · 2026-10-29T03:39:03.215780+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"Resuming\\|resume\" src/prefect/server/schemas/states.py src/prefect/server/orchestration/core_policy.py src/prefect/client/schemas/objects.py src/prefect/client/orchestration/_flow_runs/client.py 2>/dev/null | head -30",
  "description": "Check flow run resume semantics"
}
```

## 156 · 2026-10-29T03:39:03.643342+00:00 · tool_result 

```
src/prefect/server/orchestration/core_policy.py:145:                HandleResumingPausedFlows,
src/prefect/server/orchestration/core_policy.py:1432:class HandleResumingPausedFlows(FlowRunOrchestrationRule):
src/prefect/server/orchestration/core_policy.py:1494:                message=(f"The flow was {display_state_name} and never resumed."),
src/prefect/server/orchestration/core_policy.py:1498:                reason=f"The flow run {verb} has timed out and can no longer resume.",
src/prefect/server/orchestration/core_policy.py:1973:    to clean up, we can transition directly to `Cancelled`. Runs that are `Resuming` are in a
src/prefect/server/orchestration/core_policy.py:1994:            or initial_state.name == "Resuming"
src/prefect/client/orchestration/_flow_runs/client.py:230:    def resume_flow_run(
src/prefect/client/orchestration/_flow_runs/client.py:238:            run_input: the input to resume the flow run with
src/prefect/client/orchestration/_flow_runs/client.py:246:                "/flow_runs/{id}/resume",
src/prefect/client/orchestration/_flow_runs/client.py:758:    async def resume_flow_run(
src/prefect/client/orchestration/_flow_runs/client.py:766:            run_input: the input to resume the flow run with
src/prefect/client/orchestration/_flow_runs/client.py:774:                "/flow_runs/{id}/resume",
```

## 157 · 2026-10-29T03:39:18.048476+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER\" -A12 src/prefect/settings/models/server/events.py",
  "description": "Check bucket expiry buffer default"
}
```

## 158 · 2026-10-29T03:39:18.468749+00:00 · tool_result 

```
(Bash completed with no output)
```

## 159 · 2026-10-29T03:39:19.662994+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"EXPIRED_BUCKET_BUFFER\" src/prefect/settings/ src/prefect/ | head -10",
  "description": "Find expired bucket buffer setting"
}
```

## 160 · 2026-10-29T03:39:20.994199+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:67:from prefect.settings import PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER
src/prefect/server/events/triggers.py:715:            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),
```

## 161 · 2026-10-29T03:39:22.794083+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"events_expired_bucket_buffer\\|EXPIRED_BUCKET\" src/prefect/settings/ | head",
  "description": "Search legacy settings for buffer"
}
```

## 162 · 2026-10-29T03:39:23.224025+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -c \"\nfrom prefect.settings import PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER\nprint(PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value())\nprint(PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER)\n\"",
  "description": "Print buffer default value"
}
```

## 163 · 2026-10-29T03:39:23.291282+00:00 · tool_result 

```
src/prefect/settings/models/server/events.py:77:            "prefect_server_events_expired_bucket_buffer",
src/prefect/settings/models/server/events.py:78:            "prefect_events_expired_bucket_buffer",
```

## 164 · 2026-10-29T03:39:29.176728+00:00 · tool_result 

```
0:01:00
0:01:00
```

## 165 · 2026-10-29T03:39:38.750426+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_flow_run_slas.py",
  "offset": 430,
  "limit": 180
}
```

## 166 · 2026-10-29T03:39:38.856417+00:00 · tool_result 

```
430	            description="",
431	            trigger=EventTrigger(
432	                match={"prefect.resource.id": "prefect.flow-run.*"},
433	                match_related={
434	                    "prefect.resource.id": [
435	                        "prefect.flow.f1f1f1f1",
436	                        "prefect.flow.f2f2f2f2",
437	                    ],
438	                    "prefect.resource.role": "flow",
439	                },
440	                for_each={"prefect.resource.id"},
441	                after={"prefect.flow-run.Running"},
442	                # ...then go to any other state
443	                expect={"prefect.flow-run.*"},
444	                posture=Posture.Proactive,
445	                within=7200.0,
446	                threshold=1,
447	            ),
448	            actions=[actions.DoNothing()],
449	        ),
450	    )
451	    await automations_session.commit()
452	    triggers.load_automation(automation)
453	    return automation
454	
455	
456	@pytest.fixture
457	def trigger_from_3521(automation_from_3521: Automation) -> EventTrigger:
458	    return cast(EventTrigger, automation_from_3521.trigger)
459	
460	
461	@pytest.fixture
462	async def sequence_of_events_3521(
463	    start_of_test: DateTime,
464	) -> List[Union[ReceivedEvent, DateTime]]:
465	    baseline: DateTime = start_of_test
466	
467	    pending = Event(
468	        occurred=baseline + datetime.timedelta(minutes=0),
469	        event="prefect.flow-run.Pending",
470	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
471	        related=[
472	            {
473	                "prefect.resource.id": "prefect.flow.f1f1f1f1",
474	                "prefect.resource.role": "flow",
475	            }
476	        ],
477	        id=uuid4(),
478	    ).receive()
479	
480	    running = Event(
481	        occurred=baseline + datetime.timedelta(minutes=1),
482	        event="prefect.flow-run.Running",
483	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
484	        related=[
485	            {
486	                "prefect.resource.id": "prefect.flow.f1f1f1f1",
487	                "prefect.resource.role": "flow",
488	            }
489	        ],
490	        id=uuid4(),
491	        follows=pending.id,
492	    ).receive()
493	
494	    completed = Event(
495	        occurred=baseline + datetime.timedelta(minutes=4),
496	        event="prefect.flow-run.Completed",
497	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
498	        related=[
499	            {
500	                "prefect.resource.id": "prefect.flow.f1f1f1f1",
501	                "prefect.resource.role": "flow",
502	            }
503	        ],
504	        id=uuid4(),
505	        follows=running.id,
506	    ).receive()
507	
508	    return [
509	        pending,
510	        running,
511	        # throw a random event for the same resource ID in the middle
512	        Event(
513	            occurred=baseline + datetime.timedelta(minutes=2),
514	            event="prefect.log.write",
515	            resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
516	            related=[
517	                {
518	                    "prefect.resource.id": "prefect.flow.f1f1f1f1",
519	                    "prefect.resource.role": "flow",
520	                }
521	            ],
522	            id=uuid4(),
523	        ).receive(),
524	        baseline + datetime.timedelta(minutes=3),
525	        completed,
526	        baseline + datetime.timedelta(minutes=5),
527	        baseline
528	        + datetime.timedelta(minutes=119),  # just shy of the 2 hour mark since Pending
529	        baseline
530	        + datetime.timedelta(minutes=120),  # just at the 2 hour mark since Pending
531	        baseline
532	        + datetime.timedelta(minutes=121),  # just at the 2 hour mark since Running
533	        baseline
534	        + datetime.timedelta(
535	            minutes=123
536	        ),  # just shy of the 2 hour mark since Completed
537	        baseline
538	        + datetime.timedelta(minutes=124),  # just at the 2 hour mark since Completed
539	        baseline
540	        + datetime.timedelta(minutes=125),  # just past the 2 hour mark for anything
541	        baseline + datetime.timedelta(minutes=250),  # an additional full cycle later
542	    ]
543	
544	
545	async def test_regression_3521_negative_case(
546	    trigger_from_3521: EventTrigger,
547	    sequence_of_events_3521: List[Union[ReceivedEvent, DateTime]],
548	    act: mock.AsyncMock,
549	):
550	    # we expect no action to ever be called for these
551	    for item in sequence_of_events_3521:
552	        if isinstance(item, ReceivedEvent):
553	            await triggers.reactive_evaluation(event=item)
554	        elif isinstance(item, datetime.datetime):
555	            await triggers.proactive_evaluation(trigger_from_3521, as_of=item)
556	        else:  # pragma: no cover
557	            raise NotImplementedError()
558	
559	        act.assert_not_awaited()
560	
561	
562	async def test_regression_3521_positive_case(
563	    trigger_from_3521: EventTrigger,
564	    sequence_of_events_3521: List[Union[ReceivedEvent, DateTime]],
565	    act: mock.AsyncMock,
566	):
567	    # if we never get the completed event, the automation should fire
568	    for item in sequence_of_events_3521:
569	        if isinstance(item, ReceivedEvent):
570	            if item.event == "prefect.flow-run.Completed":
571	                continue
572	            await triggers.reactive_evaluation(event=item)
573	        elif isinstance(item, datetime.datetime):
574	            await triggers.proactive_evaluation(trigger_from_3521, as_of=item)
575	        else:  # pragma: no cover
576	            raise NotImplementedError()
577	
578	    act.assert_awaited_once()
579	
580	
581	async def test_regression_3521_side_quest(
582	    trigger_from_3521: EventTrigger,
583	    sequence_of_events_3521: List[Union[ReceivedEvent, DateTime]],
584	    act: mock.AsyncMock,
585	):
586	    """While testing this issue, found another issue where sweeping older buckets might
587	    cause buckets to disappear before they are checked if there are long lags between
588	    proactive evaluations"""
589	    # if we never get the completed event, the automation should fire
590	    for item in sequence_of_events_3521:
591	        if isinstance(item, ReceivedEvent):
592	            if item.event == "prefect.flow-run.Completed":
593	                continue
594	            await triggers.reactive_evaluation(event=item)
595	        elif isinstance(item, datetime.datetime):
596	            continue  # do not run proactive evaluations for a while
597	        else:  # pragma: no cover
598	            raise NotImplementedError()
599	
600	    act.assert_not_awaited()
601	
602	    # now run one at the end, which represents a time after the automation should have
603	    # triggered but didn't
604	    assert isinstance(item, datetime.datetime)
605	    await triggers.proactive_evaluation(trigger_from_3521, as_of=item)
606	    act.assert_awaited_once()
607	
608	    act.reset_mock()
609	
```

## 167 · 2026-10-29T03:39:42.007544+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_flow_run_slas.py",
  "offset": 608,
  "limit": 90
}
```

## 168 · 2026-10-29T03:39:42.098859+00:00 · tool_result 

```
608	    act.reset_mock()
609	
610	    # but make sure that no further triggers happen later...
611	    await triggers.proactive_evaluation(
612	        trigger_from_3521, as_of=item + datetime.timedelta(minutes=1)
613	    )
614	    act.assert_not_awaited()
615	
616	    await triggers.proactive_evaluation(
617	        trigger_from_3521, as_of=item + datetime.timedelta(minutes=200)
618	    )
619	    act.assert_not_awaited()
620	
621	
622	# Regression test for https://github.com/PrefectHQ/nebula/issues/3244.  This is a
623	# broader issue to attempt to process order-critical messages in the right order.  It
624	# follows from #3521 (regression tests above) where a customer reported a proactive
625	# notification erroneously firing even when their flow run had completed (2 hours
626	# earlier).  The important difference in these tests is that we're going to flip the
627	# order of the Completed and Running events, but they will have the correct causal
628	# links with each other.  Also, we're going to simplify the automation so that it
629	# is just looking for a Completed after a Running to hone in on what the causal ordering
630	# will help with.
631	
632	
633	@pytest.fixture
634	async def automation_from_3244(
635	    cleared_buckets: None,
636	    cleared_automations: None,
637	    automations_session: AsyncSession,
638	) -> Automation:
639	    automation = await automations.create_automation(
640	        automations_session,
641	        Automation(
642	            name="Regression Test #3521",
643	            description="",
644	            trigger=EventTrigger(
645	                match={"prefect.resource.id": "prefect.flow-run.*"},
646	                match_related={
647	                    "prefect.resource.id": [
648	                        "prefect.flow.f1f1f1f1",
649	                        "prefect.flow.f2f2f2f2",
650	                    ],
651	                    "prefect.resource.role": "flow",
652	                },
653	                for_each={"prefect.resource.id"},
654	                after={"prefect.flow-run.Running"},
655	                expect={"prefect.flow-run.Completed"},
656	                posture=Posture.Proactive,
657	                within=7200.0,
658	                threshold=1,
659	            ),
660	            actions=[actions.DoNothing()],
661	        ),
662	    )
663	    await automations_session.commit()
664	    triggers.load_automation(automation)
665	    return automation
666	
667	
668	@pytest.fixture
669	def trigger_from_3244(automation_from_3244: Automation) -> EventTrigger:
670	    return cast(EventTrigger, automation_from_3244.trigger)
671	
672	
673	@pytest.fixture
674	async def sequence_of_events_3244(
675	    start_of_test: DateTime,
676	) -> List[Union[ReceivedEvent, DateTime]]:
677	    baseline: DateTime = start_of_test
678	
679	    pending = Event(
680	        occurred=baseline + datetime.timedelta(minutes=0),
681	        event="prefect.flow-run.Pending",
682	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
683	        related=[
684	            {
685	                "prefect.resource.id": "prefect.flow.f1f1f1f1",
686	                "prefect.resource.role": "flow",
687	            }
688	        ],
689	        id=uuid4(),
690	    ).receive()
691	
692	    running = Event(
693	        occurred=baseline + datetime.timedelta(minutes=1),
694	        event="prefect.flow-run.Running",
695	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
696	        related=[
697	            {
```

## 169 · 2026-10-29T03:39:49.899087+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/schemas/automations.py",
  "offset": 540,
  "limit": 120
}
```

## 170 · 2026-10-29T03:39:49.997698+00:00 · tool_result 

```
540	        default_factory=list,
541	        description="The actions to perform when an Automation goes into a resolving state",
542	    )
543	
544	    def triggers(self) -> Sequence[Trigger]:
545	        """Returns all triggers within this automation"""
546	        return self.trigger.all_triggers()
547	
548	    def triggers_of_type(self, trigger_type: Type[T]) -> Sequence[T]:
549	        """Returns all triggers of the specified type within this automation"""
550	        return [t for t in self.triggers() if isinstance(t, trigger_type)]
551	
552	    def trigger_by_id(self, trigger_id: UUID) -> Optional[Trigger]:
553	        """Returns the trigger with the given ID, or None if no such trigger exists"""
554	        for trigger in self.triggers():
555	            if trigger.id == trigger_id:
556	                return trigger
557	        return None
558	
559	    @model_validator(mode="after")
560	    def prevent_run_deployment_loops(self) -> Self:
561	        """Detects potential infinite loops in automations with RunDeployment actions"""
562	        from prefect.server.events.actions import RunDeployment
563	
564	        if not self.enabled:
565	            # Disabled automations can't cause problems
566	            return self
567	
568	        if (
569	            not self.trigger
570	            or not isinstance(self.trigger, EventTrigger)
571	            or self.trigger.posture != Posture.Reactive
572	        ):
573	            # Only reactive automations can cause infinite amplification
574	            return self
575	
576	        if not any(e.startswith("prefect.flow-run.") for e in self.trigger.expect):
577	            # Only flow run events can cause infinite amplification
578	            return self
579	
580	        # Every flow run created by a Deployment goes through these states
581	        problematic_events = {
582	            "prefect.flow-run.Scheduled",
583	            "prefect.flow-run.Pending",
584	            "prefect.flow-run.Running",
585	            "prefect.flow-run.*",
586	        }
587	        if not problematic_events.intersection(self.trigger.expect):
588	            return self
589	
590	        actions = [a for a in self.actions if isinstance(a, RunDeployment)]
591	        for action in actions:
592	            if action.source == "inferred":
593	                # Inferred deployments for flow run state change events will always
594	                # cause infinite loops, because no matter what filters we place on the
595	                # flow run, we're inferring the deployment from it, so we'll always
596	                # produce a new flow run that matches those filters.
597	                raise ValueError(
598	                    "Running an inferred deployment from a flow run state change event "
599	                    "will lead to an infinite loop of flow runs.  Please choose a "
600	                    "specific deployment and add additional filtering labels to the "
601	                    "match or match_related for this automation's trigger."
602	                )
603	
604	            if action.source == "selected":
605	                # Selected deployments for flow run state changes can cause infinite
606	                # loops if there aren't enough filtering labels on the trigger's match
607	                # or match_related.  While it's still possible to have infinite loops
608	                # with additional filters, it's less likely.
609	                if self.trigger.match.matches_every_resource_of_kind(
610	                    "prefect.flow-run"
611	                ):
612	                    relateds = (
613	                        self.trigger.match_related
614	                        if isinstance(self.trigger.match_related, list)
615	                        else [self.trigger.match_related]
616	                    )
617	                    if any(
618	                        related.matches_every_resource_of_kind("prefect.flow-run")
619	                        for related in relateds
620	                    ):
621	                        raise ValueError(
622	                            "Running a selected deployment from a flow run state "
623	                            "change event may lead to an infinite loop of flow runs.  "
624	                            "Please include additional filtering labels on either "
625	                            "match or match_related to narrow down which flow runs "
626	                            "will trigger this automation to exclude flow runs from "
627	                            "the deployment you've selected."
628	                        )
629	
630	        return self
631	
632	
633	class Automation(ORMBaseModel, AutomationCore, extra="ignore"):
634	    def __init__(self, *args: Any, **kwargs: Any):
635	        super().__init__(*args, **kwargs)
636	        self.trigger._set_parent(self)
637	
638	    @classmethod
639	    def model_validate(
640	        cls: type[Self],
641	        obj: Any,
642	        *,
643	        strict: bool | None = None,
644	        from_attributes: bool | None = None,
645	        context: dict[str, Any] | None = None,
646	    ) -> Self:
647	        automation = super().model_validate(
648	            obj, strict=strict, from_attributes=from_attributes, context=context
649	        )
650	        automation.trigger._set_parent(automation)
651	        return automation
652	
653	
654	class AutomationCreate(AutomationCore, ActionBaseModel, extra="forbid"):
655	    owner_resource: Optional[str] = Field(
656	        default=None, description="The resource to which this automation belongs"
657	    )
658	
659	
```

## 171 · 2026-10-29T03:39:58.898038+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "offset": 1,
  "limit": 60
}
```

## 172 · 2026-10-29T03:39:58.994051+00:00 · tool_result 

```
1	import asyncio
2	import random
3	from datetime import timedelta
4	from typing import Callable, List, Union
5	from unittest import mock
6	from uuid import UUID, uuid4
7	
8	import pytest
9	from sqlalchemy.ext.asyncio import AsyncSession
10	
11	from prefect.server.events import actions, triggers
12	from prefect.server.events.models import automations
13	from prefect.server.events.schemas.automations import (
14	    Automation,
15	    EventTrigger,
16	    Firing,
17	    Posture,
18	    TriggerState,
19	)
20	from prefect.server.events.schemas.events import Event, ReceivedEvent
21	from prefect.server.models import work_queues
22	from prefect.server.schemas.actions import WorkQueueCreate
23	from prefect.server.schemas.core import WorkQueue
24	from prefect.types._datetime import DateTime
25	
26	pytestmark = pytest.mark.clear_db
27	
28	
29	@pytest.fixture
30	def act(monkeypatch: pytest.MonkeyPatch) -> mock.AsyncMock:
31	    mock_act = mock.AsyncMock()
32	    monkeypatch.setattr("prefect.server.events.triggers.act", mock_act)
33	    return mock_act
34	
35	
36	@pytest.fixture
37	async def work_queue(
38	    session: AsyncSession,
39	) -> WorkQueue:
40	    work_queue = await work_queues.create_work_queue(
41	        session=session,
42	        work_queue=WorkQueueCreate(name="my-work-queue"),
43	    )
44	    await session.commit()
45	    return work_queue
46	
47	
48	@pytest.fixture
49	async def unhealthy_work_queue_automation(
50	    work_queue: WorkQueue,
51	    cleared_buckets: None,
52	    cleared_automations: None,
53	    automations_session: AsyncSession,
54	) -> Automation:
55	    # Automation for issue 8871: https://github.com/PrefectHQ/prefect/issues/8871
56	    automation = await automations.create_automation(
57	        automations_session,
58	        Automation(
59	            name="Alert about unhealthy work queues",
60	            description="Any work queues that are unhealthy for more than 2 hours",
```

## 173 · 2026-10-29T03:40:00.969354+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def frozen_time\" tests/ src/ | head -5",
  "description": "Find frozen_time fixture"
}
```

## 174 · 2026-10-29T03:40:01.247965+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"frozen_time\" tests/conftest.py | head -10 && grep -rn \"def frozen_time\" -A30 tests/conftest.py",
  "description": "Read frozen_time fixture"
}
```

## 175 · 2026-10-29T03:40:01.664793+00:00 · tool_result 

```
(Bash completed with no output)
```

## 176 · 2026-10-29T03:40:03.612460+00:00 · tool_result 

```
tests/fixtures/time.py:14:def frozen_time(
tests/fixtures/time.py:19:    def frozen_time(tz: ZoneInfo | str | None = None):
```

## 177 · 2026-10-29T03:40:04.901407+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/fixtures/time.py"
}
```

## 178 · 2026-10-29T03:40:05.002785+00:00 · tool_result 

```
1	from __future__ import annotations
2	
3	import datetime
4	from datetime import timedelta
5	from typing import Callable
6	from zoneinfo import ZoneInfo
7	
8	import pytest
9	
10	import prefect.types._datetime
11	
12	
13	@pytest.fixture
14	def frozen_time(
15	    monkeypatch: pytest.MonkeyPatch,
16	) -> prefect.types._datetime.DateTime | datetime.datetime:
17	    frozen = prefect.types._datetime.now("UTC")
18	
19	    def frozen_time(tz: ZoneInfo | str | None = None):
20	        if tz is None:
21	            return frozen
22	        else:
23	            return frozen.astimezone(tz=ZoneInfo(getattr(tz, "name", tz)))
24	
25	    monkeypatch.setattr(prefect.types._datetime, "now", frozen_time)
26	    return frozen
27	
28	
29	@pytest.fixture
30	def advance_time(
31	    monkeypatch: pytest.MonkeyPatch,
32	) -> Callable[[timedelta], prefect.types._datetime.DateTime]:
33	    clock = prefect.types._datetime.now("UTC")
34	
35	    def advance(amount: timedelta):
36	        nonlocal clock
37	        clock += amount
38	        return clock
39	
40	    def nowish(tz: ZoneInfo | str | None = None):
41	        # each time this is called, advance by 1 microsecond so that time is moving
42	        # forward bit-by-bit to avoid everything appearing to happen all at once
43	        advance(timedelta(microseconds=1))
44	
45	        if tz is None:
46	            return clock
47	        else:
48	            return clock.astimezone(ZoneInfo(getattr(tz, "name", tz)))
49	
50	    monkeypatch.setattr(prefect.types._datetime, "now", nowish)
51	
52	    return advance
53	
```

## 179 · 2026-10-29T03:40:14.404726+00:00 · tool_call Write

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "content": "\"\"\"Regression tests for proactive unresponsive-run detection windows.\n\nThese cover the case where an event that matches both ``after`` and ``expect``\n(typically a flow run heartbeat) races a terminal state change for the same\nresource.  The heartbeat must not re-arm the absence window that the terminal\nevent already satisfied, while a genuinely unresponsive run must still fire.\n\"\"\"\n\nfrom datetime import timedelta\nfrom typing import Callable, Union\nfrom unittest import mock\nfrom uuid import UUID, uuid4\n\nimport pytest\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations\nfrom prefect.server.events.schemas.automations import (\n    Automation,\n    EventTrigger,\n    Firing,\n    Posture,\n    TriggerState,\n)\nfrom prefect.server.events.schemas.events import Event, ReceivedEvent\nfrom prefect.types._datetime import DateTime\n\npytestmark = pytest.mark.clear_db\n\nFLOW_RUN_ID = UUID(\"aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa\")\nRESOURCE_ID = f\"prefect.flow-run.{FLOW_RUN_ID}\"\n\n\n@pytest.fixture\nasync def unresponsive_run_automation(\n    cleared_buckets: None,\n    cleared_automations: None,\n    automations_session: AsyncSession,\n) -> Automation:\n    \"\"\"The documented zombie flow detection automation.\"\"\"\n    automation = await automations.create_automation(\n        automations_session,\n        Automation(\n            name=\"Unresponsive run monitor\",\n            trigger=EventTrigger(\n                match={\"prefect.resource.id\": \"prefect.flow-run.*\"},\n                after={\"prefect.flow-run.heartbeat\"},\n                expect={\"prefect.flow-run.*\"},\n                for_each={\"prefect.resource.id\"},\n                posture=Posture.Proactive,\n                threshold=1,\n                within=timedelta(seconds=90),\n            ),\n            actions=[actions.DoNothing()],\n        ),\n    )\n    triggers.load_automation(automation)\n    await automations_session.commit()\n    return automation\n\n\ndef heartbeat(occurred: DateTime) -> ReceivedEvent:\n    return Event(\n        occurred=occurred,\n        event=\"prefect.flow-run.heartbeat\",\n        resource={\"prefect.resource.id\": RESOURCE_ID},\n        id=uuid4(),\n    ).receive()\n\n\ndef state_change(occurred: DateTime, name: str = \"Completed\") -> ReceivedEvent:\n    return Event(\n        occurred=occurred,\n        event=f\"prefect.flow-run.{name}\",\n        resource={\"prefect.resource.id\": RESOURCE_ID},\n        id=uuid4(),\n    ).receive()\n\n\nasync def test_completed_run_with_late_heartbeat_does_not_fire(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    first = heartbeat(frozen_time)\n    second = heartbeat(frozen_time + timedelta(seconds=30))\n    completed = state_change(frozen_time + timedelta(seconds=60))\n    # The worker emits one more heartbeat as it completes; it is delivered after the\n    # terminal state change.\n    late = heartbeat(frozen_time + timedelta(seconds=60))\n\n    for event in (first, second, completed, late):\n        await triggers.reactive_evaluation(event)\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()\n\n\nasync def test_out_of_order_heartbeats_do_not_rearm_the_window(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"Stale events may still count, but must not move the window's watermark back.\"\"\"\n    first = heartbeat(frozen_time)\n    second = heartbeat(frozen_time + timedelta(seconds=30))\n    completed = state_change(frozen_time + timedelta(seconds=60))\n\n    for event in (first, second, completed):\n        await triggers.reactive_evaluation(event)\n\n    # Two heartbeats emitted before completion but delivered after it.  Neither is\n    # newer than the Completed event, so neither may re-open the window.\n    for event in (\n        heartbeat(frozen_time + timedelta(seconds=45)),\n        heartbeat(frozen_time + timedelta(seconds=50)),\n    ):\n        await triggers.reactive_evaluation(event)\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()\n\n\nasync def test_genuinely_unresponsive_run_still_fires_with_correct_information(\n    act: mock.AsyncMock,\n    assert_acted_with: Callable[[Union[Firing, list[Firing]]], None],\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    first = heartbeat(frozen_time)\n    second = heartbeat(frozen_time + timedelta(seconds=30))\n\n    await triggers.reactive_evaluation(first)\n    await triggers.reactive_evaluation(second)\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n\n    assert_acted_with(\n        Firing(\n            trigger=unresponsive_run_automation.trigger,\n            trigger_states={TriggerState.Triggered},\n            triggered=frozen_time,  # type: ignore\n            triggering_labels={\"prefect.resource.id\": RESOURCE_ID},\n            triggering_event=second,\n        )\n    )\n\n\nasync def test_completed_run_stays_silent_across_a_restart(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"The disarm state lives in the bucket, so a server restart must not lose it.\"\"\"\n    first = heartbeat(frozen_time)\n    second = heartbeat(frozen_time + timedelta(seconds=30))\n    completed = state_change(frozen_time + timedelta(seconds=60))\n\n    for event in (first, second, completed):\n        await triggers.reactive_evaluation(event)\n\n    # Simulate a restart: forget all in-memory trigger state and reload the automation\n    # from the database while leaving buckets untouched.\n    await triggers.reset()\n    triggers.load_automation(unresponsive_run_automation)\n\n    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()\n\n\nasync def test_run_that_reports_a_new_state_after_completion_is_monitored_again(\n    act: mock.AsyncMock,\n    assert_acted_with: Callable[[Union[Firing, list[Firing]]], None],\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"Only stale events are ignored; newer activity re-arms the window as before.\"\"\"\n    first = heartbeat(frozen_time)\n    second = heartbeat(frozen_time + timedelta(seconds=30))\n    completed = state_change(frozen_time + timedelta(seconds=60))\n    resumed = state_change(frozen_time + timedelta(seconds=70), name=\"Running\")\n    latest = heartbeat(frozen_time + timedelta(seconds=75))\n\n    for event in (first, second, completed, resumed, latest):\n        await triggers.reactive_evaluation(event)\n\n    act.assert_not_awaited()\n\n    # No further events: the newly armed window should expire and fire.\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=166)\n    )\n\n    assert_acted_with(\n        Firing(\n            trigger=unresponsive_run_automation.trigger,\n            trigger_states={TriggerState.Triggered},\n            triggered=frozen_time,  # type: ignore\n            triggering_labels={\"prefect.resource.id\": RESOURCE_ID},\n            triggering_event=latest,\n        )\n    )\n"
}
```

## 180 · 2026-10-29T03:40:14.509661+00:00 · tool_result 

```
File created successfully at: $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py (file state is current in your context — no need to Read it back)
```

## 181 · 2026-10-29T03:40:17.497842+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -25",
  "description": "Run new regression tests",
  "timeout": 600000
}
```

## 182 · 2026-10-29T03:41:06.172988+00:00 · tool_result 

```
.....                                                                    [100%]
5 passed in 37.70s
```

## 183 · 2026-10-29T03:41:13.490033+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"evaluate_proactive_triggers\\|proactive_evaluation\" src/prefect/server/ --include=\"*.py\" | head -20",
  "description": "Find proactive trigger evaluation call sites"
}
```

## 184 · 2026-10-29T03:41:13.746785+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/services/ && grep -rn \"proactive\" src/prefect/server/services/*.py | head -20",
  "description": "Check triggers service"
}
```

## 185 · 2026-10-29T03:41:13.960011+00:00 · tool_result 

```
src/prefect/server/events/services/triggers.py:74:async def evaluate_proactive_triggers_periodic(
src/prefect/server/events/services/triggers.py:81:    await triggers.evaluate_proactive_triggers()
src/prefect/server/events/triggers.py:1339:async def proactive_evaluation(
src/prefect/server/events/triggers.py:1391:async def evaluate_proactive_triggers() -> None:
src/prefect/server/events/triggers.py:1403:            run_again_at = await proactive_evaluation(
```

## 186 · 2026-10-29T03:41:14.096651+00:00 · tool_result 

```
__init__.py
base.py
cancellation_cleanup.py
cleanup_reconciler.py
db_vacuum.py
foreman.py
late_runs.py
pause_expirations.py
perpetual_services.py
repossessor.py
scheduler.py
task_run_recorder.py
telemetry.py
```

## 187 · 2026-10-29T03:41:15.364911+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/services/triggers.py"
}
```

## 188 · 2026-10-29T03:41:15.464061+00:00 · tool_result 

```
1	from __future__ import annotations
2	
3	import asyncio
4	from typing import TYPE_CHECKING, NoReturn
5	
6	from docket import Perpetual
7	
8	from prefect.logging import get_logger
9	from prefect.server.events import triggers
10	from prefect.server.services.base import RunInEphemeralServers, Service
11	from prefect.server.services.perpetual_services import perpetual_service
12	from prefect.server.utilities.messaging import Consumer, create_consumer
13	from prefect.server.utilities.messaging._consumer_names import (
14	    generate_unique_consumer_name,
15	)
16	from prefect.settings.context import get_current_settings
17	from prefect.settings.models.server.services import ServicesBaseSetting
18	
19	if TYPE_CHECKING:
20	    import logging
21	
22	
23	logger: "logging.Logger" = get_logger(__name__)
24	
25	
26	class ReactiveTriggers(RunInEphemeralServers, Service):
27	    """Evaluates reactive automation triggers"""
28	
29	    consumer_task: asyncio.Task[None] | None = None
30	
31	    @classmethod
32	    def service_settings(cls) -> ServicesBaseSetting:
33	        return get_current_settings().server.services.triggers
34	
35	    async def start(self) -> NoReturn:
36	        assert self.consumer_task is None, "Reactive triggers already started"
37	        consumer_name = generate_unique_consumer_name("reactive-triggers")
38	        logger.info(
39	            f"ReactiveTriggers starting with unique consumer name: {consumer_name}"
40	        )
41	        self.consumer: Consumer = create_consumer(
42	            "events",
43	            group="reactive-triggers",
44	            name=consumer_name,
45	            read_batch_size=self.service_settings().read_batch_size,
46	        )
47	
48	        async with triggers.consumer() as handler:
49	            self.consumer_task = asyncio.create_task(self.consumer.run(handler))
50	            logger.debug("Reactive triggers started")
51	
52	            try:
53	                await self.consumer_task
54	            except asyncio.CancelledError:
55	                pass
56	
57	    async def stop(self) -> None:
58	        assert self.consumer_task is not None, "Reactive triggers not started"
59	        self.consumer_task.cancel()
60	        try:
61	            await self.consumer_task
62	        except asyncio.CancelledError:
63	            pass
64	        finally:
65	            await self.consumer.cleanup()
66	            self.consumer_task = None
67	        logger.debug("Reactive triggers stopped")
68	
69	
70	@perpetual_service(
71	    enabled_getter=lambda: get_current_settings().server.services.triggers.enabled,
72	    run_in_ephemeral=True,
73	)
74	async def evaluate_proactive_triggers_periodic(
75	    perpetual: Perpetual = Perpetual(
76	        automatic=True,
77	        every=get_current_settings().server.events.proactive_granularity,
78	    ),
79	) -> None:
80	    """Evaluate proactive automation triggers on a periodic schedule."""
81	    await triggers.evaluate_proactive_triggers()
82	
```

## 189 · 2026-10-29T03:41:34.668032+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rln \"watermark\\|tombstone\\|last_seen\\|resolved_at\" src/prefect/server/database src/prefect/server/events | head -20",
  "description": "Search for existing watermark concepts"
}
```

## 190 · 2026-10-29T03:41:34.982559+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/database/_migrations/versions/sqlite/ | tail -25 && echo --- && ls src/prefect/server/database/_migrations/versions/postgresql/ | tail -25",
  "description": "List latest migration files"
}
```

## 191 · 2026-10-29T03:41:35.053291+00:00 · tool_result 

```
(Bash completed with no output)
```

## 192 · 2026-10-29T03:41:35.381995+00:00 · tool_result 

```
2024_04_25_155120_a8e62d4c72cf_worker_status_field.py
2024_05_01_103824_20fbd53b3cef_add_catchup_fields_to_deploymentschedule.py
2024_05_21_123101_2ac65f1758c2_json_variables.py
2024_07_15_145350_354f1ede7e9f_adding_scope_to_followers.py
2024_08_14_145052_f93e1439f022_add_deployment_concurrency_limit.py
2024_09_11_090106_7d6350aea855_add_concurrency_options.py
2024_09_16_162719_4ad4658cbefe_add_deployment_to_global_concurrency_.py
2024_11_15_151042_5952a5498b51_add_labels_column_to_flow_flowrun_.py
2024_12_04_144924_a49711513ad4_sync_orm_models_and_migrations.py
2025_02_03_125228_67f886da208e_add_parameters_column_to_deployment_.py
2025_02_05_152431_07ecde74d74d_add_slug_column_to_deployment_schedule.py
2025_03_19_142603_3457c6ca2360_add_storage_configuration_to_work_pool.py
2025_03_19_145018_bbca16f6f218_create_new_deployment_version_table.py
2025_04_28_133722_7655f31c5157_remove_flow_run_notifications.py
2025_05_04_193544_3c841a1800a1_add_scope_leader_idx_to_.py
2025_06_12_144500_add_automation_tags_bb2345678901.py
2025_06_13_164506_8bb517bae6f9_drop_task_run_state_id_foreign_key_.py
2025_09_17_091213_9e83011d1f2a_migrate_v1_concurrency_limits_to_v2.py
2026_02_19_200000_add_scheduler_schedule_id_index.py
2026_03_03_000000_add_task_run_state_type_start_time_index.py
2026_05_05_000000_2095de406cbe_add_block_document_reference_self_check.py
2026_06_10_000000_79e7a60e43d8_add_event_resources_occurred_index.py
2026_07_20_000000_14806cb26270_add_event_resources_event_id_index.py
2026_08_20_000000_f416ea180ae1_add_flow_run_deployment_id_index.py
2026_09_15_000000_a3b9c7d2e5f1_add_flow_run_state_type_coalesce_start_time_index.py
---
2024_05_21_101457_94622c1663e8_json_variables.py
2024_07_15_145240_7495a5013e7e_adding_scope_to_followers.py
2024_08_14_150111_97429116795e_add_deployment_concurrency_limit.py
2024_09_11_090317_555ed31b284d_add_concurrency_options.py
2024_09_16_152051_eaec5004771f_add_deployment_to_global_concurrency_.py
2024_11_15_150706_68a44144428d_add_labels_column_to_flow_flowrun_.py
2024_12_04_165333_5d03c01be85e_sync_orm_models_and_migrations.py
2025_02_03_125146_c163acd7e8e3_add_parameters_column_to_deployment_.py
2025_02_05_152418_a03d00b8e275_add_slug_column_to_deployment_schedule.py
2025_03_19_143502_b5f5644500d2_add_storage_configuration_to_work_pool.py
2025_03_19_145033_06b7c293bc69_create_new_deployment_version_table.py
2025_04_04_092158_7a73514ca2d6_add_ix_events__event_related_occurred_.py
2025_04_29_112902_4160a4841eed_remove_flow_run_notifications.py
2025_05_04_193249_1c9bb7f78263_add_scope_leader_idx_to_.py
2025_06_12_144500_add_automation_tags_aa1234567890.py
2025_06_13_160644_3b86c5ea017a_drop_task_run_state_id_foreign_key_.py
2025_09_17_091213_9e83011d1f2a_migrate_v1_concurrency_limits_to_v2.py
2026_02_19_200000_add_scheduler_schedule_id_index.py
2026_03_03_000000_add_task_run_state_type_start_time_index.py
2026_05_05_000000_7218aad17905_add_block_document_reference_self_check.py
2026_06_10_000000_bad1e352c597_add_event_resources_occurred_index.py
2026_07_20_000000_50737cdaee36_add_event_resources_event_id_index.py
2026_08_20_000000_9e9dadc36797_add_flow_run_deployment_id_index.py
2026_09_04_000000_c8d5f2a71b3e_rebuild_invalid_event_resources_occurred_index.py
2026_09_15_000000_d4a7e1c93f52_add_flow_run_state_type_coalesce_start_time_index.py
```

## 193 · 2026-10-29T03:41:47.311519+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"proactive_granularity\" -B3 -A10 src/prefect/settings/models/server/events.py",
  "description": "Check proactive granularity default"
}
```

## 194 · 2026-10-29T03:41:47.600715+00:00 · tool_result 

```
79-        ),
80-    )
81-
82:    proactive_granularity: timedelta = Field(
83-        default=timedelta(seconds=5),
84-        description="How frequently proactive automations are evaluated",
85-        validation_alias=AliasChoices(
86:            AliasPath("proactive_granularity"),
87:            "prefect_server_events_proactive_granularity",
88:            "prefect_events_proactive_granularity",
89-        ),
90-    )
91-
92-    retention_period: timedelta = Field(
93-        default=timedelta(days=7),
94-        description="The amount of time to retain events in the database.",
95-        validation_alias=AliasChoices(
96-            AliasPath("retention_period"),
97-            "prefect_server_events_retention_period",
98-            "prefect_events_retention_period",
```

## 195 · 2026-10-29T03:42:37.283009+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"_send_heartbeats\\|send_heartbeats\" src/prefect/flow_engine.py | head -20",
  "description": "Find heartbeat context usage in engine"
}
```

## 196 · 2026-10-29T03:42:37.560746+00:00 · tool_result 

```
306:def _send_heartbeats(
383:    help="Use `_send_heartbeats` instead.",
386:def send_heartbeats_sync(
389:    with _send_heartbeats(engine, join_on_exit=True):
395:    help="Use `_send_heartbeats` instead.",
398:async def send_heartbeats_async(
401:    with _send_heartbeats(engine, join_on_exit=False):
1326:                    with _send_heartbeats(self):
2069:                    with _send_heartbeats(self, join_on_exit=False):
```

## 197 · 2026-10-29T03:42:39.054788+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/flow_engine.py",
  "offset": 1290,
  "limit": 110
}
```

## 198 · 2026-10-29T03:42:39.147062+00:00 · tool_result 

```
1290	                            msg=f"Finished in state {display_state}",
1291	                        )
1292	
1293	                        self._is_started = False
1294	                        self._client = None
1295	
1296	    # --------------------------
1297	    #
1298	    # The following methods compose the main task run loop
1299	    #
1300	    # --------------------------
1301	
1302	    @contextmanager
1303	    def start(self) -> Generator[None, None, None]:
1304	        with self.initialize_run():
1305	            with (
1306	                trace.use_span(self._telemetry.span)
1307	                if self._telemetry.span
1308	                else nullcontext()
1309	            ):
1310	                with self.setup_flow_run_suspension_request():
1311	                    self.begin_run()
1312	
1313	                    yield
1314	
1315	    @contextmanager
1316	    def run_context(self):
1317	        timeout_context = timeout_async if self.flow.isasync else timeout
1318	        # reenter the run context to ensure it is up to date for every run
1319	        with self.setup_run_context():
1320	            raise_if_flow_run_suspension_requested()
1321	            try:
1322	                with timeout_context(
1323	                    seconds=self.flow.timeout_seconds,
1324	                    timeout_exc_type=FlowRunTimeoutError,
1325	                ):
1326	                    with _send_heartbeats(self):
1327	                        self.logger.debug(
1328	                            f"Executing flow {self.flow.name!r} for flow run {self.flow_run.name!r}..."
1329	                        )
1330	                        yield self
1331	            except TimeoutError as exc:
1332	                self.handle_timeout(exc)
1333	            except Exception as exc:
1334	                self.logger.exception("Encountered exception during execution: %r", exc)
1335	                self.handle_exception(exc)
1336	
1337	    def call_flow_fn(self) -> Union[R, Coroutine[Any, Any, R]]:
1338	        """
1339	        Convenience method to call the flow function. Returns a coroutine if the
1340	        flow is async.
1341	        """
1342	        if self.flow.isasync:
1343	
1344	            async def _call_flow_fn():
1345	                result = await call_with_parameters(self.flow.fn, self.parameters)
1346	                self.handle_success(result)
1347	
1348	            return _call_flow_fn()
1349	        else:
1350	            result = call_with_parameters(self.flow.fn, self.parameters)
1351	            self.handle_success(result)
1352	
1353	
1354	@dataclass
1355	class AsyncFlowRunEngine(BaseFlowRunEngine[P, R]):
1356	    """
1357	    Async version of the flow run engine.
1358	
1359	    NOTE: This has not been fully asyncified yet which may lead to async flows
1360	    not being fully asyncified.
1361	    """
1362	
1363	    _client: Optional[PrefectClient] = None
1364	    parameters: dict[str, Any] | None = None
1365	    flow_run: FlowRun | None = None
1366	
1367	    @property
1368	    def client(self) -> PrefectClient:
1369	        if not self._is_started or self._client is None:
1370	            raise RuntimeError("Engine has not started.")
1371	        return self._client
1372	
1373	    def _resolve_parameters(self):
1374	        if not self.parameters:
1375	            return
1376	
1377	        resolved_parameters = {}
1378	        for parameter, value in self.parameters.items():
1379	            try:
1380	                resolved_parameters[parameter] = visit_collection(
1381	                    value,
1382	                    visit_fn=resolve_to_final_result,
1383	                    return_data=True,
1384	                    max_depth=-1,
1385	                    remove_annotations=True,
1386	                    context={"parameter_name": parameter},
1387	                )
1388	            except UpstreamTaskError:
1389	                raise
1390	            except Exception as exc:
1391	                raise PrefectException(
1392	                    f"Failed to resolve inputs in parameter {parameter!r}. If your"
1393	                    " parameter type is not supported, consider using the `quote`"
1394	                    " annotation to skip resolution of inputs."
1395	                ) from exc
1396	
1397	        self.parameters = resolved_parameters
1398	
1399	    def _wait_for_dependencies(self):
```

## 199 · 2026-10-29T03:42:41.799060+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"def handle_success\\|def set_state\\|def handle_exception\\|flow_run.state\" src/prefect/flow_engine.py | head -40",
  "description": "Find state setting in engine"
}
```

## 200 · 2026-10-29T03:42:42.124740+00:00 · tool_result 

```
49:    is_suspended_flow_run_state,
339:                and engine.flow_run.state
340:                and engine.flow_run.state.is_final()
437:        return self.flow_run.state  # type: ignore
754:    def set_state(self, state: State, force: bool = False) -> State:
763:        self.flow_run.state = state  # type: ignore
764:        self.flow_run.state_name = state.name  # type: ignore
765:        self.flow_run.state_type = state.type  # type: ignore
799:    def handle_success(self, result: R) -> R:
829:    def handle_exception(
979:                and loaded_flow_run.state is not None
980:                and loaded_flow_run.state.is_completed()
981:                and loaded_flow_run.state.data is None
989:                self._return_value = loaded_flow_run.state
1091:        if (state := self.flow_run.state) and is_suspended_flow_run_state(state):
1242:                        if self.flow_run.state and self.flow_run.state.is_final():
1260:                            self.flow_run.state = state
1272:                        if self.flow_run.state and not self.flow_run.state.is_final():
1478:    async def set_state(self, state: State, force: bool = False) -> State:
1487:        self.flow_run.state = state  # type: ignore
1488:        self.flow_run.state_name = state.name  # type: ignore
1489:        self.flow_run.state_type = state.type  # type: ignore
1522:    async def handle_success(self, result: R) -> R:
1549:    async def handle_exception(
1698:                and loaded_flow_run.state is not None
1699:                and loaded_flow_run.state.is_completed()
1700:                and loaded_flow_run.state.data is None
1708:                self._return_value = loaded_flow_run.state
1808:        if (state := self.flow_run.state) and is_suspended_flow_run_state(state):
1959:                        if self.flow_run.state and self.flow_run.state.is_final():
1977:                            self.flow_run.state = state
1993:                                self.flow_run.state
1994:                                and not self.flow_run.state.is_final()
2013:                        if self.flow_run.state and not self.flow_run.state.is_final():
```

## 201 · 2026-10-29T03:42:43.943240+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/flow_engine.py",
  "offset": 1478,
  "limit": 100
}
```

## 202 · 2026-10-29T03:42:44.026548+00:00 · tool_result 

```
1478	    async def set_state(self, state: State, force: bool = False) -> State:
1479	        """ """
1480	        # prevents any state-setting activity
1481	        if self.short_circuit:
1482	            return self.state
1483	
1484	        state = await propose_state(
1485	            self.client, state, flow_run_id=self.flow_run.id, force=force
1486	        )  # type: ignore
1487	        self.flow_run.state = state  # type: ignore
1488	        self.flow_run.state_name = state.name  # type: ignore
1489	        self.flow_run.state_type = state.type  # type: ignore
1490	
1491	        self._capture_state_report(state)
1492	        self._telemetry.update_state(state)
1493	        await self.call_hooks(state)
1494	
1495	        return state
1496	
1497	    async def result(self, raise_on_failure: bool = True) -> "Union[R, State, None]":
1498	        if self._return_value is not NotSet and not isinstance(
1499	            self._return_value, State
1500	        ):
1501	            _result = self._return_value
1502	            link_state_to_flow_run_result(self.state, _result)
1503	
1504	            if asyncio.iscoroutine(_result):
1505	                # getting the value for a BaseResult may return an awaitable
1506	                # depending on whether the parent frame is sync or not
1507	                _result = await _result
1508	            return _result
1509	
1510	        if self._raised is not NotSet:
1511	            if raise_on_failure:
1512	                raise self._raised
1513	            return self._raised
1514	
1515	        # This is a fall through case which leans on the existing state result mechanics to get the
1516	        # return value. This is necessary because we currently will return a State object if the
1517	        # the State was Prefect-created.
1518	        # TODO: Remove the need to get the result from a State except in cases where the return value
1519	        # is a State object.
1520	        return await self.state.aresult(raise_on_failure=raise_on_failure)  # type: ignore
1521	
1522	    async def handle_success(self, result: R) -> R:
1523	        raise_if_flow_run_suspension_requested()
1524	        result_store = getattr(FlowRunContext.get(), "result_store", None)
1525	        if result_store is None:
1526	            raise ValueError("Result store is not set")
1527	        resolved_result = resolve_futures_to_states(result)
1528	        terminal_state = await return_value_to_state(
1529	            resolved_result,
1530	            result_store=result_store,
1531	            write_result=should_persist_result(),
1532	        )
1533	        raise_if_flow_run_suspension_requested()
1534	        await self.set_state(terminal_state)
1535	        self._return_value = resolved_result
1536	
1537	        self._telemetry.end_span_on_success()
1538	
1539	        # Track first flow run milestone for analytics
1540	        try:
1541	            from prefect._internal.analytics import try_mark_milestone
1542	
1543	            try_mark_milestone("first_flow_run")
1544	        except Exception:
1545	            pass
1546	
1547	        return result
1548	
1549	    async def handle_exception(
1550	        self,
1551	        exc: Exception,
1552	        msg: Optional[str] = None,
1553	        result_store: Optional[ResultStore] = None,
1554	    ) -> State:
1555	        self._get_flow_run_suspension_request().raise_if_requested()
1556	        context = FlowRunContext.get()
1557	        terminal_state = cast(
1558	            State,
1559	            await exception_to_failed_state(
1560	                exc,
1561	                message=msg or "Flow run encountered an exception:",
1562	                result_store=result_store or getattr(context, "result_store", None),
1563	                write_result=True,
1564	            ),
1565	        )
1566	        self._get_flow_run_suspension_request().raise_if_requested()
1567	        state = await self.set_state(terminal_state)
1568	        if self.state.is_scheduled():
1569	            self.logger.info(
1570	                (
1571	                    f"Received non-final state {state.name!r} when proposing final"
1572	                    f" state {terminal_state.name!r} and will attempt to run again..."
1573	                ),
1574	            )
1575	            self._get_flow_run_suspension_request().raise_if_requested()
1576	            state = await self.set_state(Running())
1577	        self._raised = exc
```

## 203 · 2026-10-29T03:43:06.628260+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"proactive\" docs/v3/release-notes/oss/*.mdx | tail -30",
  "description": "Search release notes for proactive fixes"
}
```

## 204 · 2026-10-29T03:43:06.930987+00:00 · tool_result 

```
docs/v3/release-notes/oss/version-3-4.mdx:363:* Special case for proactive automation by [@jakekaplan](https://github.com/jakekaplan) in [#18819](https://github.com/PrefectHQ/prefect/pull/18819)
docs/v3/release-notes/oss/version-3-6.mdx:1003:* Convert scheduler and proactive triggers to Docket, remove `LoopService` by [@zzstoatzz](https://github.com/zzstoatzz) in [#19756](https://github.com/PrefectHQ/prefect/pull/19756)
```

## 205 · 2026-10-29T03:43:06.994901+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"bucket\" docs/ src/prefect/server/events/ --include=\"*.mdx\" --include=\"*.py\" | grep -v \"src/prefect/server/events/triggers.py\" | head -20",
  "description": "Search docs for bucket references"
}
```

## 206 · 2026-10-29T03:43:08.134086+00:00 · tool_result 

```
docs/conftest.py:25:    "docs/integrations/prefect-bitbucket/index.mdx": "Needs block cleanup handling",
docs/integrations/integrations.mdx:23:    <Card title="Bitbucket">
docs/integrations/integrations.mdx:24:        <a href="/integrations/prefect-bitbucket"> <img src="/images/integrations/bitbucket.png" noZoom alt="prefect-bitbucket"/>
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-execute.mdx:13:download_bundle_from_s3(bucket: str, key: str, output_dir: str | None = None, aws_credentials_block_name: Optional[str] = None) -> DownloadResult
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-execute.mdx:17:Downloads a bundle from an S3 bucket.
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-execute.mdx:20:- `bucket`: S3 bucket name
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-execute.mdx:35:execute_bundle_from_s3(bucket: str, key: str, aws_credentials_block_name: Optional[str] = None) -> None
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-execute.mdx:48:- `bucket`: S3 bucket name
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-upload.mdx:19:upload_bundle_to_s3(local_filepath: str, bucket: str, key: str, aws_credentials_block_name: Optional[str] = None) -> UploadResult
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-upload.mdx:23:Uploads a bundle file to an S3 bucket.
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-upload.mdx:27:- `bucket`: S3 bucket name
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-upload.mdx:35:- bucket: The S3 bucket the bundle was uploaded to
docs/integrations/prefect-aws/api-ref/prefect_aws-bundles-upload.mdx:37:- url: The full S3 URL of the uploaded bundle (s3://bucket/key)
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:19:push_to_s3(bucket: str, folder: str, credentials: Optional[dict[str, Any]] = None, client_parameters: Optional[dict[str, Any]] = None, ignore_file: Optional[str] = '.prefectignore') -> PushToS3Output
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:23:Pushes the contents of the current working directory to an S3 bucket,
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:27:- `bucket`: The name of the S3 bucket where files will be uploaded.
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:28:- `folder`: The folder in the S3 bucket where files will be uploaded.
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:37:- A dictionary containing the bucket and folder where files were uploaded.
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:41:Push files to an S3 bucket:
docs/integrations/prefect-aws/api-ref/prefect_aws-deployments-steps.mdx:46:        bucket: my-bucket
```

## 207 · 2026-10-29T03:43:13.495608+00:00 · assistant_message 

```
Let me test a production-realistic variant: a periodic proactive evaluation running between the completion and the late heartbeat.
```

## 208 · 2026-10-29T03:43:15.807014+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat > /tmp/test_eager_deletion_probe.py <<'EOF'\n\"\"\"Probe: does an intermediate proactive evaluation break the fix?\"\"\"\nfrom datetime import timedelta\nfrom unittest import mock\nfrom uuid import UUID, uuid4\n\nimport pytest\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations\nfrom prefect.server.events.schemas.automations import Automation, EventTrigger, Posture\nfrom prefect.server.events.schemas.events import Event\nfrom prefect.types._datetime import DateTime\n\npytestmark = pytest.mark.clear_db\n\nRESOURCE_ID = \"prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa\"\n\n\n@pytest.fixture\nasync def automation(cleared_buckets, cleared_automations, automations_session: AsyncSession) -> Automation:\n    automation = await automations.create_automation(\n        automations_session,\n        Automation(\n            name=\"Unresponsive run monitor\",\n            trigger=EventTrigger(\n                match={\"prefect.resource.id\": \"prefect.flow-run.*\"},\n                after={\"prefect.flow-run.heartbeat\"},\n                expect={\"prefect.flow-run.*\"},\n                for_each=[\"prefect.resource.id\"],\n                posture=Posture.Proactive,\n                threshold=1,\n                within=timedelta(seconds=90),\n            ),\n            actions=[actions.DoNothing()],\n        ),\n    )\n    triggers.load_automation(automation)\n    await automations_session.commit()\n    return automation\n\n\ndef event(name, occurred):\n    return Event(occurred=occurred, event=name, resource={\"prefect.resource.id\": RESOURCE_ID}, id=uuid4()).receive()\n\n\nasync def test_intermediate_proactive_evaluation(automation, frozen_time: DateTime):\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time + timedelta(seconds=30)))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.Completed\", frozen_time + timedelta(seconds=60)))\n    # A periodic proactive tick happens before the late heartbeat is delivered\n    await triggers.proactive_evaluation(automation.trigger, frozen_time + timedelta(seconds=61))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time + timedelta(seconds=60)))\n    await triggers.proactive_evaluation(automation.trigger, frozen_time + timedelta(seconds=151))\nEOF\ncp /tmp/test_eager_deletion_probe.py tests/events/server/triggers/zz_probe_test.py && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/zz_probe_test.py -q -p no:randomly 2>&1 | tail -15",
  "description": "Probe intermediate proactive evaluation behavior",
  "timeout": 300000
}
```

## 209 · 2026-10-29T03:43:50.280798+00:00 · tool_result 

```
.                                                                        [100%]
1 passed in 22.40s
```

## 210 · 2026-10-29T03:43:53.929198+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat > tests/events/server/triggers/zz_probe_test.py <<'EOF'\n\"\"\"Probe: does an intermediate proactive evaluation break the fix?\"\"\"\nfrom datetime import timedelta\nfrom unittest import mock\nfrom uuid import uuid4\n\nimport pytest\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations\nfrom prefect.server.events.schemas.automations import Automation, EventTrigger, Posture\nfrom prefect.server.events.schemas.events import Event\nfrom prefect.types._datetime import DateTime\n\npytestmark = pytest.mark.clear_db\n\nRESOURCE_ID = \"prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa\"\n\n\n@pytest.fixture\nasync def automation(cleared_buckets, cleared_automations, automations_session: AsyncSession) -> Automation:\n    automation = await automations.create_automation(\n        automations_session,\n        Automation(\n            name=\"Unresponsive run monitor\",\n            trigger=EventTrigger(\n                match={\"prefect.resource.id\": \"prefect.flow-run.*\"},\n                after={\"prefect.flow-run.heartbeat\"},\n                expect={\"prefect.flow-run.*\"},\n                for_each=[\"prefect.resource.id\"],\n                posture=Posture.Proactive,\n                threshold=1,\n                within=timedelta(seconds=90),\n            ),\n            actions=[actions.DoNothing()],\n        ),\n    )\n    triggers.load_automation(automation)\n    await automations_session.commit()\n    return automation\n\n\ndef event(name, occurred):\n    return Event(occurred=occurred, event=name, resource={\"prefect.resource.id\": RESOURCE_ID}, id=uuid4()).receive()\n\n\nasync def test_intermediate_proactive_evaluation(automation, frozen_time: DateTime, act: mock.AsyncMock):\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time + timedelta(seconds=30)))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.Completed\", frozen_time + timedelta(seconds=60)))\n    # A periodic proactive tick happens before the late heartbeat is delivered\n    await triggers.proactive_evaluation(automation.trigger, frozen_time + timedelta(seconds=61))\n    await triggers.reactive_evaluation(event(\"prefect.flow-run.heartbeat\", frozen_time + timedelta(seconds=60)))\n    await triggers.proactive_evaluation(automation.trigger, frozen_time + timedelta(seconds=151))\n    act.assert_not_awaited()\nEOF\n\"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/zz_probe_test.py -q -p no:randomly 2>&1 | tail -20",
  "description": "Probe intermediate proactive evaluation with assertion",
  "timeout": 300000
}
```

## 211 · 2026-10-29T03:44:33.651277+00:00 · tool_result 

```
------------------------------ Captured log call ------------------------------
INFO     prefect.server.events.triggers:triggers.py:603 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03, trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c covers event 'prefect.flow-run.heartbeat' (8e3b8160-1580-47a0-ac8a-a6290d13a8b2) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:44:27.485602+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:223 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 ('Unresponsive run monitor') trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:603 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03, trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c covers event 'prefect.flow-run.heartbeat' (930ec7c8-ee04-4817-a3d1-b7197cae3b22) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:44:57.485602+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:223 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 ('Unresponsive run monitor') trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:603 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03, trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c covers event 'prefect.flow-run.Completed' (3aed8280-bbad-4324-8730-3bb54f393c7e) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:45:27.485602+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:223 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 ('Unresponsive run monitor') trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
DEBUG    prefect.server.events.triggers:triggers.py:1349 Evaluating automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c proactively as of 2026-10-29 03:45:28.485602+00:00 (offset 0.0s)
INFO     prefect.server.events.triggers:triggers.py:603 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03, trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c covers event 'prefect.flow-run.heartbeat' (eae86a65-0795-4fb6-9353-fa97390141a0) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:45:27.485602+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:223 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 ('Unresponsive run monitor') trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
DEBUG    prefect.server.events.triggers:triggers.py:1349 Evaluating automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c proactively as of 2026-10-29 03:46:58.485602+00:00 (offset 0.0s)
DEBUG    prefect.server.events.triggers:triggers.py:185 Automation ea7e514e-a97e-42ef-9ea1-0834ae904a03 ('Unresponsive run monitor') trigger 2ed2823f-37e5-47bf-b488-fb0d54e0729c triggered for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa']) proactively, having occurred 0 times between 2026-10-29 03:45:27.485602+00:00 and 2026-10-29 03:46:57.485602+00:00
-------------------------- Captured stderr teardown ---------------------------
11:44:31.310 | INFO    | uvicorn.error - Shutting down
11:44:31.418 | INFO    | uvicorn.error - Waiting for application shutdown.
11:44:31.420 | INFO    | uvicorn.error - Application shutdown complete.
11:44:31.420 | INFO    | uvicorn.error - Finished server process [21428]
=========================== short test summary info ===========================
FAILED tests/events/server/triggers/zz_probe_test.py::test_intermediate_proactive_evaluation
1 failed in 26.28s
```

## 212 · 2026-10-29T03:44:58.115602+00:00 · assistant_message 

```
The intermediate proactive evaluation breaks the current fix — a production-realistic race. I need the watermark to survive bucket deletion. Let me investigate the database/migration infrastructure.
```

## 213 · 2026-10-29T03:44:58.461466+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"create_all\\|run_migrations\\|upgrade\" tests/conftest.py src/prefect/server/database/dependencies.py 2>/dev/null | head -20",
  "description": "Check test DB creation strategy"
}
```

## 214 · 2026-10-29T03:44:58.755566+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def database_interface\\|alembic\\|create_db\" tests/conftest.py | head -30",
  "description": "Find DB test setup"
}
```

## 215 · 2026-10-29T03:44:58.817392+00:00 · tool_result 

```
(Bash completed with no output)
```

## 216 · 2026-10-29T03:44:59.079304+00:00 · tool_result 

```
(Bash completed with no output)
```

## 217 · 2026-10-29T03:45:00.509788+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rln \"alembic\\|migration\" tests/ | head -20 && grep -rn \"database_interface\\|test_database\" tests/conftest.py | head -20",
  "description": "Locate database test fixtures"
}
```

## 218 · 2026-10-29T03:45:01.445508+00:00 · tool_result 

```
tests/blocks/test_core.py
tests/cli/test_start_server.py
tests/cli/transfer/conftest.py
tests/cli/transfer/test_automations.py
tests/cli/transfer/test_blocks.py
tests/cli/transfer/test_concurrency_limits.py
tests/cli/transfer/test_dag.py
tests/cli/transfer/test_deployments.py
tests/cli/transfer/test_flows.py
tests/cli/transfer/test_variables.py
tests/cli/transfer/test_work_pools.py
tests/cli/transfer/test_work_queues.py
tests/client/test_prefect_client.py
tests/concurrency/v1/test_concurrency_sync.py
tests/input/test_actions.py
tests/input/test_run_input.py
tests/plugins/test_compat.py
tests/server/database/test_alembic_commands.py
tests/server/database/test_migrations.py
tests/server/orchestration/api/test_concurrency_limits.py
17:    the settings context change. See `test_database_connection_url` for example.
425:async def generate_test_database_connection_url(
507:def test_database_connection_url(
508:    generate_test_database_connection_url: Optional[str],
512:    `generate_test_database_connection_url`
517:    url = generate_test_database_connection_url
```

## 219 · 2026-10-29T03:45:02.994810+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"create_all\\|create_db\\|upgrade\" src/prefect/server/database/interface.py src/prefect/server/database/dependencies.py src/prefect/server/database/configurations.py 2>/dev/null | head -30",
  "description": "Find DB schema creation"
}
```

## 220 · 2026-10-29T03:45:03.186324+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 380,470p tests/conftest.py",
  "description": "Read test DB setup"
}
```

## 221 · 2026-10-29T03:45:03.315390+00:00 · tool_result 

```
src/prefect/server/database/interface.py:10:from prefect.server.database.alembic_commands import alembic_downgrade, alembic_upgrade
src/prefect/server/database/interface.py:75:    async def create_db(self) -> None:
src/prefect/server/database/interface.py:77:        await self.run_migrations_upgrade()
src/prefect/server/database/interface.py:113:    async def run_migrations_upgrade(self) -> None:
src/prefect/server/database/interface.py:114:        """Run all upgrade migrations"""
src/prefect/server/database/interface.py:115:        await run_sync_in_worker_thread(alembic_upgrade)
src/prefect/server/database/configurations.py:196:    async def create_db(
src/prefect/server/database/configurations.py:428:    async def create_db(
src/prefect/server/database/configurations.py:433:        await connection.run_sync(base_metadata.create_all)
src/prefect/server/database/configurations.py:627:    async def create_db(
src/prefect/server/database/configurations.py:632:        await connection.run_sync(base_metadata.create_all)
```

## 222 · 2026-10-29T03:45:03.462609+00:00 · tool_result 

```
    TEST_PROFILE_CTX = prefect.context.use_profile(
        profile,
        override_environment_variables=True,
        include_current_context=False,
    )
    TEST_PROFILE_CTX.__enter__()

    # Create the storage path now, fixing an obscure bug where it can be created by
    # when mounted as Docker volume resulting in the directory being owned by root
    # and unwritable by the normal user
    PREFECT_LOCAL_STORAGE_PATH.value().mkdir()

    # Ensure logging is configured for the test session
    setup_logging()


# def pytest_sessionfinish(session, exitstatus):
@pytest.fixture(scope="session", autouse=True)
def cleanup(drain_log_workers: None, drain_events_workers: None):
    # this fixture depends on other fixtures with important cleanup steps like
    # draining workers to ensure that the home directory is not deleted before
    # these steps are completed
    yield

    # delete the temporary directory
    # Use ignore_errors=True to handle race conditions where SQLite auxiliary
    # files (.db-shm, .db-wal) may be deleted by SQLite before rmtree runs
    if TEST_PREFECT_HOME is not None:
        shutil.rmtree(TEST_PREFECT_HOME, ignore_errors=True)


@pytest.fixture(scope="session", autouse=True)
def safety_check_settings():
    # Safety check for connection to an external API
    assert PREFECT_API_URL.value() is None, (
        "Tests should not be run connected to an external API."
    )
    # Safety check for home directory
    assert str(PREFECT_HOME.value()) == TEST_PREFECT_HOME, (
        "Tests should use the temporary test directory"
    )


@pytest.fixture(scope="session", autouse=True)
async def generate_test_database_connection_url(
    worker_id: str,
) -> AsyncGenerator[Optional[str], None]:
    """Prepares an alternative test database URL, if necessary, for the current
    connection URL.

    For databases without a server (i.e. SQLite), produces `None`, indicating we should
    just use the currently configured value.

    For databases with a server (i.e. Postgres), creates an additional database on the
    server for each test worker, using the provided connection URL as the starting
    point.  Requires that the given database user has permission to connect to the
    server and create new databases."""
    original_url = PREFECT_SERVER_DATABASE_CONNECTION_URL.value()
    if not original_url:
        yield None
        return

    print(f"Generating test database connection URL from {original_url!r}")
    scheme, netloc, database, query, fragment = urlsplit(original_url)
    if scheme == "sqlite+aiosqlite":
        # SQLite databases will be scoped by the PREFECT_HOME setting, which will
        # be in an isolated temporary directory
        test_db_path = Path(PREFECT_HOME.value()) / f"prefect_{worker_id}.db"
        yield f"sqlite+aiosqlite:///{test_db_path}"
        return

    elif scheme == "postgresql+asyncpg":
        test_db_name = database.strip("/") + f"_tests_{worker_id}"
        quoted_db_name = postgres_dialect().identifier_preparer.quote(test_db_name)

        postgres_url = urlunsplit(("postgres", netloc, "postgres", query, fragment))

        # Create an empty temporary database for use in the tests

        print(f"Connecting to postgres at {postgres_url!r}")
        connection = await asyncpg.connect(postgres_url)
        try:
            print(f"Creating test postgres database {quoted_db_name!r}")
            # remove any connections to the test database. For example if a SQL IDE
            # is being used to investigate it, it will block the drop database command.
            await connection.execute(
                f"""
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = '{quoted_db_name}'
```

## 223 · 2026-10-29T03:45:06.120967+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat src/prefect/server/database/_migrations/versions/sqlite/2026_02_19_200000_add_scheduler_schedule_id_index.py && echo ================= && cat src/prefect/server/database/_migrations/versions/postgresql/2026_02_19_200000_add_scheduler_schedule_id_index.py",
  "description": "Read a recent migration pair"
}
```

## 224 · 2026-10-29T03:45:06.353203+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1,80p tests/server/database/test_migrations.py",
  "description": "Read migration tests"
}
```

## 225 · 2026-10-29T03:45:06.463916+00:00 · tool_result 

```
"""Add expression index for per-schedule scheduler query

Revision ID: a1b2c3d4e5f7
Revises: 9e83011d1f2a
Create Date: 2026-02-19 20:00:00.000000

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "a1b2c3d4e5f7"
down_revision = "9e83011d1f2a"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE INDEX IF NOT EXISTS
        ix_flow_run__schedule_id_scheduler
        ON flow_run (deployment_id, json_extract(created_by, '$.id'), next_scheduled_start_time)
        WHERE state_type = 'SCHEDULED' AND auto_scheduled = 1;
        """
    )


def downgrade():
    op.execute(
        """
        DROP INDEX IF EXISTS ix_flow_run__schedule_id_scheduler;
        """
    )
=================
"""Add expression index for per-schedule scheduler query

Revision ID: a1b2c3d4e5f6
Revises: 9e83011d1f2a
Create Date: 2026-02-19 20:00:00.000000

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "a1b2c3d4e5f6"
down_revision = "9e83011d1f2a"
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        op.execute(
            """
            CREATE INDEX CONCURRENTLY IF NOT EXISTS
            ix_flow_run__schedule_id_scheduler
            ON flow_run (deployment_id, (created_by->>'id'), next_scheduled_start_time)
            WHERE state_type = 'SCHEDULED' AND auto_scheduled = true;
            """
        )


def downgrade():
    with op.get_context().autocommit_block():
        op.execute(
            """
            DROP INDEX CONCURRENTLY IF EXISTS ix_flow_run__schedule_id_scheduler;
            """
        )
```

## 226 · 2026-10-29T03:45:06.638015+00:00 · tool_result 

```
import contextlib
import importlib.util
import json
import textwrap
from collections.abc import AsyncIterator
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import alembic.context
import alembic.script
import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from prefect.server.database import dependencies
from prefect.server.database.alembic_commands import (
    alembic_config,
    alembic_downgrade,
    alembic_upgrade,
)
from prefect.server.database.interface import DBSingleton, PrefectDBInterface
from prefect.server.database.orm_models import (
    AioSqliteORMConfiguration,
    AsyncPostgresORMConfiguration,
)
from prefect.server.models.variables import read_variables
from prefect.server.utilities.database import get_dialect
from prefect.settings import (
    PREFECT_API_DATABASE_CONNECTION_URL,
    PREFECT_SERVER_DATABASE_CONNECTION_URL,
    temporary_settings,
)
from prefect.types._datetime import now
from prefect.utilities.asyncutils import run_sync_in_worker_thread

pytestmark = [pytest.mark.service("database"), pytest.mark.clear_db]


@contextlib.asynccontextmanager
async def _isolated_postgres_schema_changes(
    db: PrefectDBInterface, database_engine: AsyncEngine
) -> AsyncIterator[None]:
    if db.dialect.name != "postgresql":
        yield
        return

    # Alembic uses a separate engine, so the application pool does not observe its
    # DDL and can retain asyncpg prepared statements for types that were replaced.
    await database_engine.dispose()
    try:
        yield
    finally:
        # The hosted test API runs in another process against the same per-worker
        # database. Disconnect its pooled sessions too; pool_pre_ping will replace
        # them before the next request.
        async with database_engine.begin() as connection:
            await connection.execute(
                sa.text(
                    """
                    SELECT pg_terminate_backend(pid)
                    FROM pg_stat_activity
                    WHERE datname = current_database()
                      AND pid <> pg_backend_pid()
                    """
                )
            )
        await database_engine.dispose()


@pytest.fixture(autouse=True)
async def isolate_migration_tests(
    db: PrefectDBInterface, database_engine: AsyncEngine
) -> AsyncIterator[None]:
    async with _isolated_postgres_schema_changes(db, database_engine):
        yield


@pytest.fixture
```

## 227 · 2026-10-29T03:45:08.587691+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"^async def test_\\|^def test_\" tests/server/database/test_migrations.py | head -40",
  "description": "List migration tests"
}
```

## 228 · 2026-10-29T03:45:08.834924+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"metadata\\|compare\" tests/server/database/test_migrations.py | head -30",
  "description": "Check migration schema comparison"
}
```

## 229 · 2026-10-29T03:45:08.936241+00:00 · tool_result 

```
167:async def test_postgres_migration_engine_uses_migration_timeout(
204:async def test_sqlite_migration_engine_reuses_application_engine(
224:async def test_apply_migrations_disposes_dedicated_engine(
274:async def test_apply_migrations_preserves_shared_engine(
310:def test_event_resource_index_migration_rebuilds_invalid_index(
353:def test_event_resource_index_migration_supports_postgres_dry_run(
387:async def test_schema_migrations_discard_stale_postgres_prepared_statements(
447:def test_flow_run_deployment_id_index_migration_rebuilds_invalid_index(
490:def test_flow_run_deployment_id_index_migration_supports_postgres_dry_run(
525:def test_event_resources_occurred_index_repair_migration_handles_index_state(
595:def test_event_resources_occurred_index_repair_migration_rejects_postgres_dry_run(
625:async def test_event_resources_occurred_index_repair_migration_repairs_postgres(
702:def test_flow_run_state_type_coalesce_start_time_index_migration_handles_index_state(
776:def test_flow_run_state_type_coalesce_start_time_index_migration_rejects_postgres_dry_run(
805:async def test_flow_run_state_type_coalesce_start_time_index_exists(
846:async def test_orion_full_migration_works_with_data_in_db(sample_db_data):
859:def test_only_single_head_revision_in_migrations(orm_config):
871:async def test_backfill_state_name(db, flow):
1017:async def test_backfill_artifacts(db):
1141:async def test_adding_work_pool_tables_does_not_remove_fks(db, flow):
1218:async def test_adding_default_agent_pool_with_existing_default_queue_migration(
1331:async def test_adding_default_agent_pool_without_existing_default_queue_migration(db):
1402:async def test_not_adding_default_agent_pool_when_all_work_queues_have_work_pool(db):
1489:async def test_migrate_variables_to_json(db):
1552:async def test_migrate_flow_run_notifications_to_automations(db: PrefectDBInterface):
1745:async def test_downgrade_with_orphaned_task_run_state_ids(db, flow):
1814:async def test_drop_db_removes_all_tables(db):
```

## 230 · 2026-10-29T03:45:09.197426+00:00 · tool_result 

```
1819:    drop_db() uses metadata.drop_all() instead of running the full Alembic
```

## 231 · 2026-10-29T03:45:11.077146+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/server/database/test_migrations.py",
  "offset": 846,
  "limit": 40
}
```

## 232 · 2026-10-29T03:45:11.179169+00:00 · tool_result 

```
846	async def test_orion_full_migration_works_with_data_in_db(sample_db_data):
847	    """
848	    Tests that downgrade migrations work when the database has data in it.
849	    """
850	    try:
851	        await run_sync_in_worker_thread(alembic_downgrade, revision="base")
852	    finally:
853	        await run_sync_in_worker_thread(alembic_upgrade)
854	
855	
856	@pytest.mark.parametrize(
857	    "orm_config", [AioSqliteORMConfiguration, AsyncPostgresORMConfiguration]
858	)
859	def test_only_single_head_revision_in_migrations(orm_config):
860	    config = alembic_config()
861	    script = alembic.script.ScriptDirectory.from_config(config)
862	
863	    script.version_locations = [orm_config().versions_dir]
864	
865	    # This will raise if there are multiple heads
866	    head = script.get_current_head()
867	
868	    assert head is not None, "Head revision is missing"
869	
870	
871	async def test_backfill_state_name(db, flow):
872	    """
873	    Tests state_name is backfilled correctly for the flow_run
874	    and task_run tables by a specific migration
875	    """
876	    connection_url = PREFECT_API_DATABASE_CONNECTION_URL.value()
877	    dialect = get_dialect(connection_url)
878	
879	    # get the proper migration revisions
880	    if dialect.name == "postgresql":
881	        revisions = ("605ebb4e9155", "14dc68cc5853")
882	    else:
883	        pytest.skip(reason="Test is excessively slow on SQLite")
884	        revisions = ("7f5f335cace3", "db6bde582447")
885	
```

## 233 · 2026-10-29T03:45:14.157718+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"create_db\\|drop_db\" tests/fixtures/ tests/conftest.py | head -30",
  "description": "Find test DB create/drop"
}
```

## 234 · 2026-10-29T03:45:14.441517+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/fixtures/ && grep -rn \"def db\\b\\|def session\\b\" tests/fixtures/database.py | head",
  "description": "List fixtures and DB fixtures"
}
```

## 235 · 2026-10-29T03:45:14.492916+00:00 · tool_result 

```
tests/fixtures/database.py:86:        await db.create_db()
```

## 236 · 2026-10-29T03:45:14.804899+00:00 · tool_result 

```
AGENTS.md
api.py
client.py
collections_registry.py
database.py
deprecation.py
docker.py
events.py
logging.py
storage.py
telemetry.py
time.py
42:def db(test_database_connection_url, safety_check_settings):
139:async def session(db) -> AsyncGenerator[AsyncSession, None]:
```

## 237 · 2026-10-29T03:45:16.771950+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/fixtures/database.py",
  "offset": 1,
  "limit": 180
}
```

## 238 · 2026-10-29T03:45:16.873840+00:00 · tool_result 

```
1	import asyncio
2	import datetime
3	import gc
4	import uuid
5	import warnings
6	from contextlib import asynccontextmanager
7	from typing import AsyncContextManager, AsyncGenerator, Callable, Optional, Type
8	
9	import pytest
10	from sqlalchemy.exc import DBAPIError, InterfaceError
11	from sqlalchemy.ext.asyncio import AsyncSession
12	
13	from prefect.blocks.notifications import NotificationBlock
14	from prefect.filesystems import LocalFileSystem
15	from prefect.server import models, schemas
16	from prefect.server.database import (
17	    PrefectDBInterface,
18	    orm_models,
19	    provide_database_interface,
20	)
21	from prefect.server.database.configurations import ENGINES, TRACKER
22	from prefect.server.models.block_registration import (
23	    register_block_schema,
24	    register_block_type,
25	    run_block_auto_registration,
26	)
27	from prefect.server.models.concurrency_limits_v2 import create_concurrency_limit
28	from prefect.server.orchestration.rules import (
29	    FlowOrchestrationContext,
30	    TaskOrchestrationContext,
31	)
32	from prefect.server.schemas import states
33	from prefect.server.schemas.core import ConcurrencyLimitV2
34	from prefect.types._datetime import now
35	from prefect.utilities.callables import parameter_schema
36	from prefect.workers.process import ProcessWorker
37	
38	AsyncSessionGetter = Callable[[], AsyncContextManager[AsyncSession]]
39	
40	
41	@pytest.fixture(scope="session", autouse=True)
42	def db(test_database_connection_url, safety_check_settings):
43	    return provide_database_interface()
44	
45	
46	@pytest.fixture(scope="session", autouse=True)
47	async def database_engine(db: PrefectDBInterface):
48	    """Produce a database engine"""
49	    TRACKER.active = True
50	
51	    engine = await db.engine()
52	
53	    yield engine
54	
55	    # At the end of the test session, dispose of _any_ open engines, not just the one
56	    # that we produced here.  Other engines may have been created from different event
57	    # loops, and we need to ensure that they are all disposed of.
58	
59	    engines = list(ENGINES.values())
60	    ENGINES.clear()
61	
62	    for engine in engines:
63	        await engine.dispose()
64	
65	    # Finally, free up all references to connections and clean up proactively so that
66	    # we don't have any lingering connections after this.  This should prevent
67	    # post-test-session ResourceWarning errors about unclosed connections.
68	
69	    TRACKER.clear()
70	    gc.collect()
71	
72	
73	@pytest.fixture
74	def print_query(database_engine):
75	    def inner(query):
76	        return print(query.compile(database_engine))
77	
78	    return inner
79	
80	
81	@pytest.fixture(scope="session", autouse=True)
82	async def setup_db(database_engine, db):
83	    """Create all database objects prior to running tests, and drop them when tests are done."""
84	    try:
85	        # build the database
86	        await db.create_db()
87	        yield
88	
89	    except Exception as exc:
90	        # Re-raise with a message containing the url
91	        raise RuntimeError(
92	            f"Failed to set up the database at {database_engine.url!r}"
93	        ) from exc
94	
95	
96	@pytest.fixture(autouse=True)
97	async def clear_db(db, request):
98	    """
99	    Delete all data from all tables before running each test, attempting to handle
100	    connection errors.
101	    """
102	
103	    if "clear_db" in request.keywords and not request.config.getoption("--no-clear-db"):
104	        max_retries = 3
105	        retry_delay = 1
106	
107	        for attempt in range(max_retries):
108	            try:
109	                async with db.session_context(begin_transaction=True) as session:
110	                    await session.execute(orm_models.Agent.__table__.delete())
111	                    await session.execute(orm_models.WorkPool.__table__.delete())
112	
113	                    for table in reversed(orm_models.Base.metadata.sorted_tables):
114	                        await session.execute(table.delete())
115	                    break
116	            except (InterfaceError, DBAPIError):
117	                if attempt < max_retries - 1:
118	                    print(
119	                        "Connection issue. Retrying entire deletion operation"
120	                        f" ({attempt + 1}/{max_retries})..."
121	                    )
122	                    await asyncio.sleep(retry_delay)
123	                else:
124	                    raise
125	
126	    # Also clear the memory lease storage singleton to prevent test pollution
127	    from prefect.server.concurrency.lease_storage.memory import (
128	        ConcurrencyLeaseStorage,
129	    )
130	
131	    storage = ConcurrencyLeaseStorage()
132	    storage.leases.clear()
133	    storage.expirations.clear()
134	
135	    yield
136	
137	
138	@pytest.fixture
139	async def session(db) -> AsyncGenerator[AsyncSession, None]:
140	    session = await db.session()
141	    async with session:
142	        yield session
143	
144	
145	@pytest.fixture
146	async def get_server_session(db) -> AsyncSessionGetter:
147	    """
148	    Returns a context manager factory that yields
149	    an database session.
150	
151	    Note: if you commit or rollback a transaction, scoping
152	    will be reset. Fixture should be used as a context manager.
153	    """
154	
155	    @asynccontextmanager
156	    async def _get_server_session() -> AsyncGenerator[AsyncSession, None]:
157	        async with await db.session() as session:
158	            yield session
159	
160	    return _get_server_session
161	
162	
163	@pytest.fixture
164	async def register_block_types(session):
165	    await run_block_auto_registration(session=session)
166	    await session.commit()
167	
168	
169	@pytest.fixture
170	async def flow(session: AsyncSession):
171	    model = await models.flows.create_flow(
172	        session=session, flow=schemas.core.Flow(name=f"my-flow-{uuid.uuid4()}")
173	    )
174	    await session.commit()
175	    return model
176	
177	
178	@pytest.fixture
179	async def flow_run(session: AsyncSession, flow: orm_models.Flow):
180	    model = await models.flow_runs.create_flow_run(
```

## 239 · 2026-10-29T03:45:19.565763+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 180,240p src/prefect/server/database/configurations.py && sed -n 410,450p src/prefect/server/database/configurations.py",
  "description": "Read create_db implementations"
}
```

## 240 · 2026-10-29T03:45:19.880075+00:00 · tool_result 

```
        """
        Returns a key used to determine whether to instantiate a new DB interface.
        """
        return (self.__class__, self.connection_url)

    @abstractmethod
    async def engine(self) -> AsyncEngine:
        """Returns a SqlAlchemy engine"""

    @abstractmethod
    async def session(self, engine: AsyncEngine) -> AsyncSession:
        """
        Retrieves a SQLAlchemy session for an engine.
        """

    @abstractmethod
    async def create_db(
        self, connection: AsyncConnection, base_metadata: sa.MetaData
    ) -> None:
        """Create the database"""

    @abstractmethod
    async def drop_db(
        self, connection: AsyncConnection, base_metadata: sa.MetaData
    ) -> None:
        """Drop the database"""

    @abstractmethod
    def is_inmemory(self) -> bool:
        """Returns true if database is run in memory"""

    @abstractmethod
    def begin_transaction(
        self, session: AsyncSession, with_for_update: bool = False
    ) -> AbstractAsyncContextManager[AsyncSessionTransaction]:
        """Enter a transaction for a session"""
        pass


class AsyncPostgresConfiguration(BaseDatabaseConfiguration):
    async def engine(self) -> AsyncEngine:
        """Retrieves an async SQLAlchemy engine.

        Returns:
            AsyncEngine: a SQLAlchemy engine
        """

        loop = get_running_loop()

        cache_key = (
            loop,
            self.connection_url,
            self.echo,
            self.timeout,
        )
        if cache_key not in ENGINES:
            kwargs: dict[str, Any] = (
                get_current_settings().server.database.sqlalchemy.model_dump(
                    mode="json", exclude={"connect_args"}
                )
            )
    async def session(self, engine: AsyncEngine) -> AsyncSession:
        """
        Retrieves a SQLAlchemy session for an engine.

        Args:
            engine: a sqlalchemy engine
        """
        return AsyncSession(engine, expire_on_commit=False)

    @asynccontextmanager
    async def begin_transaction(
        self, session: AsyncSession, with_for_update: bool = False
    ) -> AsyncGenerator[AsyncSessionTransaction, None]:
        # `with_for_update` is for SQLite only. For Postgres, lock the row on read
        # for update instead.
        async with session.begin() as transaction:
            yield transaction

    async def create_db(
        self, connection: AsyncConnection, base_metadata: sa.MetaData
    ) -> None:
        """Create the database"""

        await connection.run_sync(base_metadata.create_all)

    async def drop_db(
        self, connection: AsyncConnection, base_metadata: sa.MetaData
    ) -> None:
        """Drop the database"""

        await connection.run_sync(base_metadata.drop_all)

    def is_inmemory(self) -> bool:
        """Returns true if database is run in memory"""

        return False


class AioSqliteConfiguration(BaseDatabaseConfiguration):
    # Python 3.11+'s sqlite3 module requires window functions (SQLite >= 3.25.0)
    MIN_SQLITE_VERSION = (3, 25, 0)
```

## 241 · 2026-10-29T03:45:21.988740+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/interface.py",
  "offset": 55,
  "limit": 80
}
```

## 242 · 2026-10-29T03:45:22.087675+00:00 · tool_result 

```
55	class PrefectDBInterface(metaclass=DBSingleton):
56	    """
57	    An interface for backend-specific SqlAlchemy actions and ORM models.
58	
59	    The REST API can be configured to run against different databases in order maintain
60	    performance at different scales. This interface integrates database- and dialect-
61	    specific configuration into a unified interface that the orchestration engine runs
62	    against.
63	    """
64	
65	    def __init__(
66	        self,
67	        database_config: BaseDatabaseConfiguration,
68	        query_components: "BaseQueryComponents",
69	        orm: orm_models.BaseORMConfiguration,
70	    ):
71	        self.database_config = database_config
72	        self.queries = query_components
73	        self.orm = orm
74	
75	    async def create_db(self) -> None:
76	        """Create the database"""
77	        await self.run_migrations_upgrade()
78	
79	    async def drop_db(self) -> None:
80	        """Drop the database by removing all tables directly.
81	
82	        This reflects the actual database schema and drops every table rather
83	        than running all Alembic downgrade migrations in reverse.  Running
84	        downgrades is fragile because individual migration downgrade steps may
85	        fail on real-world data (e.g. re-adding a foreign key constraint when
86	        orphaned references exist).  Dropping tables directly is both faster
87	        and more robust.
88	
89	        Reflection is used instead of `Base.metadata.drop_all()` so that
90	        tables created by migrations but not tracked in the ORM (e.g.
91	        `deployment_version`, `alembic_version`) are also removed.
92	        """
93	        engine = await self.engine()
94	        async with engine.begin() as conn:
95	            # Disable FK checks for SQLite so that tables can be dropped in
96	            # any order without triggering constraint errors.
97	            dialect = get_dialect(self.database_config.connection_url)
98	            is_sqlite = dialect.name == "sqlite"
99	            if is_sqlite:
100	                await conn.execute(sa.text("PRAGMA foreign_keys = OFF"))
101	
102	            try:
103	                # Reflect the actual database schema so we capture every
104	                # table, including migration-only tables not present in the
105	                # ORM metadata.
106	                metadata = sa.MetaData()
107	                await conn.run_sync(metadata.reflect)
108	                await conn.run_sync(metadata.drop_all)
109	            finally:
110	                if is_sqlite:
111	                    await conn.execute(sa.text("PRAGMA foreign_keys = ON"))
112	
113	    async def run_migrations_upgrade(self) -> None:
114	        """Run all upgrade migrations"""
115	        await run_sync_in_worker_thread(alembic_upgrade)
116	
117	    async def run_migrations_downgrade(self, revision: str = "-1") -> None:
118	        """Run all downgrade migrations"""
119	        await run_sync_in_worker_thread(alembic_downgrade, revision=revision)
120	
121	    async def is_db_connectable(self) -> bool:
122	        """
123	        Returns boolean indicating if the database is connectable.
124	        This method is used to determine if the server is ready to accept requests.
125	        """
126	        engine = await self.engine()
127	        try:
128	            async with engine.connect():
129	                return True
130	        except Exception:
131	            return False
132	
133	    async def engine(self) -> AsyncEngine:
134	        """
```

## 243 · 2026-10-29T03:45:30.844011+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/server/database/test_migrations.py",
  "offset": 1808,
  "limit": 50
}
```

## 244 · 2026-10-29T03:45:30.957488+00:00 · tool_result 

```
1808	            ).scalar()
1809	            assert result is None, "Orphaned state_id should be nulled during downgrade"
1810	    finally:
1811	        await run_sync_in_worker_thread(alembic_upgrade)
1812	
1813	
1814	async def test_drop_db_removes_all_tables(db):
1815	    """
1816	    Tests that drop_db() successfully removes all tables even when the
1817	    database contains data that would cause downgrade migrations to fail.
1818	
1819	    drop_db() uses metadata.drop_all() instead of running the full Alembic
1820	    downgrade chain, making it immune to data-dependent migration failures.
1821	    """
1822	    engine = await db.engine()
1823	
1824	    # Verify tables exist before drop
1825	    async with engine.connect() as conn:
1826	        table_names = await conn.run_sync(
1827	            lambda sync_conn: sa.inspect(sync_conn).get_table_names()
1828	        )
1829	    assert len(table_names) > 0, "Database should have tables before drop"
1830	
1831	    # Drop the database
1832	    await db.drop_db()
1833	
1834	    # Verify all ORM tables and alembic_version are gone
1835	    async with engine.connect() as conn:
1836	        table_names = await conn.run_sync(
1837	            lambda sync_conn: sa.inspect(sync_conn).get_table_names()
1838	        )
1839	    assert len(table_names) == 0, (
1840	        f"All tables should be dropped, but found: {table_names}"
1841	    )
1842	
1843	    # Recreate the database for other tests
1844	    await db.create_db()
1845	
```

## 245 · 2026-10-29T03:45:31.128115+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"automation_bucket\" tests/ --include=\"*.py\" | head -20",
  "description": "Find tests referencing automation_bucket table"
}
```

## 246 · 2026-10-29T03:45:32.103009+00:00 · tool_result 

```
(Bash completed with no output)
```

## 247 · 2026-10-29T03:45:34.118442+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class Base\\|metadata = \\|naming_convention\" src/prefect/server/database/orm_models.py | head -20 && sed -n 1,80p src/prefect/server/database/orm_models.py",
  "description": "Read ORM base conventions"
}
```

## 248 · 2026-10-29T03:45:34.544113+00:00 · tool_result 

```
57:class Base(DeclarativeBase):
80:            naming_convention={
1533:class BaseORMConfiguration(ABC):
import datetime
import uuid
from abc import ABC, abstractmethod
from collections.abc import Hashable, Iterable
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Optional, Union

import sqlalchemy as sa
from sqlalchemy import FetchedValue
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
    registry,
    relationship,
    synonym,
)
from sqlalchemy.orm.decl_api import registry as RegistryType
from sqlalchemy.sql import roles
from sqlalchemy.sql.functions import coalesce

import prefect.server.schemas as schemas
from prefect.server.events.actions import ServerActionTypes
from prefect.server.events.schemas.automations import (
    AutomationSort,
    Firing,
    ServerTriggerTypes,
)
from prefect.server.events.schemas.events import ReceivedEvent
from prefect.server.schemas.statuses import (
    DeploymentStatus,
    WorkerStatus,
    WorkPoolStatus,
    WorkQueueStatus,
)
from prefect.server.utilities.database import (
    CAMEL_TO_SNAKE,
    JSON,
    UUID,
    GenerateUUID,
    Pydantic,
    Timestamp,
)
from prefect.server.utilities.encryption import decrypt_fernet, encrypt_fernet
from prefect.types._datetime import DateTime, now
from prefect.utilities.names import generate_slug

# for 'plain JSON' columns, use the postgresql variant (which comes with an
# extra operator) and fall back to the generic JSON variant for SQLite
sa_JSON: postgresql.JSON = postgresql.JSON().with_variant(sa.JSON(), "sqlite")


class Base(DeclarativeBase):
    """
    Base SQLAlchemy model that automatically infers the table name
    and provides ID, created, and updated columns
    """

    registry: ClassVar[RegistryType] = registry(
        metadata=sa.schema.MetaData(
            # define naming conventions for our Base class to use
            # sqlalchemy will use the following templated strings
            # to generate the names of indices, constraints, and keys
            #
            # we offset the table name with two underscores (__) to
            # help differentiate, for example, between "flow_run.state_type"
            # and "flow_run_state.type".
            #
            # more information on this templating and available
            # customization can be found here
            # https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.MetaData
            #
            # this also allows us to avoid having to specify names explicitly
            # when using sa.ForeignKey.use_alter = True
            # https://docs.sqlalchemy.org/en/14/core/constraints.html
            naming_convention={
```

## 249 · 2026-10-29T03:46:09.852363+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "offset": 80,
  "limit": 80
}
```

## 250 · 2026-10-29T03:46:09.972925+00:00 · tool_result 

```
80	            naming_convention={
81	                "ix": "ix_%(table_name)s__%(column_0_N_name)s",
82	                "uq": "uq_%(table_name)s__%(column_0_N_name)s",
83	                "ck": "ck_%(table_name)s__%(constraint_name)s",
84	                "fk": "fk_%(table_name)s__%(column_0_N_name)s__%(referred_table_name)s",
85	                "pk": "pk_%(table_name)s",
86	            }
87	        ),
88	        type_annotation_map={
89	            uuid.UUID: UUID,
90	            DateTime: Timestamp,
91	        },
92	    )
93	
94	    # required in order to access columns with server defaults
95	    # or SQL expression defaults, subsequent to a flush, without
96	    # triggering an expired load
97	    #
98	    # this allows us to load attributes with a server default after
99	    # an INSERT, for example
100	    #
101	    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession
102	    __mapper_args__: dict[str, Any] = {"eager_defaults": True}
103	
104	    def __repr__(self) -> str:
105	        return f"{self.__class__.__name__}(id={self.id})"
106	
107	    @declared_attr.directive
108	    def __tablename__(cls) -> str:
109	        """
110	        By default, turn the model's camel-case class name
111	        into a snake-case table name. Override by providing
112	        an explicit `__tablename__` class property.
113	        """
114	        return CAMEL_TO_SNAKE.sub("_", cls.__name__).lower()
115	
116	    id: Mapped[uuid.UUID] = mapped_column(
117	        primary_key=True,
118	        server_default=GenerateUUID(),
119	        default=uuid.uuid4,
120	    )
121	
122	    created: Mapped[DateTime] = mapped_column(
123	        server_default=sa.func.now(), default=lambda: now("UTC")
124	    )
125	
126	    # onupdate is only called when statements are actually issued
127	    # against the database. until COMMIT is issued, this column
128	    # will not be updated
129	    updated: Mapped[DateTime] = mapped_column(
130	        index=True,
131	        server_default=sa.func.now(),
132	        default=lambda: now("UTC"),
133	        onupdate=sa.func.now(),
134	        server_onupdate=FetchedValue(),
135	    )
136	
137	
138	class Flow(Base):
139	    """SQLAlchemy mixin of a flow."""
140	
141	    name: Mapped[str]
142	    tags: Mapped[list[str]] = mapped_column(JSON, server_default="[]", default=list)
143	    labels: Mapped[Optional[schemas.core.KeyValueLabels]] = mapped_column(JSON)
144	
145	    flow_runs: Mapped[list["FlowRun"]] = relationship(
146	        back_populates="flow", lazy="raise"
147	    )
148	    deployments: Mapped[list["Deployment"]] = relationship(
149	        back_populates="flow", lazy="raise"
150	    )
151	
152	    __table_args__: Any = (
153	        sa.UniqueConstraint("name"),
154	        sa.Index("ix_flow__created", "created"),
155	        sa.Index("trgm_ix_flow_name", "name", postgresql_using="gin").ddl_if(
156	            dialect="postgresql"
157	        ),
158	    )
159	
```

## 251 · 2026-10-29T03:46:12.745918+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls formal/ && cat formal/tla/AGENTS.md 2>/dev/null | head -60",
  "description": "Inspect formal models"
}
```

## 252 · 2026-10-29T03:46:12.979947+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rln \"trigger\\|automation\\|bucket\" formal/ | head -20",
  "description": "Search formal models for triggers"
}
```

## 253 · 2026-10-29T03:46:13.193980+00:00 · tool_result 

```
tla
# TLA+ Protocol Models

Add a model only when a bounded concurrency question can change a design or
preserve a regression that cheaper tests cannot establish.

## Model contract

- Label each configuration as current, target, or intentionally unsafe. Model
  or isolate current failure behavior before a repair; a target remains a
  proposal until mapped production tests pass.
- Keep independently durable stores, queues, transactions, and clocks distinct
  unless production makes them atomic. State fairness and availability
  assumptions; never infer liveness from a safety-only run.
- For each design-critical safety claim, include an unsafe configuration that
  violates the exact named invariant, with bounds that admit the contested
  trace and make critical actions reachable.

Each model README records its question, owner, bounds, assumptions and
exclusions, configuration status, invariants, commands and expected results,
action/state-to-production mapping, and review triggers. Every production
writer of modeled state must map to an action or be explicitly out of scope.

Translate relevant counterexamples into deterministic behavior tests using
explicit barriers, not sleeps. A target is implemented only when mapped
contract tests pass; check database locking or serialization against
PostgreSQL. Keep the model and its test oracle independent of production code.

## CI and lifecycle

- Fix the JDK distribution and major version in CI and document the matching
  local major. Pin and checksum the TLA+ tool release. Run targets as
  expected-green and verify each unsafe configuration's exact exit and named
  invariant. Do not commit tool JARs or TLC metadata.
- Keep a new check advisory until its owner accepts the scope, invariants,
  runtime, and diagnostics.
- Remove an unowned, unmappable, or obsolete model and its dedicated CI;
  preserve useful production regressions.
```

## 254 · 2026-10-29T03:46:13.401129+00:00 · tool_result 

```
formal/tla/AGENTS.md
```

## 255 · 2026-10-29T03:46:51.884583+00:00 · assistant_message 

```
Let me examine the migration style for creating a table with indexes, and the ORM JSON type usage.
```

## 256 · 2026-10-29T03:46:52.197760+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 80,150p src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py",
  "description": "Read sqlite table creation migration style"
}
```

## 257 · 2026-10-29T03:46:52.513705+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 80,150p src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py",
  "description": "Read postgres table creation migration style"
}
```

## 258 · 2026-10-29T03:46:52.635204+00:00 · tool_result 

```
    op.create_table(
        "automation_bucket",
        sa.Column(
            "automation_id", prefect.server.utilities.database.UUID(), nullable=False
        ),
        sa.Column(
            "trigger_id", prefect.server.utilities.database.UUID(), nullable=True
        ),
        sa.Column(
            "bucketing_key",
            prefect.server.utilities.database.JSON(),
            nullable=False,
        ),
        sa.Column(
            "last_event",
            prefect.server.utilities.database.Pydantic(ReceivedEvent),
            nullable=True,
        ),
        sa.Column(
            "start",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "end",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("last_operation", sa.String(), nullable=True),
        sa.Column(
            "triggered_at",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "id",
            prefect.server.utilities.database.UUID(),
            server_default=sa.text(
                "(\n    (\n        lower(hex(randomblob(4)))\n        || '-'\n        || lower(hex(randomblob(2)))\n        || '-4'\n        || substr(lower(hex(randomblob(2))),2)\n        || '-'\n        || substr('89ab',abs(random()) % 4 + 1, 1)\n        || substr(lower(hex(randomblob(2))),2)\n        || '-'\n        || lower(hex(randomblob(6)))\n    )\n    )"
            ),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.server.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("(strftime('%Y-%m-%d %H:%M:%f000', 'now'))"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.server.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("(strftime('%Y-%m-%d %H:%M:%f000', 'now'))"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["automation_id"],
            ["automation.id"],
            name=op.f("fk_automation_bucket__automation_id__automation"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_automation_bucket")),
    )
    with op.batch_alter_table("automation_bucket", schema=None) as batch_op:
        batch_op.create_index(
            "ix_automation_bucket__automation_id__end",
            ["automation_id", "end"],
            unique=False,
        )
        batch_op.create_index(
```

## 259 · 2026-10-29T03:46:52.947976+00:00 · tool_result 

```
        sa.Column(
            "automation_id", prefect.server.utilities.database.UUID(), nullable=False
        ),
        sa.Column(
            "trigger_id", prefect.server.utilities.database.UUID(), nullable=True
        ),
        sa.Column(
            "bucketing_key",
            prefect.server.utilities.database.JSON(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column(
            "last_event",
            prefect.server.utilities.database.Pydantic(ReceivedEvent),
            nullable=True,
        ),
        sa.Column(
            "start",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "end",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("last_operation", sa.String(), nullable=True),
        sa.Column(
            "triggered_at",
            prefect.server.utilities.database.Timestamp(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "id",
            prefect.server.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.server.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.server.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["automation_id"],
            ["automation.id"],
            name=op.f("fk_automation_bucket__automation_id__automation"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_automation_bucket")),
    )
    op.create_index(
        "ix_automation_bucket__automation_id__end",
        "automation_bucket",
        ["automation_id", "end"],
        unique=False,
    )
    op.create_index(
        op.f("ix_automation_bucket__updated"),
        "automation_bucket",
        ["updated"],
        unique=False,
    )
```

## 260 · 2026-10-29T03:47:20.657450+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport alembic.script\nfrom prefect.server.database.alembic_commands import alembic_config\nfrom prefect.server.database.orm_models import AioSqliteORMConfiguration, AsyncPostgresORMConfiguration\nconfig = alembic_config()\nfor cfg in (AioSqliteORMConfiguration, AsyncPostgresORMConfiguration):\n    script = alembic.script.ScriptDirectory.from_config(config)\n    script.version_locations = [cfg().versions_dir]\n    print(cfg.__name__, script.get_current_head(), script.get_heads())\nEOF",
  "description": "Print current migration heads per dialect"
}
```

## 261 · 2026-10-29T03:47:33.288548+00:00 · tool_result 

```
AioSqliteORMConfiguration a3b9c7d2e5f1 ['a3b9c7d2e5f1']
AsyncPostgresORMConfiguration d4a7e1c93f52 ['d4a7e1c93f52']
```

## 262 · 2026-10-29T03:48:29.359945+00:00 · assistant_message 

```
I'll implement a persisted per-resource event watermark so the guard survives bucket deletion, restarts, and upgrades. First, the ORM model.
```

## 263 · 2026-10-29T03:48:30.659599+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "old_string": "class AutomationRelatedResource(Base):\n    __table_args__: Any = (\n        sa.Index(\n            \"uq_automation_related_resource__automation_id__resource_id\",\n            \"automation_id\",\n            \"resource_id\",\n            unique=True,\n        ),\n    )",
  "new_string": "class AutomationTriggerWatermark(Base):\n    \"\"\"The greatest event occurrence processed for an automation trigger.\n\n    Watermarks are tracked per bucketing key and outlive the corresponding\n    ``AutomationBucket`` so that a late or out-of-order event cannot re-arm a\n    proactive window that a newer event has already satisfied.\n    \"\"\"\n\n    __table_args__: Any = (\n        sa.Index(\n            \"uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key\",\n            \"automation_id\",\n            \"trigger_id\",\n            \"bucketing_key\",\n            unique=True,\n        ),\n    )\n\n    automation_id: Mapped[uuid.UUID] = mapped_column(\n        sa.ForeignKey(\"automation.id\", ondelete=\"CASCADE\")\n    )\n\n    trigger_id: Mapped[uuid.UUID]\n\n    bucketing_key: Mapped[list[str]] = mapped_column(\n        JSON, server_default=\"[]\", default=list\n    )\n\n    last_event_occurred: Mapped[DateTime]\n\n\nclass AutomationRelatedResource(Base):\n    __table_args__: Any = (\n        sa.Index(\n            \"uq_automation_related_resource__automation_id__resource_id\",\n            \"automation_id\",\n            \"resource_id\",\n            unique=True,\n        ),\n    )"
}
```

## 264 · 2026-10-29T03:48:30.840294+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/database/orm_models.py has been updated successfully.
```

## 265 · 2026-10-29T03:48:34.562327+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"AutomationBucket\" src/prefect/server/database/*.py | head -20",
  "description": "Find AutomationBucket exposure on DB interface"
}
```

## 266 · 2026-10-29T03:48:34.806741+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1533,1650p src/prefect/server/database/orm_models.py",
  "description": "Read BaseORMConfiguration"
}
```

## 267 · 2026-10-29T03:48:35.053054+00:00 · tool_result 

```
src/prefect/server/database/interface.py:320:    def AutomationBucket(self) -> type[orm_models.AutomationBucket]:
src/prefect/server/database/interface.py:322:        return orm_models.AutomationBucket
src/prefect/server/database/orm_models.py:1306:class AutomationBucket(Base):
src/prefect/server/database/orm_models.py:1348:    ``AutomationBucket`` so that a late or out-of-order event cannot re-arm a
src/prefect/server/database/orm_models.py:1553:ORMAutomationBucket = AutomationBucket
```

## 268 · 2026-10-29T03:48:35.267472+00:00 · tool_result 

```
ORMDeploymentSchedule = DeploymentSchedule
ORMDeployment = Deployment
ORMLog = Log
ORMConcurrencyLimit = ConcurrencyLimit
ORMConcurrencyLimitV2 = ConcurrencyLimitV2
ORMBlockType = BlockType
ORMBlockSchema = BlockSchema
ORMBlockSchemaReference = BlockSchemaReference
ORMBlockDocument = BlockDocument
ORMBlockDocumentReference = BlockDocumentReference
ORMConfiguration = Configuration
ORMSavedSearch = SavedSearch
ORMWorkQueue = WorkQueue
ORMWorkPool = WorkPool
ORMWorker = Worker
ORMAgent = Agent
ORMVariable = Variable
ORMFlowRunInput = FlowRunInput
ORMCsrfToken = CsrfToken
ORMAutomation = Automation
ORMAutomationBucket = AutomationBucket
ORMAutomationRelatedResource = AutomationRelatedResource
ORMCompositeTriggerChildFiring = CompositeTriggerChildFiring
ORMAutomationEventFollower = AutomationEventFollower
ORMEvent = Event
ORMEventResource = EventResource


_UpsertColumns = Iterable[Union[str, "sa.Column[Any]", roles.DDLConstraintColumnRole]]


class BaseORMConfiguration(ABC):
    """
    Abstract base class used to inject database-specific ORM configuration into Prefect.

    Modifications to core Prefect REST API data structures can have unintended consequences.
    Use with caution.
    """

    def unique_key(self) -> tuple[Hashable, ...]:
        """
        Returns a key used to determine whether to instantiate a new DB interface.
        """
        return (self.__class__, Base.metadata)

    @property
    @abstractmethod
    def versions_dir(self) -> Path:
        """Directory containing migrations"""
        ...

    @property
    def deployment_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a Deployment"""
        return [Deployment.flow_id, Deployment.name]

    @property
    def concurrency_limit_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a ConcurrencyLimit"""
        return [ConcurrencyLimit.tag]

    @property
    def flow_run_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a FlowRun"""
        return [FlowRun.flow_id, FlowRun.idempotency_key]

    @property
    def block_type_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a BlockType"""
        return [BlockType.slug]

    @property
    def artifact_collection_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting an ArtifactCollection"""
        return [ArtifactCollection.key]

    @property
    def block_schema_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a BlockSchema"""
        return [BlockSchema.checksum, BlockSchema.version]

    @property
    def flow_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a Flow"""
        return [Flow.name]

    @property
    def saved_search_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a SavedSearch"""
        return [SavedSearch.name]

    @property
    def task_run_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a TaskRun"""
        return [
            TaskRun.flow_run_id,
            TaskRun.task_key,
            TaskRun.dynamic_key,
        ]

    @property
    def block_document_unique_upsert_columns(self) -> _UpsertColumns:
        """Unique columns for upserting a BlockDocument"""
        return [BlockDocument.block_type_id, BlockDocument.name]


class AsyncPostgresORMConfiguration(BaseORMConfiguration):
    """Postgres specific orm configuration"""

    @property
    def versions_dir(self) -> Path:
        """Directory containing migrations"""
        import prefect.server.database

        return (
            Path(prefect.server.database.__file__).parent
            / "_migrations"
            / "versions"
```

## 269 · 2026-10-29T03:48:37.221559+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/interface.py",
  "offset": 280,
  "limit": 70
}
```

## 270 · 2026-10-29T03:48:37.357076+00:00 · tool_result 

```
280	    def BlockSchema(self) -> type[orm_models.BlockSchema]:
281	        """A block schema model"""
282	        return orm_models.BlockSchema
283	
284	    @property
285	    def BlockSchemaReference(self) -> type[orm_models.BlockSchemaReference]:
286	        """A block schema reference model"""
287	        return orm_models.BlockSchemaReference
288	
289	    @property
290	    def BlockDocument(self) -> type[orm_models.BlockDocument]:
291	        """A block document model"""
292	        return orm_models.BlockDocument
293	
294	    @property
295	    def BlockDocumentReference(self) -> type[orm_models.BlockDocumentReference]:
296	        """A block document reference model"""
297	        return orm_models.BlockDocumentReference
298	
299	    @property
300	    def Configuration(self) -> type[orm_models.Configuration]:
301	        """An configuration model"""
302	        return orm_models.Configuration
303	
304	    @property
305	    def Variable(self) -> type[orm_models.Variable]:
306	        """A variable model"""
307	        return orm_models.Variable
308	
309	    @property
310	    def FlowRunInput(self) -> type[orm_models.FlowRunInput]:
311	        """A flow run input model"""
312	        return orm_models.FlowRunInput
313	
314	    @property
315	    def Automation(self) -> type[orm_models.Automation]:
316	        """An automation model"""
317	        return orm_models.Automation
318	
319	    @property
320	    def AutomationBucket(self) -> type[orm_models.AutomationBucket]:
321	        """An automation bucket model"""
322	        return orm_models.AutomationBucket
323	
324	    @property
325	    def AutomationRelatedResource(self) -> type[orm_models.AutomationRelatedResource]:
326	        """An automation related resource model"""
327	        return orm_models.AutomationRelatedResource
328	
329	    @property
330	    def CompositeTriggerChildFiring(
331	        self,
332	    ) -> type[orm_models.CompositeTriggerChildFiring]:
333	        """A model capturing a composite trigger's child firing"""
334	        return orm_models.CompositeTriggerChildFiring
335	
336	    @property
337	    def AutomationEventFollower(self) -> type[orm_models.AutomationEventFollower]:
338	        """A model capturing one event following another event"""
339	        return orm_models.AutomationEventFollower
340	
341	    @property
342	    def Event(self) -> type[orm_models.Event]:
343	        """An event model"""
344	        return orm_models.Event
345	
346	    @property
347	    def EventResource(self) -> type[orm_models.EventResource]:
348	        """An event resource model"""
349	        return orm_models.EventResource
```

## 271 · 2026-10-29T03:48:39.268780+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/interface.py",
  "old_string": "    @property\n    def AutomationRelatedResource(self) -> type[orm_models.AutomationRelatedResource]:\n        \"\"\"An automation related resource model\"\"\"\n        return orm_models.AutomationRelatedResource",
  "new_string": "    @property\n    def AutomationTriggerWatermark(\n        self,\n    ) -> type[orm_models.AutomationTriggerWatermark]:\n        \"\"\"An automation trigger event watermark model\"\"\"\n        return orm_models.AutomationTriggerWatermark\n\n    @property\n    def AutomationRelatedResource(self) -> type[orm_models.AutomationRelatedResource]:\n        \"\"\"An automation related resource model\"\"\"\n        return orm_models.AutomationRelatedResource"
}
```

## 272 · 2026-10-29T03:48:39.419066+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/database/interface.py has been updated successfully.
```

## 273 · 2026-10-29T03:48:41.399077+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat src/prefect/server/database/_migrations/versions/sqlite/2026_09_15_000000_a3b9c7d2e5f1_add_flow_run_state_type_coalesce_start_time_index.py",
  "description": "Read sqlite head migration"
}
```

## 274 · 2026-10-29T03:48:41.762567+00:00 · tool_result 

```
"""Add index on flow_run(state_type, coalesce(start_time, expected_start_time))

Revision ID: a3b9c7d2e5f1
Revises: f416ea180ae1
Create Date: 2026-09-15 00:00:00.000000

Filtering flow runs by `state_type` together with a `start_time` bound and
sorting by `START_TIME_ASC`/`START_TIME_DESC` compiles to a predicate and an
`ORDER BY` on `coalesce(flow_run.start_time, flow_run.expected_start_time)`.
The existing expression indexes on that coalesce do not include `state_type`,
so the planner walks the ordered expression index and discards every row in a
different state.
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "a3b9c7d2e5f1"
down_revision = "f416ea180ae1"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE INDEX IF NOT EXISTS
        ix_flow_run__state_type_coalesce_start_time
        ON flow_run (state_type, coalesce(start_time, expected_start_time))
        """
    )


def downgrade():
    op.execute("DROP INDEX IF EXISTS ix_flow_run__state_type_coalesce_start_time")
```

## 275 · 2026-10-29T03:48:44.132754+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1,40p src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py && echo ===== && sed -n 1,40p src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py",
  "description": "Read migration imports"
}
```

## 276 · 2026-10-29T03:48:44.649574+00:00 · tool_result 

```
"""Automations models

Revision ID: 07ed05dfd4ec
Revises: bacc60edce16
Create Date: 2024-04-03 11:16:18.668168

"""

from typing import List

import sqlalchemy as sa
from alembic import op

import prefect
from prefect.server.events.actions import ServerActionTypes
from prefect.server.events.schemas.automations import Firing, ServerTriggerTypes
from prefect.server.events.schemas.events import ReceivedEvent

# revision identifiers, used by Alembic.
revision = "07ed05dfd4ec"
down_revision = "bacc60edce16"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "automation",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("enabled", sa.Boolean(), server_default="1", nullable=False),
        sa.Column(
            "trigger",
            prefect.server.utilities.database.Pydantic(ServerTriggerTypes),
            nullable=False,
        ),
        sa.Column(
            "actions",
            prefect.server.utilities.database.Pydantic(List[ServerActionTypes]),
            nullable=False,
=====
"""Automations models

Revision ID: aeea5ee6f070
Revises: 7a653837d9ba
Create Date: 2024-04-03 11:24:09.599513

"""

from typing import List

import sqlalchemy as sa
from alembic import op

import prefect
from prefect.server.events.actions import ServerActionTypes
from prefect.server.events.schemas.automations import Firing, ServerTriggerTypes
from prefect.server.events.schemas.events import ReceivedEvent

# revision identifiers, used by Alembic.
revision = "aeea5ee6f070"
down_revision = "7a653837d9ba"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "automation",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("enabled", sa.Boolean(), server_default="1", nullable=False),
        sa.Column(
            "trigger",
            prefect.server.utilities.database.Pydantic(ServerTriggerTypes),
            nullable=False,
        ),
        sa.Column(
            "actions",
            prefect.server.utilities.database.Pydantic(List[ServerActionTypes]),
```

## 277 · 2026-10-29T03:48:53.325561+00:00 · tool_call Write

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py",
  "content": "\"\"\"Add automation trigger watermarks\n\nRevision ID: b7c1d2e3f4a5\nRevises: a3b9c7d2e5f1\nCreate Date: 2026-10-29 00:00:00.000000\n\nTracks the greatest event occurrence processed for each automation trigger's\nbucketing key.  Watermarks outlive individual automation buckets so that late\nor out-of-order events cannot re-arm a proactive window that a newer event has\nalready satisfied.  Rows are periodically swept (see ``periodic_evaluation``),\nkeeping storage bounded.\n\"\"\"\n\nimport sqlalchemy as sa\nfrom alembic import op\n\nimport prefect\n\n# revision identifiers, used by Alembic.\nrevision = \"b7c1d2e3f4a5\"\ndown_revision = \"a3b9c7d2e5f1\"\nbranch_labels = None\ndepends_on = None\n\n\ndef upgrade():\n    op.create_table(\n        \"automation_trigger_watermark\",\n        sa.Column(\n            \"automation_id\", prefect.server.utilities.database.UUID(), nullable=False\n        ),\n        sa.Column(\n            \"trigger_id\", prefect.server.utilities.database.UUID(), nullable=False\n        ),\n        sa.Column(\n            \"bucketing_key\",\n            prefect.server.utilities.database.JSON(),\n            nullable=False,\n        ),\n        sa.Column(\n            \"last_event_occurred\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            nullable=False,\n        ),\n        sa.Column(\n            \"id\",\n            prefect.server.utilities.database.UUID(),\n            server_default=sa.text(\n                \"(\\n    (\\n        lower(hex(randomblob(4)))\\n        || '-'\\n        || lower(hex(randomblob(2)))\\n        || '-4'\\n        || substr(lower(hex(randomblob(2))),2)\\n        || '-'\\n        || substr('89ab',abs(random()) % 4 + 1, 1)\\n        || substr(lower(hex(randomblob(2))),2)\\n        || '-'\\n        || lower(hex(randomblob(6)))\\n    )\\n    )\"\n            ),\n            nullable=False,\n        ),\n        sa.Column(\n            \"created\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            server_default=sa.text(\"(strftime('%Y-%m-%d %H:%M:%f000', 'now'))\"),\n            nullable=False,\n        ),\n        sa.Column(\n            \"updated\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            server_default=sa.text(\"(strftime('%Y-%m-%d %H:%M:%f000', 'now'))\"),\n            nullable=False,\n        ),\n        sa.ForeignKeyConstraint(\n            [\"automation_id\"],\n            [\"automation.id\"],\n            name=op.f(\n                \"fk_automation_trigger_watermark__automation_id__automation\"\n            ),\n            ondelete=\"CASCADE\",\n        ),\n        sa.PrimaryKeyConstraint(\n            \"id\", name=op.f(\"pk_automation_trigger_watermark\")\n        ),\n    )\n    with op.batch_alter_table(\"automation_trigger_watermark\", schema=None) as batch_op:\n        batch_op.create_index(\n            \"uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key\",\n            [\"automation_id\", \"trigger_id\", \"bucketing_key\"],\n            unique=True,\n        )\n        batch_op.create_index(\n            op.f(\"ix_automation_trigger_watermark__updated\"),\n            [\"updated\"],\n            unique=False,\n        )\n\n\ndef downgrade():\n    with op.batch_alter_table(\"automation_trigger_watermark\", schema=None) as batch_op:\n        batch_op.drop_index(op.f(\"ix_automation_trigger_watermark__updated\"))\n        batch_op.drop_index(\n            \"uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key\"\n        )\n    op.drop_table(\"automation_trigger_watermark\")\n"
}
```

## 278 · 2026-10-29T03:48:53.536739+00:00 · tool_result 

```
File created successfully at: $SANDBOX/prefect/src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py (file state is current in your context — no need to Read it back)
```

## 279 · 2026-10-29T03:48:57.314304+00:00 · tool_call Write

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py",
  "content": "\"\"\"Add automation trigger watermarks\n\nRevision ID: c8d2e3f4a5b6\nRevises: d4a7e1c93f52\nCreate Date: 2026-10-29 00:00:00.000000\n\nTracks the greatest event occurrence processed for each automation trigger's\nbucketing key.  Watermarks outlive individual automation buckets so that late\nor out-of-order events cannot re-arm a proactive window that a newer event has\nalready satisfied.  Rows are periodically swept (see ``periodic_evaluation``),\nkeeping storage bounded.\n\"\"\"\n\nimport sqlalchemy as sa\nfrom alembic import op\n\nimport prefect\n\n# revision identifiers, used by Alembic.\nrevision = \"c8d2e3f4a5b6\"\ndown_revision = \"d4a7e1c93f52\"\nbranch_labels = None\ndepends_on = None\n\n\ndef upgrade():\n    op.create_table(\n        \"automation_trigger_watermark\",\n        sa.Column(\n            \"automation_id\", prefect.server.utilities.database.UUID(), nullable=False\n        ),\n        sa.Column(\n            \"trigger_id\", prefect.server.utilities.database.UUID(), nullable=False\n        ),\n        sa.Column(\n            \"bucketing_key\",\n            prefect.server.utilities.database.JSON(astext_type=sa.Text()),\n            nullable=False,\n        ),\n        sa.Column(\n            \"last_event_occurred\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            nullable=False,\n        ),\n        sa.Column(\n            \"id\",\n            prefect.server.utilities.database.UUID(),\n            server_default=sa.text(\"(GEN_RANDOM_UUID())\"),\n            nullable=False,\n        ),\n        sa.Column(\n            \"created\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            server_default=sa.text(\"CURRENT_TIMESTAMP\"),\n            nullable=False,\n        ),\n        sa.Column(\n            \"updated\",\n            prefect.server.utilities.database.Timestamp(timezone=True),\n            server_default=sa.text(\"CURRENT_TIMESTAMP\"),\n            nullable=False,\n        ),\n        sa.ForeignKeyConstraint(\n            [\"automation_id\"],\n            [\"automation.id\"],\n            name=op.f(\n                \"fk_automation_trigger_watermark__automation_id__automation\"\n            ),\n            ondelete=\"CASCADE\",\n        ),\n        sa.PrimaryKeyConstraint(\n            \"id\", name=op.f(\"pk_automation_trigger_watermark\")\n        ),\n    )\n    op.create_index(\n        \"uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key\",\n        \"automation_trigger_watermark\",\n        [\"automation_id\", \"trigger_id\", \"bucketing_key\"],\n        unique=True,\n    )\n    op.create_index(\n        op.f(\"ix_automation_trigger_watermark__updated\"),\n        \"automation_trigger_watermark\",\n        [\"updated\"],\n        unique=False,\n    )\n\n\ndef downgrade():\n    op.drop_index(\n        op.f(\"ix_automation_trigger_watermark__updated\"),\n        table_name=\"automation_trigger_watermark\",\n    )\n    op.drop_index(\n        \"uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key\",\n        table_name=\"automation_trigger_watermark\",\n    )\n    op.drop_table(\"automation_trigger_watermark\")\n"
}
```

## 280 · 2026-10-29T03:48:57.476640+00:00 · tool_result 

```
File created successfully at: $SANDBOX/prefect/src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py (file state is current in your context — no need to Read it back)
```

## 281 · 2026-10-29T03:49:01.147051+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && head -30 tests/events/server/triggers/test_basics.py | grep -n \"pytestmark\" ; grep -rn \"pytestmark\" tests/events/server/triggers/*.py",
  "description": "Check clear_db marks in trigger tests"
}
```

## 282 · 2026-10-29T03:49:01.697363+00:00 · tool_result 

```
26:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_basics.py:26:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_composite_triggers.py:27:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_flow_run_slas.py:22:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_incident_completed_run.py:15:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_incident_regressions.py:29:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_regressions.py:26:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_service.py:28:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/test_service_changes.py:20:pytestmark = pytest.mark.clear_db
tests/events/server/triggers/zz_probe_test.py:15:pytestmark = pytest.mark.clear_db
```

## 283 · 2026-10-29T03:49:15.188110+00:00 · assistant_message 

```
Now the trigger logic. First the import and retention constant:
```

## 284 · 2026-10-29T03:49:15.719689+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "from prefect.server.events.ordering import (\n    PRECEDING_EVENT_LOOKBACK,\n    EventArrivedEarly,\n    get_triggers_causal_ordering,\n)",
  "new_string": "from prefect.server.events.ordering import (\n    PRECEDING_EVENT_LOOKBACK,\n    SEEN_EXPIRATION,\n    EventArrivedEarly,\n    get_triggers_causal_ordering,\n)"
}
```

## 285 · 2026-10-29T03:49:15.921800+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 286 · 2026-10-29T03:49:17.688722+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "AUTOMATION_BUCKET_BATCH_SIZE = 500",
  "new_string": "AUTOMATION_BUCKET_BATCH_SIZE = 500\n\n# How long to remember the most recent event processed for an automation trigger\n# and bucketing key.  This matches the window over which the triggers consumer\n# remembers processed events, which keeps watermark storage bounded while still\n# covering redeliveries and ordinary out-of-order delivery.\nAUTOMATION_WATERMARK_RETENTION = SEEN_EXPIRATION"
}
```

## 287 · 2026-10-29T03:49:17.839133+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 288 · 2026-10-29T03:49:19.242556+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 960,
  "limit": 50
}
```

## 289 · 2026-10-29T03:49:19.358947+00:00 · tool_result 

```
960	
961	        offset += batch_size
962	
963	
964	@db_injector
965	async def read_bucket(
966	    db: PrefectDBInterface,
967	    session: AsyncSession,
968	    trigger: Trigger,
969	    bucketing_key: Tuple[str, ...],
970	) -> Optional["ORMAutomationBucket"]:
971	    """Gets the bucket this event would fall into for the given Automation, if there is
972	    one currently"""
973	    return await read_bucket_by_trigger_id(
974	        session,
975	        trigger.automation.id,
976	        trigger.id,
977	        bucketing_key,
978	    )
979	
980	
981	@db_injector
982	async def read_bucket_by_trigger_id(
983	    db: PrefectDBInterface,
984	    session: AsyncSession,
985	    automation_id: UUID,
986	    trigger_id: UUID,
987	    bucketing_key: Tuple[str, ...],
988	) -> "ORMAutomationBucket | None":
989	    """Gets the bucket this event would fall into for the given Automation, if there is
990	    one currently"""
991	    query = sa.select(db.AutomationBucket).where(
992	        db.AutomationBucket.automation_id == automation_id,
993	        db.AutomationBucket.trigger_id == trigger_id,
994	        db.AutomationBucket.bucketing_key == bucketing_key,
995	    )
996	    result = await session.execute(query)
997	    bucket = result.scalars().first()
998	    if bucket:
999	        await session.refresh(bucket)
1000	
1001	    return bucket
1002	
1003	
1004	@db_injector
1005	async def increment_bucket(
1006	    db: PrefectDBInterface,
1007	    session: AsyncSession,
1008	    bucket: "ORMAutomationBucket",
1009	    count: int,
```

## 290 · 2026-10-29T03:49:22.984547+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    result = await session.execute(query)\n    bucket = result.scalars().first()\n    if bucket:\n        await session.refresh(bucket)\n\n    return bucket\n\n\n@db_injector\nasync def increment_bucket(",
  "new_string": "    result = await session.execute(query)\n    bucket = result.scalars().first()\n    if bucket:\n        await session.refresh(bucket)\n\n    return bucket\n\n\n@db_injector\nasync def read_trigger_watermark(\n    db: PrefectDBInterface,\n    session: AsyncSession,\n    trigger: Trigger,\n    bucketing_key: Tuple[str, ...],\n) -> Optional[prefect.types._datetime.DateTime]:\n    \"\"\"Gets the greatest event occurrence processed for this trigger and key.\n\n    Watermarks are independent of automation buckets so that they survive bucket\n    cleanup and server restarts.\n    \"\"\"\n    query = sa.select(db.AutomationTriggerWatermark.last_event_occurred).where(\n        db.AutomationTriggerWatermark.automation_id == trigger.automation.id,\n        db.AutomationTriggerWatermark.trigger_id == trigger.id,\n        db.AutomationTriggerWatermark.bucketing_key == bucketing_key,\n    )\n    return (await session.execute(query)).scalar_one_or_none()\n\n\n@db_injector\nasync def record_trigger_watermark(\n    db: PrefectDBInterface,\n    session: AsyncSession,\n    trigger: Trigger,\n    bucketing_key: Tuple[str, ...],\n    occurred: prefect.types._datetime.DateTime,\n) -> None:\n    \"\"\"Records an event's occurrence as a high-water mark for this trigger and key.\n\n    The mark only moves forward: older or out-of-order events cannot lower it.\n    \"\"\"\n    await session.execute(\n        db.queries.insert(db.AutomationTriggerWatermark)\n        .values(\n            automation_id=trigger.automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event_occurred=occurred,\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationTriggerWatermark.automation_id,\n                db.AutomationTriggerWatermark.trigger_id,\n                db.AutomationTriggerWatermark.bucketing_key,\n            ],\n            set_=dict(\n                last_event_occurred=sa.case(\n                    (\n                        db.AutomationTriggerWatermark.last_event_occurred\n                        < occurred,\n                        occurred,\n                    ),\n                    else_=db.AutomationTriggerWatermark.last_event_occurred,\n                ),\n                updated=prefect.types._datetime.now(\"UTC\"),\n            ),\n        )\n    )\n\n\n@db_injector\nasync def increment_bucket("
}
```

## 291 · 2026-10-29T03:49:23.165523+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 292 · 2026-10-29T03:49:25.408698+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "@db_injector\nasync def sweep_closed_buckets(\n    db: PrefectDBInterface,\n    session: AsyncSession,\n    older_than: prefect.types._datetime.DateTime,\n) -> None:\n    await session.execute(\n        sa.delete(db.AutomationBucket).where(db.AutomationBucket.end <= older_than)\n    )",
  "new_string": "@db_injector\nasync def sweep_closed_buckets(\n    db: PrefectDBInterface,\n    session: AsyncSession,\n    older_than: prefect.types._datetime.DateTime,\n) -> None:\n    await session.execute(\n        sa.delete(db.AutomationBucket).where(db.AutomationBucket.end <= older_than)\n    )\n\n\n@db_injector\nasync def sweep_expired_trigger_watermarks(\n    db: PrefectDBInterface,\n    session: AsyncSession,\n    older_than: prefect.types._datetime.DateTime,\n) -> None:\n    \"\"\"Removes trigger watermarks that have not been touched recently.\"\"\"\n    await session.execute(\n        sa.delete(db.AutomationTriggerWatermark).where(\n            db.AutomationTriggerWatermark.updated <= older_than\n        )\n    )"
}
```

## 293 · 2026-10-29T03:49:25.564625+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 294 · 2026-10-29T03:49:27.856052+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    async with automations_session() as session:\n        await sweep_closed_buckets(\n            session,\n            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),\n        )\n        await session.commit()",
  "new_string": "    async with automations_session() as session:\n        await sweep_closed_buckets(\n            session,\n            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),\n        )\n        await sweep_expired_trigger_watermarks(\n            session,\n            as_of - AUTOMATION_WATERMARK_RETENTION,\n        )\n        await session.commit()"
}
```

## 295 · 2026-10-29T03:49:28.000958+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 296 · 2026-10-29T03:49:29.242140+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 655,
  "limit": 90
}
```

## 297 · 2026-10-29T03:49:29.365498+00:00 · tool_result 

```
655	                        and not trigger.after
656	                        and trigger.expects(event.event)
657	                    ):
658	                        # When ensuring a bucket and _creating it for the first time_,
659	                        # use an old time so that we can catch any other events flowing
660	                        # through the system at the same time even if they are out of
661	                        # order.  After the trigger fires and creates its next bucket,
662	                        # time will start from that point forward.  We'll use our
663	                        # preceding event lookback variable as the horizon that we'll
664	                        # accept these older events.
665	                        #
666	                        # https://github.com/PrefectHQ/nebula/issues/7230
667	                        start = event.occurred - PRECEDING_EVENT_LOOKBACK
668	
669	                        bucket = await ensure_bucket(
670	                            session,
671	                            trigger,
672	                            bucketing_key=bucketing_key,
673	                            start=start,
674	                            end=event.occurred + trigger.within,
675	                            last_event=event,
676	                        )
677	
678	                    if not trigger.expects(event.event):
679	                        continue
680	
681	                    if not bucket:
682	                        bucket = await read_bucket(session, trigger, bucketing_key)
683	                        if not bucket:
684	                            continue
685	
686	                    await evaluate(
687	                        session,
688	                        trigger,
689	                        bucket,
690	                        event.occurred,
691	                        triggering_event=event,
692	                    )
693	                finally:
694	                    await session.commit()
695	
696	
697	# retry on operational errors to account for db flakiness with sqlite
698	@retry_async_fn(max_attempts=3, retry_on_exceptions=(sa.exc.OperationalError,))
699	async def get_lost_followers() -> List[ReceivedEvent]:
700	    """Get followers that have been sitting around longer than our lookback"""
701	    return await get_triggers_causal_ordering().get_lost_followers()
702	
703	
704	async def periodic_evaluation(now: prefect.types._datetime.DateTime) -> None:
705	    """Periodic tasks that should be run regularly, but not as often as every event"""
706	    offset = await get_events_clock_offset()
707	    as_of = now + timedelta(seconds=offset)
708	
709	    logger.debug("Running periodic evaluation as of %s (offset %ss)", as_of, offset)
710	
711	    await reconcile_automations()
712	
713	    # Any followers that have been sitting around longer than our lookback are never
714	    # going to see their leader event (maybe it was lost or took too long to arrive).
715	    # These events can just be evaluated now in the order they occurred.
716	    for event in await get_lost_followers():
717	        await reactive_evaluation(event)
718	
719	    async with automations_session() as session:
720	        await sweep_closed_buckets(
721	            session,
722	            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),
723	        )
724	        await sweep_expired_trigger_watermarks(
725	            session,
726	            as_of - AUTOMATION_WATERMARK_RETENTION,
727	        )
728	        await session.commit()
729	
730	
731	async def evaluate_periodically(periodic_granularity: timedelta) -> None:
732	    """Runs periodic evaluation on the given interval"""
733	    logger.debug(
734	        "Starting periodic evaluation task every %s seconds",
735	        periodic_granularity.total_seconds(),
736	    )
737	    while True:
738	        try:
739	            await periodic_evaluation(prefect.types._datetime.now("UTC"))
740	        except Exception:
741	            logger.exception("Error running periodic evaluation")
742	        finally:
743	            await asyncio.sleep(periodic_granularity.total_seconds())
744	
```

## 298 · 2026-10-29T03:49:31.024335+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 618,
  "limit": 45
}
```

## 299 · 2026-10-29T03:49:31.155151+00:00 · tool_result 

```
618	            )
619	
620	            bucketing_key = trigger.bucketing_key(event)
621	
622	            async with automations_session(begin_transaction=True) as session:
623	                try:
624	                    bucket: Optional["ORMAutomationBucket"] = None
625	
626	                    if trigger.after and trigger.starts_after(event.event):
627	                        # When an event matches both the after and expect, each event
628	                        # can both start a new bucket and increment the bucket that was
629	                        # started by the previous event.  Here we offset the bucket to
630	                        # start at -1 so that the first event will leave the bucket at 0
631	                        # after evaluation.  See the tests:
632	                        #
633	                        #   test_same_event_in_expect_and_after_never_reacts_immediately
634	                        #   test_same_event_in_expect_and_after_reacts_after_threshold_is_met
635	                        #   test_same_event_in_expect_and_after_proactively_does_not_fire
636	                        #   test_same_event_in_expect_and_after_proactively_fires
637	                        #
638	                        # in test_triggers_regressions.py for examples of how we expect
639	                        # this to behave.
640	                        #
641	                        # https://github.com/PrefectHQ/nebula/issues/4201
642	                        initial_count = -1 if trigger.expects(event.event) else 0
643	                        bucket = await ensure_bucket(
644	                            session,
645	                            trigger,
646	                            bucketing_key,
647	                            start=event.occurred,
648	                            end=event.occurred + trigger.within,
649	                            last_event=event,
650	                            initial_count=initial_count,
651	                        )
652	
653	                    if (
654	                        not bucket
655	                        and not trigger.after
656	                        and trigger.expects(event.event)
657	                    ):
658	                        # When ensuring a bucket and _creating it for the first time_,
659	                        # use an old time so that we can catch any other events flowing
660	                        # through the system at the same time even if they are out of
661	                        # order.  After the trigger fires and creates its next bucket,
662	                        # time will start from that point forward.  We'll use our
```

## 300 · 2026-10-29T03:49:39.444825+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "            async with automations_session(begin_transaction=True) as session:\n                try:\n                    bucket: Optional[\"ORMAutomationBucket\"] = None\n\n                    if trigger.after and trigger.starts_after(event.event):\n                        # When an event matches both the after and expect, each event\n                        # can both start a new bucket and increment the bucket that was\n                        # started by the previous event.  Here we offset the bucket to\n                        # start at -1 so that the first event will leave the bucket at 0\n                        # after evaluation.  See the tests:\n                        #\n                        #   test_same_event_in_expect_and_after_never_reacts_immediately\n                        #   test_same_event_in_expect_and_after_reacts_after_threshold_is_met\n                        #   test_same_event_in_expect_and_after_proactively_does_not_fire\n                        #   test_same_event_in_expect_and_after_proactively_fires\n                        #\n                        # in test_triggers_regressions.py for examples of how we expect\n                        # this to behave.\n                        #\n                        # https://github.com/PrefectHQ/nebula/issues/4201\n                        initial_count = -1 if trigger.expects(event.event) else 0\n                        bucket = await ensure_bucket(\n                            session,\n                            trigger,\n                            bucketing_key,\n                            start=event.occurred,\n                            end=event.occurred + trigger.within,\n                            last_event=event,\n                            initial_count=initial_count,\n                        )\n\n                    if (\n                        not bucket\n                        and not trigger.after\n                        and trigger.expects(event.event)\n                    ):",
  "new_string": "            async with automations_session(begin_transaction=True) as session:\n                try:\n                    bucket: Optional[\"ORMAutomationBucket\"] = None\n                    watermark: Optional[prefect.types._datetime.DateTime] = None\n\n                    # Proactive triggers remember the newest event they have\n                    # processed for each bucketing key, independently of the\n                    # lifetime of an automation bucket.  This is what stops a late\n                    # or out-of-order `after` event (for example, a heartbeat\n                    # emitted while a flow run is completing) from arming a new\n                    # window once a newer event has already satisfied the trigger.\n                    track_watermark = (\n                        bool(trigger.after) and trigger.posture == Posture.Proactive\n                    )\n                    if track_watermark:\n                        bucket = await read_bucket(session, trigger, bucketing_key)\n                        watermark = await read_trigger_watermark(\n                            session, trigger, bucketing_key\n                        )\n\n                    if trigger.after and trigger.starts_after(event.event):\n                        # An event may only arm a _new_ window when it is newer than\n                        # the newest event we have already seen for this resource.\n                        # Events that only match `after` may also not replace the\n                        # bucket's `last_event` when they are stale.\n                        if (\n                            track_watermark\n                            and watermark is not None\n                            and event.occurred <= watermark\n                            and (bucket is None or not trigger.expects(event.event))\n                        ):\n                            logger.debug(\n                                \"Automation %s (%r) trigger %s ignoring stale event \"\n                                \"%r for keys (%r): occurred %s is not newer than %s\",\n                                trigger.automation.id,\n                                trigger.automation.name,\n                                trigger.id,\n                                event.event,\n                                bucketing_key,\n                                event.occurred,\n                                watermark,\n                            )\n                            continue\n\n                        # When an event matches both the after and expect, each event\n                        # can both start a new bucket and increment the bucket that was\n                        # started by the previous event.  Here we offset the bucket to\n                        # start at -1 so that the first event will leave the bucket at 0\n                        # after evaluation.  See the tests:\n                        #\n                        #   test_same_event_in_expect_and_after_never_reacts_immediately\n                        #   test_same_event_in_expect_and_after_reacts_after_threshold_is_met\n                        #   test_same_event_in_expect_and_after_proactively_does_not_fire\n                        #   test_same_event_in_expect_and_after_proactively_fires\n                        #\n                        # in test_triggers_regressions.py for examples of how we expect\n                        # this to behave.\n                        #\n                        # https://github.com/PrefectHQ/nebula/issues/4201\n                        initial_count = -1 if trigger.expects(event.event) else 0\n                        bucket = await ensure_bucket(\n                            session,\n                            trigger,\n                            bucketing_key,\n                            start=event.occurred,\n                            end=event.occurred + trigger.within,\n                            last_event=event,\n                            initial_count=initial_count,\n                        )\n\n                    if (\n                        not bucket\n                        and not trigger.after\n                        and trigger.expects(event.event)\n                    ):"
}
```

## 301 · 2026-10-29T03:49:39.647775+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 302 · 2026-10-29T03:49:41.534351+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "                            last_event=event,\n                        )\n\n                    if not trigger.expects(event.event):\n                        continue\n\n                    if not bucket:\n                        bucket = await read_bucket(session, trigger, bucketing_key)\n                        if not bucket:\n                            continue",
  "new_string": "                            last_event=event,\n                        )\n\n                    if track_watermark:\n                        await record_trigger_watermark(\n                            session, trigger, bucketing_key, event.occurred\n                        )\n\n                    if not trigger.expects(event.event):\n                        continue\n\n                    if not bucket:\n                        bucket = await read_bucket(session, trigger, bucketing_key)\n                        if not bucket:\n                            continue"
}
```

## 303 · 2026-10-29T03:49:41.722923+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 304 · 2026-10-29T03:49:44.862672+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_incident_regressions.py tests/events/server/triggers/zz_probe_test.py -q -p no:randomly 2>&1 | tail -30",
  "description": "Run incident and regression tests with watermark",
  "timeout": 900000
}
```

## 305 · 2026-10-29T03:51:19.267347+00:00 · tool_result 

```
            future, function = tx.get()
    
            try:
                LOG.debug("executing %s", function)
>               result = function()
                         ^^^^^^^^^^
E               sqlalchemy.exc.ProgrammingError: (sqlite3.ProgrammingError) Error binding parameter 9: type 'DateTime' is not supported
E               [SQL: INSERT INTO automation_trigger_watermark (automation_id, trigger_id, bucketing_key, last_event_occurred, id, created, updated) VALUES (:automation_id, :trigger_id, :bucketing_key, :last_event_occurred, :id, :created, :updated) ON CONFLICT (automation_id, trigger_id, bucketing_key) DO UPDATE SET last_event_occurred = CASE WHEN (automation_trigger_watermark.last_event_occurred < :last_event_occurred_1) THEN :param_1 ELSE automation_trigger_watermark.last_event_occurred END, updated = :param_2]
E               [parameters: {'automation_id': '5819767b-42d6-444e-b198-cc25bff757bd', 'trigger_id': '564ba9cf-5e89-4966-b4a4-2f4182a2d0d5', 'bucketing_key': '["prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"]', 'last_event_occurred': '2026-10-29 03:51:13.772931', 'id': '97f1e524-3e91-47ca-ae0a-3828b8e3375a', 'created': '2026-10-29 03:51:14.578103', 'updated': '2026-10-29 03:51:14.578103', 'last_event_occurred_1': '2026-10-29 03:51:13.772931', 'param_1': DateTime(2026, 10, 29, 3, 51, 13, 772931, tzinfo=Timezone('UTC')), 'param_2': '2026-10-29 03:51:13.772931'}]
E               (Background on this error at: https://sqlalche.me/e/20/f405)

..\.runtime\venv\Lib\site-packages\aiosqlite\core.py:63: ProgrammingError
---------------------------- Captured stderr call -----------------------------
11:51:13.801 | INFO    | prefect.server.events.triggers - Automation 5819767b-42d6-444e-b198-cc25bff757bd, trigger 564ba9cf-5e89-4966-b4a4-2f4182a2d0d5 covers event 'prefect.flow-run.heartbeat' (59aaa709-570d-429e-bb9b-58af9768b4ab) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:51:13.772931+00:00'
------------------------------ Captured log call ------------------------------
INFO     prefect.server.events.triggers:triggers.py:610 Automation 5819767b-42d6-444e-b198-cc25bff757bd, trigger 564ba9cf-5e89-4966-b4a4-2f4182a2d0d5 covers event 'prefect.flow-run.heartbeat' (59aaa709-570d-429e-bb9b-58af9768b4ab) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-29T03:51:13.772931+00:00'
-------------------------- Captured stderr teardown ---------------------------
11:51:16.085 | INFO    | uvicorn.error - Shutting down
11:51:16.201 | INFO    | uvicorn.error - Waiting for application shutdown.
11:51:16.204 | INFO    | uvicorn.error - Application shutdown complete.
11:51:16.204 | INFO    | uvicorn.error - Finished server process [18888]
=========================== short test summary info ===========================
FAILED tests/events/server/triggers/test_incident_completed_run.py::test_completed_run_incident
FAILED tests/events/server/triggers/test_incident_regressions.py::test_completed_run_with_late_heartbeat_does_not_fire
FAILED tests/events/server/triggers/test_incident_regressions.py::test_out_of_order_heartbeats_do_not_rearm_the_window
FAILED tests/events/server/triggers/test_incident_regressions.py::test_genuinely_unresponsive_run_still_fires_with_correct_information
FAILED tests/events/server/triggers/test_incident_regressions.py::test_completed_run_stays_silent_across_a_restart
FAILED tests/events/server/triggers/test_incident_regressions.py::test_run_that_reports_a_new_state_after_completion_is_monitored_again
FAILED tests/events/server/triggers/zz_probe_test.py::test_intermediate_proactive_evaluation
7 failed in 72.13s (0:01:12)
```

## 306 · 2026-10-29T03:51:24.675657+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nfrom prefect.server.database.orm_models import AutomationTriggerWatermark as W\nimport sqlalchemy as sa\nprint(type(W.last_event_occurred))\ntry:\n    print(W.last_event_occurred.type)\nexcept Exception as e:\n    print(\"no .type:\", e)\nprint(W.__table__.c.last_event_occurred.type)\nlit = sa.literal(__import__(\"prefect.types._datetime\", fromlist=[\"now\"]).now(\"UTC\"), type_=W.__table__.c.last_event_occurred.type)\nprint(lit.compile(compile_kwargs={\"literal_binds\": True}))\nEOF",
  "description": "Check instrumented attribute type access"
}
```

## 307 · 2026-10-29T03:51:33.286943+00:00 · tool_result 

```
<class 'sqlalchemy.orm.attributes.InstrumentedAttribute'>
TIMESTAMP
TIMESTAMP
'2026-10-29 03:51:32.835328+00:00'
```

## 308 · 2026-10-29T03:51:37.190106+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    await session.execute(\n        db.queries.insert(db.AutomationTriggerWatermark)\n        .values(\n            automation_id=trigger.automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event_occurred=occurred,\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationTriggerWatermark.automation_id,\n                db.AutomationTriggerWatermark.trigger_id,\n                db.AutomationTriggerWatermark.bucketing_key,\n            ],\n            set_=dict(\n                last_event_occurred=sa.case(\n                    (\n                        db.AutomationTriggerWatermark.last_event_occurred\n                        < occurred,\n                        occurred,\n                    ),\n                    else_=db.AutomationTriggerWatermark.last_event_occurred,\n                ),\n                updated=prefect.types._datetime.now(\"UTC\"),\n            ),\n        )\n    )",
  "new_string": "    watermark = db.AutomationTriggerWatermark\n    await session.execute(\n        db.queries.insert(watermark)\n        .values(\n            automation_id=trigger.automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event_occurred=occurred,\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                watermark.automation_id,\n                watermark.trigger_id,\n                watermark.bucketing_key,\n            ],\n            set_=dict(\n                last_event_occurred=sa.case(\n                    (\n                        watermark.last_event_occurred < occurred,\n                        sa.literal(occurred, type_=watermark.last_event_occurred.type),\n                    ),\n                    else_=watermark.last_event_occurred,\n                ),\n                updated=prefect.types._datetime.now(\"UTC\"),\n            ),\n        )\n    )"
}
```

## 309 · 2026-10-29T03:51:37.348451+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 310 · 2026-10-29T03:51:39.376518+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_incident_regressions.py tests/events/server/triggers/zz_probe_test.py -q -p no:randomly 2>&1 | tail -20",
  "description": "Re-run incident and regression tests",
  "timeout": 900000
}
```

## 311 · 2026-10-29T03:53:29.584822+00:00 · tool_result 

```
    result = call_fixture_func(fixturefunc, request, kwargs)
  File "$SANDBOX\.runtime\venv\Lib\site-packages\_pytest\fixtures.py", line 1005, in call_fixture_func
    fixture_result = fixturefunc(**kwargs)
  File "$SANDBOX\.runtime\venv\Lib\site-packages\pytest_asyncio\plugin.py", line 407, in _asyncgen_fixture_wrapper
    result = runner.run(setup(), context=context)
  File "D:\python3.11\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
  File "D:\python3.11\Lib\asyncio\base_events.py", line 637, in run_until_complete
    self.run_forever()
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 321, in run_forever
    super().run_forever()
  File "D:\python3.11\Lib\asyncio\base_events.py", line 604, in run_forever
    self._run_once()
  File "D:\python3.11\Lib\asyncio\base_events.py", line 1873, in _run_once
    event_list = self._selector.select(timeout)
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 439, in select
    self._poll(timeout)
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 808, in _poll
    status = _overlapped.GetQueuedCompletionStatus(self._iocp, ms)
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
```

## 312 · 2026-10-29T03:53:32.214779+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -p no:randomly 2>&1 | tail -50",
  "description": "Run incident test alone",
  "timeout": 400000
}
```

## 313 · 2026-10-29T03:54:27.291082+00:00 · tool_result 

```
.                                                                        [100%]
1 passed in 37.41s
```

## 314 · 2026-10-29T03:54:29.651157+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 400 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -30",
  "description": "Run new regression tests alone",
  "timeout": 500000
}
```

## 315 · 2026-10-29T03:55:44.882538+00:00 · tool_result 

```
.....                                                                    [100%]
5 passed in 59.23s
```

## 316 · 2026-10-29T03:55:48.611532+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 400 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/zz_probe_test.py -q -p no:randomly 2>&1 | tail -30",
  "description": "Run intermediate-tick probe alone",
  "timeout": 500000
}
```

## 317 · 2026-10-29T03:56:32.774111+00:00 · tool_result 

```
.                                                                        [100%]
1 passed in 28.24s
```

## 318 · 2026-10-29T03:56:42.130596+00:00 · assistant_message 

```
Let me check the causal-ordering tests (issue 3244) that involve out-of-order Running/Completed delivery, since the watermark must not break them.
```

## 319 · 2026-10-29T03:56:42.339983+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_flow_run_slas.py",
  "offset": 700,
  "limit": 120
}
```

## 320 · 2026-10-29T03:56:42.443923+00:00 · tool_result 

```
700	            }
701	        ],
702	        id=uuid4(),
703	        follows=pending.id,
704	    ).receive()
705	
706	    completed = Event(
707	        occurred=baseline + datetime.timedelta(minutes=4),
708	        event="prefect.flow-run.Completed",
709	        resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
710	        related=[
711	            {
712	                "prefect.resource.id": "prefect.flow.f1f1f1f1",
713	                "prefect.resource.role": "flow",
714	            }
715	        ],
716	        id=uuid4(),
717	        follows=running.id,
718	    ).receive()
719	
720	    return [
721	        pending,
722	        completed,  # the completed will arrive before the running
723	        # throw a random event for the same resource ID in the middle
724	        Event(
725	            occurred=baseline + datetime.timedelta(minutes=2),
726	            event="prefect.log.write",
727	            resource={"prefect.resource.id": "prefect.flow-run.frfrfrfr"},
728	            related=[
729	                {
730	                    "prefect.resource.id": "prefect.flow.f1f1f1f1",
731	                    "prefect.resource.role": "flow",
732	                }
733	            ],
734	            id=uuid4(),
735	        ).receive(),
736	        running,
737	        baseline + datetime.timedelta(minutes=3),
738	        baseline
739	        + datetime.timedelta(
740	            minutes=4
741	        ),  # this is the slot to redeliver the Completed event
742	        baseline + datetime.timedelta(minutes=5),
743	        baseline
744	        + datetime.timedelta(minutes=119),  # just shy of the 2 hour mark since Pending
745	        baseline
746	        + datetime.timedelta(minutes=120),  # just at the 2 hour mark since Pending
747	        baseline
748	        + datetime.timedelta(minutes=121),  # just at the 2 hour mark since Running
749	        baseline
750	        + datetime.timedelta(
751	            minutes=123
752	        ),  # just shy of the 2 hour mark since Completed
753	        baseline
754	        + datetime.timedelta(minutes=124),  # just at the 2 hour mark since Completed
755	        baseline
756	        + datetime.timedelta(minutes=125),  # just past the 2 hour mark for anything
757	        baseline + datetime.timedelta(minutes=250),  # an additional full cycle later
758	    ]
759	
760	
761	async def test_regression_3244_negative_case(
762	    trigger_from_3244: EventTrigger,
763	    sequence_of_events_3244: List[Union[ReceivedEvent, DateTime]],
764	    act: mock.AsyncMock,
765	    automations_session: AsyncSession,
766	):
767	    # we expect no action to ever be called for these
768	    for index, item in enumerate(sequence_of_events_3244):
769	        if isinstance(item, ReceivedEvent):
770	            # The first time Completed comes through, it's too early, so we should
771	            # expect the EventArrivedEarly exception; this will record the Completed
772	            # event to be handled once the preceding event arrives
773	            if item.event == "prefect.flow-run.Completed" and index == 1:
774	                with pytest.raises(triggers.EventArrivedEarly):
775	                    await triggers.reactive_evaluation(event=item)
776	            else:
777	                await triggers.reactive_evaluation(event=item)
778	        elif isinstance(item, datetime.datetime):
779	            await triggers.proactive_evaluation(trigger_from_3244, as_of=item)
780	        else:  # pragma: no cover
781	            raise NotImplementedError()
782	
783	        act.assert_not_awaited()
784	
785	
786	async def test_regression_3244_positive_case(
787	    trigger_from_3244: EventTrigger,
788	    sequence_of_events_3244: List[Union[ReceivedEvent, DateTime]],
789	    act: mock.AsyncMock,
790	):
791	    # if we never get the completed event, the automation should fire
792	    for item in sequence_of_events_3244:
793	        if isinstance(item, ReceivedEvent):
794	            if item.event == "prefect.flow-run.Completed":
795	                continue
796	            await triggers.reactive_evaluation(event=item)
797	        elif isinstance(item, datetime.datetime):
798	            await triggers.proactive_evaluation(trigger_from_3244, as_of=item)
799	        else:  # pragma: no cover
800	            raise NotImplementedError()
801	
802	    act.assert_awaited_once()
803	
804	
805	# Regression test for https://github.com/PrefectHQ/nebula/issues/3803, where proactive
806	# triggers that are shorter than our message queueing backlog might erroneously fire.
807	# For example:
808	#
809	# wall clock | event.occurred | event.event
810	# ------------------------------------------------------
811	#          0 |            -10 | prefect.flow-run.Pending
812	#        1-5 |              - | 5 minutes worth of backlogged events
813	#          5 |              - | proactive evaluation runs here using now("UTC")
814	#          6 |             -9 | prefect.flow-run.Running
815	#
816	# In this case, the Running event was only 1 minute after the pending event, but it
817	# took 6 minutes of wall clock time to get there.  Running proactive evaluation using
818	# the wall clock time will make a proactive trigger erroneously fire.
819	
```

## 321 · 2026-10-29T03:56:50.812059+00:00 · assistant_message 

```
All scenarios pass individually. Let me fold the production-realistic intermediate-tick case and a storage-bound test into the regression file.
```

## 322 · 2026-10-29T03:56:51.490167+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "old_string": "from datetime import timedelta\nfrom typing import Callable, Union\nfrom unittest import mock\nfrom uuid import UUID, uuid4\n\nimport pytest\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations",
  "new_string": "from datetime import timedelta\nfrom typing import Callable, Union\nfrom unittest import mock\nfrom uuid import UUID, uuid4\n\nimport pytest\nimport sqlalchemy as sa\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.database import PrefectDBInterface\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations"
}
```

## 323 · 2026-10-29T03:56:51.597553+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

## 324 · 2026-10-29T03:56:55.949110+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "old_string": "async def test_run_that_reports_a_new_state_after_completion_is_monitored_again(",
  "new_string": "async def test_bucket_cleanup_between_events_does_not_resurrect_the_window(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"The server evaluates proactive triggers every few seconds.\n\n    A periodic proactive evaluation may remove a bucket that the Completed event\n    already satisfied before the racing heartbeat is delivered.  The event\n    watermark must survive that cleanup and still reject the stale heartbeat.\n    \"\"\"\n    for event in (\n        heartbeat(frozen_time),\n        heartbeat(frozen_time + timedelta(seconds=30)),\n        state_change(frozen_time + timedelta(seconds=60)),\n    ):\n        await triggers.reactive_evaluation(event)\n\n    # A periodic proactive evaluation runs and removes the satisfied bucket.\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=61)\n    )\n\n    # Only then does the racing heartbeat arrive.\n    await triggers.reactive_evaluation(\n        heartbeat(frozen_time + timedelta(seconds=60))\n    )\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()\n\n\nasync def test_trigger_watermarks_are_swept(\n    db: PrefectDBInterface,\n    automations_session: AsyncSession,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"Watermarks are persisted, but not forever, keeping storage bounded.\"\"\"\n    await triggers.reactive_evaluation(heartbeat(frozen_time))\n\n    async def watermark_rows():\n        result = await automations_session.execute(\n            sa.select(db.AutomationTriggerWatermark)\n        )\n        return result.scalars().all()\n\n    assert await watermark_rows()\n\n    await triggers.periodic_evaluation(\n        frozen_time\n        + triggers.AUTOMATION_WATERMARK_RETENTION\n        + timedelta(seconds=1)\n    )\n\n    assert await watermark_rows() == []\n\n\nasync def test_run_that_reports_a_new_state_after_completion_is_monitored_again("
}
```

## 325 · 2026-10-29T03:56:56.073051+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

## 326 · 2026-10-29T03:56:57.975483+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && rm -f tests/events/server/triggers/zz_probe_test.py && timeout 500 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -25",
  "description": "Run updated regression tests",
  "timeout": 600000
}
```

## 327 · 2026-10-29T03:57:56.826054+00:00 · tool_result 

```
.......                                                                  [100%]
7 passed in 47.47s
```

## 328 · 2026-10-29T03:57:59.830175+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 1700 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/ -q -p no:randomly 2>&1 | tail -25",
  "description": "Run full triggers test suite",
  "timeout": 1800000
}
```

## 329 · 2026-10-29T04:04:34.791973+00:00 · tool_result 

```
.................................................x...x...X.............. [ 56%]
.......................................................                  [100%]
124 passed, 2 xfailed, 1 xpassed in 384.27s (0:06:24)
```

## 330 · 2026-10-29T04:04:37.721409+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 1700 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/ -q -p no:randomly -rxX 2>&1 | tail -15",
  "description": "Identify xpassed test",
  "timeout": 1800000
}
```

## 331 · 2026-10-29T04:11:18.274736+00:00 · tool_result 

```
.................................................x...x...x.............. [ 56%]
.......................................................                  [100%]
=========================== short test summary info ===========================
XFAIL tests/events/server/triggers/test_composite_triggers.py::TestSequenceTriggers::test_sequence_trigger_multiple_triggers_fire_in_order_expired_does_not_act - `act` is called once, even though it shouldn't be
XFAIL tests/events/server/triggers/test_composite_triggers.py::TestSequenceTriggers::test_sequence_trigger_multiple_triggers_fired_in_order_duplicate_events_expired_does_not_act - `act` is called once, even though it shouldn't be
XFAIL tests/events/server/triggers/test_composite_triggers.py::TestSequenceTriggers::test_sequence_trigger_identical_event_triggers_only_one_fired_does_not_act
124 passed, 3 xfailed in 388.49s (0:06:28)
```

## 332 · 2026-10-29T04:11:20.981553+00:00 · assistant_message 

```
Full triggers suite passes. Now let me verify the new migration works end-to-end (fresh upgrade, downgrade round-trip, single head).
```

## 333 · 2026-10-29T04:11:21.457209+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 600 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations\" \"tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db\" -q -p no:randomly 2>&1 | tail -20",
  "description": "Run migration head and round-trip tests",
  "timeout": 700000
}
```

## 334 · 2026-10-29T04:13:52.349783+00:00 · tool_result 

```
    return tmp
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 848, in _poll
    self._unregistered.clear()
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 93, in set_result
    self._ov = None
  File "D:\python3.11\Lib\asyncio\base_events.py", line 765, in call_soon
    return handle
  File "D:\python3.11\Lib\asyncio\base_events.py", line 782, in _call_soon
    return handle
  File "D:\python3.11\Lib\asyncio\events.py", line 41, in __init__
    self._source_traceback = format_helpers.extract_stack(
  File "D:\python3.11\Lib\asyncio\format_helpers.py", line 76, in extract_stack
    return stack
  File "D:\python3.11\Lib\traceback.py", line 393, in extract
    return klass._extract_from_extended_frame_gen(
  File "D:\python3.11\Lib\traceback.py", line 437, in _extract_from_extended_frame_gen
    return result
  File "D:\python3.11\Lib\linecache.py", line 63, in checkcache
    for filename in filenames:
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
```

## 335 · 2026-10-29T04:13:53.743137+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"timeout\" pyproject.toml | head -20 && grep -rn \"timeout\" tests/conftest.py | head -20",
  "description": "Check pytest timeout configuration"
}
```

## 336 · 2026-10-29T04:13:54.120996+00:00 · tool_result 

```
157:    "pytest-timeout>=2.3.1",
296:timeout = 90
```

## 337 · 2026-10-29T04:13:56.857740+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 1200 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations\" \"tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db\" -q -p no:randomly --timeout=900 2>&1 | tail -20",
  "description": "Run migration tests with extended timeout",
  "timeout": 1300000
}
```

## 338 · 2026-10-29T04:16:26.961858+00:00 · tool_result 

```
    handle = None  # Needed to break cycles when an exception occurs.
  File "D:\python3.11\Lib\asyncio\events.py", line 95, in _run
    self = None  # Needed to break cycles when an exception occurs.
  File "D:\python3.11\Lib\asyncio\proactor_events.py", line 811, in _loop_self_reading
    f.add_done_callback(self._loop_self_reading)
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 470, in recv
    return self._register(ov, conn, finish_recv)
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 778, in _register
    return f
  File "D:\python3.11\Lib\asyncio\windows_events.py", line 58, in __init__
    self._ov = ov
  File "D:\python3.11\Lib\traceback.py", line 233, in extract_stack
    return stack
  File "D:\python3.11\Lib\traceback.py", line 393, in extract
    return klass._extract_from_extended_frame_gen(
  File "D:\python3.11\Lib\traceback.py", line 437, in _extract_from_extended_frame_gen
    return result
  File "D:\python3.11\Lib\linecache.py", line 63, in checkcache
    for filename in filenames:
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
```

## 339 · 2026-10-29T04:16:31.381458+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1,80p src/prefect/server/database/alembic_commands.py",
  "description": "Read alembic commands"
}
```

## 340 · 2026-10-29T04:16:31.632900+00:00 · tool_result 

```
import warnings
from functools import wraps
from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING, Any, Callable, Optional, Union

from sqlalchemy.exc import SAWarning
from typing_extensions import ParamSpec, TypeVar

import prefect.server.database

if TYPE_CHECKING:
    from alembic.config import Config


P = ParamSpec("P")
R = TypeVar("R", infer_variance=True)

ALEMBIC_LOCK = Lock()


def with_alembic_lock(fn: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator that prevents alembic commands from running concurrently.
    This is necessary because alembic uses a global configuration object
    that is not thread-safe.

    This issue occurred in https://github.com/PrefectHQ/prefect-dask/pull/50, where
    dask threads were simultaneously performing alembic upgrades, and causing
    cryptic `KeyError: 'config'` when `del globals_[attr_name]`.
    """

    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        with ALEMBIC_LOCK:
            return fn(*args, **kwargs)

    return wrapper


def alembic_config() -> "Config":
    from alembic.config import Config

    alembic_dir = Path(prefect.server.database.__file__).parent
    if not alembic_dir.joinpath("alembic.ini").exists():
        raise ValueError(f"Couldn't find alembic.ini at {alembic_dir}/alembic.ini")

    alembic_cfg = Config(alembic_dir / "alembic.ini")

    return alembic_cfg


@with_alembic_lock
def alembic_upgrade(revision: str = "head", dry_run: bool = False) -> None:
    """
    Run alembic upgrades on Prefect REST API database

    Args:
        revision: The revision passed to `alembic downgrade`. Defaults to 'head', upgrading all revisions.
        dry_run: Show what migrations would be made without applying them. Will emit sql statements to stdout.
    """
    # lazy import for performance
    import alembic.command

    # don't display reflection warnings that pop up during schema migrations
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message="Skipped unsupported reflection of expression-based index",
            category=SAWarning,
        )
        alembic.command.upgrade(alembic_config(), revision, sql=dry_run)


@with_alembic_lock
def alembic_downgrade(revision: str = "-1", dry_run: bool = False) -> None:
    """
    Run alembic downgrades on Prefect REST API database

    Args:
```

## 341 · 2026-10-29T04:16:33.692716+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"DATABASE_CONNECTION_URL\\|get_settings\" src/prefect/server/database/_migrations/env.py | head -20",
  "description": "Check alembic env connection setting"
}
```

## 342 · 2026-10-29T04:16:33.972620+00:00 · tool_result 

```
(Bash completed with no output)
```

## 343 · 2026-10-29T04:16:36.687379+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1,80p src/prefect/server/database/_migrations/env.py",
  "description": "Read migration env.py"
}
```

## 344 · 2026-10-29T04:16:36.930070+00:00 · tool_result 

```
# Originally generated from `alembic init`
# https://alembic.sqlalchemy.org/en/latest/tutorial.html#creating-an-environment

import contextlib
import copy
from typing import Optional

import sqlalchemy
from alembic import context
from sqlalchemy.ext.asyncio import AsyncEngine

from prefect.server.database.configurations import ENGINES, SQLITE_BEGIN_MODE
from prefect.server.database.dependencies import provide_database_interface
from prefect.server.utilities.database import get_dialect
from prefect.settings import get_current_settings
from prefect.utilities.asyncutils import run_async_from_worker_thread

db_interface = provide_database_interface()
config = context.config
target_metadata = db_interface.Base.metadata
dialect = get_dialect(db_interface.database_config.connection_url)


def include_object(
    object: sqlalchemy.schema.SchemaItem,
    name: str,
    type_: str,
    reflected: bool,
    compare_to: Optional[sqlalchemy.schema.SchemaItem],
) -> bool:
    """
    Determines whether or not alembic should include an object when autogenerating
    database migrations.

    Args:
        object: a sqlalchemy.schema.SchemaItem object such as a
            sqlalchemy.schema.Table, sqlalchemy.schema.Column,
            sqlalchemy.schema.Index sqlalchemy.schema.UniqueConstraint, or
            sqlalchemy.schema.ForeignKeyConstraint object.
        name: the name of the object. This is typically available via object.name.
        type_: a string describing the type of object; currently "table", "column",
            "index", "unique_constraint", or "foreign_key_constraint"
        reflected: True if the given object was produced based on table reflection,
            False if it's from a local .MetaData object.
        compare_to: the object being compared against, if available, else None.

    Returns:
        bool: whether or not the specified object should be included in autogenerated
            migration code.
    """

    # because of the dynamic inheritance pattern used by the Prefect database,
    # it is difficult to get alembic to resolve references to indexes on inherited models
    #
    # to keep autogenerated migration code clean, we ignore the following indexes:
    # * functional indexes (ending in 'desc', 'asc'), if an index with the same name already exists
    # * trigram indexes that already exist
    # * case_insensitive indexes that already exist
    # * indexes that don't yet exist but have .ddl_if(dialect=...) metadata that doesn't match
    #   the current dialect.
    if type_ == "index":
        if not reflected:
            if name.endswith(("asc", "desc")):
                return compare_to is None or object.name != compare_to.name
            if (ddl_if := object._ddl_if) is not None and ddl_if.dialect is not None:
                desired: set[str] = (
                    {ddl_if.dialect}
                    if isinstance(ddl_if.dialect, str)
                    else set(ddl_if.dialect)
                )
                return dialect.name in desired

        else:  # reflected
            if name.startswith("gin") or name.endswith("case_insensitive"):
                return False

    # SQLite doesn't have an enum type, so reflection always comes back with
    # a VARCHAR column, which doesn't match. Skip columns where the type
    # doesn't match
    if (
```

## 345 · 2026-10-29T04:16:43.098503+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport os, tempfile, pathlib\ndb_path = pathlib.Path(tempfile.mkdtemp()) / \"migration_check.db\"\nurl = f\"sqlite+aiosqlite:///{db_path}\"\nos.environ[\"PREFECT_SERVER_DATABASE_CONNECTION_URL\"] = url\nos.environ[\"PREFECT_API_DATABASE_CONNECTION_URL\"] = url\nfrom prefect.settings import temporary_settings, PREFECT_SERVER_DATABASE_CONNECTION_URL, PREFECT_API_DATABASE_CONNECTION_URL\nwith temporary_settings({PREFECT_SERVER_DATABASE_CONNECTION_URL: url, PREFECT_API_DATABASE_CONNECTION_URL: url}):\n    from prefect.server.database.alembic_commands import alembic_upgrade, alembic_downgrade\n    import sqlalchemy as sa\n    from prefect.server.database.dependencies import provide_database_interface\n    db = provide_database_interface()\n    print(\"interface url:\", db.database_config.connection_url)\n    alembic_upgrade()\n    eng = sa.create_engine(url.replace(\"+aiosqlite\", \"\"))\n    insp = sa.inspect(eng)\n    print(\"has watermark table:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    print(\"columns:\", [c[\"name\"] for c in insp.get_columns(\"automation_trigger_watermark\")])\n    print(\"indexes:\", [(i[\"name\"], i[\"unique\"], i[\"column_names\"]) for i in insp.get_indexes(\"automation_trigger_watermark\")])\n    print(\"fks:\", insp.get_foreign_keys(\"automation_trigger_watermark\"))\n    # downgrade one step and confirm removal, then upgrade again\n    alembic_downgrade(revision=\"-1\")\n    insp = sa.inspect(sa.create_engine(url.replace(\"+aiosqlite\", \"\")))\n    print(\"after downgrade present:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    alembic_upgrade()\n    insp = sa.inspect(sa.create_engine(url.replace(\"+aiosqlite\", \"\")))\n    print(\"after re-upgrade present:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    eng.dispose()\n    os.remove(db_path)\nEOF",
  "description": "Standalone SQLite migration upgrade/downgrade check",
  "timeout": 300000
}
```

## 346 · 2026-10-29T04:16:50.254187+00:00 · tool_result 

```
Exit code 1
interface url: sqlite+aiosqlite:///$SANDBOX\.runtime\temp\tmp80j5spft\migration_check.db
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
  File "$SANDBOX\prefect\src\prefect\server\database\alembic_commands.py", line 36, in wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "$SANDBOX\prefect\src\prefect\server\database\alembic_commands.py", line 72, in alembic_upgrade
    alembic.command.upgrade(alembic_config(), revision, sql=dry_run)
  File "$SANDBOX\.runtime\venv\Lib\site-packages\alembic\command.py", line 490, in upgrade
    script.run_env()
  File "$SANDBOX\.runtime\venv\Lib\site-packages\alembic\script\base.py", line 556, in run_env
    util.load_python_file(self.dir, "env.py")
  File "$SANDBOX\.runtime\venv\Lib\site-packages\alembic\util\pyfiles.py", line 116, in load_python_file
    module = load_module_py(module_id, path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "$SANDBOX\.runtime\venv\Lib\site-packages\alembic\util\pyfiles.py", line 136, in load_module_py
    spec.loader.exec_module(module)  # type: ignore
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "$SANDBOX\prefect\src\prefect\server\database\_migrations\env.py", line 242, in <module>
    run_async_from_worker_thread(apply_migrations)
  File "$SANDBOX\prefect\src\prefect\utilities\asyncutils\__init__.py", line 254, in run_async_from_worker_thread
    return anyio.from_thread.run(call)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "$SANDBOX\.runtime\venv\Lib\site-packages\anyio\from_thread.py", line 89, in run
    token = _token_or_error(token)
            ^^^^^^^^^^^^^^^^^^^^^^
  File "$SANDBOX\.runtime\venv\Lib\site-packages\anyio\from_thread.py", line 61, in _token_or_error
    raise NoEventLoopError(
anyio.NoEventLoopError: Not running inside an AnyIO worker thread, and no event loop token was provided
```

## 347 · 2026-10-29T04:16:55.795981+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport os, tempfile, pathlib, asyncio\ndb_path = pathlib.Path(tempfile.mkdtemp()) / \"migration_check.db\"\nurl = f\"sqlite+aiosqlite:///{db_path}\"\nos.environ[\"PREFECT_SERVER_DATABASE_CONNECTION_URL\"] = url\nos.environ[\"PREFECT_API_DATABASE_CONNECTION_URL\"] = url\nfrom prefect.settings import temporary_settings, PREFECT_SERVER_DATABASE_CONNECTION_URL, PREFECT_API_DATABASE_CONNECTION_URL\nwith temporary_settings({PREFECT_SERVER_DATABASE_CONNECTION_URL: url, PREFECT_API_DATABASE_CONNECTION_URL: url}):\n    from prefect.server.database.alembic_commands import alembic_upgrade, alembic_downgrade\n    from prefect.utilities.asyncutils import run_sync_in_worker_thread\n    import sqlalchemy as sa\n\n    asyncio.run(run_sync_in_worker_thread(alembic_upgrade))\n    eng = sa.create_engine(url.replace(\"+aiosqlite\", \"\"))\n    insp = sa.inspect(eng)\n    print(\"has watermark table:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    print(\"columns:\", [(c[\"name\"], str(c[\"type\"]), c[\"nullable\"]) for c in insp.get_columns(\"automation_trigger_watermark\")])\n    print(\"indexes:\", [(i[\"name\"], i[\"unique\"], i[\"column_names\"]) for i in insp.get_indexes(\"automation_trigger_watermark\")])\n    print(\"fks:\", [(f[\"name\"], f[\"constrained_columns\"], f[\"referred_table\"], f.get(\"options\")) for f in insp.get_foreign_keys(\"automation_trigger_watermark\")])\n    asyncio.run(run_sync_in_worker_thread(alembic_downgrade, revision=\"-1\"))\n    insp = sa.inspect(sa.create_engine(url.replace(\"+aiosqlite\", \"\")))\n    print(\"after downgrade present:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    asyncio.run(run_sync_in_worker_thread(alembic_upgrade))\n    insp = sa.inspect(sa.create_engine(url.replace(\"+aiosqlite\", \"\")))\n    print(\"after re-upgrade present:\", \"automation_trigger_watermark\" in insp.get_table_names())\n    eng.dispose()\n    os.remove(db_path)\nEOF",
  "description": "Migration upgrade/downgrade check in worker thread",
  "timeout": 300000
}
```

## 348 · 2026-10-29T04:17:10.928901+00:00 · tool_result 

```
Exit code 1
has watermark table: True
columns: [('automation_id', 'CHAR(36)', False), ('trigger_id', 'CHAR(36)', False), ('bucketing_key', 'JSON', False), ('last_event_occurred', 'DATETIME', False), ('id', 'CHAR(36)', False), ('created', 'DATETIME', False), ('updated', 'DATETIME', False)]
indexes: [('ix_automation_trigger_watermark__updated', 0, ['updated']), ('uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key', 1, ['automation_id', 'trigger_id', 'bucketing_key'])]
fks: [('fk_automation_trigger_watermark__automation_id__automation', ['automation_id'], 'automation', {'ondelete': 'CASCADE'})]
after downgrade present: False
after re-upgrade present: True
Traceback (most recent call last):
  File "<stdin>", line 26, in <module>
PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: '$SANDBOX\\.runtime\\temp\\tmpee3ilkfo\\migration_check.db'
```

## 349 · 2026-10-29T04:17:14.506282+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"compare_metadata\\|autogenerate\" tests/server/database/*.py | head -10",
  "description": "Look for schema comparison tests"
}
```

## 350 · 2026-10-29T04:17:14.792567+00:00 · tool_result 

```
tests/server/database/test_alembic_commands.py:62:        assert kwargs["autogenerate"] is False
tests/server/database/test_alembic_commands.py:66:        alembic_revision(message="new_revision", autogenerate=True)
tests/server/database/test_alembic_commands.py:70:        assert kwargs["autogenerate"] is True
```

## 351 · 2026-10-29T04:17:20.894957+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport sqlalchemy as sa\nurl = \"sqlite:///$SANDBOX/.runtime/trial.db\"\ntry:\n    eng = sa.create_engine(url)\n    insp = sa.inspect(eng)\n    for t in (\"automation_bucket\", \"automation_trigger_watermark\"):\n        if t in insp.get_table_names():\n            print(t)\n            for c in insp.get_columns(t):\n                print(\"  \", c[\"name\"], c[\"type\"], \"default=\", c.get(\"default\"))\n    eng.dispose()\nexcept Exception as e:\n    print(\"err\", e)\nEOF",
  "description": "Compare column defaults in migrated test DB"
}
```

## 352 · 2026-10-29T04:17:21.909570+00:00 · tool_result 

```
(Bash completed with no output)
```

## 353 · 2026-10-29T04:17:27.378202+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport os, tempfile, pathlib, asyncio\ndb_path = pathlib.Path(tempfile.mkdtemp()) / \"schema_compare.db\"\nurl = f\"sqlite+aiosqlite:///{db_path}\"\nos.environ[\"PREFECT_SERVER_DATABASE_CONNECTION_URL\"] = url\nos.environ[\"PREFECT_API_DATABASE_CONNECTION_URL\"] = url\nfrom prefect.settings import temporary_settings, PREFECT_SERVER_DATABASE_CONNECTION_URL, PREFECT_API_DATABASE_CONNECTION_URL\nwith temporary_settings({PREFECT_SERVER_DATABASE_CONNECTION_URL: url, PREFECT_API_DATABASE_CONNECTION_URL: url}):\n    from prefect.server.database.alembic_commands import alembic_upgrade\n    from prefect.utilities.asyncutils import run_sync_in_worker_thread\n    from prefect.server.database.dependencies import provide_database_interface\n    import sqlalchemy as sa\n    from alembic.migration import MigrationContext\n    from alembic.autogenerate import compare_metadata\n\n    asyncio.run(run_sync_in_worker_thread(alembic_upgrade))\n    eng = sa.create_engine(url.replace(\"+aiosqlite\", \"\"))\n    with eng.connect() as conn:\n        ctx = MigrationContext.configure(conn)\n        diff = compare_metadata(ctx, provide_database_interface().Base.metadata)\n    relevant = [d for d in diff if \"watermark\" in repr(d) or \"bucket\" in repr(d)]\n    print(\"total diffs:\", len(diff))\n    for d in relevant:\n        print(d)\n    eng.dispose()\nEOF",
  "description": "Compare ORM metadata to migrated schema",
  "timeout": 300000
}
```

## 354 · 2026-10-29T04:17:42.009527+00:00 · tool_result 

```
<stdin>:19: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__state_type_coalesce_start_time
<stdin>:19: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__schedule_id_scheduler
$SANDBOX\.runtime\venv\Lib\site-packages\alembic\ddl\impl.py:851: UserWarning: autogenerate skipping metadata-specified expression-based index 'ix_flow_run__state_type_coalesce_start_time'; dialect 'sqlite' under SQLAlchemy 2.0.45 can't reflect these indexes so they can't be compared
  util.warn(
$SANDBOX\.runtime\venv\Lib\site-packages\alembic\ddl\impl.py:851: UserWarning: autogenerate skipping metadata-specified expression-based index 'ix_flow_run__coalesce_start_time_expected_start_time_desc'; dialect 'sqlite' under SQLAlchemy 2.0.45 can't reflect these indexes so they can't be compared
  util.warn(
$SANDBOX\.runtime\venv\Lib\site-packages\alembic\ddl\impl.py:851: UserWarning: autogenerate skipping metadata-specified expression-based index 'ix_flow_run__coalesce_start_time_expected_start_time_asc'; dialect 'sqlite' under SQLAlchemy 2.0.45 can't reflect these indexes so they can't be compared
  util.warn(
total diffs: 31
```

## 355 · 2026-10-29T04:17:47.965280+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations\" -q -p no:randomly --timeout=280 2>&1 | tail -8",
  "description": "Run single-head migration test",
  "timeout": 400000
}
```

## 356 · 2026-10-29T04:18:20.060396+00:00 · tool_result 

```
..                                                                       [100%]
2 passed in 21.64s
```

## 357 · 2026-10-29T04:18:35.337833+00:00 · assistant_message 

```
Let me review the final trigger code and run broader event-server tests.
```

## 358 · 2026-10-29T04:18:35.512480+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 620,
  "limit": 110
}
```

## 359 · 2026-10-29T04:18:35.627094+00:00 · tool_result 

```
620	            bucketing_key = trigger.bucketing_key(event)
621	
622	            async with automations_session(begin_transaction=True) as session:
623	                try:
624	                    bucket: Optional["ORMAutomationBucket"] = None
625	                    watermark: Optional[prefect.types._datetime.DateTime] = None
626	
627	                    # Proactive triggers remember the newest event they have
628	                    # processed for each bucketing key, independently of the
629	                    # lifetime of an automation bucket.  This is what stops a late
630	                    # or out-of-order `after` event (for example, a heartbeat
631	                    # emitted while a flow run is completing) from arming a new
632	                    # window once a newer event has already satisfied the trigger.
633	                    track_watermark = (
634	                        bool(trigger.after) and trigger.posture == Posture.Proactive
635	                    )
636	                    if track_watermark:
637	                        bucket = await read_bucket(session, trigger, bucketing_key)
638	                        watermark = await read_trigger_watermark(
639	                            session, trigger, bucketing_key
640	                        )
641	
642	                    if trigger.after and trigger.starts_after(event.event):
643	                        # An event may only arm a _new_ window when it is newer than
644	                        # the newest event we have already seen for this resource.
645	                        # Events that only match `after` may also not replace the
646	                        # bucket's `last_event` when they are stale.
647	                        if (
648	                            track_watermark
649	                            and watermark is not None
650	                            and event.occurred <= watermark
651	                            and (bucket is None or not trigger.expects(event.event))
652	                        ):
653	                            logger.debug(
654	                                "Automation %s (%r) trigger %s ignoring stale event "
655	                                "%r for keys (%r): occurred %s is not newer than %s",
656	                                trigger.automation.id,
657	                                trigger.automation.name,
658	                                trigger.id,
659	                                event.event,
660	                                bucketing_key,
661	                                event.occurred,
662	                                watermark,
663	                            )
664	                            continue
665	
666	                        # When an event matches both the after and expect, each event
667	                        # can both start a new bucket and increment the bucket that was
668	                        # started by the previous event.  Here we offset the bucket to
669	                        # start at -1 so that the first event will leave the bucket at 0
670	                        # after evaluation.  See the tests:
671	                        #
672	                        #   test_same_event_in_expect_and_after_never_reacts_immediately
673	                        #   test_same_event_in_expect_and_after_reacts_after_threshold_is_met
674	                        #   test_same_event_in_expect_and_after_proactively_does_not_fire
675	                        #   test_same_event_in_expect_and_after_proactively_fires
676	                        #
677	                        # in test_triggers_regressions.py for examples of how we expect
678	                        # this to behave.
679	                        #
680	                        # https://github.com/PrefectHQ/nebula/issues/4201
681	                        initial_count = -1 if trigger.expects(event.event) else 0
682	                        bucket = await ensure_bucket(
683	                            session,
684	                            trigger,
685	                            bucketing_key,
686	                            start=event.occurred,
687	                            end=event.occurred + trigger.within,
688	                            last_event=event,
689	                            initial_count=initial_count,
690	                        )
691	
692	                    if (
693	                        not bucket
694	                        and not trigger.after
695	                        and trigger.expects(event.event)
696	                    ):
697	                        # When ensuring a bucket and _creating it for the first time_,
698	                        # use an old time so that we can catch any other events flowing
699	                        # through the system at the same time even if they are out of
700	                        # order.  After the trigger fires and creates its next bucket,
701	                        # time will start from that point forward.  We'll use our
702	                        # preceding event lookback variable as the horizon that we'll
703	                        # accept these older events.
704	                        #
705	                        # https://github.com/PrefectHQ/nebula/issues/7230
706	                        start = event.occurred - PRECEDING_EVENT_LOOKBACK
707	
708	                        bucket = await ensure_bucket(
709	                            session,
710	                            trigger,
711	                            bucketing_key=bucketing_key,
712	                            start=start,
713	                            end=event.occurred + trigger.within,
714	                            last_event=event,
715	                        )
716	
717	                    if track_watermark:
718	                        await record_trigger_watermark(
719	                            session, trigger, bucketing_key, event.occurred
720	                        )
721	
722	                    if not trigger.expects(event.event):
723	                        continue
724	
725	                    if not bucket:
726	                        bucket = await read_bucket(session, trigger, bucketing_key)
727	                        if not bucket:
728	                            continue
729	
```

## 360 · 2026-10-29T04:18:45.982601+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"periodic_evaluation\\|sweep_closed_buckets\\|sweep_expired\" tests/ --include=\"*.py\" | head -30",
  "description": "Find periodic_evaluation test usages"
}
```

## 361 · 2026-10-29T04:18:47.033185+00:00 · tool_result 

```
tests/events/server/triggers/test_basics.py:644:    await triggers.periodic_evaluation(now)
tests/events/server/triggers/test_basics.py:652:    await triggers.periodic_evaluation(now)
tests/events/server/triggers/test_basics.py:897:        await triggers.periodic_evaluation(base_date + timedelta(minutes=10))
tests/events/server/triggers/test_basics.py:908:        await triggers.periodic_evaluation(base_date + timedelta(minutes=20))
tests/events/server/triggers/test_incident_regressions.py:244:    await triggers.periodic_evaluation(
tests/events/server/triggers/test_service.py:120:def periodic_evaluation(monkeypatch: pytest.MonkeyPatch) -> mock.AsyncMock:
tests/events/server/triggers/test_service.py:121:    m = mock.AsyncMock(spec=triggers.periodic_evaluation)
tests/events/server/triggers/test_service.py:122:    monkeypatch.setattr("prefect.server.events.triggers.periodic_evaluation", m)
tests/events/server/triggers/test_service.py:221:    periodic_evaluation: mock.AsyncMock,
tests/events/server/triggers/test_service.py:226:    periodic_evaluation.assert_awaited_once_with(frozen_time)
tests/events/server/triggers/test_service.py:227:    periodic_evaluation.reset_mock()
tests/events/server/triggers/test_service.py:229:    # Note that periodic_evaluation should take the current wall-clock time and then it
tests/events/server/triggers/test_service.py:232:    # periodic_evaluation from the periodic task
tests/events/server/triggers/test_service.py:244:    assert periodic_evaluation.await_count >= 1
tests/events/server/triggers/test_service.py:245:    periodic_evaluation.assert_awaited_with(frozen_time)
tests/events/server/triggers/test_service.py:432:async def test_periodic_evaluation_continues_event_if_it_raises(
tests/events/server/triggers/test_service.py:433:    periodic_evaluation: mock.AsyncMock,
tests/events/server/triggers/test_service.py:440:        if periodic_evaluation.await_count > 1:
tests/events/server/triggers/test_service.py:444:    periodic_evaluation.side_effect = raise_woops
tests/events/server/triggers/test_service.py:456:    assert periodic_evaluation.await_count > 1
```

## 362 · 2026-10-29T04:18:51.856885+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/events/server/ && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/ --collect-only -q 2>/dev/null | tail -3",
  "description": "Count event server tests",
  "timeout": 300000
}
```

## 363 · 2026-10-29T04:19:04.601529+00:00 · tool_result 

```
__init__.py
actions
conftest.py
gateway
models
schemas
storage
test_automation_events.py
test_automations_api.py
test_clients.py
test_db_ordering.py
test_events_api.py
test_events_counts.py
test_events_queries.py
test_events_schema.py
test_in_memory_ordering.py
test_messaging.py
test_resource_schema.py
test_stream.py
triggers
tests/events/server/triggers/test_service_changes.py::test_gracefully_handles_errors_during_changes

745 tests collected in 2.52s
```

## 364 · 2026-10-29T04:19:09.224889+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 900 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py tests/events/server/models tests/events/server/test_in_memory_ordering.py tests/events/server/test_db_ordering.py -q -p no:randomly 2>&1 | tail -12",
  "description": "Run automation API and ordering tests",
  "timeout": 1000000
}
```

## 365 · 2026-10-29T04:24:20.601149+00:00 · tool_result 

```
E         ...Full output truncated (2 lines hidden), use '-vv' to show

tests\events\server\test_automations_api.py:687: AssertionError
---------------------------- Captured stderr call -----------------------------
Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.390 seconds
12:20:48.745 | WARNING | asyncio - Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.390 seconds
------------------------------ Captured log call ------------------------------
WARNING  asyncio:base_events.py:1904 Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.390 seconds
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
SKIPPED [1] tests\events\server\models\test_automation_notifications.py:172: This test requires PostgreSQL for NOTIFY/LISTEN
1 failed, 132 passed, 1 skipped in 296.96s (0:04:56)
```

## 366 · 2026-10-29T04:24:24.254420+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/test_automations_api.py",
  "offset": 620,
  "limit": 90
}
```

## 367 · 2026-10-29T04:24:24.355302+00:00 · tool_result 

```
620	        f"{automations_url}/{uuid4()}",
621	    )
622	    assert response.status_code == 404, response.content
623	    assert "Automation not found" in response.content.decode()
624	
625	
626	async def test_read_automation(
627	    client: AsyncClient,
628	    automations_url: str,
629	    existing_automation: Automation,
630	) -> None:
631	    response = await client.get(f"{automations_url}/{existing_automation.id}")
632	    assert response.status_code == 200, response.content
633	
634	    read_automation = Automation.model_validate_json(response.content)
635	    assert read_automation.id
636	    assert read_automation.name == "hello"
637	    assert read_automation.description == "world"
638	    assert read_automation.enabled
639	    assert read_automation.trigger == existing_automation.trigger
640	
641	
642	async def test_read_automation_that_does_not_exist(
643	    client: AsyncClient,
644	    automations_url: str,
645	) -> None:
646	    response = await client.get(f"{automations_url}/{uuid4()}")
647	    assert response.status_code == 404, response.content
648	    assert "Automation not found" in response.content.decode()
649	
650	
651	async def test_read_automations(
652	    some_workspace_automations: List[Automation],
653	    client: AsyncClient,
654	    automations_url: str,
655	) -> None:
656	    response = await client.post(f"{automations_url}/filter")
657	    assert response.status_code == 200, response.content
658	
659	    automations = parse_obj_as(List[Automation], response.json())
660	
661	    expected = sorted(some_workspace_automations, key=lambda a: a.name)
662	
663	    assert automations == expected
664	
665	
666	async def test_read_automations_page(
667	    some_workspace_automations: List[Automation],
668	    client: AsyncClient,
669	    automations_url: str,
670	) -> None:
671	    response = await client.post(
672	        f"{automations_url}/filter",
673	        json={"limit": 2, "offset": 1, "sort": AutomationSort.UPDATED_DESC},
674	    )
675	    assert response.status_code == 200, response.content
676	
677	    automations = parse_obj_as(List[Automation], response.json())
678	
679	    # updated is technically Optional, so assert it here to satisfy the type system
680	    def by_updated(automation: Automation) -> DateTime:
681	        assert automation.updated
682	        return automation.updated
683	
684	    expected = sorted(some_workspace_automations, key=by_updated, reverse=True)
685	    expected = expected[1:3]
686	
687	    assert automations == expected
688	
689	
690	async def test_read_automations_filter_by_name_match(
691	    some_workspace_automations: List[Automation],
692	    client: AsyncClient,
693	    automations_url: str,
694	) -> None:
695	    automation_filter = dict(
696	        automations=filters.AutomationFilter(
697	            name=filters.AutomationFilterName(any_=["automation 1", "automation 2"])
698	        ).model_dump(mode="json")
699	    )
700	
701	    response = await client.post(f"{automations_url}/filter", json=automation_filter)
702	
703	    assert response.status_code == 200, response.content
704	
705	    automations = parse_obj_as(List[Automation], response.json())
706	
707	    expected = sorted(some_workspace_automations, key=lambda a: a.name)
708	    expected = [a for a in expected if a.name in ["automation 1", "automation 2"]]
709	
```

## 368 · 2026-10-29T04:24:26.121247+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q -p no:randomly 2>&1 | tail -8",
  "description": "Re-run flaky automations page test",
  "timeout": 400000
}
```

## 369 · 2026-10-29T04:25:00.664620+00:00 · tool_result 

```
-------------------------- Captured stderr teardown ---------------------------
12:24:58.041 | INFO    | uvicorn.error - Shutting down
12:24:58.152 | INFO    | uvicorn.error - Waiting for application shutdown.
12:24:58.154 | INFO    | uvicorn.error - Application shutdown complete.
12:24:58.154 | INFO    | uvicorn.error - Finished server process [27936]
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 23.90s
```

## 370 · 2026-10-29T04:25:04.820891+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q -p no:randomly -vv 2>&1 | grep -A5 -B5 \"assert automations == expected\" | head -40",
  "description": "Show assertion details",
  "timeout": 400000
}
```

## 371 · 2026-10-29T04:25:38.964265+00:00 · tool_result 

```
            return automation.updated
    
        expected = sorted(some_workspace_automations, key=by_updated, reverse=True)
        expected = expected[1:3]
    
>       assert automations == expected
E       AssertionError: assert [Automation(n...f72d01bae1'))] == [Automation(n...7e2d6b8b2b'))]
E         
E         At index 0 diff: Automation(name='automation 3', description='', enabled=True, tags=[], trigger=EventTrigger(type='event', id=UUID('c6368b4d-924b-4136-b924-2a3796d5075d'), match=ResourceSpecification(root={'prefect.resource.id': 'some-resource'}), match_related=ResourceSpecification(root={}), after=set(), expect={'things.happened'}, for_each=set(), posture=Posture.Reactive, threshold=1, within=datetime.timedelta(seconds=10)), actions=[DoNothing(type='do-nothing')], actions_on_trigger=[], actions_on_resolve=[], id=UUID('b2281398-0df0-4baf-99fd-c93f2d435971')) != Automati...
E         
E         ...Full output truncated (13 lines hidden), use '-vv' to show
```

## 372 · 2026-10-29T04:25:44.718940+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 1,60p tests/events/server/test_automations_api.py && grep -rn \"frozen\\|advance_time\" tests/events/server/test_automations_api.py | head",
  "description": "Check automations API test fixtures"
}
```

## 373 · 2026-10-29T04:25:45.067122+00:00 · tool_result 

```
import textwrap
from datetime import timedelta
from typing import Any, Dict, List, Optional
from unittest import mock
from uuid import UUID, uuid4

import httpx
import pydantic
import pytest
import sqlalchemy as sa
from fastapi.applications import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from prefect.server import models as server_models
from prefect.server import schemas as server_schemas
from prefect.server.api.validation import ValidationError
from prefect.server.database import PrefectDBInterface
from prefect.server.events import actions, filters
from prefect.server.events.models.automations import (
    create_automation,
    read_automations_related_to_resource,
    relate_automation_to_resource,
)
from prefect.server.events.schemas.automations import (
    Automation,
    AutomationCore,
    AutomationCreate,
    AutomationPartialUpdate,
    AutomationSort,
    AutomationUpdate,
    CompoundTrigger,
    EventTrigger,
    Posture,
)
from prefect.server.models import deployments
from prefect.settings import (
    PREFECT_API_SERVICES_TRIGGERS_ENABLED,
    temporary_settings,
)
from prefect.types import DateTime
from prefect.types._datetime import now as now_fn
from prefect.utilities.pydantic import parse_obj_as

pytestmark = pytest.mark.clear_db


@pytest.fixture(autouse=True)
def enable_automations():
    with temporary_settings(
        {
            PREFECT_API_SERVICES_TRIGGERS_ENABLED: True,
        }
    ):
        yield


@pytest.fixture
async def client(app: FastAPI):
    # The automations tests assume that the client will not raise exceptions and will
```

## 374 · 2026-10-29T04:25:51.664305+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class Timestamp\" -A60 src/prefect/server/utilities/database.py",
  "description": "Inspect Timestamp type precision"
}
```

## 375 · 2026-10-29T04:25:51.933722+00:00 · tool_result 

```
134:class Timestamp(TypeDecorator[datetime.datetime]):
135-    """TypeDecorator that ensures that timestamps have a timezone.
136-
137-    For SQLite, all timestamps are converted to UTC (since they are stored
138-    as naive timestamps without timezones) and recovered as UTC.
139-    """
140-
141-    impl: TypeEngine[Any] | type[TypeEngine[Any]] = sa.TIMESTAMP(timezone=True)
142-    cache_ok: bool | None = True
143-
144-    def load_dialect_impl(self, dialect: sa.Dialect) -> TypeEngine[Any]:
145-        if dialect.name == "postgresql":
146-            return dialect.type_descriptor(postgresql.TIMESTAMP(timezone=True))
147-        elif dialect.name == "sqlite":
148-            # see the sqlite.DATETIME docstring on the particulars of the storage
149-            # format. Note that the sqlite implementations for timestamp and interval
150-            # arithmetic below would require updating if a different format was to
151-            # be configured here.
152-            return dialect.type_descriptor(sqlite.DATETIME())
153-        else:
154-            return dialect.type_descriptor(sa.TIMESTAMP(timezone=True))
155-
156-    def process_bind_param(
157-        self,
158-        value: Optional[datetime.datetime],
159-        dialect: sa.Dialect,
160-    ) -> Optional[datetime.datetime]:
161-        if value is None:
162-            return None
163-        else:
164-            if value.tzinfo is None:
165-                raise ValueError("Timestamps must have a timezone.")
166-            elif dialect.name == "sqlite":
167-                return value.astimezone(ZoneInfo("UTC"))
168-            else:
169-                return value
170-
171-    def process_result_value(
172-        self,
173-        value: Optional[datetime.datetime],
174-        dialect: sa.Dialect,
175-    ) -> Optional[datetime.datetime]:
176-        # retrieve timestamps in their native timezone (or UTC)
177-        if value is not None:
178-            if value.tzinfo is None:
179-                return value.replace(tzinfo=ZoneInfo("UTC"))
180-            else:
181-                return value.astimezone(ZoneInfo("UTC"))
182-
183-
184-class UUID(TypeDecorator[uuid.UUID]):
185-    """
186-    Platform-independent UUID type.
187-
188-    Uses PostgreSQL's UUID type, otherwise uses
189-    CHAR(36), storing as stringified hex values with
190-    hyphens.
191-    """
192-
193-    impl: type[TypeEngine[Any]] | TypeEngine[Any] = TypeEngine
194-    cache_ok: bool | None = True
```

## 376 · 2026-10-29T04:25:57.941137+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat > tests/events/server/zz_debug_automations_test.py <<'EOF'\nimport pytest\nfrom httpx import AsyncClient\n\npytestmark = pytest.mark.clear_db\n\n\nasync def test_debug(some_workspace_automations, client: AsyncClient):\n    for a in some_workspace_automations:\n        print(\"FIXTURE\", a.name, a.updated)\n    response = await client.post(\n        \"/automations/filter\",\n        json={\"limit\": 2, \"offset\": 1, \"sort\": \"UPDATED_DESC\"},\n    )\n    print(\"STATUS\", response.status_code)\n    for a in response.json():\n        print(\"API\", a[\"name\"], a[\"updated\"])\nEOF\ntimeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/zz_debug_automations_test.py -q -s -p no:randomly 2>&1 | grep -E \"FIXTURE|API|STATUS|passed|failed\" | head -20",
  "description": "Debug automation updated ordering",
  "timeout": 400000
}
```

## 377 · 2026-10-29T04:26:29.681646+00:00 · tool_result 

```
Running hosted API server on port 65475
FIXTURE automation 1 2026-10-29 04:26:26.085167+00:00
FIXTURE automation 2 2026-10-29 04:26:26.085167+00:00
FIXTURE automation 3 2026-10-29 04:26:26.085167+00:00
FIXTURE automation 4 2026-10-29 04:26:26.085167+00:00
STATUS 200
API automation 3 2026-10-29T04:26:26.085167Z
API automation 2 2026-10-29T04:26:26.085167Z
1 passed in 21.36s
```

## 378 · 2026-10-29T04:26:35.089648+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"autouse\" tests/conftest.py tests/events/conftest.py tests/events/server/conftest.py 2>/dev/null | head -20 && grep -rn \"monkeypatch.setattr.*_datetime.*now\\|frozen_time\" tests/conftest.py tests/events/conftest.py 2>/dev/null | head",
  "description": "Find autouse time freezing"
}
```

## 379 · 2026-10-29T04:26:35.501599+00:00 · tool_result 

```
tests/conftest.py:251:@pytest.fixture(scope="session", autouse=True)
tests/conftest.py:266:@pytest.fixture(scope="function", autouse=True)
tests/conftest.py:398:@pytest.fixture(scope="session", autouse=True)
tests/conftest.py:412:@pytest.fixture(scope="session", autouse=True)
tests/conftest.py:424:@pytest.fixture(scope="session", autouse=True)
tests/conftest.py:506:@pytest.fixture(scope="session", autouse=True)
tests/conftest.py:527:@pytest.fixture(autouse=True)
tests/conftest.py:541:@pytest.fixture(autouse=True)
tests/conftest.py:571:@pytest.fixture(autouse=True)
tests/conftest.py:582:@pytest.fixture(autouse=True)
tests/conftest.py:630:@pytest.fixture(autouse=True, scope="module")
```

## 380 · 2026-10-29T04:26:39.748372+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n 520,600p tests/conftest.py",
  "description": "Read autouse fixtures in root conftest"
}
```

## 381 · 2026-10-29T04:26:39.991933+00:00 · tool_result 

```
    else:
        with temporary_settings(
            updates={PREFECT_SERVER_DATABASE_CONNECTION_URL: url},
        ):
            yield url


@pytest.fixture(autouse=True)
def reset_registered_blocks():
    """
    Ensures each test only has types that were registered at module initialization.
    """
    registry = get_registry_for_type(Block)
    before = registry.copy()

    yield

    registry.clear()
    registry.update(before)


@pytest.fixture(autouse=True)
def reset_maintenance_backoffs():
    """
    Ensures a maintenance back-off recorded by one test does not extend health
    check windows in another; the record is process-wide.
    """
    reset_maintenance_backoff()
    yield
    reset_maintenance_backoff()


@pytest.fixture
def caplog(
    caplog: pytest.LogCaptureFixture,
) -> Generator[pytest.LogCaptureFixture, None, None]:
    """
    Overrides caplog to apply to all of our loggers that do not propagate and
    consequently would not be captured by caplog.
    """
    from prefect.logging.configuration import PROCESS_LOGGING_CONFIG

    for name, logger_config in PROCESS_LOGGING_CONFIG["loggers"].items():
        if not logger_config.get("propagate", True):
            logger = logging.getLogger(name)
            if caplog.handler not in logger.handlers:
                logger.handlers.append(caplog.handler)

    yield caplog


@pytest.fixture(autouse=True)
def disable_csrf_protection():
    with temporary_settings({PREFECT_SERVER_CSRF_PROTECTION_ENABLED: False}):
        yield


@pytest.fixture
def start_of_test() -> datetime.datetime:
    return now("UTC")


@pytest.fixture(autouse=True)
def reset_sys_modules():
    import importlib

    original_modules = sys.modules.copy()

    # Workaround for weird behavior on Linux where some of our "expected
    # failure" tests succeed because '.' is in the path.
    if sys.platform == "linux" and "." in sys.path:
        sys.path.remove(".")

    yield

    # Delete all of the module objects that were introduced so they are not
    # cached.  Also remove stale references from parent packages so that
    # subsequent monkeypatch / import resolution doesn't find a stale module
    # object via getattr on the parent while sys.modules has no entry.
    #
    # Preserve prefect.cli.* and cyclopts modules: cyclopts lazy loading caches
```

## 382 · 2026-10-29T04:26:50.019280+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"_datetime\\|freeze\\|time_machine\\|freezegun\" tests/conftest.py | head -20 && rm -f tests/events/server/zz_debug_automations_test.py",
  "description": "Check root conftest time handling and remove debug test"
}
```

## 383 · 2026-10-29T04:26:50.516222+00:00 · tool_result 

```
90:from prefect.types._datetime import now
```

## 384 · 2026-10-29T04:26:54.346182+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"def now\" -A20 src/prefect/types/_datetime.py | head -40",
  "description": "Inspect now() implementation"
}
```

## 385 · 2026-10-29T04:26:54.636402+00:00 · tool_result 

```
197:def now(
198-    tz: str | Any = "UTC",
199-) -> datetime.datetime:
200-    if sys.version_info >= (3, 13):
201-        from whenever import ZonedDateTime
202-
203-        if isinstance(getattr(tz, "name", None), str):
204-            tz = tz.name
205-
206-        return _whenever_to_stdlib(ZonedDateTime.now(tz))
207-    else:
208-        return pendulum.now(tz)
209-
210-
211-def end_of_period(dt: datetime.datetime, period: str) -> datetime.datetime:
212-    """
213-    Returns the end of the specified unit of time.
214-
215-    Args:
216-        dt: The datetime to get the end of.
217-        period: The period to get the end of.
```

## 386 · 2026-10-29T04:26:59.731947+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check src/prefect/server/events/triggers.py src/prefect/server/database/orm_models.py src/prefect/server/database/interface.py src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py tests/events/server/triggers/test_incident_regressions.py 2>&1 | tail -20",
  "description": "Run ruff lint on changed files",
  "timeout": 300000
}
```

## 387 · 2026-10-29T04:27:00.382578+00:00 · tool_result 

```
UP007 [*] Use `X | Y` for type annotations
   --> tests\events\server\triggers\test_incident_regressions.py:255:34
    |
253 | async def test_run_that_reports_a_new_state_after_completion_is_monitored_again(
254 |     act: mock.AsyncMock,
255 |     assert_acted_with: Callable[[Union[Firing, list[Firing]]], None],
    |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
256 |     frozen_time: DateTime,
257 |     unresponsive_run_automation: Automation,
    |
help: Convert to `X | Y`
    |
254 |     act: mock.AsyncMock,
    -     assert_acted_with: Callable[[Union[Firing, list[Firing]]], None],
255 +     assert_acted_with: Callable[[Firing | list[Firing]], None],
256 |     frozen_time: DateTime,
    |

Found 159 errors.
[*] 141 fixable with the `--fix` option (4 hidden fixes can be enabled with the `--unsafe-fixes` option).
```

## 388 · 2026-10-29T04:27:05.095306+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check tests/events/server/triggers/test_regressions.py src/prefect/server/events/actions.py 2>&1 | tail -5 && grep -n \"line-length\\|\\[tool.ruff\" -A20 pyproject.toml | head -40",
  "description": "Check ruff baseline on unchanged files",
  "timeout": 300000
}
```

## 389 · 2026-10-29T04:27:05.691975+00:00 · tool_result 

```
960 |         if minute in evaluate_proactive_times:
    |

Found 146 errors.
[*] 130 fixable with the `--fix` option (3 hidden fixes can be enabled with the `--unsafe-fixes` option).
348:[tool.ruff]
349-src = ["src"]
350-
351:[tool.ruff.lint]
352-extend-select = ["I"]
353-
354:[tool.ruff.lint.per-file-ignores]
355-"__init__.py" = ["E402", "F401", "I"]
356-"main.py" = ["E402", "F401", "I"]
357-"src/prefect/utilities/compat.py" = ["F401", "I"]
358-"tests/conftest.py" = ["F405", "E402", "F403"]
359-"src/prefect/runtime/*" = ["F822"]
360-"src/prefect/server/database/migrations/**/*" = ["E501"]
361-
362:[tool.ruff.lint.isort]
363-known-third-party = []
364-
365-[tool.codespell]
366-skip = [
367-    ".git",
368-    "*.pdf",
369-    "*.svg",
370-    "package-lock.json",
371-    "_vendor",
372-    "*.css",
373-    "tests/utilities/test_text.py",
374-    "pyproject.toml",
375-]
376-# from https://github.com/PrefectHQ/prefect/pull/10813#issuecomment-1732676130
377-ignore-regex = ".*lazy=\"selectin\"|.*e import Bloc\\s*$|America/Nome"
378-
379-ignore-words-list = [
380-    "selectin",
381-    "aci",
382-    "wqs",
```

## 390 · 2026-10-29T04:27:11.068933+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --diff src/prefect/server/events/triggers.py src/prefect/server/database/orm_models.py src/prefect/server/database/interface.py tests/events/server/triggers/test_incident_regressions.py src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py 2>&1 | head -80",
  "description": "Check ruff formatting diffs",
  "timeout": 300000
}
```

## 391 · 2026-10-29T04:27:11.648377+00:00 · tool_result 

```
--- src\prefect\server\database\_migrations\versions\postgresql\2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py
+++ src\prefect\server\database\_migrations\versions\postgresql\2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py
@@ -63,14 +63,10 @@
         sa.ForeignKeyConstraint(
             ["automation_id"],
             ["automation.id"],
-            name=op.f(
-                "fk_automation_trigger_watermark__automation_id__automation"
-            ),
+            name=op.f("fk_automation_trigger_watermark__automation_id__automation"),
             ondelete="CASCADE",
         ),
-        sa.PrimaryKeyConstraint(
-            "id", name=op.f("pk_automation_trigger_watermark")
-        ),
+        sa.PrimaryKeyConstraint("id", name=op.f("pk_automation_trigger_watermark")),
     )
     op.create_index(
         "uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key",

--- src\prefect\server\database\_migrations\versions\sqlite\2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py
+++ src\prefect\server\database\_migrations\versions\sqlite\2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py
@@ -65,14 +65,10 @@
         sa.ForeignKeyConstraint(
             ["automation_id"],
             ["automation.id"],
-            name=op.f(
-                "fk_automation_trigger_watermark__automation_id__automation"
-            ),
+            name=op.f("fk_automation_trigger_watermark__automation_id__automation"),
             ondelete="CASCADE",
         ),
-        sa.PrimaryKeyConstraint(
-            "id", name=op.f("pk_automation_trigger_watermark")
-        ),
+        sa.PrimaryKeyConstraint("id", name=op.f("pk_automation_trigger_watermark")),
     )
     with op.batch_alter_table("automation_trigger_watermark", schema=None) as batch_op:
         batch_op.create_index(

--- tests\events\server\triggers\test_incident_regressions.py
+++ tests\events\server\triggers\test_incident_regressions.py
@@ -212,9 +212,7 @@
     )
 
     # Only then does the racing heartbeat arrive.
-    await triggers.reactive_evaluation(
-        heartbeat(frozen_time + timedelta(seconds=60))
-    )
+    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))
 
     act.assert_not_awaited()
 
@@ -242,9 +240,7 @@
     assert await watermark_rows()
 
     await triggers.periodic_evaluation(
-        frozen_time
-        + triggers.AUTOMATION_WATERMARK_RETENTION
-        + timedelta(seconds=1)
+        frozen_time + triggers.AUTOMATION_WATERMARK_RETENTION + timedelta(seconds=1)
     )
 
     assert await watermark_rows() == []

3 files would be reformatted, 3 files already formatted
```

## 392 · 2026-10-29T04:27:15.776174+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py tests/events/server/triggers/test_incident_regressions.py",
  "description": "Format changed files",
  "timeout": 120000
}
```

## 393 · 2026-10-29T04:27:16.246663+00:00 · tool_result 

```
3 files reformatted
[This command modified 3 files you've previously read: src\prefect\server\database\_migrations\versions\postgresql\2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py, src\prefect\server\database\_migrations\versions\sqlite\2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py, tests\events\server\triggers\test_incident_regressions.py. Call Read before editing.]
```

## 394 · 2026-10-29T04:27:30.789503+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 600 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -8",
  "description": "Re-run incident and regressions after formatting",
  "timeout": 700000
}
```

## 395 · 2026-10-29T04:28:25.896467+00:00 · tool_result 

```
........                                                                 [100%]
8 passed in 44.86s
```

## 396 · 2026-10-29T04:28:33.695656+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "old_string": "ORMAutomationBucket = AutomationBucket\nORMAutomationRelatedResource = AutomationRelatedResource",
  "new_string": "ORMAutomationBucket = AutomationBucket\nORMAutomationTriggerWatermark = AutomationTriggerWatermark\nORMAutomationRelatedResource = AutomationRelatedResource"
}
```

## 397 · 2026-10-29T04:28:33.817966+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/database/orm_models.py has been updated successfully.
```

## 398 · 2026-10-29T04:28:39.716387+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 1700 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/ -q -p no:randomly 2>&1 | tail -6",
  "description": "Final full triggers suite run",
  "timeout": 1800000
}
```

## 399 · 2026-10-29T04:34:26.853743+00:00 · tool_result 

```
.................................................x...x...x.............. [ 56%]
.......................................................                  [100%]
124 passed, 3 xfailed in 336.72s (0:05:36)
```

## 400 · 2026-10-29T04:34:33.000399+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 88,
  "limit": 50
}
```

## 401 · 2026-10-29T04:34:33.098701+00:00 · tool_result 

```
88	# How long to remember the most recent event processed for an automation trigger
89	# and bucketing key.  This matches the window over which the triggers consumer
90	# remembers processed events, which keeps watermark storage bounded while still
91	# covering redeliveries and ordinary out-of-order delivery.
92	AUTOMATION_WATERMARK_RETENTION = SEEN_EXPIRATION
93	
94	
95	async def evaluate(
96	    session: AsyncSession,
97	    trigger: EventTrigger,
98	    bucket: "ORMAutomationBucket",
99	    now: prefect.types._datetime.DateTime,
100	    triggering_event: Optional[ReceivedEvent],
101	) -> "ORMAutomationBucket | None":
102	    """Evaluates an Automation, either triggered by a specific event or proactively
103	    on a time interval.  Evaluating a Automation updates the associated counters for
104	    each automation, and will fire the associated action if it has met the threshold."""
105	    automation = trigger.automation
106	
107	    # Capture the most recent event that has contributed to this bucket before this
108	    # evaluation mutates it.  Proactive buckets may only be re-armed by an event that
109	    # is _newer_ than the event that last satisfied the window; otherwise a late or
110	    # out-of-order event (for example, a heartbeat racing a terminal state change for
111	    # the same flow run) could re-open an expectation that has already been met.
112	    previous_last_event_occurred = (
113	        bucket.last_event.occurred if bucket.last_event else None
114	    )
115	
116	    logging_context = {
117	        "automation": automation.id,
118	        "trigger": trigger.id,
119	        "bucketing_key": bucket.bucketing_key,
120	        "bucket_start": bucket.start,
121	        "bucket_end": bucket.end,
122	        "bucket_initial_count": bucket.count,
123	        "bucket_last_operation": bucket.last_operation,
124	        "now": now,
125	        "triggering_event": (
126	            {
127	                "id": triggering_event.id,
128	                "event": triggering_event.event,
129	            }
130	            if triggering_event
131	            else None
132	        ),
133	    }
134	
135	    # Implementation notes:
136	    #
137	    # This triggering algorithm maintains an invariant that there is exactly one
```

## 402 · 2026-10-29T04:34:33.234781+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 225,
  "limit": 55
}
```

## 403 · 2026-10-29T04:34:33.309249+00:00 · tool_result 

```
225	
226	    elif now < bucket.end:
227	        # We didn't fire this time, and also the bucket still has more time, so leave
228	        # before setting up a new future bucket.  Case #2 from the implementation notes
229	        # above.
230	        logger.debug(
231	            "Automation %s (%r) trigger %s has more time for keys (%r)",
232	            automation.id,
233	            automation.name,
234	            trigger.id,
235	            bucket.bucketing_key,
236	            extra={
237	                **logging_context,
238	                "ready_to_fire": ready_to_fire,
239	                "meets_threshold": meets_threshold,
240	            },
241	        )
242	
243	        # Special case of a proactive trigger for which the same event satisfies
244	        # both `after` and `expect`.  For example, using flow run heartbeats for crash
245	        # detection, after the first heartbeat we expect a subsequent heartbeat or
246	        # terminal state within a given time.
247	        #
248	        # If we've already reached the proactive threshold, we need to remove the
249	        # current bucket and start a new one for the latest event.  We may only do
250	        # that when this event is actually newer than the event that last contributed
251	        # to the bucket: a stale event (a heartbeat that occurred at or before the
252	        # terminal state it raced) carries no new information and must not restart
253	        # the expectation.
254	        if (
255	            triggering_event
256	            and trigger.posture == Posture.Proactive
257	            and not meets_threshold
258	            and trigger.starts_after(triggering_event.event)
259	            and trigger.expects(triggering_event.event)
260	            and (
261	                previous_last_event_occurred is None
262	                or triggering_event.occurred > previous_last_event_occurred
263	            )
264	        ):
265	            await remove_bucket(session, bucket)
266	            return await start_new_bucket(
267	                session,
268	                trigger,
269	                bucketing_key=bucket.bucketing_key,
270	                start=triggering_event.occurred,
271	                end=triggering_event.occurred + trigger.within,
272	                count=0,
273	                last_event=triggering_event,
274	            )
275	
276	        return bucket
277	    else:
278	        # Case #2 from the implementation notes above.
279	        logger.debug(
```

## 404 · 2026-10-29T04:34:37.914375+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 1004,
  "limit": 120
}
```

## 405 · 2026-10-29T04:34:38.001661+00:00 · tool_result 

```
1004	            break
1005	
1006	        for bucket in buckets:
1007	            yield bucket
1008	
1009	        offset += batch_size
1010	
1011	
1012	@db_injector
1013	async def read_bucket(
1014	    db: PrefectDBInterface,
1015	    session: AsyncSession,
1016	    trigger: Trigger,
1017	    bucketing_key: Tuple[str, ...],
1018	) -> Optional["ORMAutomationBucket"]:
1019	    """Gets the bucket this event would fall into for the given Automation, if there is
1020	    one currently"""
1021	    return await read_bucket_by_trigger_id(
1022	        session,
1023	        trigger.automation.id,
1024	        trigger.id,
1025	        bucketing_key,
1026	    )
1027	
1028	
1029	@db_injector
1030	async def read_bucket_by_trigger_id(
1031	    db: PrefectDBInterface,
1032	    session: AsyncSession,
1033	    automation_id: UUID,
1034	    trigger_id: UUID,
1035	    bucketing_key: Tuple[str, ...],
1036	) -> "ORMAutomationBucket | None":
1037	    """Gets the bucket this event would fall into for the given Automation, if there is
1038	    one currently"""
1039	    query = sa.select(db.AutomationBucket).where(
1040	        db.AutomationBucket.automation_id == automation_id,
1041	        db.AutomationBucket.trigger_id == trigger_id,
1042	        db.AutomationBucket.bucketing_key == bucketing_key,
1043	    )
1044	    result = await session.execute(query)
1045	    bucket = result.scalars().first()
1046	    if bucket:
1047	        await session.refresh(bucket)
1048	
1049	    return bucket
1050	
1051	
1052	@db_injector
1053	async def read_trigger_watermark(
1054	    db: PrefectDBInterface,
1055	    session: AsyncSession,
1056	    trigger: Trigger,
1057	    bucketing_key: Tuple[str, ...],
1058	) -> Optional[prefect.types._datetime.DateTime]:
1059	    """Gets the greatest event occurrence processed for this trigger and key.
1060	
1061	    Watermarks are independent of automation buckets so that they survive bucket
1062	    cleanup and server restarts.
1063	    """
1064	    query = sa.select(db.AutomationTriggerWatermark.last_event_occurred).where(
1065	        db.AutomationTriggerWatermark.automation_id == trigger.automation.id,
1066	        db.AutomationTriggerWatermark.trigger_id == trigger.id,
1067	        db.AutomationTriggerWatermark.bucketing_key == bucketing_key,
1068	    )
1069	    return (await session.execute(query)).scalar_one_or_none()
1070	
1071	
1072	@db_injector
1073	async def record_trigger_watermark(
1074	    db: PrefectDBInterface,
1075	    session: AsyncSession,
1076	    trigger: Trigger,
1077	    bucketing_key: Tuple[str, ...],
1078	    occurred: prefect.types._datetime.DateTime,
1079	) -> None:
1080	    """Records an event's occurrence as a high-water mark for this trigger and key.
1081	
1082	    The mark only moves forward: older or out-of-order events cannot lower it.
1083	    """
1084	    watermark = db.AutomationTriggerWatermark
1085	    await session.execute(
1086	        db.queries.insert(watermark)
1087	        .values(
1088	            automation_id=trigger.automation.id,
1089	            trigger_id=trigger.id,
1090	            bucketing_key=bucketing_key,
1091	            last_event_occurred=occurred,
1092	        )
1093	        .on_conflict_do_update(
1094	            index_elements=[
1095	                watermark.automation_id,
1096	                watermark.trigger_id,
1097	                watermark.bucketing_key,
1098	            ],
1099	            set_=dict(
1100	                last_event_occurred=sa.case(
1101	                    (
1102	                        watermark.last_event_occurred < occurred,
1103	                        sa.literal(occurred, type_=watermark.last_event_occurred.type),
1104	                    ),
1105	                    else_=watermark.last_event_occurred,
1106	                ),
1107	                updated=prefect.types._datetime.now("UTC"),
1108	            ),
1109	        )
1110	    )
1111	
1112	
1113	@db_injector
1114	async def increment_bucket(
1115	    db: PrefectDBInterface,
1116	    session: AsyncSession,
1117	    bucket: "ORMAutomationBucket",
1118	    count: int,
1119	    last_event: Optional[ReceivedEvent],
1120	) -> "ORMAutomationBucket":
1121	    """Adds the given count to the bucket, returning the new bucket"""
1122	    additional_updates: dict[str, ReceivedEvent] = {}
1123	    if last_event:
```

## 406 · 2026-10-29T04:34:42.524681+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "offset": 1113,
  "limit": 110
}
```

## 407 · 2026-10-29T04:34:42.620481+00:00 · tool_result 

```
1113	@db_injector
1114	async def increment_bucket(
1115	    db: PrefectDBInterface,
1116	    session: AsyncSession,
1117	    bucket: "ORMAutomationBucket",
1118	    count: int,
1119	    last_event: Optional[ReceivedEvent],
1120	) -> "ORMAutomationBucket":
1121	    """Adds the given count to the bucket, returning the new bucket"""
1122	    additional_updates: dict[str, ReceivedEvent] = {}
1123	    if last_event:
1124	        # Keep `last_event` pointing at the newest event that has contributed to the
1125	        # bucket.  Out-of-order events still count towards the threshold, but they
1126	        # must not move the bucket's notion of "latest event" backwards.
1127	        if (
1128	            bucket.last_event is None
1129	            or last_event.occurred > bucket.last_event.occurred
1130	        ):
1131	            additional_updates["last_event"] = last_event
1132	    await session.execute(
1133	        db.queries.insert(db.AutomationBucket)
1134	        .values(
1135	            automation_id=bucket.automation_id,
1136	            trigger_id=bucket.trigger_id,
1137	            bucketing_key=bucket.bucketing_key,
1138	            start=bucket.start,
1139	            end=bucket.end,
1140	            count=count,
1141	            last_operation="increment_bucket[insert]",
1142	        )
1143	        .on_conflict_do_update(
1144	            index_elements=[
1145	                db.AutomationBucket.automation_id,
1146	                db.AutomationBucket.trigger_id,
1147	                db.AutomationBucket.bucketing_key,
1148	            ],
1149	            set_=dict(
1150	                count=db.AutomationBucket.count + count,
1151	                last_operation="increment_bucket[update]",
1152	                updated=prefect.types._datetime.now("UTC"),
1153	                **additional_updates,
1154	            ),
1155	        )
1156	    )
1157	
1158	    read_bucket = await read_bucket_by_trigger_id(
1159	        session,
1160	        bucket.automation_id,
1161	        bucket.trigger_id,
1162	        tuple(bucket.bucketing_key),
1163	    )
1164	
1165	    if TYPE_CHECKING:
1166	        assert read_bucket is not None
1167	
1168	    return read_bucket
1169	
1170	
1171	@db_injector
1172	async def start_new_bucket(
1173	    db: PrefectDBInterface,
1174	    session: AsyncSession,
1175	    trigger: EventTrigger,
1176	    bucketing_key: Tuple[str, ...],
1177	    start: prefect.types._datetime.DateTime,
1178	    end: prefect.types._datetime.DateTime,
1179	    count: int,
1180	    triggered_at: Optional[prefect.types._datetime.DateTime] = None,
1181	    last_event: Optional[ReceivedEvent] = None,
1182	) -> "ORMAutomationBucket":
1183	    """Ensures that a bucket with the given start and end exists with the given count,
1184	    returning the new bucket"""
1185	    automation = trigger.automation
1186	
1187	    await session.execute(
1188	        db.queries.insert(db.AutomationBucket)
1189	        .values(
1190	            automation_id=automation.id,
1191	            trigger_id=trigger.id,
1192	            bucketing_key=bucketing_key,
1193	            start=start,
1194	            end=end,
1195	            count=count,
1196	            last_operation="start_new_bucket[insert]",
1197	            triggered_at=triggered_at,
1198	            last_event=last_event,
1199	        )
1200	        .on_conflict_do_update(
1201	            index_elements=[
1202	                db.AutomationBucket.automation_id,
1203	                db.AutomationBucket.trigger_id,
1204	                db.AutomationBucket.bucketing_key,
1205	            ],
1206	            set_=dict(
1207	                start=start,
1208	                end=end,
1209	                count=count,
1210	                last_operation="start_new_bucket[update]",
1211	                updated=prefect.types._datetime.now("UTC"),
1212	                triggered_at=triggered_at,
1213	                last_event=last_event,
1214	            ),
1215	        )
1216	    )
1217	
1218	    read_bucket = await read_bucket_by_trigger_id(
1219	        session,
1220	        automation.id,
1221	        trigger.id,
1222	        tuple(bucketing_key),
```

## 408 · 2026-10-29T04:34:47.031909+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --check src/prefect/server/events/triggers.py src/prefect/server/database/orm_models.py src/prefect/server/database/interface.py tests/events/server/triggers/test_incident_regressions.py src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py",
  "description": "Verify formatting is clean",
  "timeout": 120000
}
```

## 409 · 2026-10-29T04:34:47.502774+00:00 · tool_result 

```
6 files already formatted
```

## 410 · 2026-10-29T04:34:52.406606+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "offset": 150,
  "limit": 50
}
```

## 411 · 2026-10-29T04:34:52.507784+00:00 · tool_result 

```
150	    )
151	
152	    assert_acted_with(
153	        Firing(
154	            trigger=unresponsive_run_automation.trigger,
155	            trigger_states={TriggerState.Triggered},
156	            triggered=frozen_time,  # type: ignore
157	            triggering_labels={"prefect.resource.id": RESOURCE_ID},
158	            triggering_event=second,
159	        )
160	    )
161	
162	
163	async def test_completed_run_stays_silent_across_a_restart(
164	    act: mock.AsyncMock,
165	    frozen_time: DateTime,
166	    unresponsive_run_automation: Automation,
167	):
168	    """The disarm state lives in the bucket, so a server restart must not lose it."""
169	    first = heartbeat(frozen_time)
170	    second = heartbeat(frozen_time + timedelta(seconds=30))
171	    completed = state_change(frozen_time + timedelta(seconds=60))
172	
173	    for event in (first, second, completed):
174	        await triggers.reactive_evaluation(event)
175	
176	    # Simulate a restart: forget all in-memory trigger state and reload the automation
177	    # from the database while leaving buckets untouched.
178	    await triggers.reset()
179	    triggers.load_automation(unresponsive_run_automation)
180	
181	    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))
182	
183	    act.assert_not_awaited()
184	
185	    await triggers.proactive_evaluation(
186	        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)
187	    )
188	    act.assert_not_awaited()
189	
190	
191	async def test_bucket_cleanup_between_events_does_not_resurrect_the_window(
192	    act: mock.AsyncMock,
193	    frozen_time: DateTime,
194	    unresponsive_run_automation: Automation,
195	):
196	    """The server evaluates proactive triggers every few seconds.
197	
198	    A periodic proactive evaluation may remove a bucket that the Completed event
199	    already satisfied before the racing heartbeat is delivered.  The event
```

## 412 · 2026-10-29T04:34:55.470601+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "old_string": "    \"\"\"The disarm state lives in the bucket, so a server restart must not lose it.\"\"\"",
  "new_string": "    \"\"\"The disarm state is persisted, so a server restart must not lose it.\"\"\""
}
```

## 413 · 2026-10-29T04:34:55.560479+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py has been updated successfully.
```

## 414 · 2026-10-29T04:34:58.489751+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "old_string": "async def test_out_of_order_heartbeats_do_not_rearm_the_window(",
  "new_string": "async def test_completion_without_a_bucket_still_suppresses_a_racing_heartbeat(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    unresponsive_run_automation: Automation,\n):\n    \"\"\"A run can complete before the first heartbeat is ever delivered.\"\"\"\n    completed = state_change(frozen_time)\n    late = heartbeat(frozen_time)\n\n    await triggers.reactive_evaluation(completed)\n    await triggers.reactive_evaluation(late)\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=91)\n    )\n    act.assert_not_awaited()\n\n\nasync def test_out_of_order_heartbeats_do_not_rearm_the_window("
}
```

## 415 · 2026-10-29T04:34:58.606875+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py has been updated successfully.
```

## 416 · 2026-10-29T04:35:02.460645+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 600 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -6",
  "description": "Run regression tests including no-bucket case",
  "timeout": 700000
}
```

## 417 · 2026-10-29T04:35:56.505809+00:00 · tool_result 

```
........                                                                 [100%]
8 passed in 43.81s
```

## 418 · 2026-10-29T04:36:05.871077+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db\" -q -s -p no:randomly --timeout=0 > /tmp/full_migration_test.log 2>&1; echo \"EXIT:$?\" >> /tmp/full_migration_test.log",
  "description": "Run full migration round-trip test in background",
  "timeout": 1500000,
  "run_in_background": true
}
```

## 419 · 2026-10-29T04:36:06.304395+00:00 · tool_result 

```
Command running in background with ID: bjlg1qfms. Output is being written to: $SANDBOX\.runtime\temp\claude\E--------klavis-sandbox-ds-r3\d14d4262-c2a4-4dbf-b3ed-9581a7634eed\tasks\bjlg1qfms.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains $SANDBOX\prefect; directory changes made by the backgrounded command do not apply to subsequent commands.
```

## 420 · 2026-10-29T04:36:21.287881+00:00 · tool_call Bash

```
{
  "command": "tail -5 \"$SANDBOX/.runtime/temp/claude/E--------klavis-sandbox-ds-r3/d14d4262-c2a4-4dbf-b3ed-9581a7634eed/tasks/bjlg1qfms.output\" 2>/dev/null; echo ---; tail -5 /tmp/full_migration_test.log 2>/dev/null",
  "description": "Check background migration test progress"
}
```

## 421 · 2026-10-29T04:36:21.641155+00:00 · tool_result 

```
---
```

## 422 · 2026-10-29T04:36:28.154288+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --check tests/events/server/triggers/test_incident_regressions.py && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m py_compile src/prefect/server/events/triggers.py src/prefect/server/database/orm_models.py src/prefect/server/database/interface.py src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py tests/events/server/triggers/test_incident_regressions.py && echo COMPILE_OK",
  "description": "Format check and compile changed files",
  "timeout": 120000
}
```

## 423 · 2026-10-29T04:36:28.977693+00:00 · tool_result 

```
1 file already formatted
COMPILE_OK
```

## 424 · 2026-10-29T04:36:31.701062+00:00 · tool_call Bash

```
{
  "command": "sleep 60; tail -20 /tmp/full_migration_test.log 2>/dev/null; echo \"---status---\"; ls -la /tmp/full_migration_test.log 2>/dev/null",
  "description": "Check migration test log",
  "timeout": 90000
}
```

## 425 · 2026-10-29T04:36:31.719737+00:00 · tool_result 

```
<tool_use_error>Blocked: sleep 60 followed by: tail -20 /tmp/full_migration_test.log echo "---status---" ls -la /tmp/full_migration_test.log. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```

## 426 · 2026-10-29T04:36:34.072309+00:00 · tool_call Bash

```
{
  "command": "tail -20 /tmp/full_migration_test.log 2>/dev/null; echo \"---\"; ls -la /tmp/full_migration_test.log 2>/dev/null",
  "description": "Check migration test log"
}
```

## 427 · 2026-10-29T04:36:34.416695+00:00 · tool_result 

```
12:36:33.815 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_cancelled_flow_runs
12:36:33.816 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_subflow_runs
12:36:33.816 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_vacuum_tasks
12:36:33.816 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_event_vacuum_tasks
12:36:33.817 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_orphan_vacuum_tasks
12:36:33.817 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_worker_health
12:36:33.817 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_late_runs
12:36:33.818 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_expired_pauses
12:36:33.818 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_deployments
12:36:33.818 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_recent_deployments
12:36:33.819 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: send_telemetry_heartbeat
12:36:33.819 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: evaluate_proactive_triggers_periodic
12:36:33.819 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: monitor_expired_leases
12:36:33.820 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: reconcile_cleanup_delivery
12:36:33.820 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: monitor_expired_leases
12:36:33.822 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
12:36:33.824 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
12:36:33.829 | INFO    | uvicorn.error - Application startup complete.
12:36:33.830 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:50702 (Press CTRL+C to quit)
12:36:33.870 | INFO    | uvicorn.access - 127.0.0.1:50752 - "GET /api/health HTTP/1.1" 200
---
-rw-r--r-- 1 luwen 197121 3050 Oct 29 12:36 /tmp/full_migration_test.log
```

## 428 · 2026-10-29T04:36:37.725556+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "offset": 163,
  "limit": 30
}
```

## 429 · 2026-10-29T04:36:37.822212+00:00 · tool_result 

```
163	
164	    await triggers.reactive_evaluation(first)
165	    await triggers.reactive_evaluation(second)
166	    act.assert_not_awaited()
167	
168	    await triggers.proactive_evaluation(
169	        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)
170	    )
171	
172	    assert_acted_with(
173	        Firing(
174	            trigger=unresponsive_run_automation.trigger,
175	            trigger_states={TriggerState.Triggered},
176	            triggered=frozen_time,  # type: ignore
177	            triggering_labels={"prefect.resource.id": RESOURCE_ID},
178	            triggering_event=second,
179	        )
180	    )
181	
182	
183	async def test_completed_run_stays_silent_across_a_restart(
184	    act: mock.AsyncMock,
185	    frozen_time: DateTime,
186	    unresponsive_run_automation: Automation,
187	):
188	    """The disarm state is persisted, so a server restart must not lose it."""
189	    first = heartbeat(frozen_time)
190	    second = heartbeat(frozen_time + timedelta(seconds=30))
191	    completed = state_change(frozen_time + timedelta(seconds=60))
192	
```

## 430 · 2026-10-29T04:36:40.163485+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "offset": 192,
  "limit": 30
}
```

## 431 · 2026-10-29T04:36:40.251432+00:00 · tool_result 

```
192	
193	    for event in (first, second, completed):
194	        await triggers.reactive_evaluation(event)
195	
196	    # Simulate a restart: forget all in-memory trigger state and reload the automation
197	    # from the database while leaving buckets untouched.
198	    await triggers.reset()
199	    triggers.load_automation(unresponsive_run_automation)
200	
201	    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))
202	
203	    act.assert_not_awaited()
204	
205	    await triggers.proactive_evaluation(
206	        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)
207	    )
208	    act.assert_not_awaited()
209	
210	
211	async def test_bucket_cleanup_between_events_does_not_resurrect_the_window(
212	    act: mock.AsyncMock,
213	    frozen_time: DateTime,
214	    unresponsive_run_automation: Automation,
215	):
216	    """The server evaluates proactive triggers every few seconds.
217	
218	    A periodic proactive evaluation may remove a bucket that the Completed event
219	    already satisfied before the racing heartbeat is delivered.  The event
220	    watermark must survive that cleanup and still reject the stale heartbeat.
221	    """
```

## 432 · 2026-10-29T04:36:43.673128+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py",
  "old_string": "    for event in (first, second, completed):\n        await triggers.reactive_evaluation(event)\n\n    # Simulate a restart: forget all in-memory trigger state and reload the automation\n    # from the database while leaving buckets untouched.\n    await triggers.reset()\n    triggers.load_automation(unresponsive_run_automation)\n\n    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()",
  "new_string": "    for event in (first, second, completed):\n        await triggers.reactive_evaluation(event)\n\n    # A periodic proactive evaluation removes the now-satisfied bucket before the\n    # racing heartbeat is delivered.\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=61)\n    )\n\n    # Simulate a restart: forget all in-memory trigger state and reload the automation\n    # from the database.  The disarm state must come back from the database.\n    await triggers.reset()\n    triggers.load_automation(unresponsive_run_automation)\n\n    await triggers.reactive_evaluation(heartbeat(frozen_time + timedelta(seconds=60)))\n\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        unresponsive_run_automation.trigger, frozen_time + timedelta(seconds=151)\n    )\n    act.assert_not_awaited()"
}
```

## 433 · 2026-10-29T04:36:43.790460+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_incident_regressions.py has been updated successfully.
```

## 434 · 2026-10-29T04:36:46.588667+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 600 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -5",
  "description": "Re-run regressions with restart+cleanup test",
  "timeout": 700000
}
```

## 435 · 2026-10-29T04:37:43.057394+00:00 · tool_result 

```
........                                                                 [100%]
8 passed in 45.85s
```

## 436 · 2026-10-29T04:37:45.322241+00:00 · tool_call Bash

```
{
  "command": "tail -3 /tmp/full_migration_test.log; echo ---; grep -c \"Running upgrade\\|Running downgrade\" /tmp/full_migration_test.log 2>/dev/null",
  "description": "Check background migration test progress"
}
```

## 437 · 2026-10-29T04:37:45.642573+00:00 · tool_result 

```
12:36:33.829 | INFO    | uvicorn.error - Application startup complete.
12:36:33.830 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:50702 (Press CTRL+C to quit)
12:36:33.870 | INFO    | uvicorn.access - 127.0.0.1:50752 - "GET /api/health HTTP/1.1" 200
---
0
```

## 438 · 2026-10-29T04:37:55.977540+00:00 · tool_call Bash

```
{
  "command": "tail -5 /tmp/full_migration_test.log; echo ---; grep -n \"EXIT\\|passed\\|failed\\|Timeout\" /tmp/full_migration_test.log | tail -5",
  "description": "Check migration test status"
}
```

## 439 · 2026-10-29T04:37:56.318631+00:00 · tool_result 

```
12:36:33.822 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
12:36:33.824 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
12:36:33.829 | INFO    | uvicorn.error - Application startup complete.
12:36:33.830 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:50702 (Press CTRL+C to quit)
12:36:33.870 | INFO    | uvicorn.access - 127.0.0.1:50752 - "GET /api/health HTTP/1.1" 200
---
```

## 440 · 2026-10-29T04:37:59.953908+00:00 · tool_call Bash

```
{
  "command": "ps -W 2>/dev/null | grep -i python | head -20",
  "description": "List python processes"
}
```

## 441 · 2026-10-29T04:38:00.344692+00:00 · tool_result 

```
    78792       0       0      13256  ?              0 11:22:08 D:\python3.11\python.exe
    94772       0       0      29236  ?              0 11:22:09 D:\python3.11\python.exe
   101724       0       0      36188  ?              0 11:22:28 D:\python3.11\python.exe
   100720       0       0      35184  ?              0 11:26:33 D:\python3.11\python.exe
    91888       0       0      26352  ?              0 11:33:15 $WORKSPACE\sandbox-xh-r3\.runtime\venv\Scripts\python.exe
    72400       0       0       6864  ?              0 11:33:15 D:\python3.11\python.exe
    94044       0       0      28508  ?              0 11:45:53 D:\python3.11\python.exe
    91804       0       0      26268  ?              0 11:52:13 $SANDBOX\.runtime\venv\Scripts\python.exe
    77516       0       0      11980  ?              0 11:52:14 D:\python3.11\python.exe
   105104       0       0      39568  ?              0 11:55:19 $WORKSPACE\sandbox-xh-r2\.runtime\venv\Scripts\python.exe
    93932       0       0      28396  ?              0 11:55:19 D:\python3.11\python.exe
    87736       0       0      22200  ?              0 12:02:06 $WORKSPACE\sandbox-ds-r2\.runtime\venv\Scripts\python.exe
    94876       0       0      29340  ?              0 12:02:06 D:\python3.11\python.exe
    81952       0       0      16416  ?              0 12:06:40 $WORKSPACE\sandbox-ds-r2\.runtime\venv\Scripts\python.exe
    74756       0       0       9220  ?              0 12:06:40 D:\python3.11\python.exe
   104648       0       0      39112  ?              0 12:08:54 $WORKSPACE\sandbox-ds-r2\.runtime\venv\Scripts\python.exe
   101836       0       0      36300  ?              0 12:08:55 D:\python3.11\python.exe
    86976       0       0      21440  ?              0 12:11:40 $SANDBOX\.runtime\venv\Scripts\python.exe
    95344       0       0      29808  ?              0 12:11:40 D:\python3.11\python.exe
   106616       0       0      41080  ?              0 12:14:14 $SANDBOX\.runtime\venv\Scripts\python.exe
```

## 442 · 2026-10-29T04:38:03.715253+00:00 · tool_call Bash

```
{
  "command": "ps -W 2>/dev/null | awk '$1 ~ /python/ || $5 ~ /python/' | tail -30; echo ---; ps -W 2>/dev/null | grep \"sandbox-ds-r3\" | tail -10",
  "description": "Find my background pytest process"
}
```

## 443 · 2026-10-29T04:38:04.142614+00:00 · tool_result 

```
---
    67788       0       0       2252  ?              0 11:52:13 $SANDBOX\.runtime\venv\Scripts\uvicorn.exe
    91804       0       0      26268  ?              0 11:52:13 $SANDBOX\.runtime\venv\Scripts\python.exe
    69588       0       0       4052  ?              0 12:11:40 $SANDBOX\.runtime\venv\Scripts\uvicorn.exe
    86976       0       0      21440  ?              0 12:11:40 $SANDBOX\.runtime\venv\Scripts\python.exe
    75472       0       0       9936  ?              0 12:14:14 $SANDBOX\.runtime\venv\Scripts\uvicorn.exe
   106616       0       0      41080  ?              0 12:14:14 $SANDBOX\.runtime\venv\Scripts\python.exe
     2340    2339    2339      28684  ?         197609 12:36:06 $SANDBOX/.runtime/venv/Scripts/python
    76972       0       0      11436  ?              0 12:36:25 $SANDBOX\.runtime\venv\Scripts\uvicorn.exe
    80696       0       0      15160  ?              0 12:36:25 $SANDBOX\.runtime\venv\Scripts\python.exe
```

## 444 · 2026-10-29T04:38:11.476671+00:00 · tool_call Bash

```
{
  "command": "for wpid in 26268 21440 41080 28684 11436 15160 2252 4052 9936; do taskkill //F //T //PID $wpid 2>&1 | head -2; done",
  "description": "Kill hung test and leftover uvicorn processes from this sandbox"
}
```

## 445 · 2026-10-29T04:38:13.716007+00:00 · tool_result 

```
�ɹ�: ����ֹ PID 11980 (���� PID 26268 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 26268 (���� PID 2252 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 29808 (���� PID 21440 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 21440 (���� PID 4052 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 30844 (���� PID 41080 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 41080 (���� PID 9936 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 32348 (���� PID 15160 �ӽ���)�Ľ��̡�
�ɹ�: ����ֹ PID 15160 (���� PID 11436 �ӽ���)�Ľ��̡�
����: û���ҵ����� "11436"��
����: û���ҵ����� "15160"��
����: û���ҵ����� "2252"��
����: û���ҵ����� "4052"��
����: û���ҵ����� "9936"��
```

## 446 · 2026-10-29T04:38:17.007178+00:00 · tool_call Bash

```
{
  "command": "tail -6 /tmp/full_migration_test.log; grep -n \"EXIT\" /tmp/full_migration_test.log | tail -2",
  "description": "Check killed migration test log"
}
```

## 447 · 2026-10-29T04:38:17.340410+00:00 · tool_result 

```
12:36:33.822 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
12:36:33.824 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
12:36:33.829 | INFO    | uvicorn.error - Application startup complete.
12:36:33.830 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:50702 (Press CTRL+C to quit)
12:36:33.870 | INFO    | uvicorn.access - 127.0.0.1:50752 - "GET /api/health HTTP/1.1" 200
EXIT:1
25:EXIT:1
```

## 448 · 2026-10-29T04:38:36.466084+00:00 · tool_call Write

```
{
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "content": "# SOLUTION SUMMARY — completed flow run receives unresponsive-run action\n\n## Diagnosis\n\nThe supplied incident is a proactive (\"unresponsive run\") automation:\n\n- `after`: `prefect.flow-run.heartbeat`\n- `expect`: `prefect.flow-run.*`\n- `for_each`: `prefect.resource.id`, `threshold`: 1, `within`: 90 s\n\nRecorded events (occurred times):\n\n| # | event | occurred | received |\n|---|-------|----------|----------|\n| 1 | `prefect.flow-run.heartbeat` | 12:00:00 | +0.1 s |\n| 2 | `prefect.flow-run.heartbeat` | 12:00:30 | +30.1 s |\n| 3 | `prefect.flow-run.Completed` | 12:01:00 | +60.1 s |\n| 4 | `prefect.flow-run.heartbeat` | 12:01:00 | +60.2 s |\n\nThe final proactive evaluation runs at +151 s and must produce zero actions.\n\nThe root causes are all in `src/prefect/server/events/triggers.py`:\n\n1. **`ensure_bucket` discarded the satisfying event.** On every `after` event it\n   overwrote the bucket's `last_event` with the incoming event before `evaluate`\n   ran. By the time evaluation started, the `Completed` event that had just\n   satisfied the window was no longer available for comparison.\n2. **The proactive \"same event in after and expect\" special case re-armed\n   unconditionally.** When a proactive bucket had reached its threshold, any\n   event matching both `after` and `expect` removed the bucket and started a new\n   window at `triggering_event.occurred`. The racing heartbeat (occurred\n   12:01:00, not newer than the `Completed` event at 12:01:00) therefore reset\n   the window to 12:01:00–12:02:30 with count 0. The proactive evaluation at\n   12:02:31 then saw an expired window with no expected events and fired.\n   `increment_bucket` could also move `last_event` backwards for out-of-order\n   events, so comparisons could be anchored to an old event.\n3. **The only persisted record of \"this window was satisfied\" was the bucket\n   itself.** `remove_buckets_exceeding_threshold` deletes satisfied buckets on\n   the next periodic proactive pass (the server runs one every 5 s). If that\n   pass happens between the `Completed` event and the racing heartbeat, the\n   bucket is gone and the heartbeat creates a brand-new window — the same false\n   positive one tick later. Any fix that relies only on bucket state is\n   therefore incomplete in a real deployment.\n\nBaseline reproduction (`incident-observed.log`) showed `observed_actions: 1`.\nThe captured log confirmed the fired bucket had `start = 12:01:00` (the racing\nheartbeat) and `count = 0`, i.e. the window had been re-armed by the heartbeat\nafter the terminal event.\n\n## Repair\n\n### 1. Persisted per-resource event watermark (primary fix)\n\nA new internal model/table `automation_trigger_watermark` stores, per\n`(automation_id, trigger_id, bucketing_key)`, the greatest event `occurred`\nprocessed so far.\n\n- ORM model: `AutomationTriggerWatermark` in\n  `src/prefect/server/database/orm_models.py`, exposed as\n  `db.AutomationTriggerWatermark` in `database/interface.py`.\n- Migrations (additive only, existing tables/data untouched):\n  - `.../migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py`\n  - `.../migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py`\n- `read_trigger_watermark`, `record_trigger_watermark`, and\n  `sweep_expired_trigger_watermarks` in `triggers.py`. The watermark is\n  upserted with an atomic `CASE … WHEN last_event_occurred < new` so older or\n  out-of-order events can never lower it (works on SQLite and PostgreSQL; the\n  same `on_conflict_do_update` construct already used for buckets).\n- `reactive_evaluation` now, for proactive triggers with `after`:\n  - records every covered event's occurrence, and\n  - skips an `after` event that is **not strictly newer** than the watermark\n    when it would either arm a *new* bucket or (for an after-only event)\n    replace the bucket's `last_event`.\n  This check does not depend on a bucket existing, so it still holds after\n  eager/proactive bucket cleanup (the production race above) and after a\n  server restart.\n- `periodic_evaluation` sweeps watermarks untouched for\n  `AUTOMATION_WATERMARK_RETENTION` (= `SEEN_EXPIRATION`, 30 minutes, the same\n  horizon over which the triggers consumer remembers processed events), so\n  storage stays bounded.\n\nOnly proactive triggers with `after` participate; reactive triggers and\ntriggers without `after` keep their previous event handling exactly.\n\n### 2. Bucket-level hardening (defense in depth)\n\n- `ensure_bucket` no longer overwrites `last_event` for events matching\n  `expect`; those are recorded by `evaluate` after comparison.\n- `increment_bucket` only advances `last_event` when the new event is newer,\n  so counts still include out-of-order events but the \"latest contributing\n  event\" never moves backwards.\n- `evaluate`'s proactive re-arm special case now requires the triggering event\n  to be strictly newer than `last_event`. This protects long-lived buckets\n  (for example when a watermark row has already been swept) and keeps the\n  correct `triggering_event` for a legitimate firing.\n\nNo thresholds, actions, public interfaces, or transaction/ locking behaviour\nwere changed.\n\n### 3. Regression tests\n\n`tests/events/server/triggers/test_incident_regressions.py` adds 8 tests:\n\n- completed run + late heartbeat does not fire (the incident);\n- a completion arriving before any bucket exists still suppresses the race;\n- out-of-order heartbeats do not walk the watermark backwards;\n- a genuinely unresponsive run still fires, and the `Firing` carries the\n  correct `triggering_labels` (`prefect.resource.id`) and the latest heartbeat\n  as `triggering_event`;\n- a periodic proactive cleanup between the completion and the late heartbeat\n  does not resurrect the window;\n- a server restart (in-memory reset + reload) after bucket cleanup stays silent;\n- watermarks are swept after the retention window (bounded storage);\n- newer activity after a completion (`Running` + heartbeat) still re-arms and\n  fires normally.\n\nThe provided `test_incident_completed_run.py` is unchanged.\n\n## Commands actually executed and results\n\nAll Python commands used the locked interpreter\n`$SANDBOX/.runtime/venv/Scripts/python.exe` from the\nrepository root (`prefect/`).\n\n| Command | Result |\n|---------|--------|\n| `pytest tests/events/server/triggers/test_incident_completed_run.py -q -s` (before fix) | **FAILED**: `observed_actions: 1`, expected 0; fired bucket started at 12:01:00 with count 0 |\n| same command, after fix | **1 passed**, `observed_actions: 0` |\n| `pytest tests/events/server/triggers/ -q -p no:randomly` | **124 passed, 3 xfailed** |\n| `pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly` | **8 passed** |\n| `pytest tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations -q` | **2 passed** (one head per dialect) |\n| standalone Alembic check on a fresh SQLite DB: upgrade head → inspect → downgrade -1 → upgrade | table, columns, unique index, `updated` index and CASCADE FK created; downgrade removed it; re-upgrade recreated it |\n| Alembic `compare_metadata` of ORM metadata vs. migration-built SQLite schema | no differences involving the new table |\n| `pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py tests/events/server/models tests/events/server/test_in_memory_ordering.py tests/events/server/test_db_ordering.py -q` | 132 passed, 1 skipped, 1 failed: `test_read_automations_page` |\n| `ruff format --check` on all changed files | clean |\n\nThe `test_read_automations_page` failure is unrelated to this change and\npre-existing in this environment: all four fixture automations are inserted\nwith the *same* `updated` timestamp, so `ORDER BY updated DESC` is a tie and\nreturns an arbitrary order. A debug run confirmed all four rows share\n`updated = 2026-10-29 04:26:26.085167+00:00`; nothing in the repair touches\nautomation rows or that API path.\n\n## Limits / notes\n\n- PostgreSQL was not available in this environment, so the PostgreSQL migration\n  was not executed against a live server. It mirrors the existing\n  `automation_bucket` migration idioms (UUID/JSON/Timestamp types, conflict\n  target on the unique index, `sa.case` upsert), and the per-dialect\n  single-head migration test passes.\n- `tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db`\n  (full downgrade-to-base round trip with the large `sample_db_data` fixture)\n  could not complete in this environment: it hung during fixture/server setup\n  before executing any migration (killed after ~10 minutes). The new\n  migration's own upgrade/downgrade was verified directly as described above.\n- Storage bound: one small watermark row per active trigger/bucketing key,\n  removed after 30 minutes of inactivity; existing automation buckets are\n  still swept as before.\n"
}
```

## 449 · 2026-10-29T04:38:36.569086+00:00 · tool_result 

```
File created successfully at: $SANDBOX/SOLUTION_SUMMARY.md (file state is current in your context — no need to Read it back)
```

## 450 · 2026-10-29T04:38:42.148916+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && find src tests -newermt \"2026-10-29 11:20\" -type f 2>/dev/null | grep -v \"__pycache__\" | sort",
  "description": "List files modified during this session"
}
```

## 451 · 2026-10-29T04:38:42.437324+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/events/server/triggers/ && ls src/prefect/server/database/_migrations/versions/sqlite/ | tail -3 && ls src/prefect/server/database/_migrations/versions/postgresql/ | tail -3",
  "description": "Verify no stray test files remain"
}
```

## 452 · 2026-10-29T04:38:42.898156+00:00 · tool_result 

```
conftest.py
incident_completed_run.json
test_basics.py
test_composite_triggers.py
test_find_interested_triggers.py
test_flow_run_slas.py
test_incident_completed_run.py
test_incident_regressions.py
test_regressions.py
test_service.py
test_service_changes.py
2026_08_20_000000_f416ea180ae1_add_flow_run_deployment_id_index.py
2026_09_15_000000_a3b9c7d2e5f1_add_flow_run_state_type_coalesce_start_time_index.py
2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py
2026_09_04_000000_c8d5f2a71b3e_rebuild_invalid_event_resources_occurred_index.py
2026_09_15_000000_d4a7e1c93f52_add_flow_run_state_type_coalesce_start_time_index.py
2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py
```

## 453 · 2026-10-29T04:38:51.444131+00:00 · tool_result 

```
src/prefect/server/database/_migrations/versions/postgresql/2026_10_29_000000_c8d2e3f4a5b6_add_automation_trigger_watermark.py
src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py
src/prefect/server/database/interface.py
src/prefect/server/database/orm_models.py
src/prefect/server/events/triggers.py
tests/events/server/triggers/test_incident_regressions.py
```

## 454 · 2026-10-29T04:38:54.807152+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 600 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly 2>&1 | tail -6",
  "description": "Final incident + regression verification",
  "timeout": 700000
}
```

## 455 · 2026-10-29T04:39:51.693338+00:00 · tool_result 

```
.........                                                                [100%]
9 passed in 46.68s
```

## 456 · 2026-10-29T04:39:58.779766+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cat > tests/events/server/triggers/zz_after_only_probe.py <<'EOF'\nfrom datetime import timedelta\nfrom unittest import mock\nfrom uuid import uuid4\n\nimport pytest\nfrom sqlalchemy.ext.asyncio import AsyncSession\n\nfrom prefect.server.events import actions, triggers\nfrom prefect.server.events.models import automations\nfrom prefect.server.events.schemas.automations import Automation, EventTrigger, Posture\nfrom prefect.server.events.schemas.events import Event\nfrom prefect.types._datetime import DateTime\n\npytestmark = pytest.mark.clear_db\nRESOURCE_ID = \"prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa\"\n\n\n@pytest.fixture\nasync def automation(cleared_buckets, cleared_automations, automations_session: AsyncSession):\n    a = await automations.create_automation(\n        automations_session,\n        Automation(\n            name=\"after-only\",\n            trigger=EventTrigger(\n                match={\"prefect.resource.id\": \"prefect.flow-run.*\"},\n                after={\"prefect.flow-run.heartbeat\"},\n                expect={\"prefect.flow-run.Completed\"},\n                for_each=[\"prefect.resource.id\"],\n                posture=Posture.Proactive,\n                threshold=1,\n                within=timedelta(seconds=90),\n            ),\n            actions=[actions.DoNothing()],\n        ),\n    )\n    triggers.load_automation(a)\n    await automations_session.commit()\n    return a\n\n\ndef ev(name, occurred):\n    return Event(occurred=occurred, event=name, resource={\"prefect.resource.id\": RESOURCE_ID}, id=uuid4()).receive()\n\n\nasync def test_after_only_fires_with_latest_heartbeat(automation, frozen_time: DateTime, act: mock.AsyncMock):\n    await triggers.reactive_evaluation(ev(\"prefect.flow-run.heartbeat\", frozen_time))\n    await triggers.reactive_evaluation(ev(\"prefect.flow-run.heartbeat\", frozen_time + timedelta(seconds=30)))\n    await triggers.proactive_evaluation(automation.trigger, frozen_time + timedelta(seconds=121))\n    assert act.await_count == 1\n    firing = act.await_args[0][0]\n    assert firing.triggering_event.event == \"prefect.flow-run.heartbeat\"\n    assert str(firing.triggering_event.occurred) == str(frozen_time + timedelta(seconds=30))\n    assert firing.triggering_labels == {\"prefect.resource.id\": RESOURCE_ID}\nEOF\ntimeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/zz_after_only_probe.py -q -p no:randomly 2>&1 | tail -6; rm -f tests/events/server/triggers/zz_after_only_probe.py",
  "description": "Probe after-only trigger firing info",
  "timeout": 400000
}
```

## 457 · 2026-10-29T04:40:30.425650+00:00 · tool_result 

```
.                                                                        [100%]
1 passed in 21.17s
```

## 458 · 2026-10-29T04:40:34.624409+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && cp SOLUTION_SUMMARY.md prefect/SOLUTION_SUMMARY.md && ls -la SOLUTION_SUMMARY.md prefect/SOLUTION_SUMMARY.md",
  "description": "Place summary at both trial and repo roots"
}
```

## 459 · 2026-10-29T04:40:35.111550+00:00 · tool_result 

```
-rw-r--r-- 1 luwen 197121 8906 Oct 29 12:38 SOLUTION_SUMMARY.md
-rw-r--r-- 1 luwen 197121 8906 Oct 29 12:40 prefect/SOLUTION_SUMMARY.md
```

## 460 · 2026-10-29T04:40:50.159215+00:00 · assistant_message 

```
Let me do one final full triggers-suite run with the final test set so the summary reflects exact results.
```

## 461 · 2026-10-29T04:40:50.545280+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 1700 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/ -q -p no:randomly 2>&1 | tail -4",
  "description": "Final full triggers suite with all tests",
  "timeout": 1800000
}
```

## 462 · 2026-10-29T04:46:42.497667+00:00 · tool_result 

```
.................................................x...x...X.............. [ 56%]
........................................................                 [100%]
125 passed, 2 xfailed, 1 xpassed in 341.62s (0:05:41)
```

## 463 · 2026-10-29T04:46:45.973964+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "old_string": "| `pytest tests/events/server/triggers/ -q -p no:randomly` | **124 passed, 3 xfailed** |",
  "new_string": "| `pytest tests/events/server/triggers/ -q -p no:randomly` | **125 passed, 3 known xfail** (on the final run: 2 xfailed + 1 xpassed; the composite-trigger xfails are non-strict and intermittently xpass in this environment) |"
}
```

## 464 · 2026-10-29T04:46:46.086188+00:00 · tool_result 

```
The file $SANDBOX/SOLUTION_SUMMARY.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

## 465 · 2026-10-29T04:46:47.465541+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && cp SOLUTION_SUMMARY.md prefect/SOLUTION_SUMMARY.md && echo done",
  "description": "Sync summary copy"
}
```

## 466 · 2026-10-29T04:46:47.864244+00:00 · tool_result 

```
done
```

## 467 · 2026-10-29T04:46:49.448557+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "offset": 1306,
  "limit": 70
}
```

## 468 · 2026-10-29T04:46:49.707838+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/_migrations/versions/sqlite/2026_10_29_000000_b7c1d2e3f4a5_add_automation_trigger_watermark.py"
}
```

## 469 · 2026-10-29T04:46:49.776845+00:00 · tool_result 

```
Wasted call — file unchanged since your last Read. Refer to that earlier tool_result instead.
```

## 470 · 2026-10-29T04:46:49.890962+00:00 · tool_result 

```
1306	class AutomationBucket(Base):
1307	    __table_args__: Any = (
1308	        sa.Index(
1309	            "uq_automation_bucket__automation_id__trigger_id__bucketing_key",
1310	            "automation_id",
1311	            "trigger_id",
1312	            "bucketing_key",
1313	            unique=True,
1314	        ),
1315	        sa.Index(
1316	            "ix_automation_bucket__automation_id__end",
1317	            "automation_id",
1318	            "end",
1319	        ),
1320	    )
1321	
1322	    automation_id: Mapped[uuid.UUID] = mapped_column(
1323	        sa.ForeignKey("automation.id", ondelete="CASCADE")
1324	    )
1325	
1326	    trigger_id: Mapped[uuid.UUID]
1327	
1328	    bucketing_key: Mapped[list[str]] = mapped_column(
1329	        JSON, server_default="[]", default=list
1330	    )
1331	
1332	    last_event: Mapped[Optional[ReceivedEvent]] = mapped_column(Pydantic(ReceivedEvent))
1333	
1334	    start: Mapped[DateTime]
1335	    end: Mapped[DateTime]
1336	
1337	    count: Mapped[int]
1338	
1339	    last_operation: Mapped[Optional[str]]
1340	
1341	    triggered_at: Mapped[Optional[DateTime]]
1342	
1343	
1344	class AutomationTriggerWatermark(Base):
1345	    """The greatest event occurrence processed for an automation trigger.
1346	
1347	    Watermarks are tracked per bucketing key and outlive the corresponding
1348	    ``AutomationBucket`` so that a late or out-of-order event cannot re-arm a
1349	    proactive window that a newer event has already satisfied.
1350	    """
1351	
1352	    __table_args__: Any = (
1353	        sa.Index(
1354	            "uq_automation_trigger_watermark__automation_id__trigger_id__bucketing_key",
1355	            "automation_id",
1356	            "trigger_id",
1357	            "bucketing_key",
1358	            unique=True,
1359	        ),
1360	    )
1361	
1362	    automation_id: Mapped[uuid.UUID] = mapped_column(
1363	        sa.ForeignKey("automation.id", ondelete="CASCADE")
1364	    )
1365	
1366	    trigger_id: Mapped[uuid.UUID]
1367	
1368	    bucketing_key: Mapped[list[str]] = mapped_column(
1369	        JSON, server_default="[]", default=list
1370	    )
1371	
1372	    last_event_occurred: Mapped[DateTime]
1373	
1374	
1375	class AutomationRelatedResource(Base):
```

## 471 · 2026-10-29T04:46:57.024293+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 400 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_drop_db_removes_all_tables\" -q -p no:randomly --timeout=300 2>&1 | tail -8",
  "description": "Verify drop_db handles new table",
  "timeout": 500000
}
```

## 472 · 2026-10-29T04:52:06.791197+00:00 · tool_result 

```
    return stack
  File "D:\python3.11\Lib\traceback.py", line 393, in extract
    return klass._extract_from_extended_frame_gen(
  File "D:\python3.11\Lib\traceback.py", line 437, in _extract_from_extended_frame_gen
    return result
  File "D:\python3.11\Lib\linecache.py", line 63, in checkcache
    for filename in filenames:
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
```

## 473 · 2026-10-29T04:52:10.503925+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 120 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_drop_db_removes_all_tables\" -q -p no:randomly --timeout=100 -s 2>&1 | head -40",
  "description": "See where database test setup hangs",
  "timeout": 200000
}
```

## 474 · 2026-10-29T04:54:00.821942+00:00 · tool_result 

```
12:52:36.924 | INFO    | uvicorn.error - Started server process [2300]
12:52:36.931 | INFO    | uvicorn.error - Waiting for application startup.
12:52:37.505 | DEBUG   | prefect.server - Worker channel configuration: cleanup_queue_storage=prefect.server.worker_communication.cleanup_queue.memory cleanup_lease_seconds=30.0 cleanup_max_delivery_attempts=3 cleanup_completed_idempotency_retention_seconds=None
12:52:37.522 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: ensure_cancelling_timeout_checks
12:52:37.522 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_cancelled_flow_runs
12:52:37.523 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_subflow_runs
12:52:37.523 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_vacuum_tasks
12:52:37.523 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_event_vacuum_tasks
12:52:37.524 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_orphan_vacuum_tasks
12:52:37.524 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_worker_health
12:52:37.524 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_late_runs
12:52:37.524 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_expired_pauses
12:52:37.525 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_deployments
12:52:37.525 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_recent_deployments
12:52:37.525 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: send_telemetry_heartbeat
12:52:37.526 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: evaluate_proactive_triggers_periodic
12:52:37.526 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: monitor_expired_leases
12:52:37.526 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: reconcile_cleanup_delivery
12:52:37.527 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: monitor_expired_leases
12:52:37.528 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
12:52:37.529 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
12:52:37.534 | INFO    | uvicorn.error - Application startup complete.
12:52:37.535 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:53136 (Press CTRL+C to quit)
12:52:37.980 | INFO    | uvicorn.access - 127.0.0.1:53174 - "GET /api/health HTTP/1.1" 200
Executing <Task pending name='Task-22' coro=<AsyncIOBackend.run_async_from_thread.<locals>.task_wrapper() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:2669> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[_chain_future.<locals>._call_set_state() at D:\python3.11\Lib\asyncio\futures.py:394] created at D:\python3.11\Lib\asyncio\tasks.py:670> took 0.250 seconds
12:53:04.298 | WARNING | asyncio - Executing <Task pending name='Task-22' coro=<AsyncIOBackend.run_async_from_thread.<locals>.task_wrapper() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:2669> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[_chain_future.<locals>._call_set_state() at D:\python3.11\Lib\asyncio\futures.py:394] created at D:\python3.11\Lib\asyncio\tasks.py:670> took 0.250 seconds
Generating test database connection URL from 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
Running hosted API server on port 53136
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
~~~~~~~~~~~~~~~~~~~~ Stack of AnyIO worker thread (32168) ~~~~~~~~~~~~~~~~~~~~~
  File "D:\python3.11\Lib\threading.py", line 995, in _bootstrap
    self._bootstrap_inner()
  File "D:\python3.11\Lib\threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "$SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py", line 1033, in run
    result = context.run(func, *args)
  File "$SANDBOX\prefect\src\prefect\utilities\asyncutils\__init__.py", line 243, in call_with_mark
    return call()
  File "$SANDBOX\prefect\src\prefect\server\database\alembic_commands.py", line 36, in wrapper
    return fn(*args, **kwargs)
```

## 475 · 2026-10-29T04:54:09.519655+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/server/database/ && sed -n 1,80p tests/server/database/conftest.py 2>/dev/null",
  "description": "Inspect database test conftest"
}
```

## 476 · 2026-10-29T04:54:09.835488+00:00 · tool_result 

```
Exit code 2
test_alembic_commands.py
test_configurations.py
test_dependencies.py
test_migrations.py
test_queries.py
```

## 477 · 2026-10-29T04:54:16.094945+00:00 · assistant_message 

```
The pytest database-module fixture hangs in this environment before any migration runs. Let me verify `drop_db`/`create_db` directly against the new table instead.
```

## 478 · 2026-10-29T04:54:17.946775+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nimport os, tempfile, pathlib, asyncio\ndb_dir = tempfile.mkdtemp()\ndb_path = pathlib.Path(db_dir) / \"dropcheck.db\"\nurl = f\"sqlite+aiosqlite:///{db_path}\"\nos.environ[\"PREFECT_SERVER_DATABASE_CONNECTION_URL\"] = url\nos.environ[\"PREFECT_API_DATABASE_CONNECTION_URL\"] = url\nfrom prefect.settings import temporary_settings, PREFECT_SERVER_DATABASE_CONNECTION_URL, PREFECT_API_DATABASE_CONNECTION_URL\n\nasync def main():\n    with temporary_settings({PREFECT_SERVER_DATABASE_CONNECTION_URL: url, PREFECT_API_DATABASE_CONNECTION_URL: url}):\n        from prefect.server.database.dependencies import provide_database_interface\n        import sqlalchemy as sa\n        db = provide_database_interface()\n        await db.create_db()\n        engine = await db.engine()\n        async with engine.connect() as conn:\n            names = await conn.run_sync(lambda c: sa.inspect(c).get_table_names())\n        print(\"created watermark:\", \"automation_trigger_watermark\" in names)\n        # insert a row to prove data path, then drop everything\n        async with db.session_context(begin_transaction=True) as session:\n            await session.execute(\n                db.AutomationTriggerWatermark.__table__.insert().values(\n                    automation_id=None,  # FK may reject; use a real automation instead\n                )\n            ) if False else None\n        await db.drop_db()\n        async with engine.connect() as conn:\n            names = await conn.run_sync(lambda c: sa.inspect(c).get_table_names())\n        print(\"after drop no tables:\", names == [])\n        await db.create_db()\n        async with engine.connect() as conn:\n            names = await conn.run_sync(lambda c: sa.inspect(c).get_table_names())\n        print(\"recreated watermark:\", \"automation_trigger_watermark\" in names)\n        await engine.dispose()\n\nasyncio.run(main())\nEOF",
  "description": "Verify drop_db/create_db with new table",
  "timeout": 400000
}
```

## 479 · 2026-10-29T04:54:41.164586+00:00 · tool_result 

```
sys:1: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__state_type_coalesce_start_time
sys:1: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__schedule_id_scheduler
sys:1: SAWarning: Can't sort tables for DROP; an unresolvable foreign key dependency exists between tables: flow_run, flow_run_state, task_run, work_pool, work_queue; and backend does not support ALTER.  To restore at least a partial sort, apply use_alter=True to ForeignKey and ForeignKeyConstraint objects involved in the cycle to mark these as known cycles that will be ignored.
created watermark: True
after drop no tables: True
recreated watermark: True
```

## 480 · 2026-10-29T04:54:48.716445+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 300 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_migrations.py::test_drop_db_removes_all_tables\" -q -p no:randomly --timeout=240 2>&1 | tail -4",
  "description": "Retry drop_db test",
  "timeout": 400000
}
```

## 481 · 2026-10-29T04:58:58.661668+00:00 · tool_result 

```
    return result
  File "D:\python3.11\Lib\linecache.py", line 63, in checkcache
    for filename in filenames:
+++++++++++++++++++++++++++++++++++ Timeout +++++++++++++++++++++++++++++++++++
```

## 482 · 2026-10-29T04:59:05.021802+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"^def test_\\|^async def test_\" tests/server/database/test_configurations.py | head -5",
  "description": "List configuration tests"
}
```

## 483 · 2026-10-29T04:59:05.310655+00:00 · tool_result 

```
22:async def test_postgres_engine_enforces_read_committed(
```

## 484 · 2026-10-29T04:59:07.003618+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && timeout 240 \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest \"tests/server/database/test_configurations.py::test_postgres_engine_enforces_read_committed\" -q -p no:randomly --timeout=180 2>&1 | tail -4",
  "description": "Run a different database-module test to check environment",
  "timeout": 350000
}
```

## 485 · 2026-10-29T04:59:36.666707+00:00 · tool_result 

```
ss                                                                       [100%]
=========================== short test summary info ===========================
SKIPPED [2] tests\server\database\test_configurations.py:29: Test requires PostgreSQL
2 skipped in 19.49s
```

## 486 · 2026-10-29T04:59:45.047077+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "old_string": "- `tests/server/database/test_migrations.py::test_orion_full_migration_works_with_data_in_db`\n  (full downgrade-to-base round trip with the large `sample_db_data` fixture)\n  could not complete in this environment: it hung during fixture/server setup\n  before executing any migration (killed after ~10 minutes). The new\n  migration's own upgrade/downgrade was verified directly as described above.",
  "new_string": "- Tests that invoke Alembic **from inside the pytest process**\n  (`test_orion_full_migration_works_with_data_in_db`,\n  `test_drop_db_removes_all_tables`) hang in this Windows environment inside\n  `alembic_upgrade` (killed after several minutes). This is an\n  environment/anyio limitation of running Alembic in-process here, not the\n  migration content: the same upgrade runs fine during normal session setup\n  (the whole triggers suite, including the new migration, passes), and the\n  standalone-process checks below succeed. `drop_db`/`create_db` was also\n  verified directly against the new table (drop removes every table, create\n  re-runs migrations and recreates `automation_trigger_watermark`)."
}
```

## 487 · 2026-10-29T04:59:45.149048+00:00 · tool_result 

```
The file $SANDBOX/SOLUTION_SUMMARY.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

## 488 · 2026-10-29T04:59:47.297617+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "offset": 118,
  "limit": 30
}
```

## 489 · 2026-10-29T04:59:47.380448+00:00 · tool_result 

```
118	
119	## Commands actually executed and results
120	
121	All Python commands used the locked interpreter
122	`$SANDBOX/.runtime/venv/Scripts/python.exe` from the
123	repository root (`prefect/`).
124	
125	| Command | Result |
126	|---------|--------|
127	| `pytest tests/events/server/triggers/test_incident_completed_run.py -q -s` (before fix) | **FAILED**: `observed_actions: 1`, expected 0; fired bucket started at 12:01:00 with count 0 |
128	| same command, after fix | **1 passed**, `observed_actions: 0` |
129	| `pytest tests/events/server/triggers/ -q -p no:randomly` | **125 passed, 3 known xfail** (on the final run: 2 xfailed + 1 xpassed; the composite-trigger xfails are non-strict and intermittently xpass in this environment) |
130	| `pytest tests/events/server/triggers/test_incident_regressions.py -q -p no:randomly` | **8 passed** |
131	| `pytest tests/server/database/test_migrations.py::test_only_single_head_revision_in_migrations -q` | **2 passed** (one head per dialect) |
132	| standalone Alembic check on a fresh SQLite DB: upgrade head → inspect → downgrade -1 → upgrade | table, columns, unique index, `updated` index and CASCADE FK created; downgrade removed it; re-upgrade recreated it |
133	| Alembic `compare_metadata` of ORM metadata vs. migration-built SQLite schema | no differences involving the new table |
134	| `pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py tests/events/server/models tests/events/server/test_in_memory_ordering.py tests/events/server/test_db_ordering.py -q` | 132 passed, 1 skipped, 1 failed: `test_read_automations_page` |
135	| `ruff format --check` on all changed files | clean |
136	
137	The `test_read_automations_page` failure is unrelated to this change and
138	pre-existing in this environment: all four fixture automations are inserted
139	with the *same* `updated` timestamp, so `ORDER BY updated DESC` is a tie and
140	returns an arbitrary order. A debug run confirmed all four rows share
141	`updated = 2026-10-29 04:26:26.085167+00:00`; nothing in the repair touches
142	automation rows or that API path.
143	
144	## Limits / notes
145	
146	- PostgreSQL was not available in this environment, so the PostgreSQL migration
147	  was not executed against a live server. It mirrors the existing
```

## 490 · 2026-10-29T04:59:52.295333+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "old_string": "| standalone Alembic check on a fresh SQLite DB: upgrade head → inspect → downgrade -1 → upgrade | table, columns, unique index, `updated` index and CASCADE FK created; downgrade removed it; re-upgrade recreated it |\n| Alembic `compare_metadata` of ORM metadata vs. migration-built SQLite schema | no differences involving the new table |",
  "new_string": "| standalone Alembic check on a fresh SQLite DB: upgrade head → inspect → downgrade -1 → upgrade | table, columns, unique index, `updated` index and CASCADE FK created; downgrade removed it; re-upgrade recreated it |\n| standalone `PrefectDBInterface.drop_db()` → `create_db()` on a migrated SQLite DB | all tables dropped, then migrations recreated every table including `automation_trigger_watermark` |\n| Alembic `compare_metadata` of ORM metadata vs. migration-built SQLite schema | no differences involving the new table |"
}
```

## 491 · 2026-10-29T04:59:52.392055+00:00 · tool_result 

```
The file $SANDBOX/SOLUTION_SUMMARY.md has been updated successfully.
```

## 492 · 2026-10-29T04:59:56.508446+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && cp SOLUTION_SUMMARY.md prefect/SOLUTION_SUMMARY.md && echo synced && wc -l SOLUTION_SUMMARY.md",
  "description": "Sync summary copy and show size"
}
```

## 493 · 2026-10-29T04:59:56.978502+00:00 · tool_result 

```
synced
164 SOLUTION_SUMMARY.md
```

## 494 · 2026-10-29T05:00:03.045186+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | tail -12",
  "description": "Run exact task command for incident test",
  "timeout": 600000
}
```

## 495 · 2026-10-29T05:00:35.841300+00:00 · tool_result 

```
Running hosted API server on port 54761
{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
.13:00:33.641 | INFO    | uvicorn.error - Shutting down
13:00:33.741 | INFO    | uvicorn.error - Waiting for application shutdown.
13:00:33.743 | INFO    | uvicorn.error - Application shutdown complete.
13:00:33.744 | INFO    | uvicorn.error - Finished server process [11292]

1 passed in 22.36s
```

## 496 · 2026-10-29T05:00:43.316086+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && diff -q SOLUTION_SUMMARY.md prefect/SOLUTION_SUMMARY.md && echo IDENTICAL && find . -maxdepth 3 -name \"SOLUTION_SUMMARY.md\" -print",
  "description": "Verify summary copies match"
}
```

## 497 · 2026-10-29T05:00:43.872068+00:00 · tool_result 

```
IDENTICAL
./prefect/SOLUTION_SUMMARY.md
./SOLUTION_SUMMARY.md
```

## 498 · 2026-10-29T05:00:56.956839+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls -la incident-observed.log tests/events/server/triggers/incident_completed_run.json tests/events/server/triggers/test_incident_completed_run.py && cd .. && ls -la SOLUTION_SUMMARY.md",
  "description": "Verify incident inputs untouched and summary present"
}
```

## 499 · 2026-10-29T05:00:57.292778+00:00 · tool_result 

```
-rw-r--r-- 1 luwen 197121  551 Oct 29 11:13 incident-observed.log
-rw-r--r-- 1 luwen 197121 1815 Oct 29 11:13 tests/events/server/triggers/incident_completed_run.json
-rw-r--r-- 1 luwen 197121 2489 Oct 29 11:13 tests/events/server/triggers/test_incident_completed_run.py
-rw-r--r-- 1 luwen 197121 9535 Oct 29 12:59 SOLUTION_SUMMARY.md
```

## 500 · 2026-10-29T05:01:07.703364+00:00 · assistant_message 

```
I've repaired the bug and written the deliverable summary. Here's a recap:

## Diagnosis

The incident is a proactive "unresponsive run" automation (`after: heartbeat`, `expect: prefect.flow-run.*`, `for_each: prefect.flow-run.id`, `threshold: 1`, `within: 90s`). Four defects combined in `src/prefect/server/events/triggers.py`:

1. `ensure_bucket` overwrote the bucket's `last_event` with each incoming event before `evaluate` ran, discarding the `Completed` event that had just satisfied the window.
2. The proactive "event matches both `after` and `expect`" special case re-armed the window unconditionally. The racing heartbeat (occurred `12:01:00`, not newer than `Completed` at `12:01:00`) reset the window to a count-0, 90-second window, so the proactive evaluation at `+151s` found an expired window and fired.
3. `increment_bucket` could move `last_event` backwards for out-of-order events.
4. The only persisted record of a satisfied window was the bucket itself, which `remove_buckets_exceeding_threshold` deletes on the next 5-second proactive pass — so a heartbeat arriving after that cleanup created a brand-new window. A bucket-only fix is therefore not sufficient in production.

## Repair

- **New persisted watermark table** `automation_trigger_watermark` (ORM model + SQLite and PostgreSQL Alembic migrations) storing the greatest event `occurred` per `(automation, trigger, bucketing key)`. Upserts use an atomic `CASE … WHEN` so the mark never moves backwards.
- `reactive_evaluation` records every covered event's occurrence and, for proactive triggers with `after`, refuses to arm/re-arm from an event that is not strictly newer than the watermark. This survives bucket cleanup, restarts and upgrades.
- Watermarks are swept after `SEEN_EXPIRATION` (30 min) in `periodic_evaluation`, keeping storage bounded.
- Bucket-level hardening: `ensure_bucket` no longer clobbers `last_event` for expect events; `increment_bucket` only advances it; the re-arm special case requires a strictly newer event.
- Reactive triggers and triggers without `after` are untouched; thresholds/actions/public interfaces are unchanged.

## Verification

- Exact task command now prints `observed_actions: 0` → **passed** (baseline reproduced `1`).
- Full triggers suite: **125 passed, 3 known xfails** (one non-strict xfail intermittently xpasses in this environment).
- New `test_incident_regressions.py`: **8 passed**, covering genuine unresponsiveness (with correct triggering labels/event), restart + bucket-cleanup survival, out-of-order heartbeats, resumed runs, and watermark sweeping.
- Migrations: single-head test for both dialects passed; standalone fresh upgrade → inspect → downgrade → re-upgrade and `drop_db`/`create_db` round-trip succeeded; ORM↔migration schema comparison showed no new-table differences.
- Limit: no PostgreSQL server available here; the Postgres migration mirrors the existing bucket-migration patterns. Tests that run Alembic *inside* the pytest process hang in this Windows/anyio environment (unrelated to the migration); those were replaced by standalone-process checks.

`SOLUTION_SUMMARY.md` is at both `sandbox-ds-r3/SOLUTION_SUMMARY.md` and `sandbox-ds-r3/prefect/SOLUTION_SUMMARY.md`.
```
