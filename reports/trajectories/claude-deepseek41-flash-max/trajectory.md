# 可见操作轨迹

时间戳保留 UTC。路径已用占位符替换；内部推理、系统消息、协作消息正文及本地通用技能正文未导出。
工具调用和结果是实际记录；省略处明确标记。模型的公开自述不等于作者侧验收结论。

## 1 · 2026-10-28T08:11:36.040675+00:00 · tool_call Bash

```
{
  "command": "ls -la \"$SANDBOX\"",
  "description": "List root directory contents"
}
```

## 2 · 2026-10-28T08:11:36.270348+00:00 · tool_call Bash

```
{
  "command": "ls -la \"$SANDBOX/prefect\" | head -60",
  "description": "List prefect directory contents"
}
```

## 3 · 2026-10-28T08:11:39.031558+00:00 · tool_result 

```
total 22
drwxr-xr-x 1 luwen 197121    0 Oct 28 16:07 .
drwxr-xr-x 1 luwen 197121    0 Oct 28 16:05 ..
drwxr-xr-x 1 luwen 197121    0 Oct 28 16:11 .runtime
-rw-r--r-- 1 luwen 197121  285 Oct 28 16:05 AGENTS.md
-rw-r--r-- 1 luwen 197121  285 Oct 28 16:07 CLAUDE.md
-rw-r--r-- 1 luwen 197121 2987 Oct 28 16:05 TASK.md
drwxr-xr-x 1 luwen 197121    0 Oct 28 16:05 prefect
```

## 4 · 2026-10-28T08:11:39.143716+00:00 · tool_result 

```
total 1282
drwxr-xr-x 1 luwen 197121       0 Oct 28 16:05 .
drwxr-xr-x 1 luwen 197121       0 Oct 28 16:07 ..
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
-rw-r--r-- 1 luwen 197121     551 Oct 28 16:05 incident-observed.log
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
```

## 5 · 2026-10-28T08:11:40.122857+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/AGENTS.md"
}
```

## 6 · 2026-10-28T08:11:40.242610+00:00 · tool_result 

```
1	# Independent diagnostic trial
2	
3	Read TASK.md and solve it directly.
4	Keep task reads/writes under this working root. No parent/sibling files,
5	prior solutions or task-specific online answers. Generic installed skills
6	may be read. Implementation is authorized; finish autonomously.
7	
```

## 7 · 2026-10-28T08:11:40.274405+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/TASK.md"
}
```

## 8 · 2026-10-28T08:11:40.369116+00:00 · tool_result 

````
1	You are independently solving a software-engineering task in a fresh session.
2	Your working root is $SANDBOX.
3	Only inspect and modify task files under this root. Do not read parent/sibling
4	directories, other Codex sessions, previous attempts, author materials, references,
5	or saved patches. Do not search for task-specific online solutions or PR discussions.
6	General installed tool documentation and applicable generic skills are allowed.
7	Respect the repository's coding/testing conventions. Implementation is authorized:
8	work autonomously, do not pause for design approval or contact upstream maintainers.
9	The locked development dependencies are already installed in .runtime/venv.
10	On Windows, source .runtime/environment.ps1 from this root (or
11	../.runtime/environment.ps1 from prefect/) before Python commands to use the isolated
12	interpreter, home, SQLite database, temporary files and caches. Use $TrialPython for
13	that interpreter. Never connect to an existing user database.
14	Deliver the source changes and SOLUTION_SUMMARY.md with diagnosis, commands actually
15	executed, results and limits. Do not delegate or switch models.
16	
17	Some completed flow runs still receive the automation action intended for an unresponsive run. The flow's event history shows that it completed, yet its monitoring automation later acts on it as though it had stopped responding.
18	
19	The source is at `$SANDBOX/prefect`. An incident reproduction is included in the repository. It uses synthetic, anonymized event records and the real server evaluation path; outgoing actions are captured rather than executed.
20	
21	From the repository root, run:
22	
23	```sh
24	python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s
25	```
26	
27	The accompanying `incident_completed_run.json` contains the automation configuration and recorded events. `incident-observed.log` contains captured replay output from this version. The replay prints the observed action count. The completed run in this incident should produce **zero** unresponsive-run actions.
28	
29	Investigate the failure, identify its cause in the existing code, and deliver a general repair. A genuinely unresponsive run must still cause its configured action. Actions that legitimately fire must retain correct information about the affected resource and triggering event.
30	
31	Preserve existing automation behavior, public interfaces and deployment concurrency behavior. The repair must work with SQLite, survive server restarts and upgrades without losing existing data, and keep storage use bounded during continued operation. Do not change monitoring thresholds or disable actions to suppress the symptom.
32	
33	You may add regression tests. No UI build, external services or real workflow worker is required. Deliver the repaired source and a brief description of the diagnosis and verification performed.
34	
````

## 9 · 2026-10-28T08:11:40.423332+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/AGENTS.md"
}
```

## 10 · 2026-10-28T08:11:40.608884+00:00 · tool_result 

````
1	Prefect is a workflow orchestration platform that coordinates and observes data pipelines. It provides a Python SDK for building workflows, a server backend for orchestration, and a web-based UI for managing and monitoring workflows.
2	
3	# Guiding Principles
4	
5	Your primary responsibility is to the project and its users. Every change should serve the broader user base — not just the immediate request. Be a quality gate: prefer correct, minimal, well-tested changes over fast ones.
6	
7	# Before You Start
8	
9	Before making code changes, read the public contribution guide in `docs/contribute/dev-contribute.mdx` so your work follows Prefect's contribution expectations, design principles, AI-use policy, testing standards, and maintainer review criteria.
10	For documentation-only changes, also read `docs/contribute/docs-contribute.mdx`.
11	For integration changes, also read `docs/contribute/contribute-integrations.mdx`.
12	
13	# Directory Structure
14	
15	```
16	prefect/
17	├── benches/                         # Benchmarks (CLI, flows, tasks, imports)
18	├── client/                          # prefect-client build: subset of src/prefect/ published as a separate PyPI package
19	├── compat-tests/                    # Tests for REST API compatibility with Prefect Cloud
20	├── Dockerfile                       # Production container image
21	├── docs/                            # Mintlify documentation (see docs/AGENTS.md)
22	├── examples/                        # Example flows (auto-published to docs)
23	├── formal/                          # Executable formal models (see formal/tla/AGENTS.md)
24	├── integration-tests/               # End-to-end integration tests (require running server)
25	├── justfile                         # Task runner (just <command>)
26	├── load_testing/                    # Load/performance testing
27	├── plans/                           # Design/implementation plan documents
28	├── pyproject.toml                   # Root package config
29	├── schemas/                         # JSON schemas (prefect.yaml, settings)
30	├── scripts/                         # Code generation and release scripts
31	├── src/
32	│   ├── integrations/                # External service integrations (see src/integrations/AGENTS.md)
33	│   └── prefect/                     # Core package: SDK, server, CLI (see src/prefect/AGENTS.md)
34	├── tests/                           # Test suite, mirrors src/prefect/ (see tests/AGENTS.md)
35	├── tools/                           # Build tools
36	├── ui/                              # Vue UI (legacy, will be replaced by ui-v2)
37	├── ui-v2/                           # React UI rewrite (see ui-v2/AGENTS.md)
38	└── uv.lock                          # Lockfile (auto-generated, do not edit manually)
39	```
40	
41	# Essential Commands
42	
43	```bash
44	# Dependencies
45	uv sync                                # Install all dev dependencies
46	just install                           # Same as above, plus perf group
47	
48	# Running code
49	uv run -s my_script.py                             # Run a script with an editable prefect install
50	uv run --extra aws repros/1234.py                  # Run repro needing an integration extra
51	uv run --project ./src/integrations/<name> <cmd>   # Run against a local integration from repo root
52	prefect server start                               # Start local server
53	prefect config view                                # Inspect current configuration
54	
55	# Testing (see tests/AGENTS.md for full details)
56	uv run pytest tests/path.py -k name    # Run specific test
57	uv run pytest tests/path.py -x -n4     # Parallel, stop on first failure
58	
59	# Linting & formatting
60	uv run ruff check --fix .              # Lint with auto-fix
61	uv run ruff format .                   # Format code
62	uv run pre-commit run --all-files      # Run all pre-commit hooks
63	
64	# Docs (from repo root)
65	just docs                              # Start Mintlify dev server at localhost:3000
66	just generate-docs                     # Regenerate all doc artifacts
67	
68	# UI (from repo root)
69	just ui-v2                             # Start React dev server at localhost:5173
70	
71	# Docker
72	docker build -t prefect .                              # Default build (Python 3.11)
73	docker build --build-arg PYTHON_VERSION=3.12 -t prefect .  # Custom Python version
74	docker build --build-arg EXTRA_PIP_PACKAGES="prefect-aws" -t prefect .  # With extras
75	```
76	
77	## Quick Reference
78	
79	| Component | Path | Tests |
80	|-----------|------|-------|
81	| Core SDK (flows, tasks, states, deployments) | `src/prefect/` | `tests/` |
82	| Flow & task engines (async orchestration) | `src/prefect/flow_engine.py`, `task_engine.py` | `tests/engine/` |
83	| Client SDK (schemas, HTTP client) | `src/prefect/client/` | `tests/client/` |
84	| Server (API, database, scheduling) | `src/prefect/server/` | `tests/server/` |
85	| CLI | `src/prefect/cli/` | `tests/cli/` |
86	| Settings | `src/prefect/settings/` | `tests/settings/` |
87	| Integrations (`prefect-aws`, `prefect-dbt`, etc.) | `src/integrations/` | per-integration |
88	| React UI (replacing Vue `ui/`) | `ui-v2/` | `ui-v2/e2e/` |
89	
90	## Tech Stack & Tooling
91	
92	- **Python >=3.11,<3.15** with modern typing (`list[int]`, `T | None`)
93	- **FastAPI** for REST APIs
94	- **Pydantic v2** for validation
95	- **SQLAlchemy 2.0** async ORM
96	- **Alembic** for database migrations
97	- **PostgreSQL/SQLite** databases
98	- **React + TypeScript** for UI (see ui-v2/AGENTS.md)
99	- **Ruff** for linting and formatting
100	- **Pre-commit** hooks: ruff, codespell, mypy (partial), uv-lock, no-commit-to-branch
101	
102	## Architecture Overview
103	
104	- **Three user-facing surfaces**: Python SDK (`@flow`/`@task` decorators), CLI (`prefect` command), REST API (FastAPI server)
105	- **Server is the source of truth for flow state transitions** — the flow engine proposes states, and the server's orchestration layer accepts or rejects them. Task state transitions are managed locally by the task engine via `set_state` and communicated through `prefect.task_run.*` events
106	- **Two published packages**: `prefect` (full SDK + server) and `prefect-client` (lightweight client subset). `client/` contains the build config that selects which files from `src/prefect/` go into `prefect-client`
107	- **Integrations are separate PyPI packages** (`prefect-aws`, `prefect-dbt`, etc.) each with their own version, published independently from `src/integrations/`
108	- **Async-first execution model** with sync wrappers — the engines (`flow_engine.py`, `task_engine.py`) are async; sync `@flow`/`@task` functions are run in workers
109	
110	## Anti-patterns
111	
112	- **Never bypass the server for flow state transitions** — always go through the orchestration API, even in tests. Task state transitions are managed locally by the task engine by design
113	- **Never use `pip install` or `uv pip`** — use `uv` for all dependency management
114	- **Never use deferred imports** (imports inside functions) unless required to break circular imports or for optional dependencies
115	- **Never commit directly to `main`** — a pre-commit hook enforces this
116	- **Never skip pre-commit hooks** (`--no-verify`) — fix the underlying issue instead
117	- **Never amend commits** (`--amend`) — create new commits instead
118	
119	# Development Guidelines
120	
121	## Make sure you have a Prefect server or Prefect Cloud
122	- use `prefect config view` to check your current profile
123	- run `prefect server start` in the background if needed
124	
125	## Code Conventions
126	
127	- Private implementation details (`_private_method`)
128	- No public API changes without approval
129	- Use single backticks for inline code references in docstrings, not double backticks
130	
131	## Testing
132	
133	- Directory structure mirrors source code
134	- Run affected tests after changes: `uv run pytest tests/module/`
135	- Tests require deterministic behavior
136	- Mock external dependencies
137	
138	## Formal Protocol Models
139	
140	- Use TLA+ selectively for bounded concurrent or distributed protocols whose correctness depends on interleavings, retries, duplication, time, or ownership. Prefer ordinary tests for local or sequential behavior.
141	- Treat each `formal/tla/<protocol>/README.md` as the authority for its scope, configurations, action-to-code mapping, owner, and review triggers.
142	- Before changing mapped behavior, review the model and its deterministic regressions. Update them when the abstraction changes; otherwise state in the PR why it remains valid.
143	- A green model validates only its documented abstraction, not Prefect's implementation. Implementation evidence comes from mapped behavior and contract tests.
144	
145	## Working on Issues
146	
147	- Read the GitHub issue/PR and comments (`gh issue view`, `gh pr view`) before writing code
148	- Understand the scope and intended behavior — ask clarifying questions if unclear
149	- Create reproduction scripts in `repros/` directory (create it if needed; add to `.gitignore`)
150	- Name files by issue number: `repros/1234.py` (only create one file per issue)
151	- Ensure the issue is reproducible before fixing
152	- Add unit tests for fixes
153	- DO NOT delete files from `repros/` directory after reproducing the issue unless asked
154	
155	## PR Body Style
156	
157	- Start with "closes #1234" if resolving issue
158	- Brief summary: "this PR {changes}"
159	- Details in `<details>` tag
160	- Include relevant links
161	
162	## Code Review Rules
163	
164	When reviewing changes, read and apply [REVIEW.md](REVIEW.md).
165	
166	# Project Practices
167	
168	- All PRs require test coverage for new functionality
169	- GitHub issues are used for tracking issues (use the `gh` cli)
170	- Dependencies: updates to client-side deps in `pyproject.toml` require parallel changes in `client/pyproject.toml`
171	- AGENTS.md always symlinked to CLAUDE.md
172	
````

## 11 · 2026-10-28T08:11:41.680651+00:00 · tool_call Bash

```
{
  "command": "find \"$SANDBOX/prefect\" -iname \"*incident*\" -o -iname \"incident-observed.log\" | head -50",
  "description": "Find incident files"
}
```

## 12 · 2026-10-28T08:11:41.924705+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/events/server/triggers/ 2>/dev/null",
  "description": "List trigger test directory"
}
```

## 13 · 2026-10-28T08:11:42.198601+00:00 · tool_result 

```
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

## 14 · 2026-10-28T08:11:42.752808+00:00 · tool_result 

```
$SANDBOX/prefect/docs/images/incidents1.png
$SANDBOX/prefect/docs/images/incidents2.png
$SANDBOX/prefect/docs/v3/img/ui/declare-incident.png
$SANDBOX/prefect/docs/v3/img/ui/incidents-dashboard.png
$SANDBOX/prefect/incident-observed.log
$SANDBOX/prefect/tests/events/server/triggers/incident_completed_run.json
$SANDBOX/prefect/tests/events/server/triggers/test_incident_completed_run.py
```

## 15 · 2026-10-28T08:11:43.610254+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_incident_completed_run.py"
}
```

## 16 · 2026-10-28T08:11:43.752599+00:00 · tool_result 

```
1	"""Replay the supplied synthetic incident through the server's event evaluator."""
2	
3	import json
4	from datetime import timedelta
5	from pathlib import Path
6	from unittest.mock import AsyncMock
7	
8	import pytest
9	from prefect.server.events import triggers
10	from prefect.server.events.models import automations
11	from prefect.server.events.schemas.automations import Automation
12	from prefect.server.events.schemas.events import Event
13	from prefect.types._datetime import parse_datetime
14	
15	pytestmark = pytest.mark.clear_db
16	
17	
18	async def test_completed_run_incident(
19	    automations_session, cleared_buckets, cleared_automations, frozen_time, monkeypatch
20	):
21	    incident = json.loads(
22	        Path(__file__).with_name("incident_completed_run.json").read_text("utf-8")
23	    )
24	    action_sink = AsyncMock()
25	    monkeypatch.setattr(triggers, "act", action_sink)
26	    automation = await automations.create_automation(
27	        automations_session, Automation.model_validate(incident["automation"])
28	    )
29	    triggers.load_automation(automation)
30	    await automations_session.commit()
31	
32	    # Shift the synthetic time anchor to the test clock, preserving all intervals.
33	    anchor = parse_datetime(incident["time_anchor"])
34	    for record in incident["records"]:
35	        payload = {key: record[key] for key in ("id", "occurred", "event", "resource")}
36	        payload["occurred"] = frozen_time + (
37	            parse_datetime(record["occurred"]) - anchor
38	        )
39	        event = Event.model_validate(payload).receive(
40	            received=frozen_time + timedelta(seconds=record["received_offset_seconds"])
41	        )
42	        print(
43	            json.dumps(
44	                {
45	                    "received_sequence": record["received_sequence"],
46	                    "event": record["event"],
47	                    "occurred": record["occurred"],
48	                }
49	            )
50	        )
51	        await triggers.reactive_evaluation(event)
52	
53	    await triggers.proactive_evaluation(
54	        automation.trigger,
55	        frozen_time + timedelta(seconds=incident["evaluate_at_offset_seconds"]),
56	    )
57	    observed = action_sink.await_count
58	    print(
59	        json.dumps(
60	            {
61	                "incident_id": incident["incident_id"],
62	                "observed_actions": observed,
63	                "expected_actions": incident["expected_actions"],
64	            }
65	        )
66	    )
67	    assert observed == incident["expected_actions"], (
68	        f"Completed run received {observed} unresponsive-run action(s); expected zero"
69	    )
70	
```

## 17 · 2026-10-28T08:11:43.770276+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/incident-observed.log"
}
```

## 18 · 2026-10-28T08:11:43.870120+00:00 · tool_result 

```
1	Captured baseline replay output; input records are synthetic.
2	{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
3	{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
4	{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
5	{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
6	{"incident_id": "completed-run-001", "observed_actions": 1, "expected_actions": 0}
7	
```

## 19 · 2026-10-28T08:11:44.705083+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/incident_completed_run.json"
}
```

## 20 · 2026-10-28T08:11:44.803079+00:00 · tool_result 

```
1	{
2	  "fixture_provenance": "Synthetic incident; identifiers and time anchor are artificial. Execution output is captured separately from actual replay.",
3	  "incident_id": "completed-run-001",
4	  "time_anchor": "2026-10-20T12:00:00Z",
5	  "automation": {
6	    "name": "Unresponsive run monitor",
7	    "trigger": {
8	      "match": {"prefect.resource.id": "prefect.flow-run.*"},
9	      "after": ["prefect.flow-run.heartbeat"],
10	      "expect": ["prefect.flow-run.*"],
11	      "for_each": ["prefect.resource.id"],
12	      "posture": "Proactive",
13	      "threshold": 1,
14	      "within": 90
15	    },
16	    "actions": [{"type": "do-nothing"}]
17	  },
18	  "records": [
19	    {"received_sequence": 1, "received_offset_seconds": 0.1, "id": "11111111-1111-4111-8111-111111111111", "occurred": "2026-10-20T12:00:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
20	    {"received_sequence": 2, "received_offset_seconds": 30.1, "id": "22222222-2222-4222-8222-222222222222", "occurred": "2026-10-20T12:00:30Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
21	    {"received_sequence": 3, "received_offset_seconds": 60.1, "id": "33333333-3333-4333-8333-333333333333", "occurred": "2026-10-20T12:01:00Z", "event": "prefect.flow-run.Completed", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
22	    {"received_sequence": 4, "received_offset_seconds": 60.2, "id": "44444444-4444-4444-8444-444444444444", "occurred": "2026-10-20T12:01:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}}
23	  ],
24	  "evaluate_at_offset_seconds": 151,
25	  "expected_actions": 0
26	}
27	
```

## 21 · 2026-10-28T08:11:48.672178+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/events/ src/prefect/server/events/triggers* 2>/dev/null | head -60",
  "description": "List events module files"
}
```

## 22 · 2026-10-28T08:11:48.938138+00:00 · tool_call Grep

```
{
  "pattern": "def proactive_evaluation|async def proactive_evaluation",
  "path": "$SANDBOX/prefect/src/prefect/server/events",
  "output_mode": "content"
}
```

## 23 · 2026-10-28T08:11:49.303042+00:00 · tool_result 

```
src/prefect/server/events/triggers.py

src/prefect/server/events/:
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
```

## 24 · 2026-10-28T08:11:49.570778+00:00 · tool_result 

```
src\prefect\server\events\triggers.py:1307:async def proactive_evaluation(
```

## 25 · 2026-10-28T08:11:50.498539+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py"
}
```

## 26 · 2026-10-28T08:11:50.708372+00:00 · tool_result 

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

## 27 · 2026-10-28T08:11:52.168767+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class EventTrigger\" -A 260 src/prefect/server/events/schemas/automations.py",
  "description": "Read EventTrigger schema"
}
```

## 28 · 2026-10-28T08:11:52.536897+00:00 · tool_result 

```
289:class EventTrigger(ResourceTrigger):
290-    """
291-    A trigger that fires based on the presence or absence of events within a given
292-    period of time.
293-    """
294-
295-    type: Literal["event"] = "event"
296-
297-    after: Set[str] = Field(
298-        default_factory=set,
299-        description=(
300-            "The event(s) which must first been seen to fire this trigger.  If "
301-            "empty, then fire this trigger immediately.  Events may include "
302-            "trailing wildcards, like `prefect.flow-run.*`"
303-        ),
304-    )
305-    expect: Set[str] = Field(
306-        default_factory=set,
307-        description=(
308-            "The event(s) this trigger is expecting to see.  If empty, this "
309-            "trigger will match any event.  Events may include trailing wildcards, "
310-            "like `prefect.flow-run.*`"
311-        ),
312-    )
313-
314-    for_each: Set[str] = Field(
315-        default_factory=set,
316-        description=(
317-            "Evaluate the trigger separately for each distinct value of these labels "
318-            "on the resource.  By default, labels refer to the primary resource of the "
319-            "triggering event.  You may also refer to labels from related "
320-            "resources by specifying `related:<role>:<label>`.  This will use the "
321-            "value of that label for the first related resource in that role.  For "
322-            'example, `"for_each": ["related:flow:prefect.resource.id"]` would '
323-            "evaluate the trigger for each flow."
324-        ),
325-    )
326-    posture: Literal[Posture.Reactive, Posture.Proactive] = Field(  # type: ignore[valid-type]
327-        ...,
328-        description=(
329-            "The posture of this trigger, either Reactive or Proactive.  Reactive "
330-            "triggers respond to the _presence_ of the expected events, while "
331-            "Proactive triggers respond to the _absence_ of those expected events."
332-        ),
333-    )
334-    threshold: int = Field(
335-        1,
336-        description=(
337-            "The number of events required for this trigger to fire (for "
338-            "Reactive triggers), or the number of events expected (for Proactive "
339-            "triggers)"
340-        ),
341-    )
342-    within: timedelta = Field(
343-        timedelta(seconds=0),
344-        ge=timedelta(seconds=0),
345-        description=(
346-            "The time period over which the events must occur.  For Reactive triggers, "
347-            "this may be as low as 0 seconds, but must be at least 10 seconds for "
348-            "Proactive triggers"
349-        ),
350-    )
351-
352-    @model_validator(mode="before")
353-    @classmethod
354-    def enforce_minimum_within_for_proactive_triggers(
355-        cls, data: Dict[str, Any] | Any
356-    ) -> Dict[str, Any]:
357-        if not isinstance(data, dict):
358-            return data
359-
360-        if "within" in data and data["within"] is None:
361-            raise ValueError("`within` should be a valid timedelta")
362-
363-        posture: Optional[Posture] = data.get("posture")
364-        within: Optional[timedelta] = data.get("within")
365-
366-        if isinstance(within, (int, float)):
367-            data["within"] = within = timedelta(seconds=within)
368-
369-        if posture == Posture.Proactive:
370-            if not within or within == timedelta(0):
371-                data["within"] = timedelta(seconds=10.0)
372-            elif within < timedelta(seconds=10.0):
373-                raise ValueError(
374-                    "`within` for Proactive triggers must be greater than or equal to "
375-                    "10 seconds"
376-                )
377-
378-        return data
379-
380-    def covers(self, event: ReceivedEvent) -> bool:
381-        if not self.event_pattern.match(event.event):
382-            return False
383-
384-        if not self.covers_resources(event.resource, event.related):
385-            return False
386-
387-        return True
388-
389-    @property
390-    def immediate(self) -> bool:
391-        """Does this reactive trigger fire immediately for all events?"""
392-        return self.posture == Posture.Reactive and self.within == timedelta(0)
393-
394-    _event_pattern: Optional[re.Pattern[str]] = PrivateAttr(None)
395-
396-    @property
397-    def event_pattern(self) -> re.Pattern[str]:
398-        """A regular expression which may be evaluated against any event string to
399-        determine if this trigger would be interested in the event"""
400-        if self._event_pattern:
401-            return self._event_pattern
402-
403-        if not self.expect:
404-            # This preserves the trivial match for `expect`, and matches the behavior
405-            # of expects() below
406-            self._event_pattern = re.compile(".+")
407-        else:
408-            patterns = [
409-                # escape each pattern, then translate wildcards ('*' -> r'.+')
410-                re.escape(e).replace("\\*", ".+")
411-                for e in self.expect | self.after
412-            ]
413-            self._event_pattern = re.compile("|".join(patterns))
414-
415-        return self._event_pattern
416-
417-    def starts_after(self, event: str) -> bool:
418-        # Warning: Previously we returned 'True' if there was trivial 'after' criteria.
419-        # Although this is not wrong, it led to automations processing more events
420-        # than they should have.
421-        if not self.after:
422-            return False
423-
424-        for candidate in self.after:
425-            if matches(candidate, event):
426-                return True
427-        return False
428-
429-    def expects(self, event: str) -> bool:
430-        if not self.expect:
431-            return True
432-
433-        for candidate in self.expect:
434-            if matches(candidate, event):
435-                return True
436-        return False
437-
438-    def bucketing_key(self, event: ReceivedEvent) -> Tuple[str, ...]:
439-        return tuple(
440-            event.find_resource_label(label) or "" for label in sorted(self.for_each)
441-        )
442-
443-    def meets_threshold(self, event_count: int) -> bool:
444-        if self.posture == Posture.Reactive and event_count >= self.threshold:
445-            return True
446-
447-        if self.posture == Posture.Proactive and event_count < self.threshold:
448-            return True
449-
450-        return False
451-
452-    def create_automation_state_change_event(
453-        self, firing: Firing, trigger_state: TriggerState
454-    ) -> ReceivedEvent:
455-        """Returns a ReceivedEvent for an automation state change
456-        into a triggered or resolved state."""
457-        automation = firing.trigger.automation
458-        triggering_event = firing.triggering_event
459-
460-        resource_data = Resource(
461-            {
462-                "prefect.resource.id": f"prefect.automation.{automation.id}",
463-                "prefect.resource.name": automation.name,
464-            }
465-        )
466-
467-        if self.posture.value:
468-            resource_data["prefect.posture"] = self.posture.value
469-
470-        return ReceivedEvent(
471-            occurred=firing.triggered,
472-            event=f"prefect.automation.{trigger_state.value.lower()}",
473-            resource=resource_data,
474-            related=(
475-                [
476-                    RelatedResource(
477-                        {
478-                            "prefect.resource.id": f"prefect.event.{triggering_event.id}",
479-                            "prefect.resource.role": "triggering-event",
480-                        }
481-                    )
482-                ]
483-                if triggering_event
484-                else []
485-            ),
486-            payload={
487-                "triggering_labels": firing.triggering_labels,
488-                "triggering_event": (
489-                    triggering_event.model_dump(mode="json")
490-                    if triggering_event
491-                    else None
492-                ),
493-            },
494-            id=uuid7(),
495-        )
496-
497-
498-ServerTriggerTypes: TypeAlias = Union[EventTrigger, CompoundTrigger, SequenceTrigger]
499-"""The union of all concrete trigger types that a user may actually create"""
500-
501-T = TypeVar("T", bound=Trigger)
502-
503-
504-class AutomationCore(PrefectBaseModel, extra="ignore"):
505-    """Defines an action a user wants to take when a certain number of events
506-    do or don't happen to the matching resources"""
507-
508-    name: str = Field(default=..., description="The name of this automation")
509-    description: str = Field(
510-        default="", description="A longer description of this automation"
511-    )
512-
513-    enabled: bool = Field(
514-        default=True, description="Whether this automation will be evaluated"
515-    )
516-    tags: list[str] = Field(
517-        default_factory=list,
518-        description="A list of tags associated with this automation",
519-    )
520-
521-    trigger: ServerTriggerTypes = Field(
522-        default=...,
523-        description=(
524-            "The criteria for which events this Automation covers and how it will "
525-            "respond to the presence or absence of those events"
526-        ),
527-    )
528-
529-    actions: list[ServerActionTypes] = Field(
530-        default=...,
531-        description="The actions to perform when this Automation triggers",
532-    )
533-
534-    actions_on_trigger: list[ServerActionTypes] = Field(
535-        default_factory=list,
536-        description="The actions to perform when an Automation goes into a triggered state",
537-    )
538-
539-    actions_on_resolve: list[ServerActionTypes] = Field(
540-        default_factory=list,
541-        description="The actions to perform when an Automation goes into a resolving state",
542-    )
543-
544-    def triggers(self) -> Sequence[Trigger]:
545-        """Returns all triggers within this automation"""
546-        return self.trigger.all_triggers()
547-
548-    def triggers_of_type(self, trigger_type: Type[T]) -> Sequence[T]:
549-        """Returns all triggers of the specified type within this automation"""
```

## 29 · 2026-10-28T08:12:00.331423+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls src/prefect/server/events/ordering/ && wc -l src/prefect/server/events/ordering/*.py",
  "description": "List ordering module"
}
```

## 30 · 2026-10-28T08:12:00.705968+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && wc -l tests/events/server/triggers/test_regressions.py tests/events/server/triggers/test_basics.py src/prefect/server/events/schemas/automations.py",
  "description": "Line counts of related files"
}
```

## 31 · 2026-10-28T08:12:00.761224+00:00 · tool_result 

```
__init__.py
db.py
memory.py
   99 src/prefect/server/events/ordering/__init__.py
  183 src/prefect/server/events/ordering/db.py
  314 src/prefect/server/events/ordering/memory.py
  596 total
```

## 32 · 2026-10-28T08:12:01.032333+00:00 · tool_result 

```
  980 tests/events/server/triggers/test_regressions.py
  918 tests/events/server/triggers/test_basics.py
  818 src/prefect/server/events/schemas/automations.py
 2716 total
```

## 33 · 2026-10-28T08:12:02.007481+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/ordering/memory.py"
}
```

## 34 · 2026-10-28T08:12:02.149619+00:00 · tool_result 

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

## 35 · 2026-10-28T08:12:07.771560+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && git status 2>&1 | head -5; ls -a | head; cat .git 2>/dev/null | head",
  "description": "Check git repo presence"
}
```

## 36 · 2026-10-28T08:12:08.122979+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"terminal\" src/prefect/server/events/ | head -30",
  "description": "Search terminal references"
}
```

## 37 · 2026-10-28T08:12:08.256097+00:00 · tool_result 

```
fatal: not a git repository (or any of the parent directories): .git
.
..
.claude
.dockerignore
.github
.gitignore
.gitmodules
.nvmrc
.pre-commit-config.yaml
.prefectignore
```

## 38 · 2026-10-28T08:12:08.512125+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:230:        # terminal state within a given time.
```

## 39 · 2026-10-28T08:12:10.437673+00:00 · tool_call Bash

```
{
  "command": "cat \"$SANDBOX/.runtime/environment.ps1\" 2>/dev/null | head -80; ls \"$SANDBOX/.runtime\"",
  "description": "Inspect runtime environment script"
}
```

## 40 · 2026-10-28T08:12:10.773135+00:00 · tool_result 

```
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
claude-config
environment.ps1
prefect-home
pycache
python
ruff-cache
temp
uv-cache
venv
```

## 41 · 2026-10-28T08:12:12.204531+00:00 · tool_call Bash

```
{
  "command": "echo \"PREFECT_HOME=$PREFECT_HOME\"; echo \"PYTHONPATH=$PYTHONPATH\"; echo \"DB=$PREFECT_SERVER_DATABASE_CONNECTION_URL\"; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -c \"import sys, prefect; print(sys.version); print(prefect.__version__); print(prefect.__file__)\"",
  "description": "Check environment and prefect import"
}
```

## 42 · 2026-10-28T08:12:17.788190+00:00 · tool_result 

```
PREFECT_HOME=$SANDBOX/.runtime/prefect-home
PYTHONPATH=$SANDBOX/prefect/src
DB=sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db
3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]
3.6.24+nogit
$SANDBOX\prefect\src\prefect\__init__.py
```

## 43 · 2026-10-28T08:12:18.870812+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | tail -40",
  "description": "Run incident reproduction test",
  "timeout": 300000
}
```

## 44 · 2026-10-28T08:13:24.118484+00:00 · tool_result 

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
INFO     prefect.server.events.triggers:triggers.py:586 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4, trigger a1488cde-8a31-44ac-9941-ae10a7074756 covers event 'prefect.flow-run.heartbeat' (11111111-1111-4111-8111-111111111111) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:13:17.646887+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 ('Unresponsive run monitor') trigger a1488cde-8a31-44ac-9941-ae10a7074756 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4, trigger a1488cde-8a31-44ac-9941-ae10a7074756 covers event 'prefect.flow-run.heartbeat' (22222222-2222-4222-8222-222222222222) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:13:47.646887+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 ('Unresponsive run monitor') trigger a1488cde-8a31-44ac-9941-ae10a7074756 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4, trigger a1488cde-8a31-44ac-9941-ae10a7074756 covers event 'prefect.flow-run.Completed' (33333333-3333-4333-8333-333333333333) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:14:17.646887+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 ('Unresponsive run monitor') trigger a1488cde-8a31-44ac-9941-ae10a7074756 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
INFO     prefect.server.events.triggers:triggers.py:586 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4, trigger a1488cde-8a31-44ac-9941-ae10a7074756 covers event 'prefect.flow-run.heartbeat' (44444444-4444-4444-8444-444444444444) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:14:17.646887+00:00'
DEBUG    prefect.server.events.triggers:triggers.py:214 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 ('Unresponsive run monitor') trigger a1488cde-8a31-44ac-9941-ae10a7074756 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
DEBUG    prefect.server.events.triggers:triggers.py:1317 Evaluating automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 trigger a1488cde-8a31-44ac-9941-ae10a7074756 proactively as of 2026-10-28 08:15:48.646887+00:00 (offset 0.0s)
DEBUG    prefect.server.events.triggers:triggers.py:176 Automation 76f302e0-8a9e-4d5f-97fd-544b74077bc4 ('Unresponsive run monitor') trigger a1488cde-8a31-44ac-9941-ae10a7074756 triggered for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa']) proactively, having occurred 0 times between 2026-10-28 08:14:17.646887+00:00 and 2026-10-28 08:15:47.646887+00:00
=========================== short test summary info ===========================
FAILED tests/events/server/triggers/test_incident_completed_run.py::test_completed_run_incident
1 failed in 28.42s
```

## 45 · 2026-10-28T08:13:27.551947+00:00 · tool_call Grep

```
{
  "pattern": "flow-run\\.heartbeat",
  "path": "$SANDBOX/prefect",
  "output_mode": "content",
  "-n": true,
  "head_limit": 80
}
```

## 46 · 2026-10-28T08:13:39.150252+00:00 · tool_result 

```
incident-observed.log:2:{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
incident-observed.log:3:{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
incident-observed.log:5:{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
schemas\settings.schema.json:1910:                        "prefect.flow-run.heartbeat": "P7D"
schemas\settings.schema.json:1912:                    "description": "Per-event-type retention period overrides. Keys are event type strings (e.g. 'prefect.flow-run.heartbeat'), values are retention periods in seconds. Event types not listed fall back to server.events.retention_period. Each override is capped by the global events retention period.",
tests\events\server\triggers\test_regressions.py:853:                after={"prefect.flow-run.heartbeat"},
tests\events\server\triggers\test_regressions.py:878:        event="prefect.flow-run.heartbeat",
tests\events\server\triggers\test_regressions.py:884:        event="prefect.flow-run.heartbeat",
tests\events\server\triggers\incident_completed_run.json:9:      "after": ["prefect.flow-run.heartbeat"],
tests\events\server\triggers\incident_completed_run.json:19:    {"received_sequence": 1, "received_offset_seconds": 0.1, "id": "11111111-1111-4111-8111-111111111111", "occurred": "2026-10-20T12:00:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
tests\events\server\triggers\incident_completed_run.json:20:    {"received_sequence": 2, "received_offset_seconds": 30.1, "id": "22222222-2222-4222-8222-222222222222", "occurred": "2026-10-20T12:00:30Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}},
tests\events\server\triggers\incident_completed_run.json:22:    {"received_sequence": 4, "received_offset_seconds": 60.2, "id": "44444444-4444-4444-8444-444444444444", "occurred": "2026-10-20T12:01:00Z", "event": "prefect.flow-run.heartbeat", "resource": {"prefect.resource.id": "prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"}}
tests\test_flow_runs.py:77:            event="prefect.flow-run.heartbeat",
tests\test_flow_engine.py:5989:            if kwargs.get("event") == "prefect.flow-run.heartbeat":
tests\test_flow_engine.py:6017:            if kwargs.get("event") == "prefect.flow-run.heartbeat":
tests\test_flow_engine.py:6057:        assert emitted_events[0]["event"] == "prefect.flow-run.heartbeat"
tests\test_flow_engine.py:6081:        assert emitted_events[0]["event"] == "prefect.flow-run.heartbeat"
tests\test_flow_engine.py:6420:            if kwargs.get("event") == "prefect.flow-run.heartbeat":
docs\v3\release-notes\oss\version-3-1.mdx:382:        after={"prefect.flow-run.heartbeat"},
docs\v3\release-notes\oss\version-3-1.mdx:384:            "prefect.flow-run.heartbeat",
tests\server\services\test_db_vacuum.py:788:        await _create_event(db, "prefect.flow-run.heartbeat", OLD)
tests\server\services\test_db_vacuum.py:801:        await _create_event(db, "prefect.flow-run.heartbeat", RECENT)
tests\server\services\test_db_vacuum.py:832:        await _create_event(db, "prefect.flow-run.heartbeat", eighteen_hours_ago)
tests\server\services\test_db_vacuum.py:848:            {"prefect.flow-run.heartbeat": timedelta(hours=2)},
tests\server\services\test_db_vacuum.py:853:        await _create_event(db, "prefect.flow-run.heartbeat", four_hours_ago)
tests\server\services\test_db_vacuum.py:871:        await _create_event(db, "prefect.flow-run.heartbeat", OLD)
tests\server\services\test_db_vacuum.py:881:        event = await _create_event(db, "prefect.flow-run.heartbeat", OLD)
tests\server\services\test_db_vacuum.py:1014:        await _create_event(db, "prefect.flow-run.heartbeat", OLD)
tests\test_settings.py:476:        "test_value": '{"prefect.flow-run.heartbeat": 3600}',
tests\test_settings.py:477:        "expected_value": {"prefect.flow-run.heartbeat": timedelta(hours=1)},
tests\test_settings.py:1313:            '{"prefect.flow-run.heartbeat": -1}',
tests\test_settings.py:3020:        # tables, but event types like "prefect.flow-run.heartbeat" need to be
tests\test_settings.py:3024:            "prefect.flow-run.heartbeat" = 3600
tests\test_settings.py:3034:                    "prefect.flow-run.heartbeat": timedelta(hours=1),
src\prefect\flow_engine.py:548:            event="prefect.flow-run.heartbeat",
src\prefect\settings\models\server\services.py:160:        default={"prefect.flow-run.heartbeat": timedelta(days=7)},
src\prefect\settings\models\server\services.py:161:        description="Per-event-type retention period overrides. Keys are event type strings (e.g. 'prefect.flow-run.heartbeat'), values are retention periods in seconds. Event types not listed fall back to server.events.retention_period. Each override is capped by the global events retention period.",
ui-v2\src\components\automations\trigger-details\trigger-utils.ts:179: * `prefect.flow-run.heartbeat`) are only editable as a custom trigger.
ui-v2\src\components\automations\trigger-details\trigger-utils.test.ts:607:					after: ["prefect.flow-run.heartbeat"],
ui-v2\src\components\automations\trigger-details\trigger-utils.test.ts:616:					expect: ["prefect.flow-run.heartbeat"],
ui-v2\src\components\automations\trigger-details\trigger-utils.test.ts:732:					after: ["prefect.flow-run.heartbeat"],
docs\v3\api-ref\settings-ref.mdx:2116:Per-event-type retention period overrides. Keys are event type strings (e.g. 'prefect.flow-run.heartbeat'), values are retention periods in seconds. Event types not listed fall back to server.events.retention_period. Each override is capped by the global events retention period.
docs\v3\api-ref\settings-ref.mdx:2120:**Default**: `{'prefect.flow-run.heartbeat': 'P7D'}`
ui-v2\src\components\automations\automations-wizard\trigger-step\flow-run-state-trigger-fields.tsx:40:// Events that are not known state names (e.g. "prefect.flow-run.heartbeat") are ignored
ui-v2\src\components\automations\automations-wizard\trigger-step\flow-run-state-trigger-fields.test.tsx:164:				defaultAfter={["prefect.flow-run.heartbeat"]}
ui-v2\src\components\automations\automations-wizard\trigger-step\flow-run-state-trigger-fields.test.tsx:165:				defaultExpect={["prefect.flow-run.heartbeat"]}
docs\v3\advanced\detect-zombie-flows.mdx:55:        after={"prefect.flow-run.heartbeat"},
docs\v3\advanced\detect-zombie-flows.mdx:101:    "prefect.flow-run.heartbeat",
docs\v3\advanced\database-maintenance.mdx:249:| `PREFECT_SERVER_SERVICES_DB_VACUUM_EVENT_RETENTION_OVERRIDES` | `{"prefect.flow-run.heartbeat": 604800}` | Per-event-type retention period overrides in seconds. Event types not listed fall back to `PREFECT_SERVER_EVENTS_RETENTION_PERIOD`. Each override is capped by the global events retention period. |
docs\v3\api-ref\rest-api\server\schema.json:24989:                        "description": "Per-event-type retention period overrides. Keys are event type strings (e.g. 'prefect.flow-run.heartbeat'), values are retention periods in seconds. Event types not listed fall back to server.events.retention_period. Each override is capped by the global events retention period.",
docs\v3\api-ref\rest-api\server\schema.json:24991:                            "prefect.flow-run.heartbeat": "P7D"
ui-v2\src\api\prefect.ts:10115:             * @description Per-event-type retention period overrides. Keys are event type strings (e.g. 'prefect.flow-run.heartbeat'), values are retention periods in seconds. Event types not listed fall back to server.events.retention_period. Each override is capped by the global events retention period.
ui-v2\src\api\prefect.ts:10117:             *       "prefect.flow-run.heartbeat": "P7D"
docs\v3\api-ref\events\index.mdx:66:| `prefect.flow-run.heartbeat` | Periodic flow run liveness signal | [Flow run events](/v3/api-ref/events/flow-run-events) |
docs\v3\api-ref\events\flow-run-events.mdx:127:## `prefect.flow-run.heartbeat`
```

## 47 · 2026-10-28T08:13:39.967506+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/docs/v3/advanced/detect-zombie-flows.mdx"
}
```

## 48 · 2026-10-28T08:13:40.094156+00:00 · tool_result 

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

## 49 · 2026-10-28T08:13:40.249031+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '800,980p' tests/events/server/triggers/test_regressions.py",
  "description": "Read heartbeat regression tests"
}
```

## 50 · 2026-10-28T08:13:40.618827+00:00 · tool_result 

```
    # Verify not fired yet
    act.assert_not_awaited()

    # Send another Running event within the window (e.g., a heartbeat)
    # This should trigger the special case condition in event.py lines 189-195
    second_running_event = Event(
        occurred=frozen_time + timedelta(minutes=30),
        event="prefect.flow-run.Running",
        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
        related=[],
        payload={},
        id=uuid4(),
    ).receive()

    # Process the second Running event - this hits the special case
    await triggers.reactive_evaluation(second_running_event)

    # Still shouldn't fire yet (within window)
    act.assert_not_awaited()

    # After the 2-hour window from the SECOND event, should fire
    await triggers.proactive_evaluation(
        proactive_flow_run_automation.trigger,
        frozen_time + timedelta(minutes=30) + timedelta(hours=2, minutes=1),
    )

    # Verify the automation fired with the correct triggering_event
    # The triggering_event should be the second Running event (the one that restarted the bucket)
    assert_acted_with(
        Firing(
            trigger=proactive_flow_run_automation.trigger,
            trigger_states={TriggerState.Triggered},
            triggered=frozen_time,  # type: ignore
            triggering_labels={
                "prefect.resource.id": f"prefect.flow-run.{flow_run_id}"
            },
            triggering_event=second_running_event,  # Should be the second Running event
        )
    )


@pytest.fixture
async def zombie_flow_detection_automation(
    cleared_buckets: None,
    cleared_automations: None,
    automations_session: AsyncSession,
) -> Automation:
    automation = await automations.create_automation(
        automations_session,
        Automation(
            name="Crash zombie flows",
            trigger=EventTrigger(
                match={"prefect.resource.id": "prefect.flow-run.*"},
                after={"prefect.flow-run.heartbeat"},
                expect={"prefect.flow-run.*"},
                for_each={"prefect.resource.id"},
                posture=Posture.Proactive,
                threshold=1,
                within=timedelta(seconds=90),
            ),
            actions=[actions.DoNothing()],
        ),
    )
    triggers.load_automation(automation)
    await automations_session.commit()
    return automation


async def test_zombie_flow_detection_fires_when_heartbeats_stop(
    act: mock.AsyncMock,
    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
    frozen_time: DateTime,
    zombie_flow_detection_automation: Automation,
):
    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
    flow_run_id = uuid4()
    first_heartbeat = Event(
        occurred=frozen_time,
        event="prefect.flow-run.heartbeat",
        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
        id=uuid4(),
    ).receive()
    second_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=30),
        event="prefect.flow-run.heartbeat",
        resource={"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"},
        id=uuid4(),
    ).receive()

    await triggers.reactive_evaluation(first_heartbeat)
    await triggers.reactive_evaluation(second_heartbeat)
    act.assert_not_awaited()

    await triggers.proactive_evaluation(
        zombie_flow_detection_automation.trigger,
        frozen_time + timedelta(seconds=31),
    )
    act.assert_not_awaited()

    await triggers.proactive_evaluation(
        zombie_flow_detection_automation.trigger,
        frozen_time + timedelta(seconds=121),
    )

    assert_acted_with(
        Firing(
            trigger=zombie_flow_detection_automation.trigger,
            trigger_states={TriggerState.Triggered},
            triggered=frozen_time,  # type: ignore
            triggering_labels={
                "prefect.resource.id": f"prefect.flow-run.{flow_run_id}"
            },
            triggering_event=second_heartbeat,
        )
    )


@pytest.fixture
async def proactive_extended_expect_and_after_with_threshold_1(
    cleared_buckets: None,
    cleared_automations: None,
    automations_session: AsyncSession,
) -> Automation:
    automation = await automations.create_automation(
        automations_session,
        Automation(
            name="Both expect and after",
            trigger=EventTrigger(
                for_each=["prefect.resource.id"],
                after=["some-event"],
                expect=["some-event"],
                posture=Posture.Proactive,
                threshold=1,
                within=timedelta(minutes=5),
            ),
            actions=[actions.DoNothing()],
        ),
    )
    triggers.load_automation(automation)
    await automations_session.commit()
    return automation


async def test_same_event_in_expect_and_after_proactively_fires_with_for_each_threshold_1(
    act: mock.AsyncMock,
    frozen_time: DateTime,
    proactive_extended_expect_and_after_with_threshold_1: Automation,
):
    """
    During the test, an event is emitted every minute starting at t=1.
    Proactive automations are run every 5 minutes, starting at t=0
    """
    assert isinstance(
        proactive_extended_expect_and_after_with_threshold_1.trigger, EventTrigger
    )

    evaluate_proactive_times = range(0, 15, 5)
    heartbeat_times = range(1, 3)

    for minute in range(0, 11):
        if minute in evaluate_proactive_times:
            act.reset_mock()
            await triggers.proactive_evaluation(
                proactive_extended_expect_and_after_with_threshold_1.trigger,
                frozen_time + timedelta(minutes=minute),
            )

            if minute != 10:
                act.assert_not_awaited()
            else:
                act.assert_awaited_once()

        if minute in heartbeat_times:
            await triggers.reactive_evaluation(
                Event(
                    occurred=frozen_time + timedelta(minutes=minute),
                    event="some-event",
                    resource={"prefect.resource.id": "some.resource"},
                    id=uuid4(),
                ).receive()
            )
```

## 51 · 2026-10-28T08:13:49.307539+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '500,610p' src/prefect/flow_engine.py",
  "description": "Read heartbeat emission code"
}
```

## 52 · 2026-10-28T08:13:49.537453+00:00 · tool_result 

```
        }

        tags: list[str] = list(self.flow_run.tags or [])

        if self.flow_run.flow_id:
            related.append(
                RelatedResource.model_validate(
                    {
                        "prefect.resource.id": f"prefect.flow.{self.flow_run.flow_id}",
                        "prefect.resource.role": "flow",
                        "prefect.resource.name": self.flow.name if self.flow else "",
                    }
                )
            )

        if self.flow_run.deployment_id:
            related.append(
                RelatedResource.model_validate(
                    {
                        "prefect.resource.id": f"prefect.deployment.{self.flow_run.deployment_id}",
                        "prefect.resource.role": "deployment",
                    }
                )
            )

        related += tags_as_related_resources(set(tags))

        return resource, related

    def _emit_flow_run_heartbeat(
        self,
        resource: dict[str, str] | None = None,
        related: list[RelatedResource] | None = None,
    ) -> None:
        """Emit a heartbeat event for the current flow run.

        Args:
            resource: Pre-computed resource dict from _build_heartbeat_event_template.
            related: Pre-computed related list from _build_heartbeat_event_template.
                If not provided, builds the template on the fly (backward compat).
        """
        if not self.flow_run:
            return

        if resource is None or related is None:
            resource, related = self._build_heartbeat_event_template()

        emit_event(
            event="prefect.flow-run.heartbeat",
            resource=resource,
            related=related,
        )

    def _update_otel_labels(
        self, span: trace.Span, client: Union[SyncPrefectClient, PrefectClient]
    ):
        parent_flow_run_ctx = FlowRunContext.get()

        if parent_flow_run_ctx and parent_flow_run_ctx.flow_run:
            if traceparent := parent_flow_run_ctx.flow_run.labels.get(
                LABELS_TRACEPARENT_KEY
            ):
                carrier: KeyValueLabels = {TRACEPARENT_KEY: traceparent}
                propagate.get_global_textmap().inject(
                    carrier={TRACEPARENT_KEY: traceparent},
                    setter=OTELSetter(),
                )

            else:
                carrier: KeyValueLabels = {}
                propagate.get_global_textmap().inject(
                    carrier,
                    context=trace.set_span_in_context(span),
                    setter=OTELSetter(),
                )
            if carrier.get(TRACEPARENT_KEY):
                if self.flow_run:
                    client.update_flow_run_labels(
                        flow_run_id=self.flow_run.id,
                        labels={LABELS_TRACEPARENT_KEY: carrier[TRACEPARENT_KEY]},
                    )
                else:
                    self.logger.info(
                        f"Tried to set traceparent {carrier[TRACEPARENT_KEY]} for flow run, but None was found"
                    )

    def _engine_owns_cancellation_handling(self) -> bool:
        """Return whether this engine owns cancellation state and hooks.

        Runner-managed subprocesses set `PREFECT__ENABLE_CANCELLATION_AND_CRASHED_HOOKS=false`
        and retain ownership of acknowledged cancellation state and hooks.
        Engine-reported Crashed states are different: their hooks remain
        engine-owned and are not governed by this switch. Same-process nested
        subflows have no external supervisor, so the engine ignores suppression
        when it started inside a non-detached parent `FlowRunContext`. Top-level
        non-runner flows also fall through to engine ownership because the env
        defaults to enabled.
        """

        return self._started_with_in_process_parent_flow_run_context or (
            os.environ.get(
                "PREFECT__ENABLE_CANCELLATION_AND_CRASHED_HOOKS", "true"
            ).lower()
            == "true"
        )

    def _get_flow_run_suspension_request(self) -> FlowRunSuspensionRequest:
        parent_flow_run_context = FlowRunContext.get()
        if parent_flow_run_context:
            return parent_flow_run_context.flow_run_suspension_request
        return self._flow_run_suspension_request
```

## 53 · 2026-10-28T08:13:49.608127+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"heartbeat\" -n src/prefect/flow_engine.py | head -30",
  "description": "Locate heartbeat code in flow engine"
}
```

## 54 · 2026-10-28T08:13:49.897628+00:00 · tool_result 

```
306:def _send_heartbeats(
310:    """Context manager that maintains heartbeats for a flow run using a daemon thread.
312:    Uses a background OS thread instead of an asyncio task so that heartbeats
316:        engine: The flow run engine instance to emit heartbeats for.
317:        join_on_exit: Whether to join the heartbeat thread on exit. Set to
323:    heartbeat_seconds = engine.heartbeat_seconds
324:    if heartbeat_seconds is None:
327:    heartbeat_seconds = max(heartbeat_seconds, MINIMUM_HEARTBEAT_INTERVAL)
329:    # Pre-compute the event template once to minimize per-heartbeat GIL hold time
330:    resource, related = engine._build_heartbeat_event_template()
334:    def heartbeat_loop() -> None:
342:                engine.logger.debug("Flow run in terminal state, stopping heartbeat")
346:                engine._emit_flow_run_heartbeat(resource, related)
348:                engine.logger.debug("Failed to emit heartbeat", exc_info=True)
351:            for _ in range(heartbeat_seconds):
356:    # Copy the current context so the heartbeat thread sees the same
362:    # the heartbeat path to spawn an ephemeral `SubprocessASGIServer` during
365:    heartbeat_ctx = contextvars.copy_context()
367:        target=heartbeat_ctx.run, args=(heartbeat_loop,), daemon=True
370:    engine.logger.debug("Started flow run heartbeat context")
378:        engine.logger.debug("Stopped flow run heartbeat context")
383:    help="Use `_send_heartbeats` instead.",
386:def send_heartbeats_sync(
389:    with _send_heartbeats(engine, join_on_exit=True):
395:    help="Use `_send_heartbeats` instead.",
398:async def send_heartbeats_async(
401:    with _send_heartbeats(engine, join_on_exit=False):
450:    def heartbeat_seconds(self) -> Optional[int]:
451:        """Get the heartbeat interval from settings."""
452:        value = get_current_settings().flows.heartbeat_frequency
```

## 55 · 2026-10-28T08:13:51.139458+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/flow_engine.py",
  "offset": 300,
  "limit": 100
}
```

## 56 · 2026-10-28T08:13:51.245776+00:00 · tool_result 

```
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
380	
381	@deprecated_callable(
382	    start_date=datetime.datetime(2026, 3, 1),
383	    help="Use `_send_heartbeats` instead.",
384	)
385	@contextmanager
386	def send_heartbeats_sync(
387	    engine: "FlowRunEngine[Any, Any]",
388	) -> Generator[None, None, None]:
389	    with _send_heartbeats(engine, join_on_exit=True):
390	        yield
391	
392	
393	@deprecated_callable(
394	    start_date=datetime.datetime(2026, 3, 1),
395	    help="Use `_send_heartbeats` instead.",
396	)
397	@asynccontextmanager
398	async def send_heartbeats_async(
399	    engine: "AsyncFlowRunEngine[Any, Any]",
```

## 57 · 2026-10-28T08:14:05.571787+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"follows\" src/prefect/server/events/schemas/events.py | head -40",
  "description": "Find follows field in event schema"
}
```

## 58 · 2026-10-28T08:14:05.618324+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"follows\" src/prefect/server/ | head -50",
  "description": "Find follows usage server-side"
}
```

## 59 · 2026-10-28T08:14:05.862895+00:00 · tool_result 

```
141:    follows: Optional[UUID] = Field(
```

## 60 · 2026-10-28T08:14:06.092258+00:00 · tool_result 

```
src/prefect/server/database/orm_models.py:1459:    follows: Mapped[Optional[uuid.UUID]]
src/prefect/server/database/_migrations/versions/postgresql/2024_04_10_194742_15768c2ec702_add_events_and_event_resources_tables.py:107:        sa.Column("follows", prefect.server.utilities.database.UUID(), nullable=True),
src/prefect/server/database/_migrations/versions/sqlite/2024_04_10_104304_824e9edafa60_adds_events_tables.py:106:        sa.Column("follows", prefect.server.utilities.database.UUID(), nullable=True),
src/prefect/server/events/actions.py:163:            # Only set follows if timing is tight (within 5 minutes) to avoid unnecessary
src/prefect/server/events/actions.py:164:            # waiting at CausalOrdering when events arrive >15 min after their follows event.
src/prefect/server/events/actions.py:165:            follows_id = None
src/prefect/server/events/actions.py:176:                    follows_id = triggered_action.triggering_event.id
src/prefect/server/events/actions.py:206:                    follows=follows_id,
src/prefect/server/events/actions.py:220:                    follows=triggered_event_id,
src/prefect/server/events/actions.py:252:            # Only set follows if timing is tight (within 5 minutes) to avoid unnecessary
src/prefect/server/events/actions.py:253:            # waiting at CausalOrdering when events arrive >15 min after their follows event.
src/prefect/server/events/actions.py:254:            follows_id = None
src/prefect/server/events/actions.py:265:                    follows_id = triggered_action.triggering_event.id
src/prefect/server/events/actions.py:295:                    follows=follows_id,
src/prefect/server/events/actions.py:309:                    follows=triggered_event_id,
src/prefect/server/events/ordering/db.py:57:        assert event.follows
src/prefect/server/events/ordering/db.py:63:                    leader_event_id=event.follows,
src/prefect/server/events/ordering/db.py:75:        assert follower.follows
src/prefect/server/events/ordering/db.py:138:            if and what event it follows.
src/prefect/server/events/ordering/db.py:155:        if event.follows:
src/prefect/server/events/ordering/db.py:156:            if not await self.event_has_been_seen(event.follows):
src/prefect/server/events/ordering/db.py:160:                        "Event %r (%s) for %r arrived before the event it follows %s",
src/prefect/server/events/ordering/db.py:164:                        event.follows,
src/prefect/server/events/ordering/db.py:182:        if event.follows:
src/prefect/server/events/ordering/memory.py:115:        assert event.follows
src/prefect/server/events/ordering/memory.py:119:            if event.follows not in self._followers:
src/prefect/server/events/ordering/memory.py:120:                self._followers[event.follows] = set()
src/prefect/server/events/ordering/memory.py:121:            self._followers[event.follows].add(event.id)
src/prefect/server/events/ordering/memory.py:126:        assert follower.follows
src/prefect/server/events/ordering/memory.py:130:            if follower.follows in self._followers:
src/prefect/server/events/ordering/memory.py:131:                self._followers[follower.follows].discard(follower.id)
src/prefect/server/events/ordering/memory.py:132:                if not self._followers[follower.follows]:
src/prefect/server/events/ordering/memory.py:133:                    del self._followers[follower.follows]
src/prefect/server/events/ordering/memory.py:177:                    if event.follows and event.follows in self._followers:
src/prefect/server/events/ordering/memory.py:178:                        self._followers[event.follows].discard(event_id)
src/prefect/server/events/ordering/memory.py:179:                        if not self._followers[event.follows]:
src/prefect/server/events/ordering/memory.py:180:                            del self._followers[event.follows]
src/prefect/server/events/ordering/memory.py:207:        if not event.follows or event.follows == event.id:
src/prefect/server/events/ordering/memory.py:217:        if await self.event_has_been_seen(event.follows):
src/prefect/server/events/ordering/memory.py:222:        if await self.event_has_started_processing(event.follows):
src/prefect/server/events/ordering/memory.py:225:                    while not await self.event_has_been_seen(event.follows):
src/prefect/server/events/ordering/memory.py:232:                    event.follows,
src/prefect/server/events/ordering/memory.py:237:        self._log(event, "arrived before the event it follows %s", event.follows)
src/prefect/server/events/ordering/memory.py:263:                metadata indicating if and what event it follows.
src/prefect/server/events/ordering/memory.py:299:        if event.follows and event.follows != event.id:
src/prefect/server/events/ordering/memory.py:311:                "follows": event.follows,
src/prefect/server/events/schemas/events.py:141:    follows: Optional[UUID] = Field(
src/prefect/server/models/events.py:83:        follows=initial_state_id if _timing_is_tight(occurred, initial_state) else None,
src/prefect/server/models/events.py:283:    # Only connect events with event.follows if the timing here is tight, which will
src/prefect/server/models/events.py:514:        follows=_get_recent_preceding_work_pool_event_id(pre_update_work_pool),
```

## 61 · 2026-10-28T08:14:07.584920+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/models/events.py",
  "limit": 130,
  "offset": 40
}
```

## 62 · 2026-10-28T08:14:07.695645+00:00 · tool_result 

```
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
131	    task_run: Union[ORMTaskRun, schemas.core.TaskRun, None] = None,
132	) -> ResourceData:
133	    return {
134	        "flow-run": {
135	            "id": str(flow_run.id),
136	            "name": flow_run.name,
137	            "tags": flow_run.tags if flow_run.tags else [],
138	            "role": "flow-run",
139	        },
140	        "flow": (
141	            {
142	                "id": str(flow.id),
143	                "name": flow.name,
144	                "tags": flow.tags if flow.tags else [],
145	                "role": "flow",
146	            }
147	            if flow
148	            else {}
149	        ),
150	        "deployment": (
151	            {
152	                "id": str(deployment.id),
153	                "name": deployment.name,
154	                "tags": deployment.tags if deployment.tags else [],
155	                "role": "deployment",
156	            }
157	            if deployment
158	            else {}
159	        ),
160	        "work-queue": (
161	            {
162	                "id": str(work_queue.id),
163	                "name": work_queue.name,
164	                "tags": [],
165	                "role": "work-queue",
166	            }
167	            if work_queue
168	            else {}
169	        ),
```

## 63 · 2026-10-28T08:14:09.301840+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"test_same_event_in_expect_and_after\\|test_proactive.*restart\\|restart\" tests/events/server/triggers/test_regressions.py | head -40",
  "description": "Find related regression tests"
}
```

## 64 · 2026-10-28T08:14:09.573019+00:00 · tool_result 

```
218:async def test_same_event_in_expect_and_after_never_reacts_immediately(
296:async def test_same_event_in_expect_and_after_reacts_after_threshold_is_met(
403:async def test_same_event_in_expect_and_after_proactively_does_not_fire(
476:async def test_same_event_in_expect_and_after_proactively_fires(
827:    # The triggering_event should be the second Running event (the one that restarted the bucket)
943:async def test_same_event_in_expect_and_after_proactively_fires_with_for_each_threshold_1(
```

## 65 · 2026-10-28T08:14:09.579979+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '1,120p' tests/events/server/triggers/test_regressions.py",
  "description": "Read regression test file header"
}
```

## 66 · 2026-10-28T08:14:09.870038+00:00 · tool_result 

```
import asyncio
import random
from datetime import timedelta
from typing import Callable, List, Union
from unittest import mock
from uuid import UUID, uuid4

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from prefect.server.events import actions, triggers
from prefect.server.events.models import automations
from prefect.server.events.schemas.automations import (
    Automation,
    EventTrigger,
    Firing,
    Posture,
    TriggerState,
)
from prefect.server.events.schemas.events import Event, ReceivedEvent
from prefect.server.models import work_queues
from prefect.server.schemas.actions import WorkQueueCreate
from prefect.server.schemas.core import WorkQueue
from prefect.types._datetime import DateTime

pytestmark = pytest.mark.clear_db


@pytest.fixture
def act(monkeypatch: pytest.MonkeyPatch) -> mock.AsyncMock:
    mock_act = mock.AsyncMock()
    monkeypatch.setattr("prefect.server.events.triggers.act", mock_act)
    return mock_act


@pytest.fixture
async def work_queue(
    session: AsyncSession,
) -> WorkQueue:
    work_queue = await work_queues.create_work_queue(
        session=session,
        work_queue=WorkQueueCreate(name="my-work-queue"),
    )
    await session.commit()
    return work_queue


@pytest.fixture
async def unhealthy_work_queue_automation(
    work_queue: WorkQueue,
    cleared_buckets: None,
    cleared_automations: None,
    automations_session: AsyncSession,
) -> Automation:
    # Automation for issue 8871: https://github.com/PrefectHQ/prefect/issues/8871
    automation = await automations.create_automation(
        automations_session,
        Automation(
            name="Alert about unhealthy work queues",
            description="Any work queues that are unhealthy for more than 2 hours",
            trigger=EventTrigger(
                match={
                    "prefect.resource.id": f"prefect.work-queue.{work_queue.id}",
                },
                for_each={"prefect.resource.id"},
                after={"prefect.work-queue.unhealthy"},
                expect={"prefect.work-queue.healthy"},
                posture=Posture.Proactive,
                threshold=1,
                within=timedelta(minutes=119),
            ),
            actions=[actions.DoNothing()],
        ),
    )
    triggers.load_automation(automation)
    await automations_session.commit()
    return automation


@pytest.fixture
def work_queue_health_unhealthy(
    work_queue: WorkQueue,
    frozen_time: DateTime,
) -> List[ReceivedEvent]:
    events = [
        Event(
            occurred=frozen_time,
            event="prefect.work-queue.unhealthy",
            resource={"prefect.resource.id": f"prefect.work-queue.{work_queue.id}"},
            related=[],
            payload={},
            id=uuid4(),
        )
    ]

    return [event.receive() for event in events]


@pytest.fixture
def work_queue_health_healthy(
    work_queue: WorkQueue,
    frozen_time: DateTime,
) -> List[ReceivedEvent]:
    events = (
        Event(
            occurred=frozen_time,
            event="prefect.work-queue.unhealthy",
            resource={"prefect.resource.id": f"prefect.work-queue.{work_queue.id}"},
            related=[],
            payload={},
            id=uuid4(),
        ),
        Event(
            occurred=frozen_time + timedelta(minutes=20),
            event="prefect.work-queue.healthy",
            resource={"prefect.resource.id": f"prefect.work-queue.{work_queue.id}"},
            related=[],
            payload={},
            id=uuid4(),
        ),
```

## 67 · 2026-10-28T08:14:11.269271+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "offset": 200,
  "limit": 420
}
```

## 68 · 2026-10-28T08:14:11.363695+00:00 · tool_result 

```
200	        automations_session,
201	        Automation(
202	            name="Both expect and after",
203	            trigger=EventTrigger(
204	                after={"some-event"},
205	                expect={"some-event"},
206	                posture=Posture.Reactive,
207	                threshold=1,
208	                within=timedelta(seconds=0),
209	            ),
210	            actions=[actions.DoNothing()],
211	        ),
212	    )
213	    triggers.load_automation(automation)
214	    await automations_session.commit()
215	    return automation
216	
217	
218	async def test_same_event_in_expect_and_after_never_reacts_immediately(
219	    act: mock.AsyncMock,
220	    frozen_time: DateTime,
221	    reactive_immediate_expect_and_after: Automation,
222	):
223	    """Regression test for https://github.com/PrefectHQ/nebula/issues/4201, where
224	    having the same event in after and expect causes weird behavior
225	
226	    Case one: Reactive, within = 0 (immediately fires on all events) -> this will never
227	    fire because there's no time for an event to come after itself like this
228	    """
229	    await triggers.reactive_evaluation(
230	        Event(
231	            occurred=frozen_time,
232	            event="some-event",
233	            resource={"prefect.resource.id": "some.resource"},
234	            id=uuid4(),
235	        ).receive()
236	    )
237	    act.assert_not_awaited()
238	
239	    await triggers.reactive_evaluation(
240	        Event(
241	            occurred=frozen_time + timedelta(seconds=1),
242	            event="some-event",
243	            resource={"prefect.resource.id": "some.resource"},
244	            id=uuid4(),
245	        ).receive()
246	    )
247	    act.assert_not_awaited()
248	
249	    await triggers.reactive_evaluation(
250	        Event(
251	            occurred=frozen_time + timedelta(seconds=2),
252	            event="some-event",
253	            resource={"prefect.resource.id": "some.resource"},
254	            id=uuid4(),
255	        ).receive()
256	    )
257	    act.assert_not_awaited()
258	
259	    await triggers.reactive_evaluation(
260	        Event(
261	            occurred=frozen_time + timedelta(seconds=3),
262	            event="some-event",
263	            resource={"prefect.resource.id": "some.resource"},
264	            id=uuid4(),
265	        ).receive()
266	    )
267	    act.assert_not_awaited()
268	
269	
270	@pytest.fixture
271	async def reactive_extended_expect_and_after(
272	    cleared_buckets: None,
273	    cleared_automations: None,
274	    automations_session: AsyncSession,
275	) -> Automation:
276	    # Automation for https://github.com/PrefectHQ/nebula/issues/4201
277	    automation = await automations.create_automation(
278	        automations_session,
279	        Automation(
280	            name="Both expect and after",
281	            trigger=EventTrigger(
282	                after={"some-event"},
283	                expect={"some-event"},
284	                posture=Posture.Reactive,
285	                threshold=1,
286	                within=timedelta(seconds=5),
287	            ),
288	            actions=[actions.DoNothing()],
289	        ),
290	    )
291	    triggers.load_automation(automation)
292	    await automations_session.commit()
293	    return automation
294	
295	
296	async def test_same_event_in_expect_and_after_reacts_after_threshold_is_met(
297	    act: mock.AsyncMock,
298	    frozen_time: DateTime,
299	    reactive_extended_expect_and_after: Automation,
300	):
301	    """Regression test for https://github.com/PrefectHQ/nebula/issues/4201, where
302	    having the same event in after and expect causes weird behavior.
303	
304	    Case two: Reactive, within > 0 -> this will fire on the second (or `threshold + 1`)
305	    occurrence of the event in the window
306	    """
307	    await triggers.reactive_evaluation(
308	        Event(
309	            occurred=frozen_time + timedelta(seconds=1),
310	            event="some-event",
311	            resource={"prefect.resource.id": "some.resource"},
312	            id=uuid4(),
313	        ).receive()
314	    )
315	    act.assert_not_awaited()
316	
317	    act.reset_mock()
318	    await triggers.reactive_evaluation(
319	        Event(
320	            occurred=frozen_time + timedelta(seconds=2),
321	            event="some-event",
322	            resource={"prefect.resource.id": "some.resource"},
323	            id=uuid4(),
324	        ).receive()
325	    )
326	    act.assert_awaited_once()  # we've reached the threshold, fire
327	
328	    # now the window should have been cleared, so we can fire again
329	
330	    act.reset_mock()
331	    await triggers.reactive_evaluation(
332	        Event(
333	            occurred=frozen_time + timedelta(seconds=3),
334	            event="some-event",
335	            resource={"prefect.resource.id": "some.resource"},
336	            id=uuid4(),
337	        ).receive()
338	    )
339	    act.assert_not_awaited()  # another hit for the `after`, may fire on the next one
340	
341	    act.reset_mock()
342	    await triggers.reactive_evaluation(
343	        Event(
344	            occurred=frozen_time + timedelta(seconds=4),
345	            event="some-event",
346	            resource={"prefect.resource.id": "some.resource"},
347	            id=uuid4(),
348	        ).receive()
349	    )
350	    act.assert_awaited_once()  # we've reached the threshold, fire
351	
352	    # now advance far past the previous windows
353	
354	    act.reset_mock()
355	    await triggers.reactive_evaluation(
356	        Event(
357	            occurred=frozen_time + timedelta(seconds=61),
358	            event="some-event",
359	            resource={"prefect.resource.id": "some.resource"},
360	            id=uuid4(),
361	        ).receive()
362	    )
363	    act.assert_not_awaited()
364	
365	    act.reset_mock()
366	    await triggers.reactive_evaluation(
367	        Event(
368	            occurred=frozen_time + timedelta(seconds=62),
369	            event="some-event",
370	            resource={"prefect.resource.id": "some.resource"},
371	            id=uuid4(),
372	        ).receive()
373	    )
374	    act.assert_awaited_once()  # we've reached the threshold, fire
375	
376	
377	@pytest.fixture
378	async def proactive_extended_expect_and_after(
379	    cleared_buckets: None,
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
600	            for event in events
601	        ],
602	    )
603	
604	
605	@pytest.fixture
606	async def rapid_fire_automation_with_a_threshold(
607	    work_queue: WorkQueue,
608	    cleared_buckets: None,
609	    cleared_automations: None,
610	    automations_session: AsyncSession,
611	) -> Automation:
612	    # Automation for https://github.com/PrefectHQ/nebula/issues/4201
613	    automation = await automations.create_automation(
614	        automations_session,
615	        Automation(
616	            name="Excepts 10 events within in sixty seconds",
617	            trigger=EventTrigger(
618	                expect={"some-event"},
619	                posture=Posture.Reactive,
```

## 69 · 2026-10-28T08:14:13.091382+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "limit": 130,
  "offset": 905
}
```

## 70 · 2026-10-28T08:14:13.193755+00:00 · tool_result 

```
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

## 71 · 2026-10-28T08:14:31.459288+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class AutomationBucket\" -A 80 src/prefect/server/database/orm_models.py",
  "description": "Read ORMAutomationBucket"
}
```

## 72 · 2026-10-28T08:14:31.728112+00:00 · tool_result 

```
1306:class AutomationBucket(Base):
1307-    __table_args__: Any = (
1308-        sa.Index(
1309-            "uq_automation_bucket__automation_id__trigger_id__bucketing_key",
1310-            "automation_id",
1311-            "trigger_id",
1312-            "bucketing_key",
1313-            unique=True,
1314-        ),
1315-        sa.Index(
1316-            "ix_automation_bucket__automation_id__end",
1317-            "automation_id",
1318-            "end",
1319-        ),
1320-    )
1321-
1322-    automation_id: Mapped[uuid.UUID] = mapped_column(
1323-        sa.ForeignKey("automation.id", ondelete="CASCADE")
1324-    )
1325-
1326-    trigger_id: Mapped[uuid.UUID]
1327-
1328-    bucketing_key: Mapped[list[str]] = mapped_column(
1329-        JSON, server_default="[]", default=list
1330-    )
1331-
1332-    last_event: Mapped[Optional[ReceivedEvent]] = mapped_column(Pydantic(ReceivedEvent))
1333-
1334-    start: Mapped[DateTime]
1335-    end: Mapped[DateTime]
1336-
1337-    count: Mapped[int]
1338-
1339-    last_operation: Mapped[Optional[str]]
1340-
1341-    triggered_at: Mapped[Optional[DateTime]]
1342-
1343-
1344-class AutomationRelatedResource(Base):
1345-    __table_args__: Any = (
1346-        sa.Index(
1347-            "uq_automation_related_resource__automation_id__resource_id",
1348-            "automation_id",
1349-            "resource_id",
1350-            unique=True,
1351-        ),
1352-    )
1353-
1354-    automation_id: Mapped[uuid.UUID] = mapped_column(
1355-        sa.ForeignKey("automation.id", ondelete="CASCADE")
1356-    )
1357-
1358-    resource_id: Mapped[Optional[str]] = mapped_column(index=True)
1359-    automation_owned_by_resource: Mapped[bool] = mapped_column(
1360-        default=False, server_default="0"
1361-    )
1362-
1363-    automation: Mapped["Automation"] = relationship(
1364-        "Automation", back_populates="related_resources", lazy="raise"
1365-    )
1366-
1367-
1368-class CompositeTriggerChildFiring(Base):
1369-    __table_args__: Any = (
1370-        sa.Index(
1371-            "uq_composite_trigger_child_firing__a_id__pt_id__ct__id",
1372-            "automation_id",
1373-            "parent_trigger_id",
1374-            "child_trigger_id",
1375-            unique=True,
1376-        ),
1377-    )
1378-
1379-    automation_id: Mapped[uuid.UUID] = mapped_column(
1380-        sa.ForeignKey("automation.id", ondelete="CASCADE")
1381-    )
1382-
1383-    parent_trigger_id: Mapped[uuid.UUID]
1384-
1385-    child_trigger_id: Mapped[uuid.UUID]
1386-    child_firing_id: Mapped[uuid.UUID]
```

## 73 · 2026-10-28T08:14:45.891427+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/schemas/events.py",
  "limit": 120,
  "offset": 60
}
```

## 74 · 2026-10-28T08:14:45.995793+00:00 · tool_result 

```
60	
61	    @model_validator(mode="after")
62	    def requires_resource_id(self) -> Self:
63	        if "prefect.resource.id" not in self.root:
64	            raise ValueError("Resources must include the prefect.resource.id label")
65	        if not self.root["prefect.resource.id"]:
66	            raise ValueError("The prefect.resource.id label must be non-empty")
67	
68	        return self
69	
70	    @property
71	    def id(self) -> str:
72	        return self["prefect.resource.id"]
73	
74	    @property
75	    def name(self) -> Optional[str]:
76	        return self.get("prefect.resource.name")
77	
78	    def prefect_object_id(self, kind: str) -> UUID:
79	        """Extracts the UUID from an event's resource ID if it's the expected kind
80	        of prefect resource"""
81	        prefix = f"{kind}." if not kind.endswith(".") else kind
82	
83	        if not self.id.startswith(prefix):
84	            raise ValueError(f"Resource ID {self.id} does not start with {prefix}")
85	
86	        return UUID(self.id[len(prefix) :])
87	
88	
89	class RelatedResource(Resource):
90	    """A Resource with a specific role in an Event"""
91	
92	    @model_validator(mode="after")
93	    def requires_resource_role(self) -> Self:
94	        if "prefect.resource.role" not in self.root:
95	            raise ValueError(
96	                "Related Resources must include the prefect.resource.role label"
97	            )
98	        if not self.root["prefect.resource.role"]:
99	            raise ValueError("The prefect.resource.role label must be non-empty")
100	
101	        return self
102	
103	    @property
104	    def role(self) -> str:
105	        return self["prefect.resource.role"]
106	
107	
108	def _validate_event_name_length(value: str) -> str:
109	    from prefect.settings import PREFECT_SERVER_EVENTS_MAXIMUM_EVENT_NAME_LENGTH
110	
111	    if len(value) > PREFECT_SERVER_EVENTS_MAXIMUM_EVENT_NAME_LENGTH.value():
112	        raise ValueError(
113	            f"Event name must be at most {PREFECT_SERVER_EVENTS_MAXIMUM_EVENT_NAME_LENGTH.value()} characters"
114	        )
115	    return value
116	
117	
118	class Event(PrefectBaseModel):
119	    """The client-side view of an event that has happened to a Resource"""
120	
121	    occurred: prefect.types._datetime.DateTime = Field(
122	        description="When the event happened from the sender's perspective",
123	    )
124	    event: Annotated[str, AfterValidator(_validate_event_name_length)] = Field(
125	        description="The name of the event that happened",
126	    )
127	    resource: Resource = Field(
128	        description="The primary Resource this event concerns",
129	    )
130	    related: list[RelatedResource] = Field(
131	        default_factory=list,
132	        description="A list of additional Resources involved in this event",
133	    )
134	    payload: dict[str, Any] = Field(
135	        default_factory=dict,
136	        description="An open-ended set of data describing what happened",
137	    )
138	    id: UUID = Field(
139	        description="The client-provided identifier of this event",
140	    )
141	    follows: Optional[UUID] = Field(
142	        default=None,
143	        description=(
144	            "The ID of an event that is known to have occurred prior to this one. "
145	            "If set, this may be used to establish a more precise ordering of causally-"
146	            "related events when they occur close enough together in time that the "
147	            "system may receive them out-of-order."
148	        ),
149	    )
150	
151	    @property
152	    def size_bytes(self) -> int:
153	        return len(self.model_dump_json().encode())
154	
155	    @property
156	    def involved_resources(self) -> Sequence[Resource]:
157	        return [self.resource] + list(self.related)
158	
159	    @property
160	    def resource_in_role(self) -> Mapping[str, RelatedResource]:
161	        """Returns a mapping of roles to the first related resource in that role"""
162	        return {related.role: related for related in reversed(self.related)}
163	
164	    @property
165	    def resources_in_role(self) -> Mapping[str, Sequence[RelatedResource]]:
166	        """Returns a mapping of roles to related resources in that role"""
167	        resources: Dict[str, List[RelatedResource]] = defaultdict(list)
168	        for related in self.related:
169	            resources[related.role].append(related)
170	        return resources
171	
172	    @field_validator("related")
173	    @classmethod
174	    def enforce_maximum_related_resources(
175	        cls, value: List[RelatedResource]
176	    ) -> List[RelatedResource]:
177	        if len(value) > PREFECT_EVENTS_MAXIMUM_RELATED_RESOURCES.value():
178	            raise ValueError(
179	                "The maximum number of related resources "
```

## 75 · 2026-10-28T08:14:47.183148+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class ReceivedEvent\" -A 60 src/prefect/server/events/schemas/events.py",
  "description": "Read ReceivedEvent schema"
}
```

## 76 · 2026-10-28T08:14:47.446829+00:00 · tool_result 

```
206:class ReceivedEvent(Event):
207-    """The server-side view of an event that has happened to a Resource after it has
208-    been received by the server"""
209-
210-    model_config: ClassVar[ConfigDict] = ConfigDict(
211-        extra="ignore", from_attributes=True
212-    )
213-
214-    received: prefect.types._datetime.DateTime = Field(
215-        default_factory=lambda: prefect.types._datetime.now("UTC"),
216-        description="When the event was received by Prefect Cloud",
217-    )
218-
219-    @property
220-    def url(self) -> Optional[str]:
221-        """Returns the UI URL for this event, allowing users to link to events
222-        in automation templates without parsing date strings."""
223-        return url_for(self, url_type="ui")
224-
225-    def as_database_row(self) -> dict[str, Any]:
226-        row = self.model_dump()
227-        row["resource_id"] = self.resource.id
228-        row["recorded"] = prefect.types._datetime.now("UTC")
229-        row["related_resource_ids"] = [related.id for related in self.related]
230-        return row
231-
232-    def as_database_resource_rows(self) -> List[Dict[str, Any]]:
233-        def without_id_and_role(resource: Resource) -> Dict[str, str]:
234-            d: Dict[str, str] = resource.root.copy()
235-            d.pop("prefect.resource.id", None)
236-            d.pop("prefect.resource.role", None)
237-            return d
238-
239-        return [
240-            {
241-                "occurred": self.occurred,
242-                "resource_id": resource.id,
243-                "resource_role": (
244-                    resource.role if isinstance(resource, RelatedResource) else ""
245-                ),
246-                "resource": without_id_and_role(resource),
247-                "event_id": self.id,
248-            }
249-            for resource in [self.resource, *self.related]
250-        ]
251-
252-
253-def matches(expected: str, value: Optional[str]) -> bool:
254-    """Returns true if the given value matches the expected string.
255-
256-    Args:
257-        expected: A glob pattern to match against;
258-            if it starts with an `!`, the pattern is negated.
259-        value: The value of the label.
260-    """
261-    if value is None:
262-        return False
263-
264-    is_positive = not expected.startswith("!")
265-    expected = expected.removeprefix("!")
266-
```

## 77 · 2026-10-28T08:14:48.807922+00:00 · tool_call Grep

```
{
  "-n": true,
  "output_mode": "content",
  "path": "$SANDBOX/prefect/src",
  "pattern": "Unresponsive|unresponsive|zombie"
}
```

## 78 · 2026-10-28T08:14:49.087385+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '1,120p' src/prefect/server/events/ordering/__init__.py",
  "description": "Read ordering init"
}
```

## 79 · 2026-10-28T08:14:49.217350+00:00 · tool_result 

```
src\prefect\runner\server.py:64:                content={"message": "Runner is unresponsive at this time"},
src\prefect\workers\server.py:53:                content={"message": "Worker may be unresponsive at this time"},
src\integrations\prefect-databricks\prefect_databricks\schemas\original\jobs-2.1-aws.yaml:3130:        \ because it was unresponsive.\n* INSTANCE_UNREACHABLE: Databricks was not\
src\integrations\prefect-databricks\prefect_databricks\schemas\jobs-2.1-aws.yaml:3179:        \ because it was unresponsive.\n* INSTANCE_UNREACHABLE: Databricks was not\
src\integrations\prefect-databricks\prefect_databricks\models\jobs.py:1653:    * DRIVER_UNRESPONSIVE: Databricks was not able to access the Spark driver, because it was unresponsive.
src\integrations\prefect-databricks\prefect_databricks\models\jobs.py:1676:    driverunresponsive = "DRIVER_UNRESPONSIVE"
```

## 80 · 2026-10-28T08:14:49.400719+00:00 · tool_result 

```
"""
Manages the partial causal ordering of events for a particular consumer.  This module
maintains a buffer of events to be processed, aiming to process them in the order they
occurred causally.
"""

import abc
from datetime import timedelta
import importlib
from typing import (
    TYPE_CHECKING,
    AsyncContextManager,
    List,
    Protocol,
    Union,
    runtime_checkable,
)
from uuid import UUID
from prefect.logging import get_logger
from prefect.server.events.schemas.events import Event, ReceivedEvent
from prefect.settings import get_current_settings

if TYPE_CHECKING:
    import logging

logger: "logging.Logger" = get_logger(__name__)

# How long we'll retain preceding events (to aid with ordering)
PRECEDING_EVENT_LOOKBACK = timedelta(minutes=15)

# How long we'll retain events we've processed (to prevent re-processing an event)
PROCESSED_EVENT_LOOKBACK = timedelta(minutes=30)

# How long we'll remember that we've seen an event
SEEN_EXPIRATION = max(PRECEDING_EVENT_LOOKBACK, PROCESSED_EVENT_LOOKBACK)

# How deep we'll allow the recursion to go when processing events
MAX_DEPTH_OF_PRECEDING_EVENT = 20


@runtime_checkable
class CausalOrderingModule(Protocol):
    CausalOrdering: type["CausalOrdering"]


class EventArrivedEarly(Exception):
    def __init__(self, event: ReceivedEvent):
        self.event = event


class MaxDepthExceeded(Exception):
    def __init__(self, event: ReceivedEvent):
        self.event = event


class event_handler(Protocol):
    async def __call__(
        self, event: ReceivedEvent, depth: int = 0
    ) -> None: ...  # pragma: no cover


class CausalOrdering(abc.ABC):
    def __init__(self, scope: str):
        self.scope = scope

    @abc.abstractmethod
    async def event_has_been_seen(self, event: Union[UUID, Event]) -> bool: ...

    @abc.abstractmethod
    async def record_event_as_seen(self, event: ReceivedEvent) -> None: ...

    @abc.abstractmethod
    async def record_follower(self, event: ReceivedEvent) -> None: ...

    @abc.abstractmethod
    async def forget_follower(self, follower: ReceivedEvent) -> None: ...

    @abc.abstractmethod
    async def get_followers(self, leader: ReceivedEvent) -> List[ReceivedEvent]: ...

    @abc.abstractmethod
    async def get_lost_followers(self) -> List[ReceivedEvent]: ...

    @abc.abstractmethod
    def preceding_event_confirmed(
        self, handler: event_handler, event: ReceivedEvent, depth: int = 0
    ) -> AsyncContextManager[None]: ...


def get_triggers_causal_ordering() -> CausalOrdering:
    import_path = get_current_settings().server.events.causal_ordering
    causal_ordering_module = importlib.import_module(import_path)

    if not isinstance(causal_ordering_module, CausalOrderingModule):
        raise ValueError(
            f"Module at {import_path} does not export a CausalOrdering class. Please check your server.events.causal_ordering setting."
        )

    return causal_ordering_module.CausalOrdering(scope="triggers")
```

## 81 · 2026-10-28T08:14:51.723869+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"def test.*proactive\\|def test.*heartbeat\\|def test.*zombie\" tests/events/server/triggers/test_basics.py | head -60",
  "description": "List proactive tests in basics"
}
```

## 82 · 2026-10-28T08:14:52.067505+00:00 · tool_result 

```
475:async def test_proactive_trigger_fires_after_time_expires(
810:async def test_lost_followers_are_processed_during_proactive_evaluation(
```

## 83 · 2026-10-28T08:14:53.011090+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_basics.py",
  "limit": 160,
  "offset": 380
}
```

## 84 · 2026-10-28T08:14:53.220182+00:00 · tool_result 

```
380	        Firing(
381	            trigger=chonk_lonely.trigger,
382	            trigger_states={TriggerState.Triggered},
383	            triggered=frozen_time,  # type: ignore
384	            triggering_labels={},
385	            triggering_event=woodchonk_table_for_one,
386	        ),
387	    )
388	
389	
390	async def test_reactive_automation_triggers_for_each_related_label(
391	    cleared_buckets: None,
392	    cleared_automations: None,
393	    automations_session: AsyncSession,
394	    woodchonk_nibbled: ReceivedEvent,
395	    woodchonk_gobbled: ReceivedEvent,
396	    act: mock.AsyncMock,
397	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
398	    frozen_time: DateTime,
399	):
400	    """Test that we can create an automation that is tracked separate for each value
401	    of a related resource's labels."""
402	
403	    automation = await automations.create_automation(
404	        automations_session,
405	        Automation(
406	            name="Let me know when I've lost 3 of any flower species",
407	            trigger=EventTrigger(
408	                expect={"animal.ingested"},
409	                for_each={"related:meal:genus", "related:meal:species"},
410	                posture=Posture.Reactive,
411	                threshold=3,
412	                within=timedelta(minutes=10),
413	            ),
414	            actions=[actions.DoNothing()],
415	            enabled=True,
416	        ),
417	    )
418	    triggers.load_automation(automation)
419	    await automations_session.commit()
420	
421	    woodchonk_nibbled.id = uuid4()
422	    woodchonk_nibbled.occurred += timedelta(seconds=1)
423	    await triggers.reactive_evaluation(woodchonk_nibbled)
424	    act.assert_not_awaited()
425	
426	    woodchonk_nibbled.id = uuid4()
427	    woodchonk_nibbled.occurred += timedelta(seconds=1)
428	    await triggers.reactive_evaluation(woodchonk_nibbled)
429	    act.assert_not_awaited()
430	
431	    woodchonk_gobbled.id = uuid4()
432	    woodchonk_gobbled.occurred += timedelta(seconds=1)
433	    await triggers.reactive_evaluation(woodchonk_gobbled)
434	    act.assert_not_awaited()
435	
436	    woodchonk_nibbled.id = uuid4()
437	    woodchonk_nibbled.occurred += timedelta(seconds=1)
438	    await triggers.reactive_evaluation(woodchonk_nibbled)
439	    assert_acted_with(
440	        Firing(
441	            trigger=automation.trigger,
442	            trigger_states={TriggerState.Triggered},
443	            triggered=frozen_time,  # type: ignore
444	            triggering_labels={
445	                "related:meal:genus": "Hemerocallis",
446	                "related:meal:species": "fulva",
447	            },
448	            triggering_event=woodchonk_nibbled,
449	        ),
450	    )
451	    act.reset_mock()
452	
453	    woodchonk_gobbled.id = uuid4()
454	    woodchonk_gobbled.occurred += timedelta(seconds=1)
455	    await triggers.reactive_evaluation(woodchonk_gobbled)
456	    act.assert_not_awaited()
457	
458	    woodchonk_gobbled.id = uuid4()
459	    woodchonk_gobbled.occurred += timedelta(seconds=1)
460	    await triggers.reactive_evaluation(woodchonk_gobbled)
461	    assert_acted_with(
462	        Firing(
463	            trigger=automation.trigger,
464	            trigger_states={TriggerState.Triggered},
465	            triggered=frozen_time,  # type: ignore
466	            triggering_labels={
467	                "related:meal:genus": "Dicentra",
468	                "related:meal:species": "cucullaria",
469	            },
470	            triggering_event=woodchonk_gobbled,
471	        ),
472	    )
473	
474	
475	async def test_proactive_trigger_fires_after_time_expires(
476	    effective_automations: List[Automation],
477	    chonk_sadness: Automation,
478	    start_of_test: DateTime,
479	    act: mock.AsyncMock,
480	    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
481	    frozen_time: DateTime,
482	):
483	    async def run_proactive_evaluation(automations: List[Automation], as_of: DateTime):
484	        for automation in automations:
485	            trigger = automation.trigger
486	            assert isinstance(trigger, EventTrigger), repr(trigger)
487	            await triggers.proactive_evaluation(trigger, as_of)
488	
489	    await run_proactive_evaluation(effective_automations, start_of_test)
490	    act.assert_not_awaited()
491	
492	    await run_proactive_evaluation(
493	        effective_automations, start_of_test + timedelta(seconds=9)
494	    )
495	    act.assert_not_awaited()
496	
497	    await run_proactive_evaluation(
498	        effective_automations,
499	        start_of_test + timedelta(seconds=10),
500	    )
501	    act.assert_not_awaited()
502	
503	    await run_proactive_evaluation(
504	        effective_automations,
505	        start_of_test + timedelta(seconds=30),
506	    )
507	    assert_acted_with(
508	        Firing(
509	            trigger=chonk_sadness.trigger,
510	            trigger_states={TriggerState.Triggered},
511	            triggered=frozen_time,  # type: ignore
512	            triggering_labels={},
513	        ),
514	    )
515	    act.reset_mock()
516	
517	    # The period should start over after 30 seconds
518	
519	    await run_proactive_evaluation(
520	        effective_automations,
521	        start_of_test + timedelta(seconds=31),
522	    )
523	    act.assert_not_awaited()
524	
525	    await run_proactive_evaluation(
526	        effective_automations,
527	        start_of_test + timedelta(seconds=60),
528	    )
529	    assert_acted_with(
530	        Firing(
531	            trigger=chonk_sadness.trigger,
532	            trigger_states={TriggerState.Triggered},
533	            triggered=frozen_time,  # type: ignore
534	            triggering_labels={},
535	        ),
536	    )
537	
538	
539	async def test_reactive_triggers_clean_up_after_themselves_if_they_do_fire(
```

## 85 · 2026-10-28T08:15:12.793456+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"flow_run_state_change_event(\" src/prefect/server | head -20",
  "description": "Find callers of flow_run_state_change_event"
}
```

## 86 · 2026-10-28T08:15:13.292049+00:00 · tool_result 

```
src/prefect/server/models/events.py:42:async def flow_run_state_change_event(
src/prefect/server/orchestration/instrumentation_policies.py:58:                await flow_run_state_change_event(
```

## 87 · 2026-10-28T08:15:15.046462+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/orchestration/instrumentation_policies.py",
  "limit": 110,
  "offset": 30
}
```

## 88 · 2026-10-28T08:15:15.151397+00:00 · tool_result 

```
30	    ) -> None:
31	        if not context.proposed_state or not context.validated_state:
32	            return
33	
34	        if not isinstance(context, FlowOrchestrationContext):
35	            return
36	
37	        initial_state = (
38	            context.initial_state.model_copy() if context.initial_state else None
39	        )
40	        validated_state = context.validated_state.model_copy()
41	
42	        # Guard against passing large state payloads to arq
43	        if initial_state and context.initial_state:
44	            initial_state.timestamp = context.initial_state.timestamp
45	            initial_state.message = truncated_to(
46	                TRUNCATE_STATE_MESSAGES_AT, initial_state.message
47	            )
48	        if validated_state:
49	            validated_state.timestamp = context.validated_state.timestamp
50	            validated_state.message = truncated_to(
51	                TRUNCATE_STATE_MESSAGES_AT, validated_state.message
52	            )
53	
54	        assert isinstance(context.session, AsyncSession)
55	
56	        async with PrefectServerEventsClient() as events:
57	            await events.emit(
58	                await flow_run_state_change_event(
59	                    session=context.session,
60	                    occurred=validated_state.timestamp,
61	                    flow_run=context.run,
62	                    initial_state_id=initial_state.id if initial_state else None,
63	                    initial_state=initial_state,
64	                    validated_state_id=validated_state.id,
65	                    validated_state=validated_state,
66	                )
67	            )
68	
```

## 89 · 2026-10-28T08:15:22.142980+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls plans | head -30 && grep -rln \"proactive\\|heartbeat\\|bucket\" plans | head -20",
  "description": "Search plans directory"
}
```

## 90 · 2026-10-28T08:15:22.440734+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls .claude; cat .claude/* 2>/dev/null | head -40",
  "description": "Check repo claude instructions"
}
```

## 91 · 2026-10-28T08:15:22.533598+00:00 · tool_result 

```
2025-01-31-per-node-dbt-orchestration.md
2026-01-06-custom-deployment-sdks.md
2026-01-12-deployment-crud-events.md
2026-02-05-cli-cyclopts-migration.md
completed
plans/2025-01-31-per-node-dbt-orchestration.md
plans/2026-01-06-custom-deployment-sdks.md
```

## 92 · 2026-10-28T08:15:22.844912+00:00 · tool_result 

```
commands
hooks
settings.json
skills
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/symlink-agents-to-claude.sh"
          }
        ]
      }
    ]
  }
}
```

## 93 · 2026-10-28T08:15:31.445160+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "limit": 130,
  "offset": 680
}
```

## 94 · 2026-10-28T08:15:31.616980+00:00 · tool_result 

```
680	            name="Expects 1 event every 10 seconds",
681	            trigger=EventTrigger(
682	                expect={"some-event"},
683	                posture=Posture.Reactive,
684	                threshold=1,
685	                within=timedelta(seconds=10),
686	            ),
687	            actions=[actions.DoNothing()],
688	        ),
689	    )
690	    triggers.load_automation(automation)
691	    await automations_session.commit()
692	    return automation
693	
694	
695	async def test_reactive_automation_can_trigger_on_events_arriving_in_the_future(
696	    act: mock.AsyncMock,
697	    simple_recurring_automation: Automation,
698	    start_of_test: DateTime,
699	    frozen_time: DateTime,
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
```

## 95 · 2026-10-28T08:15:49.678993+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"flow_run.state = \\|flow_run\\.state =\" src/prefect/flow_engine.py | head -20",
  "description": "Find flow run state assignment in engine"
}
```

## 96 · 2026-10-28T08:15:50.081347+00:00 · tool_result 

```
763:        self.flow_run.state = state  # type: ignore
1260:                            self.flow_run.state = state
1487:        self.flow_run.state = state  # type: ignore
1977:                            self.flow_run.state = state
```

## 97 · 2026-10-28T08:15:51.208999+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/flow_engine.py",
  "limit": 80,
  "offset": 720
}
```

## 98 · 2026-10-28T08:15:51.315079+00:00 · tool_result 

```
720	        if (
721	            not self.short_circuit
722	            and not self._flow_run_name_set
723	            and self.flow.flow_run_name
724	        ):
725	            if self.flow_run is None:
726	                raise ValueError("Flow run not set")
727	
728	            with FlowRunContext(
729	                flow=self.flow,
730	                flow_run=self.flow_run,
731	                parameters=self.parameters,
732	                client=self.client,
733	                task_runner=self.flow.task_runner,
734	                result_store=get_result_store().update_for_flow(self.flow, _sync=True),
735	            ):
736	                flow_run_name = resolve_custom_flow_run_name(
737	                    flow=self.flow, parameters=self.parameters or {}
738	                )
739	            self.client.set_flow_run_name(
740	                flow_run_id=self.flow_run.id, name=flow_run_name
741	            )
742	            self.flow_run.name = flow_run_name
743	            self._flow_run_name_set = True
744	            self._telemetry.update_run_name(name=flow_run_name)
745	
746	        self._get_flow_run_suspension_request().raise_if_requested()
747	        new_state = Running()
748	        state = self.set_state(new_state)
749	        while state.is_pending():
750	            time.sleep(0.2)
751	            state = self.set_state(new_state)
752	        return state
753	
754	    def set_state(self, state: State, force: bool = False) -> State:
755	        """ """
756	        # prevents any state-setting activity
757	        if self.short_circuit:
758	            return self.state
759	
760	        state = propose_state_sync(
761	            self.client, state, flow_run_id=self.flow_run.id, force=force
762	        )  # type: ignore
763	        self.flow_run.state = state  # type: ignore
764	        self.flow_run.state_name = state.name  # type: ignore
765	        self.flow_run.state_type = state.type  # type: ignore
766	
767	        self._capture_state_report(state)
768	        self._telemetry.update_state(state)
769	        self.call_hooks(state)
770	
771	        return state
772	
773	    def result(self, raise_on_failure: bool = True) -> "Union[R, State, None]":
774	        if self._return_value is not NotSet and not isinstance(
775	            self._return_value, State
776	        ):
777	            _result = self._return_value
778	            link_state_to_flow_run_result(self.state, _result)
779	
780	            if asyncio.iscoroutine(_result):
781	                # getting the value for a BaseResult may return an awaitable
782	                # depending on whether the parent frame is sync or not
783	                _result = run_coro_as_sync(_result)
784	            return _result
785	
786	        if self._raised is not NotSet:
787	            if raise_on_failure:
788	                raise self._raised
789	            return self._raised
790	
791	        # This is a fall through case which leans on the existing state result mechanics to get the
792	        # return value. This is necessary because we currently will return a State object if the
793	        # the State was Prefect-created.
794	        # TODO: Remove the need to get the result from a State except in cases where the return value
795	        # is a State object.
796	        _result = self.state.result(raise_on_failure=raise_on_failure, _sync=True)  # type: ignore
797	        return _result
798	
799	    def handle_success(self, result: R) -> R:
```

## 99 · 2026-10-28T08:17:03.499288+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"ensure_bucket\\|increment_bucket\\|start_new_bucket\" src tests | grep -v \"def ensure_bucket\\|def increment_bucket\\|def start_new_bucket\"",
  "description": "Find bucket helper usages"
}
```

## 100 · 2026-10-28T08:17:05.100548+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:160:        bucket = await increment_bucket(session, bucket, count, triggering_event)
src/prefect/server/events/triggers.py:242:            return await start_new_bucket(
src/prefect/server/events/triggers.py:290:            bucket = await start_new_bucket(
src/prefect/server/events/triggers.py:300:            return await start_new_bucket(
src/prefect/server/events/triggers.py:619:                        bucket = await ensure_bucket(
src/prefect/server/events/triggers.py:645:                        bucket = await ensure_bucket(
src/prefect/server/events/triggers.py:1001:            last_operation="increment_bucket[insert]",
src/prefect/server/events/triggers.py:1011:                last_operation="increment_bucket[update]",
src/prefect/server/events/triggers.py:1056:            last_operation="start_new_bucket[insert]",
src/prefect/server/events/triggers.py:1070:                last_operation="start_new_bucket[update]",
src/prefect/server/events/triggers.py:1118:            last_operation="ensure_bucket[insert]",
src/prefect/server/events/triggers.py:1332:                await ensure_bucket(
```

## 101 · 2026-10-28T08:17:07.062899+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"last_event\" src/prefect tests/events | head -60",
  "description": "Find last_event usages"
}
```

## 102 · 2026-10-28T08:17:07.831757+00:00 · tool_result 

```
src/prefect/server/database/orm_models.py:1332:    last_event: Mapped[Optional[ReceivedEvent]] = mapped_column(Pydantic(ReceivedEvent))
src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py:92:            "last_event",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py:95:            "last_event",
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
src/prefect/server/models/events.py:724:    time_since_last_event = timedelta(hours=24)
src/prefect/server/models/events.py:726:        time_since_last_event = now("UTC") - work_pool.last_transitioned_status_at
src/prefect/server/models/events.py:730:        if time_since_last_event < timedelta(minutes=10)
src/prefect/task_engine.py:250:    _last_event: Optional[PrefectEvent] = None
src/prefect/task_engine.py:424:        self._last_event = emit_task_run_state_change_event(
src/prefect/task_engine.py:428:            follows=self._last_event,
src/prefect/task_engine.py:603:        self._last_event = emit_task_run_state_change_event(
src/prefect/task_engine.py:607:            follows=self._last_event,
src/prefect/task_engine.py:862:                            self._last_event = emit_task_run_state_change_event(
src/prefect/task_engine.py:1235:        self._last_event = emit_task_run_state_change_event(
src/prefect/task_engine.py:1239:            follows=self._last_event,
src/prefect/task_engine.py:1498:                            self._last_event = emit_task_run_state_change_event(
tests/events/server/test_events_api.py:107:def last_events_page(
tests/events/server/test_events_api.py:230:    last_events_page: mock.AsyncMock,
tests/events/server/test_events_api.py:239:    last_events_page.assert_awaited_once_with(
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

## 103 · 2026-10-28T08:17:10.069183+00:00 · assistant_message 

```
Let me establish a baseline by running the relevant trigger test suites before making changes.
```

## 104 · 2026-10-28T08:17:10.509692+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_regressions.py -q 2>&1 | tail -15",
  "description": "Run trigger regression tests baseline",
  "timeout": 900000
}
```

## 105 · 2026-10-28T08:18:37.874981+00:00 · tool_result 

```
............                                                             [100%]
12 passed in 75.23s (0:01:15)
```

## 106 · 2026-10-28T08:18:39.730081+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_basics.py -q 2>&1 | tail -8",
  "description": "Run trigger basics tests baseline",
  "timeout": 900000
}
```

## 107 · 2026-10-28T08:20:26.496409+00:00 · tool_result 

```
..................................                                       [100%]
34 passed in 95.39s (0:01:35)
```

## 108 · 2026-10-28T08:20:51.250098+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"zombie\\|heartbeat\" docs/v3/release-notes/oss/*.mdx | head -20",
  "description": "Search release notes for heartbeat feature"
}
```

## 109 · 2026-10-28T08:20:51.580139+00:00 · tool_result 

```
docs/v3/release-notes/oss/version-3-1.mdx:353:* Add an example for creating an automation to mark zombie flow runs as crashed by [@desertaxle](https://github.com/desertaxle) in [#16425](https://github.com/PrefectHQ/prefect/pull/16425)
docs/v3/release-notes/oss/version-3-1.mdx:367:Flow runs can now emit heartbeat events to detect infrastructure failures (crashed machines, evicted containers, etc). When enabled, an automation can automatically mark flows as crashed when heartbeats stop, preventing stuck "zombie" flows in the running state.
docs/v3/release-notes/oss/version-3-1.mdx:371:- Deploy the provided automation script to update flow states when heartbeats stop
docs/v3/release-notes/oss/version-3-1.mdx:380:    name="Crash zombie flows",
docs/v3/release-notes/oss/version-3-1.mdx:382:        after={"prefect.flow-run.heartbeat"},
docs/v3/release-notes/oss/version-3-1.mdx:384:            "prefect.flow-run.heartbeat",
docs/v3/release-notes/oss/version-3-1.mdx:399:            message="Flow run marked as crashed due to missing heartbeats.",
docs/v3/release-notes/oss/version-3-1.mdx:425:* Enhance `Runner` to send heartbeat events for flow runs by [@desertaxle](https://github.com/desertaxle) in [#16410](https://github.com/PrefectHQ/prefect/pull/16410)
docs/v3/release-notes/oss/version-3-1.mdx:761:* Send worker metadata with first heartbeat by [@abrookins](https://github.com/abrookins) in [#15898](https://github.com/PrefectHQ/prefect/pull/15898)
docs/v3/release-notes/oss/version-3-2.mdx:203:* Fix bug causing duplicate flow run heartbeats with a process worker by [@desertaxle](https://github.com/desertaxle) in [#17375](https://github.com/PrefectHQ/prefect/pull/17375)
docs/v3/release-notes/oss/version-3-4.mdx:842:* fix dead link to zombie flow runs by [@zzstoatzz](https://github.com/zzstoatzz) in [#18244](https://github.com/PrefectHQ/prefect/pull/18244)
docs/v3/release-notes/oss/version-3-4.mdx:1014:* handle heartbeat event in `wait_for_flow_run` by [@zzstoatzz](https://github.com/zzstoatzz) in [#17930](https://github.com/PrefectHQ/prefect/pull/17930)
docs/v3/release-notes/oss/version-3-6.mdx:30:* Fix wildcard in zombie flow detection docs for custom state names by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21736](https://github.com/PrefectHQ/prefect/pull/21736)
docs/v3/release-notes/oss/version-3-6.mdx:107:* Propagate contextvars to the flow heartbeat thread by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#21577](https://github.com/PrefectHQ/prefect/pull/21577)
docs/v3/release-notes/oss/version-3-6.mdx:233:* Fix heartbeat starvation under CPU-bound workloads by [@desertaxle](https://github.com/desertaxle) in [#21276](https://github.com/PrefectHQ/prefect/pull/21276)
docs/v3/release-notes/oss/version-3-6.mdx:294:* Enforce minimum heartbeat interval at the engine level by [@desertaxle](https://github.com/desertaxle) in [#21188](https://github.com/PrefectHQ/prefect/pull/21188)
docs/v3/release-notes/oss/version-3-6.mdx:340:* Change heartbeat default from `None` to 180s by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#21058](https://github.com/PrefectHQ/prefect/pull/21058)
docs/v3/release-notes/oss/version-3-6.mdx:365:* Fix flaky `test_two_subscriptions_get_all_events` by handling `None` heartbeats by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#21037](https://github.com/PrefectHQ/prefect/pull/21037)
docs/v3/release-notes/oss/version-3-6.mdx:367:* Disable heartbeats in tests to fix CI timeout by [@desertaxle](https://github.com/desertaxle) in [#21062](https://github.com/PrefectHQ/prefect/pull/21062)
docs/v3/release-notes/oss/version-3-6.mdx:746:## 3.6.13 - The heartbeat is coming from *inside* the engine
```

## 110 · 2026-10-28T08:20:51.632138+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/events/server/triggers/ && grep -rn \"proactive\" tests/events/server/triggers/test_service_changes.py | head",
  "description": "Inspect trigger test files"
}
```

## 111 · 2026-10-28T08:20:51.980933+00:00 · tool_result 

```
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

## 112 · 2026-10-28T08:21:13.564317+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"flow-run\\|payload\\[\" src/prefect/server/events/triggers.py | head -20; grep -rn \"StateType\" src/prefect/server/events/ | head",
  "description": "Check flow-run coupling in triggers"
}
```

## 113 · 2026-10-28T08:21:13.914762+00:00 · tool_result 

```
src/prefect/server/events/actions.py:73:from prefect.server.schemas.states import Scheduled, State, StateType, Suspended
src/prefect/server/events/actions.py:533:                        type=StateType(resource["prefect.state-type"]),
src/prefect/server/events/actions.py:1159:    state: StateType = Field(
src/prefect/server/events/actions.py:1192:            type=StateType.CANCELLING,
```

## 114 · 2026-10-28T08:21:13.946730+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"class StateType\" -A 20 src/prefect/server/schemas/states.py | head -30; grep -rn \"def is_final\" -B3 -A8 src/prefect/server/schemas/states.py",
  "description": "Inspect state type definitions"
}
```

## 115 · 2026-10-28T08:21:14.337927+00:00 · tool_result 

```
40:class StateType(AutoEnum):
41-    """Enumeration of state types."""
42-
43-    SCHEDULED = AutoEnum.auto()
44-    PENDING = AutoEnum.auto()
45-    RUNNING = AutoEnum.auto()
46-    COMPLETED = AutoEnum.auto()
47-    FAILED = AutoEnum.auto()
48-    CANCELLED = AutoEnum.auto()
49-    CRASHED = AutoEnum.auto()
50-    PAUSED = AutoEnum.auto()
51-    CANCELLING = AutoEnum.auto()
52-
53-
54-class CountByState(PrefectBaseModel):
55-    COMPLETED: int = Field(default=0)
56-    PENDING: int = Field(default=0)
57-    RUNNING: int = Field(default=0)
58-    FAILED: int = Field(default=0)
59-    CANCELLED: int = Field(default=0)
60-    CRASHED: int = Field(default=0)
207-    def is_cancelling(self) -> bool:
208-        return self.type == StateType.CANCELLING
209-
210:    def is_final(self) -> bool:
211-        return self.type in TERMINAL_STATES
212-
213-    def is_paused(self) -> bool:
214-        return self.type == StateType.PAUSED
215-
216-    def fresh_copy(self, **kwargs: Any) -> Self:
217-        """
218-        Return a fresh copy of the state with a new ID.
```

## 116 · 2026-10-28T08:21:53.225413+00:00 · assistant_message 

```
Now I understand the root cause. Let me implement the fix in the bucket evaluation logic.
```

## 117 · 2026-10-28T08:21:53.640674+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "limit": 50,
  "offset": 136
}
```

## 118 · 2026-10-28T08:21:53.749735+00:00 · tool_result 

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
```

## 119 · 2026-10-28T08:22:01.367268+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "AUTOMATION_BUCKET_BATCH_SIZE = 500\n\n\nasync def evaluate(",
  "new_string": "AUTOMATION_BUCKET_BATCH_SIZE = 500\n\n\ndef _event_is_at_least_as_recent(\n    event: Optional[ReceivedEvent], previous: Optional[ReceivedEvent]\n) -> bool:\n    \"\"\"Whether ``event`` is at least as recent as the last event on a bucket.\n\n    Events that share an ``occurred`` timestamp are considered equally recent: a\n    distinct event that happened at the same instant does not supersede the event\n    that was already recorded for that instant.  This keeps ``last_event``\n    monotonically increasing so an out-of-order or duplicate event cannot make the\n    bucket forget about a newer event that has already been accounted for.\n    \"\"\"\n    if event is None:\n        return False\n    if previous is None or event.id == previous.id:\n        return True\n    return event.occurred > previous.occurred\n\n\ndef _can_restart_proactive_window(\n    trigger: EventTrigger,\n    triggering_event: ReceivedEvent,\n    previous_last_event: Optional[ReceivedEvent],\n) -> bool:\n    \"\"\"Whether a proactive window may be restarted at ``triggering_event``.\n\n    An ``after`` event that also matches ``expect`` restarts the window so the\n    trigger waits for the next expected event.  That is only safe when the event is\n    newer than everything the bucket has already seen.  In particular, when an\n    expected event (such as a flow run reaching a terminal state) was observed at\n    the same moment as, or after, this ``after`` event, restarting the window would\n    discard that observation and produce a false positive even though the resource\n    already responded.\n    \"\"\"\n    if previous_last_event is None:\n        return True\n    if previous_last_event.id == triggering_event.id:\n        return True\n    if not trigger.expects(previous_last_event.event):\n        # The previous event does not satisfy what this trigger is waiting for, so\n        # it does not represent a response that should keep the window from being\n        # restarted.\n        return True\n    return triggering_event.occurred > previous_last_event.occurred\n\n\nasync def evaluate("
}
```

## 120 · 2026-10-28T08:22:01.491436+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 121 · 2026-10-28T08:22:03.599637+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    if count and (trigger.immediate or bucket.start <= now < bucket.end):\n        # we are still within the automation time period, so spend the count in the\n        # current bucket\n        bucket = await increment_bucket(session, bucket, count, triggering_event)\n        count = 0",
  "new_string": "    # Remember the most recent event this bucket had already accounted for before\n    # this evaluation.  It may be newer than the triggering event when events arrive\n    # out of order (or at the same instant); in that case it must not be replaced by\n    # the older event, and a proactive window must not be restarted at the older one.\n    previous_last_event = bucket.last_event\n\n    if count and (trigger.immediate or bucket.start <= now < bucket.end):\n        # we are still within the automation time period, so spend the count in the\n        # current bucket\n        last_event = (\n            triggering_event\n            if _event_is_at_least_as_recent(triggering_event, previous_last_event)\n            else None\n        )\n        bucket = await increment_bucket(session, bucket, count, last_event)\n        count = 0"
}
```

## 122 · 2026-10-28T08:22:03.723829+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 123 · 2026-10-28T08:22:05.472899+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "        if (\n            triggering_event\n            and trigger.posture == Posture.Proactive\n            and not meets_threshold\n            and trigger.starts_after(triggering_event.event)\n            and trigger.expects(triggering_event.event)\n        ):\n            await remove_bucket(session, bucket)",
  "new_string": "        if (\n            triggering_event\n            and trigger.posture == Posture.Proactive\n            and not meets_threshold\n            and trigger.starts_after(triggering_event.event)\n            and trigger.expects(triggering_event.event)\n            and _can_restart_proactive_window(\n                trigger, triggering_event, previous_last_event\n            )\n        ):\n            await remove_bucket(session, bucket)"
}
```

## 124 · 2026-10-28T08:22:05.564908+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 125 · 2026-10-28T08:22:07.296582+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "limit": 70,
  "offset": 1148
}
```

## 126 · 2026-10-28T08:22:07.396624+00:00 · tool_result 

```
1148	
1149	
1150	@db_injector
1151	async def ensure_bucket(
1152	    db: PrefectDBInterface,
1153	    session: AsyncSession,
1154	    trigger: EventTrigger,
1155	    bucketing_key: Tuple[str, ...],
1156	    start: prefect.types._datetime.DateTime,
1157	    end: prefect.types._datetime.DateTime,
1158	    last_event: Optional[ReceivedEvent],
1159	    initial_count: int = 0,
1160	) -> "ORMAutomationBucket":
1161	    """Ensures that a bucket has been started for the given automation and key,
1162	    returning the current bucket.  Will not modify the existing bucket."""
1163	    automation = trigger.automation
1164	    additional_updates: dict[str, ReceivedEvent] = (
1165	        {"last_event": last_event} if last_event else {}
1166	    )
1167	    await session.execute(
1168	        db.queries.insert(db.AutomationBucket)
1169	        .values(
1170	            automation_id=automation.id,
1171	            trigger_id=trigger.id,
1172	            bucketing_key=bucketing_key,
1173	            last_event=last_event,
1174	            start=start,
1175	            end=end,
1176	            count=initial_count,
1177	            last_operation="ensure_bucket[insert]",
1178	        )
1179	        .on_conflict_do_update(
1180	            index_elements=[
1181	                db.AutomationBucket.automation_id,
1182	                db.AutomationBucket.trigger_id,
1183	                db.AutomationBucket.bucketing_key,
1184	            ],
1185	            set_=dict(
1186	                # no-op, but this counts as an update so the query returns a row
1187	                count=db.AutomationBucket.count,
1188	                **additional_updates,
1189	            ),
1190	        )
1191	    )
1192	
1193	    read_bucket = await read_bucket_by_trigger_id(
1194	        session, automation.id, trigger.id, tuple(bucketing_key)
1195	    )
1196	
1197	    if TYPE_CHECKING:
1198	        assert read_bucket is not None
1199	
1200	    return read_bucket
1201	
1202	
1203	@db_injector
1204	async def remove_bucket(
1205	    db: PrefectDBInterface, session: AsyncSession, bucket: "ORMAutomationBucket"
1206	):
1207	    """Removes the given bucket from the database"""
1208	    await session.execute(
1209	        sa.delete(db.AutomationBucket).where(
1210	            db.AutomationBucket.automation_id == bucket.automation_id,
1211	            db.AutomationBucket.trigger_id == bucket.trigger_id,
1212	            db.AutomationBucket.bucketing_key == bucket.bucketing_key,
1213	        )
1214	    )
1215	
1216	
1217	@db_injector
```

## 127 · 2026-10-28T08:22:10.205671+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "    \"\"\"Ensures that a bucket has been started for the given automation and key,\n    returning the current bucket.  Will not modify the existing bucket.\"\"\"\n    automation = trigger.automation\n    additional_updates: dict[str, ReceivedEvent] = (\n        {\"last_event\": last_event} if last_event else {}\n    )\n    await session.execute(\n        db.queries.insert(db.AutomationBucket)\n        .values(\n            automation_id=automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event=last_event,\n            start=start,\n            end=end,\n            count=initial_count,\n            last_operation=\"ensure_bucket[insert]\",\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationBucket.automation_id,\n                db.AutomationBucket.trigger_id,\n                db.AutomationBucket.bucketing_key,\n            ],\n            set_=dict(\n                # no-op, but this counts as an update so the query returns a row\n                count=db.AutomationBucket.count,\n                **additional_updates,\n            ),\n        )\n    )",
  "new_string": "    \"\"\"Ensures that a bucket has been started for the given automation and key,\n    returning the current bucket.  Will not modify the existing bucket.\"\"\"\n    automation = trigger.automation\n    await session.execute(\n        db.queries.insert(db.AutomationBucket)\n        .values(\n            automation_id=automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event=last_event,\n            start=start,\n            end=end,\n            count=initial_count,\n            last_operation=\"ensure_bucket[insert]\",\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationBucket.automation_id,\n                db.AutomationBucket.trigger_id,\n                db.AutomationBucket.bucketing_key,\n            ],\n            set_=dict(\n                # no-op, but this counts as an update so the query returns a row.\n                # Importantly, an existing bucket is left untouched: its\n                # `last_event` is only advanced by `increment_bucket` (which keeps\n                # the most recent event), so an out-of-order event cannot replace a\n                # newer one that has already been recorded.\n                count=db.AutomationBucket.count,\n            ),\n        )\n    )"
}
```

## 128 · 2026-10-28T08:22:10.315269+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 129 · 2026-10-28T08:22:11.982513+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | tail -20",
  "description": "Run incident test after fix",
  "timeout": 300000
}
```

## 130 · 2026-10-28T08:22:45.664476+00:00 · tool_result 

```
16:22:42.242 | INFO    | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133, trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 covers event 'prefect.flow-run.heartbeat' (22222222-2222-4222-8222-222222222222) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:23:11.440342+00:00'
16:22:42.514 | DEBUG   | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133 ('Unresponsive run monitor') trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
16:22:42.668 | INFO    | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133, trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 covers event 'prefect.flow-run.Completed' (33333333-3333-4333-8333-333333333333) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:23:41.440342+00:00'
16:22:42.866 | DEBUG   | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133 ('Unresponsive run monitor') trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
16:22:42.898 | INFO    | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133, trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 covers event 'prefect.flow-run.heartbeat' (44444444-4444-4444-8444-444444444444) for 'prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa' at '2026-10-28T08:23:41.440342+00:00'
16:22:43.123 | DEBUG   | prefect.server.events.triggers - Automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133 ('Unresponsive run monitor') trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 has more time for keys (['prefect.flow-run.aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa'])
16:22:43.158 | DEBUG   | prefect.server.events.triggers - Evaluating automation e0dd617b-fd7d-49aa-906b-f5aaa3e04133 trigger 05cb03ba-286a-49dd-81f0-9f6bfb937850 proactively as of 2026-10-28 08:25:12.440342+00:00 (offset 0.0s)
Generating test database connection URL from 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
Running hosted API server on port 55587
{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
.16:22:43.399 | INFO    | uvicorn.error - Shutting down
16:22:43.509 | INFO    | uvicorn.error - Waiting for application shutdown.
16:22:43.510 | INFO    | uvicorn.error - Application shutdown complete.
16:22:43.511 | INFO    | uvicorn.error - Finished server process [38064]

1 passed in 22.64s
```

## 131 · 2026-10-28T08:22:46.812915+00:00 · assistant_message 

```
The incident now produces zero actions. Let me verify the existing trigger behavior is preserved.
```

## 132 · 2026-10-28T08:22:47.338781+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_regressions.py tests/events/server/triggers/test_basics.py -q 2>&1 | tail -8",
  "description": "Run trigger regression and basics tests",
  "timeout": 1200000
}
```

## 133 · 2026-10-28T08:25:30.325910+00:00 · tool_result 

```
..............................................                           [100%]
46 passed in 151.45s (0:02:31)
```

## 134 · 2026-10-28T08:25:35.415680+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"TERMINAL_STATES\" src/prefect/server/schemas/states.py src/prefect/client/schemas/objects.py | head -10; grep -rn \"^from\\|^import\" src/prefect/server/schemas/states.py | head -30",
  "description": "Find TERMINAL_STATES definition"
}
```

## 135 · 2026-10-28T08:25:35.824077+00:00 · tool_result 

```
src/prefect/server/schemas/states.py:73:TERMINAL_STATES = {
src/prefect/server/schemas/states.py:211:        return self.type in TERMINAL_STATES
src/prefect/client/schemas/objects.py:103:TERMINAL_STATES: set[StateType] = {
src/prefect/client/schemas/objects.py:450:        return self.type in TERMINAL_STATES
5:import warnings
6:from datetime import timedelta
7:from typing import (
17:from uuid import UUID
19:from pydantic import ConfigDict, Field, ValidationInfo, field_validator, model_validator
20:from typing_extensions import Self
22:from prefect._internal.uuid7 import uuid7
23:from prefect.client.schemas import objects
24:from prefect.server.utilities.schemas.bases import (
28:from prefect.types._datetime import DateTime, now
29:from prefect.utilities.collections import AutoEnum
```

## 136 · 2026-10-28T08:25:53.635636+00:00 · assistant_message 

```
Let me review the complete diff so far.
```

## 137 · 2026-10-28T08:25:53.640634+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '78,135p' src/prefect/server/events/triggers.py && echo ---- && sed -n '175,300p' src/prefect/server/events/triggers.py",
  "description": "Review modified evaluate and helpers"
}
```

## 138 · 2026-10-28T08:25:53.973042+00:00 · tool_result 

```
AutomationID: TypeAlias = UUID
TriggerID: TypeAlias = UUID
AutomationStateSnapshot: TypeAlias = Tuple[
    Optional[prefect.types._datetime.DateTime], int
]


AUTOMATION_BUCKET_BATCH_SIZE = 500


def _event_is_at_least_as_recent(
    event: Optional[ReceivedEvent], previous: Optional[ReceivedEvent]
) -> bool:
    """Whether ``event`` is at least as recent as the last event on a bucket.

    Events that share an ``occurred`` timestamp are considered equally recent: a
    distinct event that happened at the same instant does not supersede the event
    that was already recorded for that instant.  This keeps ``last_event``
    monotonically increasing so an out-of-order or duplicate event cannot make the
    bucket forget about a newer event that has already been accounted for.
    """
    if event is None:
        return False
    if previous is None or event.id == previous.id:
        return True
    return event.occurred > previous.occurred


def _can_restart_proactive_window(
    trigger: EventTrigger,
    triggering_event: ReceivedEvent,
    previous_last_event: Optional[ReceivedEvent],
) -> bool:
    """Whether a proactive window may be restarted at ``triggering_event``.

    An ``after`` event that also matches ``expect`` restarts the window so the
    trigger waits for the next expected event.  That is only safe when the event is
    newer than everything the bucket has already seen.  In particular, when an
    expected event (such as a flow run reaching a terminal state) was observed at
    the same moment as, or after, this ``after`` event, restarting the window would
    discard that observation and produce a false positive even though the resource
    already responded.
    """
    if previous_last_event is None:
        return True
    if previous_last_event.id == triggering_event.id:
        return True
    if not trigger.expects(previous_last_event.event):
        # The previous event does not satisfy what this trigger is waiting for, so
        # it does not represent a response that should keep the window from being
        # restarted.
        return True
    return triggering_event.occurred > previous_last_event.occurred


async def evaluate(
    session: AsyncSession,
    trigger: EventTrigger,
----
    #    we fire immediately and advance the bucket to the next time period.
    # 4. The event matches the current bucket, but the event is for a future time after
    #    the current bucket has expired, so we will start the new bucket and re-evaluate
    #
    # Automations are also evaluated proactively without an event to see if they have
    # met their proactive threshold (where not enough events have happened in the time
    # period)

    # If there was a triggering event, then we need to "spend" this count somewhere,
    # either in the currently open bucket or in the next time period's bucket
    count = 1 if triggering_event else 0

    if now < bucket.start:
        # This is an older out-of-order message or a redundant event for a reactive
        # trigger that has has already fired, so it should not should not affect the
        # current bucket.  We can safely ignore this event/timestamp entirely.  Case #1
        # from the implementation notes above.
        logger.debug(
            "Automation %s (%r) trigger %s got a late event for keys (%r)",
            automation.id,
            automation.name,
            trigger.id,
            bucket.bucketing_key,
            extra=logging_context,
        )
        return bucket

    # Remember the most recent event this bucket had already accounted for before
    # this evaluation.  It may be newer than the triggering event when events arrive
    # out of order (or at the same instant); in that case it must not be replaced by
    # the older event, and a proactive window must not be restarted at the older one.
    previous_last_event = bucket.last_event

    if count and (trigger.immediate or bucket.start <= now < bucket.end):
        # we are still within the automation time period, so spend the count in the
        # current bucket
        last_event = (
            triggering_event
            if _event_is_at_least_as_recent(triggering_event, previous_last_event)
            else None
        )
        bucket = await increment_bucket(session, bucket, count, last_event)
        count = 0

    # Reactive automations will fire "eagerly", meaning they will fire as _soon_ as the
    # threshold is reached, then wait for the rest of their time period before
    # firing again.  This is done by creating a new bucket in the future after the
    # trigger has fired.

    # Proactive automations must wait until the whole bucket has expired before they can
    # fire, because we can't know if we'll get one late event just in time to cause the
    # automation _not_ to fire.

    ready_to_fire = trigger.posture == Posture.Reactive or bucket.end <= now
    meets_threshold = trigger.meets_threshold(bucket.count)

    if ready_to_fire and meets_threshold:
        logger.debug(
            (
                "Automation %s (%r) trigger %s triggered for keys (%r) %s, "
                "having occurred %s times between %s and %s"
            ),
            automation.id,
            automation.name,
            trigger.id,
            bucket.bucketing_key,
            "reactively" if triggering_event else "proactively",
            bucket.count,
            bucket.start,
            bucket.end,
            extra=logging_context,
        )

        firing = Firing(
            trigger=trigger,
            trigger_states={TriggerState.Triggered},
            triggered=prefect.types._datetime.now("UTC"),
            triggering_labels={
                label: value
                for label, value in zip(sorted(trigger.for_each), bucket.bucketing_key)
            },
            triggering_event=triggering_event or bucket.last_event,
        )

        await fire(session, firing)

        # when acting, remove the current bucket from the database immediately to avoid
        # potentially double-acting in the case of a crash between now and the next
        # time we backup buckets to the database
        await remove_bucket(session, bucket)

    elif now < bucket.end:
        # We didn't fire this time, and also the bucket still has more time, so leave
        # before setting up a new future bucket.  Case #2 from the implementation notes
        # above.
        logger.debug(
            "Automation %s (%r) trigger %s has more time for keys (%r)",
            automation.id,
            automation.name,
            trigger.id,
            bucket.bucketing_key,
            extra={
                **logging_context,
                "ready_to_fire": ready_to_fire,
                "meets_threshold": meets_threshold,
            },
        )

        # Special case of a proactive trigger for which the same event satisfies
        # both `after` and `expect`.  For example, using flow run heartbeats for crash
        # detection, after the first heartbeat we expect a subsequent heartbeat or
        # terminal state within a given time.
        #
        # If we've already reached the proactive threshold, we need to remove the
        # current bucket and start a new one for the latest event.
        if (
            triggering_event
            and trigger.posture == Posture.Proactive
            and not meets_threshold
            and trigger.starts_after(triggering_event.event)
            and trigger.expects(triggering_event.event)
            and _can_restart_proactive_window(
                trigger, triggering_event, previous_last_event
            )
        ):
            await remove_bucket(session, bucket)
```

## 139 · 2026-10-28T08:25:59.876888+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"chonk_sadness\" -B5 -A40 tests/events/server/triggers/test_basics.py | head -90",
  "description": "Inspect chonk_sadness fixture and expectations"
}
```

## 140 · 2026-10-28T08:26:00.196099+00:00 · tool_result 

```
182-    cleared_automations: None,
183-    automations_session: AsyncSession,
184-    arachnophobia: Automation,
185-    chonk_lonely: Automation,
186-    chonk_party: Automation,
187:    chonk_sadness: Automation,
188-):
189:    for automation in [arachnophobia, chonk_party, chonk_sadness, chonk_lonely]:
190-        persisted = await automations.create_automation(automations_session, automation)
191-        automation.created = persisted.created
192-        automation.updated = persisted.updated
193-        triggers.load_automation(persisted)
194-    await automations_session.commit()
195:    return [arachnophobia, chonk_lonely, chonk_party, chonk_sadness]
196-
197-
198-async def test_reactive_automation_triggers_can_trigger_immediately(
199-    effective_automations,
200-    arachnophobia: Automation,
201-    daddy_long_legs_walked: ReceivedEvent,
202-    act: mock.AsyncMock,
203-    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
204-    frozen_time: DateTime,
205-):
206-    await triggers.reactive_evaluation(daddy_long_legs_walked)
207-    assert_acted_with(
208-        Firing(
209-            trigger=arachnophobia.trigger,
210-            trigger_states={TriggerState.Triggered},
211-            triggered=frozen_time,  # type: ignore
212-            triggering_labels={},
213-            triggering_event=daddy_long_legs_walked,
214-        ),
215-    )
216-
217-    act.reset_mock()
218-
219-    # The minimum window is 10 seconds, so advance to just after that
220-    daddy_long_legs_walked.occurred += timedelta(seconds=10, microseconds=1)
221-
222-    await triggers.reactive_evaluation(daddy_long_legs_walked)
223-    assert_acted_with(
224-        Firing(
225-            trigger=arachnophobia.trigger,
226-            trigger_states={TriggerState.Triggered},
227-            triggered=frozen_time,  # type: ignore
228-            triggering_labels={},
229-            triggering_event=daddy_long_legs_walked,
230-        ),
231-    )
232-
233-
234-async def test_reactive_automation_triggers_only_on_expected_events(
235-    effective_automations,
--
472-    )
473-
474-
475-async def test_proactive_trigger_fires_after_time_expires(
476-    effective_automations: List[Automation],
477:    chonk_sadness: Automation,
478-    start_of_test: DateTime,
479-    act: mock.AsyncMock,
480-    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
481-    frozen_time: DateTime,
482-):
483-    async def run_proactive_evaluation(automations: List[Automation], as_of: DateTime):
484-        for automation in automations:
485-            trigger = automation.trigger
486-            assert isinstance(trigger, EventTrigger), repr(trigger)
487-            await triggers.proactive_evaluation(trigger, as_of)
488-
489-    await run_proactive_evaluation(effective_automations, start_of_test)
490-    act.assert_not_awaited()
491-
492-    await run_proactive_evaluation(
493-        effective_automations, start_of_test + timedelta(seconds=9)
494-    )
495-    act.assert_not_awaited()
496-
497-    await run_proactive_evaluation(
498-        effective_automations,
499-        start_of_test + timedelta(seconds=10),
500-    )
501-    act.assert_not_awaited()
502-
503-    await run_proactive_evaluation(
504-        effective_automations,
505-        start_of_test + timedelta(seconds=30),
506-    )
```

## 141 · 2026-10-28T08:26:04.043825+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"def receive\" -A 20 src/prefect/server/events/schemas/events.py",
  "description": "Read Event.receive signature"
}
```

## 142 · 2026-10-28T08:26:04.324348+00:00 · tool_result 

```
185:    def receive(
186-        self, received: Optional[prefect.types._datetime.DateTime] = None
187-    ) -> "ReceivedEvent":
188-        kwargs = self.model_dump()
189-        if received is not None:
190-            kwargs["received"] = received
191-        return ReceivedEvent(**kwargs)
192-
193-    def find_resource_label(self, label: str) -> Optional[str]:
194-        """Finds the value of the given label in this event's resource or one of its
195-        related resources.  If the label starts with `related:<role>:`, search for the
196-        first matching label in a related resource with that role."""
197-        directive, _, related_label = label.rpartition(":")
198-        directive, _, role = directive.partition(":")
199-        if directive == "related":
200-            for related in self.related:
201-                if related.role == role:
202-                    return related.get(related_label)
203-        return self.resource.get(label)
204-
205-
```

## 143 · 2026-10-28T08:26:25.807517+00:00 · assistant_message 

```
Now let me add focused regression tests covering the incident and the ordering guarantees.
```

## 144 · 2026-10-28T08:26:26.085372+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "limit": 60,
  "offset": 860
}
```

## 145 · 2026-10-28T08:26:26.193092+00:00 · tool_result 

```
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
```

## 146 · 2026-10-28T08:26:31.013863+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "old_string": "    assert_acted_with(\n        Firing(\n            trigger=zombie_flow_detection_automation.trigger,\n            trigger_states={TriggerState.Triggered},\n            triggered=frozen_time,  # type: ignore\n            triggering_labels={\n                \"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"\n            },\n            triggering_event=second_heartbeat,\n        )\n    )\n\n\n@pytest.fixture\nasync def proactive_extended_expect_and_after_with_threshold_1(",
  "new_string": "    assert_acted_with(\n        Firing(\n            trigger=zombie_flow_detection_automation.trigger,\n            trigger_states={TriggerState.Triggered},\n            triggered=frozen_time,  # type: ignore\n            triggering_labels={\n                \"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"\n            },\n            triggering_event=second_heartbeat,\n        )\n    )\n\n\nasync def test_zombie_flow_detection_ignores_heartbeat_that_predates_terminal_event(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    zombie_flow_detection_automation: Automation,\n):\n    \"\"\"A terminal state event satisfies the window and must not be undone by a\n    concurrent or stale heartbeat that arrives afterwards.\n\n    This is the incident reproduction: the run completes at the same moment as its\n    final heartbeat, but the heartbeat is received after the completion event.  The\n    heartbeat must not restart the window, because the run already responded by\n    completing.\n    \"\"\"\n    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)\n    flow_run_id = uuid4()\n    resource = {\"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"}\n\n    first_heartbeat = Event(\n        occurred=frozen_time,\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=0.1))\n    second_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=30),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=30.1))\n    completed = Event(\n        occurred=frozen_time + timedelta(seconds=60),\n        event=\"prefect.flow-run.Completed\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.1))\n    stale_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=60),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.2))\n\n    for event in (\n        first_heartbeat,\n        second_heartbeat,\n        completed,\n        stale_heartbeat,\n    ):\n        await triggers.reactive_evaluation(event)\n\n    await triggers.proactive_evaluation(\n        zombie_flow_detection_automation.trigger,\n        frozen_time + timedelta(seconds=151),\n    )\n    act.assert_not_awaited()\n\n\nasync def test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    zombie_flow_detection_automation: Automation,\n):\n    \"\"\"An out-of-order heartbeat older than an already-seen terminal event must not\n    move the window backwards and cause a false unresponsive-run action.\"\"\"\n    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)\n    flow_run_id = uuid4()\n    resource = {\"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"}\n\n    first_heartbeat = Event(\n        occurred=frozen_time,\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n    second_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=30),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n    completed = Event(\n        occurred=frozen_time + timedelta(seconds=60),\n        event=\"prefect.flow-run.Completed\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.1))\n    older_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=50),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.2))\n\n    for event in (\n        first_heartbeat,\n        second_heartbeat,\n        completed,\n        older_heartbeat,\n    ):\n        await triggers.reactive_evaluation(event)\n\n    await triggers.proactive_evaluation(\n        zombie_flow_detection_automation.trigger,\n        frozen_time + timedelta(seconds=151),\n    )\n    act.assert_not_awaited()\n\n\n@pytest.fixture\nasync def proactive_extended_expect_and_after_with_threshold_1("
}
```

## 147 · 2026-10-28T08:26:31.114847+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_regressions.py has been updated successfully.
```

## 148 · 2026-10-28T08:26:32.537937+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_regressions.py -q 2>&1 | tail -8",
  "description": "Run regression tests including new ones",
  "timeout": 900000
}
```

## 149 · 2026-10-28T08:28:07.625737+00:00 · tool_result 

```
..............                                                           [100%]
14 passed in 84.09s (0:01:24)
```

## 150 · 2026-10-28T08:28:12.436195+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers -q --ignore=tests/events/server/triggers/test_incident_completed_run.py 2>&1 | tail -10",
  "description": "Run full triggers test directory",
  "timeout": 1800000
}
```

## 151 · 2026-10-28T08:34:10.841104+00:00 · tool_result 

```
.................................................x...x...X.............. [ 59%]
.................................................                        [100%]
118 passed, 2 xfailed, 1 xpassed in 346.88s (0:05:46)
```

## 152 · 2026-10-28T08:34:15.565322+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '1,160p' tests/events/server/triggers/conftest.py",
  "description": "Read triggers conftest fixtures"
}
```

## 153 · 2026-10-28T08:34:15.918181+00:00 · tool_result 

```
from typing import Callable, List, Tuple, Union
from unittest import mock

import pytest

from prefect.server.events import messaging, triggers
from prefect.server.events.schemas.automations import Firing


@pytest.fixture(autouse=True)
async def reset_triggers(cleared_automations: None):
    await triggers.reset()
    yield
    await triggers.reset()


@pytest.fixture
async def reset_events_clock():
    await triggers.reset_events_clock()


@pytest.fixture
def actions_publish_mocks(
    monkeypatch: pytest.MonkeyPatch,
) -> Tuple[mock.MagicMock, mock.AsyncMock]:
    mock_create_publisher = mock.MagicMock(spec=messaging.create_actions_publisher)
    mock_publish = mock.AsyncMock()
    mock_create_publisher.return_value.__aenter__.return_value.publish_data = (
        mock_publish
    )

    monkeypatch.setattr(
        "prefect.server.events.messaging.create_actions_publisher",
        mock_create_publisher,
    )

    return mock_create_publisher, mock_publish


@pytest.fixture
def actions_publish(
    actions_publish_mocks: Tuple[mock.MagicMock, mock.AsyncMock],
) -> mock.AsyncMock:
    return actions_publish_mocks[1]


@pytest.fixture
def create_actions_publisher(
    actions_publish_mocks: Tuple[mock.MagicMock, mock.AsyncMock],
) -> mock.MagicMock:
    return actions_publish_mocks[0]


@pytest.fixture
def assert_acted_with(
    act: mock.AsyncMock,
) -> Callable[[Union[Firing, List[Firing]]], None]:
    def assertion(expected: Union[Firing, List[Firing]]):
        if not isinstance(expected, list):
            expected = [expected]

        assert act.await_count == len(expected)
        actuals: list[Firing] = [args[0][0] for args in act.await_args_list]
        for actual in actuals:
            assert isinstance(actual, Firing)

        dumped_actuals = [actual.model_dump(exclude={"id"}) for actual in actuals]
        dumped_expected = [exp.model_dump(exclude={"id"}) for exp in expected]
        for exp in dumped_expected:
            assert exp in dumped_actuals

    return assertion
```

## 154 · 2026-10-28T08:34:19.924329+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py 2>&1 | tail -20; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py 2>&1 | tail -10",
  "description": "Run ruff lint and format check"
}
```

## 155 · 2026-10-28T08:34:20.922484+00:00 · tool_result 

```
PIE808 [*] Unnecessary `start` argument in `range`
    --> tests\events\server\triggers\test_regressions.py:1067:25
     |
1065 |     heartbeat_times = range(1, 3)
1066 |
1067 |     for minute in range(0, 11):
     |                         ^
1068 |         if minute in evaluate_proactive_times:
1069 |             act.reset_mock()
     |
help: Remove `start` argument
     |
1066 |
     -     for minute in range(0, 11):
1067 +     for minute in range(11):
1068 |         if minute in evaluate_proactive_times:
     |

Found 63 errors.
[*] 50 fixable with the `--fix` option (3 hidden fixes can be enabled with the `--unsafe-fixes` option).
2 files already formatted
```

## 156 · 2026-10-28T08:34:23.411835+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check src/prefect/server/events/triggers.py 2>&1 | tail -20; echo \"---counts---\"; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check tests/events/server/triggers/test_regressions.py --output-format concise 2>&1 | head -20",
  "description": "Check ruff on source file and list test errors"
}
```

## 157 · 2026-10-28T08:34:24.312544+00:00 · tool_result 

```
1297 |             logger.error(
     |                    ^^^^^
1298 |                 f"Error in automation change listener: {e}. Reconnecting in {reconnect_seconds}s...",
1299 |                 exc_info=True,
     |

C408 Unnecessary `tuple()` call (rewrite as a literal)
    --> src\prefect\server\events\triggers.py:1394:35
     |
1392 |                     session,
1393 |                     trigger,
1394 |                     bucketing_key=tuple(),
     |                                   ^^^^^^^
1395 |                     start=as_of,
1396 |                     end=as_of + trigger.within,
     |
help: Rewrite as a literal

Found 48 errors.
[*] 36 fixable with the `--fix` option (3 hidden fixes can be enabled with the `--unsafe-fixes` option).
---counts---
tests\events\server\triggers\test_regressions.py:4:1: UP035 [*] Import from `collections.abc` instead: `Callable`
tests\events\server\triggers\test_regressions.py:4:1: UP035 `typing.List` is deprecated, use `list` instead
tests\events\server\triggers\test_regressions.py:84:6: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:103:6: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:129:34: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:131:34: UP007 [*] Use `X | Y` for type annotations
tests\events\server\triggers\test_regressions.py:131:48: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:166:32: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:562:34: UP007 [*] Use `X | Y` for type annotations
tests\events\server\triggers\test_regressions.py:562:48: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:767:34: UP007 [*] Use `X | Y` for type annotations
tests\events\server\triggers\test_regressions.py:767:48: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:870:34: UP007 [*] Use `X | Y` for type annotations
tests\events\server\triggers\test_regressions.py:870:48: UP006 [*] Use `list` instead of `List` for type annotation
tests\events\server\triggers\test_regressions.py:1067:25: PIE808 [*] Unnecessary `start` argument in `range`
Found 15 errors.
[*] 14 fixable with the `--fix` option.
```

## 158 · 2026-10-28T08:34:26.846071+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check src/prefect/server/events/triggers.py --output-format concise 2>&1 | grep -E \":(9[0-9]|1[0-2][0-9]|2[0-9][0-9]|3[0-2][0-9]|11[5-9][0-9]|12[0-1][0-9]):\" | head -20",
  "description": "Check ruff errors in modified source ranges"
}
```

## 159 · 2026-10-28T08:34:27.379130+00:00 · tool_result 

```
src\prefect\server\events\triggers.py:109:26: UP045 [*] Use `X | None` for type annotations
src\prefect\server\events\triggers.py:1155:20: UP006 [*] Use `tuple` instead of `Tuple` for type annotation
src\prefect\server\events\triggers.py:1158:17: UP045 [*] Use `X | None` for type annotations
src\prefect\server\events\triggers.py:1182:18: C408 Unnecessary `dict()` call (rewrite as a literal)
```

## 160 · 2026-10-28T08:34:40.018948+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"AutomationBucket\" tests/events | head -20",
  "description": "Find tests inspecting automation buckets"
}
```

## 161 · 2026-10-28T08:34:40.351956+00:00 · tool_result 

```
tests/events/server/conftest.py:42:    await automations_session.execute(sa.delete(db.AutomationBucket))
```

## 162 · 2026-10-28T08:35:18.804098+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"triggered_at\" src/prefect tests | head -20",
  "description": "Check triggered_at usage"
}
```

## 163 · 2026-10-28T08:35:20.589380+00:00 · tool_result 

```
src/prefect/server/database/orm_models.py:1341:    triggered_at: Mapped[Optional[DateTime]]
src/prefect/server/database/_migrations/versions/postgresql/2024_04_03_112409_aeea5ee6f070_automations_models.py:109:            "triggered_at",
src/prefect/server/database/_migrations/versions/postgresql/2024_04_09_132036_954db7517015_trigger_in_index.py:29:        "triggered_at",
src/prefect/server/database/_migrations/versions/postgresql/2024_04_09_132036_954db7517015_trigger_in_index.py:58:        "triggered_at",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_03_111618_07ed05dfd4ec_automations_models.py:112:            "triggered_at",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_09_131832_2b6c2b548f95_trigger_in_index.py:29:            "triggered_at",
src/prefect/server/database/_migrations/versions/sqlite/2024_04_09_131832_2b6c2b548f95_trigger_in_index.py:58:            "triggered_at",
src/prefect/server/events/triggers.py:1099:    triggered_at: Optional[prefect.types._datetime.DateTime] = None,
src/prefect/server/events/triggers.py:1116:            triggered_at=triggered_at,
src/prefect/server/events/triggers.py:1131:                triggered_at=triggered_at,
```

## 164 · 2026-10-28T08:35:42.770879+00:00 · assistant_message 

```
Let me strengthen the fix for equal-timestamp ordering variants (a response and an arming event arriving in either order at the same instant).
```

## 165 · 2026-10-28T08:35:46.697468+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "def _event_is_at_least_as_recent(\n    event: Optional[ReceivedEvent], previous: Optional[ReceivedEvent]\n) -> bool:\n    \"\"\"Whether ``event`` is at least as recent as the last event on a bucket.\n\n    Events that share an ``occurred`` timestamp are considered equally recent: a\n    distinct event that happened at the same instant does not supersede the event\n    that was already recorded for that instant.  This keeps ``last_event``\n    monotonically increasing so an out-of-order or duplicate event cannot make the\n    bucket forget about a newer event that has already been accounted for.\n    \"\"\"\n    if event is None:\n        return False\n    if previous is None or event.id == previous.id:\n        return True\n    return event.occurred > previous.occurred\n\n\ndef _can_restart_proactive_window(\n    trigger: EventTrigger,\n    triggering_event: ReceivedEvent,\n    previous_last_event: Optional[ReceivedEvent],\n) -> bool:\n    \"\"\"Whether a proactive window may be restarted at ``triggering_event``.\n\n    An ``after`` event that also matches ``expect`` restarts the window so the\n    trigger waits for the next expected event.  That is only safe when the event is\n    newer than everything the bucket has already seen.  In particular, when an\n    expected event (such as a flow run reaching a terminal state) was observed at\n    the same moment as, or after, this ``after`` event, restarting the window would\n    discard that observation and produce a false positive even though the resource\n    already responded.\n    \"\"\"\n    if previous_last_event is None:\n        return True\n    if previous_last_event.id == triggering_event.id:\n        return True\n    if not trigger.expects(previous_last_event.event):\n        # The previous event does not satisfy what this trigger is waiting for, so\n        # it does not represent a response that should keep the window from being\n        # restarted.\n        return True\n    return triggering_event.occurred > previous_last_event.occurred",
  "new_string": "def _should_record_last_event(\n    trigger: EventTrigger,\n    event: Optional[ReceivedEvent],\n    previous: Optional[ReceivedEvent],\n) -> bool:\n    \"\"\"Whether ``event`` should become the bucket's recorded ``last_event``.\n\n    The recorded event is kept as the most recent event the bucket has accounted\n    for: it never moves backwards in time, so an out-of-order event cannot make the\n    bucket forget about a newer event that has already been seen.\n\n    When distinct events share an ``occurred`` timestamp, an expected event that\n    does not start a window (a \"response\", such as a flow run reaching a terminal\n    state) takes precedence over an ``after`` event that simply re-arms the window.\n    This keeps the response recorded regardless of the order in which the events\n    happen to be received.\n    \"\"\"\n    if event is None:\n        return False\n    if previous is None or event.id == previous.id:\n        return True\n    if event.occurred > previous.occurred:\n        return True\n    if event.occurred < previous.occurred:\n        return False\n    # The events happened at the same instant: prefer a response over an event that\n    # merely re-arms the window.\n    return (\n        trigger.expects(event.event)\n        and not trigger.starts_after(event.event)\n        and trigger.starts_after(previous.event)\n    )\n\n\ndef _can_restart_proactive_window(\n    trigger: EventTrigger,\n    triggering_event: ReceivedEvent,\n    previous_last_event: Optional[ReceivedEvent],\n) -> bool:\n    \"\"\"Whether a proactive window may be restarted at ``triggering_event``.\n\n    An ``after`` event that also matches ``expect`` restarts the window so the\n    trigger waits for the next expected event.  That is only safe when the event is\n    newer than everything the bucket has already seen.  In particular, when an\n    expected event (such as a flow run reaching a terminal state) was observed at\n    the same moment as, or after, this ``after`` event, restarting the window would\n    discard that observation and produce a false positive even though the resource\n    already responded.\n    \"\"\"\n    if previous_last_event is None:\n        return True\n    if previous_last_event.id == triggering_event.id:\n        return True\n    if not trigger.expects(previous_last_event.event):\n        # The previous event does not satisfy what this trigger is waiting for, so\n        # it does not represent a response that should keep the window from being\n        # restarted.\n        return True\n    if triggering_event.occurred > previous_last_event.occurred:\n        return True\n    if (\n        triggering_event.occurred == previous_last_event.occurred\n        and trigger.starts_after(previous_last_event.event)\n    ):\n        # The previous event was another window-arming event at the same instant, so\n        # there is no response to preserve and the window can be restarted.  A\n        # response at this instant would have been preferred as `last_event` and\n        # would have made the checks above fail instead.\n        return True\n    return False"
}
```

## 166 · 2026-10-28T08:35:46.842092+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 167 · 2026-10-28T08:35:48.380295+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "old_string": "        last_event = (\n            triggering_event\n            if _event_is_at_least_as_recent(triggering_event, previous_last_event)\n            else None\n        )",
  "new_string": "        last_event = (\n            triggering_event\n            if _should_record_last_event(\n                trigger, triggering_event, previous_last_event\n            )\n            else None\n        )"
}
```

## 168 · 2026-10-28T08:35:48.483571+00:00 · tool_result 

```
The file $SANDBOX/prefect/src/prefect/server/events/triggers.py has been updated successfully.
```

## 169 · 2026-10-28T08:35:53.135706+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "old_string": "async def test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat(",
  "new_string": "async def test_zombie_flow_detection_ignores_completion_received_after_heartbeat(\n    act: mock.AsyncMock,\n    frozen_time: DateTime,\n    zombie_flow_detection_automation: Automation,\n):\n    \"\"\"A terminal state event is a response even when it is received after a\n    heartbeat that shares its timestamp, and it must satisfy the window.\"\"\"\n    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)\n    flow_run_id = uuid4()\n    resource = {\"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"}\n\n    first_heartbeat = Event(\n        occurred=frozen_time,\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n    second_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=30),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n    final_heartbeat = Event(\n        occurred=frozen_time + timedelta(seconds=60),\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.1))\n    completed = Event(\n        occurred=frozen_time + timedelta(seconds=60),\n        event=\"prefect.flow-run.Completed\",\n        resource=resource,\n        id=uuid4(),\n    ).receive(received=frozen_time + timedelta(seconds=60.2))\n\n    for event in (\n        first_heartbeat,\n        second_heartbeat,\n        final_heartbeat,\n        completed,\n    ):\n        await triggers.reactive_evaluation(event)\n\n    await triggers.proactive_evaluation(\n        zombie_flow_detection_automation.trigger,\n        frozen_time + timedelta(seconds=151),\n    )\n    act.assert_not_awaited()\n\n\nasync def test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat("
}
```

## 170 · 2026-10-28T08:35:53.258210+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_regressions.py has been updated successfully.
```

## 171 · 2026-10-28T08:35:54.626839+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_regressions.py tests/events/server/triggers/test_incident_completed_run.py -q 2>&1 | tail -8",
  "description": "Run new regression tests and incident",
  "timeout": 900000
}
```

## 172 · 2026-10-28T08:37:47.175112+00:00 · tool_result 

```
................                                                         [100%]
16 passed in 99.58s (0:01:39)
```

## 173 · 2026-10-28T08:37:52.775196+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/prefect/tests/events/server/triggers/test_regressions.py",
  "old_string": "@pytest.fixture\nasync def proactive_extended_expect_and_after_with_threshold_1(",
  "new_string": "async def test_zombie_flow_detection_fires_when_heartbeats_share_timestamp(\n    act: mock.AsyncMock,\n    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],\n    frozen_time: DateTime,\n    zombie_flow_detection_automation: Automation,\n):\n    \"\"\"Repeated heartbeats at the same instant still re-arm the window, so a run\n    that stops responding afterwards is detected.\"\"\"\n    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)\n    flow_run_id = uuid4()\n    resource = {\"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"}\n    first_heartbeat = Event(\n        occurred=frozen_time,\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n    second_heartbeat = Event(\n        occurred=frozen_time,\n        event=\"prefect.flow-run.heartbeat\",\n        resource=resource,\n        id=uuid4(),\n    ).receive()\n\n    await triggers.reactive_evaluation(first_heartbeat)\n    await triggers.reactive_evaluation(second_heartbeat)\n    act.assert_not_awaited()\n\n    await triggers.proactive_evaluation(\n        zombie_flow_detection_automation.trigger,\n        frozen_time + timedelta(seconds=91),\n    )\n\n    assert_acted_with(\n        Firing(\n            trigger=zombie_flow_detection_automation.trigger,\n            trigger_states={TriggerState.Triggered},\n            triggered=frozen_time,  # type: ignore\n            triggering_labels={\n                \"prefect.resource.id\": f\"prefect.flow-run.{flow_run_id}\"\n            },\n            triggering_event=second_heartbeat,\n        )\n    )\n\n\n@pytest.fixture\nasync def proactive_extended_expect_and_after_with_threshold_1("
}
```

## 174 · 2026-10-28T08:37:52.911195+00:00 · tool_result 

```
The file $SANDBOX/prefect/tests/events/server/triggers/test_regressions.py has been updated successfully.
```

## 175 · 2026-10-28T08:37:55.222880+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_regressions.py -q 2>&1 | tail -6",
  "description": "Run regression tests with new timestamp test",
  "timeout": 900000
}
```

## 176 · 2026-10-28T08:39:44.789789+00:00 · tool_result 

```
................                                                         [100%]
16 passed in 96.17s (0:01:36)
```

## 177 · 2026-10-28T08:39:49.285625+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls tests/events/server/ && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server --collect-only -q 2>/dev/null | tail -3",
  "description": "List events server tests and count",
  "timeout": 300000
}
```

## 178 · 2026-10-28T08:40:06.883419+00:00 · tool_result 

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

742 tests collected in 2.36s
```

## 179 · 2026-10-28T08:40:09.160702+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py -q 2>&1 | tail -6",
  "description": "Run automation API/event tests",
  "timeout": 1200000
}
```

## 180 · 2026-10-28T08:44:03.720711+00:00 · tool_result 

```
16:41:50.325 | WARNING | asyncio - Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.421 seconds
------------------------------ Captured log call ------------------------------
WARNING  asyncio:base_events.py:1904 Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.421 seconds
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed, 61 passed in 218.58s (0:03:38)
```

## 181 · 2026-10-28T08:44:05.406462+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q 2>&1 | tail -40",
  "description": "Run failing automation API test alone",
  "timeout": 600000
}
```

## 182 · 2026-10-28T08:44:42.784924+00:00 · tool_result 

```
Generating test database connection URL from 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
Running hosted API server on port 60231
---------------------------- Captured stderr setup ----------------------------
16:44:33.609 | INFO    | uvicorn.error - Started server process [10616]
16:44:33.619 | INFO    | uvicorn.error - Waiting for application startup.
16:44:34.259 | DEBUG   | prefect.server - Worker channel configuration: cleanup_queue_storage=prefect.server.worker_communication.cleanup_queue.memory cleanup_lease_seconds=30.0 cleanup_max_delivery_attempts=3 cleanup_completed_idempotency_retention_seconds=None
16:44:34.279 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: ensure_cancelling_timeout_checks
16:44:34.280 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_cancelled_flow_runs
16:44:34.280 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_subflow_runs
16:44:34.291 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_vacuum_tasks
16:44:34.292 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_event_vacuum_tasks
16:44:34.293 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_orphan_vacuum_tasks
16:44:34.293 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_worker_health
16:44:34.293 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_late_runs
16:44:34.294 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_expired_pauses
16:44:34.294 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_deployments
16:44:34.294 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_recent_deployments
16:44:34.295 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: send_telemetry_heartbeat
16:44:34.295 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: evaluate_proactive_triggers_periodic
16:44:34.295 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: monitor_expired_leases
16:44:34.296 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: reconcile_cleanup_delivery
16:44:34.297 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: monitor_expired_leases
16:44:34.299 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
16:44:34.301 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
16:44:34.307 | INFO    | uvicorn.error - Application startup complete.
16:44:34.309 | INFO    | uvicorn.error - Uvicorn running on http://127.0.0.1:60231 (Press CTRL+C to quit)
16:44:34.752 | INFO    | uvicorn.access - 127.0.0.1:60245 - "GET /api/health HTTP/1.1" 200
---------------------------- Captured stderr call -----------------------------
Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.422 seconds
16:44:37.746 | WARNING | asyncio - Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.422 seconds
------------------------------ Captured log call ------------------------------
WARNING  asyncio:base_events.py:1904 Executing <Task pending name='starlette.middleware.base.BaseHTTPMiddleware.__call__.<locals>.call_next.<locals>.coro' coro=<TaskHandle._run_coro() running at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_core\_tasks.py:275> wait_for=<Future pending cb=[Task.task_wakeup()] created at D:\python3.11\Lib\asyncio\base_events.py:427> cb=[TaskGroup._spawn.<locals>.task_done() at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:836] created at $SANDBOX\.runtime\venv\Lib\site-packages\anyio\_backends\_asyncio.py:899> took 0.422 seconds
-------------------------- Captured stderr teardown ---------------------------
16:44:40.202 | INFO    | uvicorn.error - Shutting down
16:44:40.295 | INFO    | uvicorn.error - Waiting for application shutdown.
16:44:40.296 | INFO    | uvicorn.error - Application shutdown complete.
16:44:40.297 | INFO    | uvicorn.error - Finished server process [10616]
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 25.95s
```

## 183 · 2026-10-28T08:44:44.424474+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q 2>&1 | grep -B5 -A25 \"FAILED\\|AssertionError\\|assert \" | head -100",
  "description": "Show assertion details of failing test",
  "timeout": 600000
}
```

## 184 · 2026-10-28T08:45:22.568041+00:00 · tool_result 

```
    ) -> None:
        response = await client.post(
            f"{automations_url}/filter",
            json={"limit": 2, "offset": 1, "sort": AutomationSort.UPDATED_DESC},
        )
        assert response.status_code == 200, response.content
    
        automations = parse_obj_as(List[Automation], response.json())
    
        # updated is technically Optional, so assert it here to satisfy the type system
        def by_updated(automation: Automation) -> DateTime:
            assert automation.updated
            return automation.updated
    
        expected = sorted(some_workspace_automations, key=by_updated, reverse=True)
        expected = expected[1:3]
    
>       assert automations == expected
E       AssertionError: assert [Automation(n...811b8c5479'))] == [Automation(n...dec9ae4688'))]
E         
E         At index 0 diff: Automation(name='automation 3', description='', enabled=True, tags=[], trigger=EventTrigger(type='event', id=UUID('6790222d-47c2-4104-97ae-054253e45d08'), match=ResourceSpecification(root={'prefect.resource.id': 'some-resource'}), match_related=ResourceSpecification(root={}), after=set(), expect={'things.happened'}, for_each=set(), posture=Posture.Reactive, threshold=1, within=datetime.timedelta(seconds=10)), actions=[DoNothing(type='do-nothing')], actions_on_trigger=[], actions_on_resolve=[], id=UUID('cc3b4b9b-98ad-49b4-a856-8ddec9ae4688')) != Automati...
E         
E         ...Full output truncated (2 lines hidden), use '-vv' to show

tests\events\server\test_automations_api.py:687: AssertionError
---------------------------- Captured stdout setup ----------------------------
Generating test database connection URL from 'sqlite+aiosqlite:///$SANDBOX/.runtime/trial.db'
Running hosted API server on port 60348
---------------------------- Captured stderr setup ----------------------------
16:45:13.407 | INFO    | uvicorn.error - Started server process [16232]
16:45:13.418 | INFO    | uvicorn.error - Waiting for application startup.
16:45:14.092 | DEBUG   | prefect.server - Worker channel configuration: cleanup_queue_storage=prefect.server.worker_communication.cleanup_queue.memory cleanup_lease_seconds=30.0 cleanup_max_delivery_attempts=3 cleanup_completed_idempotency_retention_seconds=None
16:45:14.112 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: ensure_cancelling_timeout_checks
16:45:14.113 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_cancelled_flow_runs
16:45:14.113 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_subflow_runs
16:45:14.126 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_vacuum_tasks
16:45:14.126 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_event_vacuum_tasks
16:45:14.127 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_orphan_vacuum_tasks
16:45:14.127 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_worker_health
16:45:14.127 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_late_runs
16:45:14.128 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: monitor_expired_pauses
16:45:14.128 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_deployments
16:45:14.128 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: schedule_recent_deployments
16:45:14.128 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: send_telemetry_heartbeat
16:45:14.129 | DEBUG   | prefect.server.services.perpetual_services - Skipping disabled perpetual service: evaluate_proactive_triggers_periodic
16:45:14.129 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: monitor_expired_leases
16:45:14.130 | DEBUG   | prefect.server.services.perpetual_services - Registered perpetual service: reconcile_cleanup_delivery
16:45:14.130 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: monitor_expired_leases
16:45:14.131 | INFO    | prefect.server.services.perpetual_services - Scheduling perpetual service: reconcile_cleanup_delivery
16:45:14.133 | INFO    | prefect.server.services.perpetual_services - Perpetual services: 2 enabled, 13 disabled, 15 total
--
16:45:19.891 | INFO    | uvicorn.error - Shutting down
16:45:19.984 | INFO    | uvicorn.error - Waiting for application shutdown.
16:45:19.986 | INFO    | uvicorn.error - Application shutdown complete.
16:45:19.987 | INFO    | uvicorn.error - Finished server process [16232]
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 26.34s
```

## 185 · 2026-10-28T08:45:25.068583+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/tests/events/server/test_automations_api.py",
  "limit": 80,
  "offset": 620
}
```

## 186 · 2026-10-28T08:45:25.175223+00:00 · tool_result 

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
```

## 187 · 2026-10-28T08:45:27.619336+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"some_workspace_automations\" -A 40 tests/events/server/test_automations_api.py | head -60",
  "description": "Inspect automations API test fixture"
}
```

## 188 · 2026-10-28T08:45:27.966361+00:00 · tool_result 

```
652:    some_workspace_automations: List[Automation],
653-    client: AsyncClient,
654-    automations_url: str,
655-) -> None:
656-    response = await client.post(f"{automations_url}/filter")
657-    assert response.status_code == 200, response.content
658-
659-    automations = parse_obj_as(List[Automation], response.json())
660-
661:    expected = sorted(some_workspace_automations, key=lambda a: a.name)
662-
663-    assert automations == expected
664-
665-
666-async def test_read_automations_page(
667:    some_workspace_automations: List[Automation],
668-    client: AsyncClient,
669-    automations_url: str,
670-) -> None:
671-    response = await client.post(
672-        f"{automations_url}/filter",
673-        json={"limit": 2, "offset": 1, "sort": AutomationSort.UPDATED_DESC},
674-    )
675-    assert response.status_code == 200, response.content
676-
677-    automations = parse_obj_as(List[Automation], response.json())
678-
679-    # updated is technically Optional, so assert it here to satisfy the type system
680-    def by_updated(automation: Automation) -> DateTime:
681-        assert automation.updated
682-        return automation.updated
683-
684:    expected = sorted(some_workspace_automations, key=by_updated, reverse=True)
685-    expected = expected[1:3]
686-
687-    assert automations == expected
688-
689-
690-async def test_read_automations_filter_by_name_match(
691:    some_workspace_automations: List[Automation],
692-    client: AsyncClient,
693-    automations_url: str,
694-) -> None:
695-    automation_filter = dict(
696-        automations=filters.AutomationFilter(
697-            name=filters.AutomationFilterName(any_=["automation 1", "automation 2"])
698-        ).model_dump(mode="json")
699-    )
700-
701-    response = await client.post(f"{automations_url}/filter", json=automation_filter)
702-
703-    assert response.status_code == 200, response.content
704-
705-    automations = parse_obj_as(List[Automation], response.json())
706-
707:    expected = sorted(some_workspace_automations, key=lambda a: a.name)
708-    expected = [a for a in expected if a.name in ["automation 1", "automation 2"]]
709-
710-    assert automations == expected
711-    assert len(automations) == 2
```

## 189 · 2026-10-28T08:45:29.539359+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def some_workspace_automations\" -A 45 tests/events/server/conftest.py tests/events/server/test_automations_api.py | head -80",
  "description": "Find some_workspace_automations fixture definition"
}
```

## 190 · 2026-10-28T08:45:29.875023+00:00 · tool_result 

```
tests/events/server/conftest.py:368:async def some_workspace_automations(
tests/events/server/conftest.py-369-    db: PrefectDBInterface, automations_session: AsyncSession
tests/events/server/conftest.py-370-) -> Sequence[Automation]:
tests/events/server/conftest.py-371-    uninteresting_kwargs: Dict[str, Any] = dict(
tests/events/server/conftest.py-372-        trigger=EventTrigger(
tests/events/server/conftest.py-373-            expect=("things.happened",),
tests/events/server/conftest.py-374-            match=ResourceSpecification.model_validate(
tests/events/server/conftest.py-375-                {"prefect.resource.id": "some-resource"}
tests/events/server/conftest.py-376-            ),
tests/events/server/conftest.py-377-            match_related=ResourceSpecification.model_validate({}),
tests/events/server/conftest.py-378-            posture=Posture.Reactive,
tests/events/server/conftest.py-379-            threshold=1,
tests/events/server/conftest.py-380-            within=timedelta(seconds=10),
tests/events/server/conftest.py-381-        ),
tests/events/server/conftest.py-382-        actions=[actions.DoNothing()],
tests/events/server/conftest.py-383-    )
tests/events/server/conftest.py-384-
tests/events/server/conftest.py-385-    automations = [
tests/events/server/conftest.py-386-        db.Automation(
tests/events/server/conftest.py-387-            id=uuid4(),
tests/events/server/conftest.py-388-            name="automation 1",
tests/events/server/conftest.py-389-            **uninteresting_kwargs,
tests/events/server/conftest.py-390-        ),
tests/events/server/conftest.py-391-        db.Automation(
tests/events/server/conftest.py-392-            id=uuid4(),
tests/events/server/conftest.py-393-            name="automation 2",
tests/events/server/conftest.py-394-            **uninteresting_kwargs,
tests/events/server/conftest.py-395-        ),
tests/events/server/conftest.py-396-        db.Automation(
tests/events/server/conftest.py-397-            id=uuid4(),
tests/events/server/conftest.py-398-            name="automation 3",
tests/events/server/conftest.py-399-            **uninteresting_kwargs,
tests/events/server/conftest.py-400-        ),
tests/events/server/conftest.py-401-        db.Automation(
tests/events/server/conftest.py-402-            id=uuid4(),
tests/events/server/conftest.py-403-            name="automation 4",
tests/events/server/conftest.py-404-            **uninteresting_kwargs,
tests/events/server/conftest.py-405-        ),
tests/events/server/conftest.py-406-    ]
tests/events/server/conftest.py-407-
tests/events/server/conftest.py-408-    automations_session.add_all(automations)
tests/events/server/conftest.py-409-    await automations_session.commit()
tests/events/server/conftest.py-410-    return parse_obj_as(List[Automation], automations)
tests/events/server/conftest.py-411-
tests/events/server/conftest.py-412-
tests/events/server/conftest.py-413-@pytest.fixture
```

## 191 · 2026-10-28T08:45:33.362752+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && head -40 tests/events/server/test_automations_api.py | grep -n \"pytestmark\\|clear_db\"; grep -n \"updated\" src/prefect/server/database/orm_models.py | grep -n \"Automation\" ; grep -n \"class Automation(Base)\" -A 40 src/prefect/server/database/orm_models.py | grep -n \"updated\" -B2 -A4",
  "description": "Check test marks and updated column"
}
```

## 192 · 2026-10-28T08:45:33.888525+00:00 · tool_result 

```
7:1299:            AutomationSort.UPDATED_DESC: cls.updated.desc(),
27-1297-        sort_mapping: dict[AutomationSort, sa.ColumnExpressionArgument[Any]] = {
28-1298-            AutomationSort.CREATED_DESC: cls.created.desc(),
29:1299-            AutomationSort.UPDATED_DESC: cls.updated.desc(),
30-1300-            AutomationSort.NAME_ASC: cls.name.asc(),
31-1301-            AutomationSort.NAME_DESC: cls.name.desc(),
32-1302-        }
33-1303-        return sort_mapping[value]
```

## 193 · 2026-10-28T08:45:35.782975+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '1,60p' tests/events/server/test_automations_api.py; grep -n \"class Automation\" -A 120 src/prefect/server/database/orm_models.py | grep -n \"updated\\|created\" | head",
  "description": "Read test header and Automation ORM timestamps"
}
```

## 194 · 2026-10-28T08:45:36.219587+00:00 · tool_result 

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
28:1298-            AutomationSort.CREATED_DESC: cls.created.desc(),
29:1299-            AutomationSort.UPDATED_DESC: cls.updated.desc(),
```

## 195 · 2026-10-28T08:45:39.190366+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && awk '/^class Automation\\(Base\\):/{f=1} f&&/created|updated/{print NR\": \"$0} f&&/^class /&&!/^class Automation\\(Base\\)/{exit}' src/prefect/server/database/orm_models.py | head; grep -n \"class Automation(Base)\" src/prefect/server/database/orm_models.py",
  "description": "Locate Automation timestamps"
}
```

## 196 · 2026-10-28T08:45:39.710681+00:00 · tool_result 

```
1298:             AutomationSort.CREATED_DESC: cls.created.desc(),
1299:             AutomationSort.UPDATED_DESC: cls.updated.desc(),
1271:class Automation(Base):
```

## 197 · 2026-10-28T08:45:41.447773+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "limit": 36,
  "offset": 1240
}
```

## 198 · 2026-10-28T08:45:41.571287+00:00 · tool_result 

```
1240	    )
1241	
1242	    __table_args__: Any = (sa.UniqueConstraint("name"),)
1243	
1244	
1245	class Variable(Base):
1246	    name: Mapped[str]
1247	    value: Mapped[Optional[Any]] = mapped_column(JSON)
1248	    tags: Mapped[list[str]] = mapped_column(JSON, server_default="[]", default=list)
1249	
1250	    __table_args__: Any = (sa.UniqueConstraint("name"),)
1251	
1252	
1253	class FlowRunInput(Base):
1254	    flow_run_id: Mapped[uuid.UUID] = mapped_column(
1255	        sa.ForeignKey("flow_run.id", ondelete="cascade")
1256	    )
1257	
1258	    key: Mapped[str]
1259	    value: Mapped[str] = mapped_column(sa.Text())
1260	    sender: Mapped[Optional[str]]
1261	
1262	    __table_args__: Any = (sa.UniqueConstraint("flow_run_id", "key"),)
1263	
1264	
1265	class CsrfToken(Base):
1266	    token: Mapped[str]
1267	    client: Mapped[str] = mapped_column(unique=True)
1268	    expiration: Mapped[DateTime]
1269	
1270	
1271	class Automation(Base):
1272	    name: Mapped[str]
1273	    description: Mapped[str] = mapped_column(default="")
1274	
1275	    enabled: Mapped[bool] = mapped_column(server_default="1", default=True)
```

## 199 · 2026-10-28T08:45:43.060592+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "limit": 25,
  "offset": 1275
}
```

## 200 · 2026-10-28T08:45:43.144784+00:00 · tool_result 

```
1275	    enabled: Mapped[bool] = mapped_column(server_default="1", default=True)
1276	    tags: Mapped[list[str]] = mapped_column(JSON, server_default="[]", default=list)
1277	
1278	    trigger: Mapped[ServerTriggerTypes] = mapped_column(Pydantic(ServerTriggerTypes))
1279	
1280	    actions: Mapped[ServerActionTypes] = mapped_column(
1281	        Pydantic(list[ServerActionTypes])
1282	    )
1283	    actions_on_trigger: Mapped[list[ServerActionTypes]] = mapped_column(
1284	        Pydantic(list[ServerActionTypes]), server_default="[]", default=list
1285	    )
1286	    actions_on_resolve: Mapped[list[ServerActionTypes]] = mapped_column(
1287	        Pydantic(list[ServerActionTypes]), server_default="[]", default=list
1288	    )
1289	
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
```

## 201 · 2026-10-28T08:45:46.297259+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"class Base(\" -B5 -A40 src/prefect/server/database/orm_models.py | head -80; grep -rn \"created: Mapped\\|updated: Mapped\" src/prefect/server/database/orm_models.py | head",
  "description": "Inspect ORM Base timestamp defaults"
}
```

## 202 · 2026-10-28T08:45:46.713759+00:00 · tool_result 

```
52-# for 'plain JSON' columns, use the postgresql variant (which comes with an
53-# extra operator) and fall back to the generic JSON variant for SQLite
54-sa_JSON: postgresql.JSON = postgresql.JSON().with_variant(sa.JSON(), "sqlite")
55-
56-
57:class Base(DeclarativeBase):
58-    """
59-    Base SQLAlchemy model that automatically infers the table name
60-    and provides ID, created, and updated columns
61-    """
62-
63-    registry: ClassVar[RegistryType] = registry(
64-        metadata=sa.schema.MetaData(
65-            # define naming conventions for our Base class to use
66-            # sqlalchemy will use the following templated strings
67-            # to generate the names of indices, constraints, and keys
68-            #
69-            # we offset the table name with two underscores (__) to
70-            # help differentiate, for example, between "flow_run.state_type"
71-            # and "flow_run_state.type".
72-            #
73-            # more information on this templating and available
74-            # customization can be found here
75-            # https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.MetaData
76-            #
77-            # this also allows us to avoid having to specify names explicitly
78-            # when using sa.ForeignKey.use_alter = True
79-            # https://docs.sqlalchemy.org/en/14/core/constraints.html
80-            naming_convention={
81-                "ix": "ix_%(table_name)s__%(column_0_N_name)s",
82-                "uq": "uq_%(table_name)s__%(column_0_N_name)s",
83-                "ck": "ck_%(table_name)s__%(constraint_name)s",
84-                "fk": "fk_%(table_name)s__%(column_0_N_name)s__%(referred_table_name)s",
85-                "pk": "pk_%(table_name)s",
86-            }
87-        ),
88-        type_annotation_map={
89-            uuid.UUID: UUID,
90-            DateTime: Timestamp,
91-        },
92-    )
93-
94-    # required in order to access columns with server defaults
95-    # or SQL expression defaults, subsequent to a flush, without
96-    # triggering an expired load
97-    #
122:    created: Mapped[DateTime] = mapped_column(
129:    updated: Mapped[DateTime] = mapped_column(
```

## 203 · 2026-10-28T08:45:48.071124+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/database/orm_models.py",
  "limit": 25,
  "offset": 118
}
```

## 204 · 2026-10-28T08:45:48.178855+00:00 · tool_result 

```
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
```

## 205 · 2026-10-28T08:45:50.958819+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && for i in 1 2; do \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q 2>&1 | tail -2; done",
  "description": "Rerun flaky test twice",
  "timeout": 900000
}
```

## 206 · 2026-10-28T08:47:07.520679+00:00 · tool_result 

```
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 26.37s
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 25.81s
```

## 207 · 2026-10-28T08:47:12.527787+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"from prefect.server.events import\\|triggers\\.\" src/prefect/server/events/models/automations.py | head; grep -rn \"triggers\" tests/events/server/conftest.py | head",
  "description": "Check if automation model imports triggers"
}
```

## 208 · 2026-10-28T08:47:12.906855+00:00 · tool_result 

```
14:from prefect.server.events import clients, filters
380:    from prefect.server.events import actions
30:    monkeypatch.setattr("prefect.server.events.triggers.act", mock_act)
48:    from prefect.server.events import triggers
50:    await triggers.reset()
52:    await triggers.reset()
```

## 209 · 2026-10-28T08:47:16.140488+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q -vv 2>&1 | grep -o \"Automation(name='automation [0-9]'[^)]*id=UUID('[^']*')\" | head; echo ---; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q -vv 2>&1 | grep -E \"At index|assert \\[\" | head -5",
  "description": "Inspect automation ordering values",
  "timeout": 600000
}
```

## 210 · 2026-10-28T08:48:35.511535+00:00 · tool_result 

```
Automation(name='automation 3', description='', enabled=True, tags=[], trigger=EventTrigger(type='event', id=UUID('10ca6362-b9e4-46df-bd76-43f4110ea2ca')
---
E       AssertionError: assert [Automation(n...a5af65a888'))] == [Automation(n...39bdc9f1a4'))]
E         At index 1 diff: Automation(name='automation 2', description='', enabled=True, tags=[], trigger=EventTrigger(type='event', id=UUID('8bb5378e-7521-4d05-8392-7f9e4a25c5d4'), match=ResourceSpecification(root={'prefect.resource.id': 'some-resource'}), match_related=ResourceSpecification(root={}), after=set(), expect={'things.happened'}, for_each=set(), posture=Posture.Reactive, threshold=1, within=datetime.timedelta(seconds=10)), actions=[DoNothing(type='do-nothing')], actions_on_trigger=[], actions_on_resolve=[], id=UUID('e987663b-0370-4b4e-8e3a-fea5af65a888')) != Automati...
```

## 211 · 2026-10-28T08:48:40.527550+00:00 · assistant_message 

```
Let me verify the unrelated API failure is pre-existing by temporarily restoring the original logic.
```

## 212 · 2026-10-28T08:48:43.706530+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cp src/prefect/server/events/triggers.py /tmp/triggers_modified_backup.py && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" - <<'EOF'\nfrom pathlib import Path\np = Path(\"src/prefect/server/events/triggers.py\")\nsrc = p.read_text(encoding=\"utf-8\")\n\n# 1. remove helper block\nstart = src.index(\"def _should_record_last_event(\")\nend = src.index(\"async def evaluate(\")\nsrc = src[:start] + src[end:]\n\n# 2. restore increment call\nsrc = src.replace(\n'''    # Remember the most recent event this bucket had already accounted for before\n    # this evaluation.  It may be newer than the triggering event when events arrive\n    # out of order (or at the same instant); in that case it must not be replaced by\n    # the older event, and a proactive window must not be restarted at the older one.\n    previous_last_event = bucket.last_event\n\n    if count and (trigger.immediate or bucket.start <= now < bucket.end):\n        # we are still within the automation time period, so spend the count in the\n        # current bucket\n        last_event = (\n            triggering_event\n            if _should_record_last_event(\n                trigger, triggering_event, previous_last_event\n            )\n            else None\n        )\n        bucket = await increment_bucket(session, bucket, count, last_event)\n        count = 0''',\n'''    if count and (trigger.immediate or bucket.start <= now < bucket.end):\n        # we are still within the automation time period, so spend the count in the\n        # current bucket\n        bucket = await increment_bucket(session, bucket, count, triggering_event)\n        count = 0''',\n)\n\n# 3. restore reset condition\nsrc = src.replace(\n'''            and _can_restart_proactive_window(\n                trigger, triggering_event, previous_last_event\n            )\n''', \"\")\n\n# 4. restore ensure_bucket additional_updates\nsrc = src.replace(\n'''    automation = trigger.automation\n    await session.execute(\n        db.queries.insert(db.AutomationBucket)\n        .values(\n            automation_id=automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event=last_event,\n            start=start,\n            end=end,\n            count=initial_count,\n            last_operation=\"ensure_bucket[insert]\",\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationBucket.automation_id,\n                db.AutomationBucket.trigger_id,\n                db.AutomationBucket.bucketing_key,\n            ],\n            set_=dict(\n                # no-op, but this counts as an update so the query returns a row.\n                # Importantly, an existing bucket is left untouched: its\n                # `last_event` is only advanced by `increment_bucket` (which keeps\n                # the most recent event), so an out-of-order event cannot replace a\n                # newer one that has already been recorded.\n                count=db.AutomationBucket.count,\n            ),\n        )\n    )''',\n'''    automation = trigger.automation\n    additional_updates: dict[str, ReceivedEvent] = (\n        {\"last_event\": last_event} if last_event else {}\n    )\n    await session.execute(\n        db.queries.insert(db.AutomationBucket)\n        .values(\n            automation_id=automation.id,\n            trigger_id=trigger.id,\n            bucketing_key=bucketing_key,\n            last_event=last_event,\n            start=start,\n            end=end,\n            count=initial_count,\n            last_operation=\"ensure_bucket[insert]\",\n        )\n        .on_conflict_do_update(\n            index_elements=[\n                db.AutomationBucket.automation_id,\n                db.AutomationBucket.trigger_id,\n                db.AutomationBucket.bucketing_key,\n            ],\n            set_=dict(\n                # no-op, but this counts as an update so the query returns a row\n                count=db.AutomationBucket.count,\n                **additional_updates,\n            ),\n        )\n    )''',\n)\np.write_text(src, encoding=\"utf-8\")\nprint(\"reverted\", \"_should_record_last_event\" in src, \"_can_restart\" in src)\nEOF",
  "description": "Temporarily revert source changes for baseline check"
}
```

## 213 · 2026-10-28T08:48:45.149835+00:00 · tool_result 

```
reverted False False
```

## 214 · 2026-10-28T08:48:46.730583+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/test_automations_api.py::test_read_automations_page -q 2>&1 | tail -3",
  "description": "Run API test with original trigger logic",
  "timeout": 600000
}
```

## 215 · 2026-10-28T08:49:29.600588+00:00 · tool_result 

```
=========================== short test summary info ===========================
FAILED tests/events/server/test_automations_api.py::test_read_automations_page
1 failed in 26.64s
```

## 216 · 2026-10-28T08:49:31.371477+00:00 · assistant_message 

```
The API test failure reproduces with the original logic, so it is unrelated. Restoring the repaired file.
```

## 217 · 2026-10-28T08:49:31.791924+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && cp /tmp/triggers_modified_backup.py src/prefect/server/events/triggers.py && grep -n \"_should_record_last_event\\|_can_restart_proactive_window\" src/prefect/server/events/triggers.py | head",
  "description": "Restore repaired triggers.py"
}
```

## 218 · 2026-10-28T08:49:32.518231+00:00 · tool_result 

```
88:def _should_record_last_event(
122:def _can_restart_proactive_window(
240:            if _should_record_last_event(
325:            and _can_restart_proactive_window(
```

## 219 · 2026-10-28T08:49:37.536611+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "limit": 80,
  "offset": 82
}
```

## 220 · 2026-10-28T08:49:37.650990+00:00 · tool_result 

```
82	]
83	
84	
85	AUTOMATION_BUCKET_BATCH_SIZE = 500
86	
87	
88	def _should_record_last_event(
89	    trigger: EventTrigger,
90	    event: Optional[ReceivedEvent],
91	    previous: Optional[ReceivedEvent],
92	) -> bool:
93	    """Whether ``event`` should become the bucket's recorded ``last_event``.
94	
95	    The recorded event is kept as the most recent event the bucket has accounted
96	    for: it never moves backwards in time, so an out-of-order event cannot make the
97	    bucket forget about a newer event that has already been seen.
98	
99	    When distinct events share an ``occurred`` timestamp, an expected event that
100	    does not start a window (a "response", such as a flow run reaching a terminal
101	    state) takes precedence over an ``after`` event that simply re-arms the window.
102	    This keeps the response recorded regardless of the order in which the events
103	    happen to be received.
104	    """
105	    if event is None:
106	        return False
107	    if previous is None or event.id == previous.id:
108	        return True
109	    if event.occurred > previous.occurred:
110	        return True
111	    if event.occurred < previous.occurred:
112	        return False
113	    # The events happened at the same instant: prefer a response over an event that
114	    # merely re-arms the window.
115	    return (
116	        trigger.expects(event.event)
117	        and not trigger.starts_after(event.event)
118	        and trigger.starts_after(previous.event)
119	    )
120	
121	
122	def _can_restart_proactive_window(
123	    trigger: EventTrigger,
124	    triggering_event: ReceivedEvent,
125	    previous_last_event: Optional[ReceivedEvent],
126	) -> bool:
127	    """Whether a proactive window may be restarted at ``triggering_event``.
128	
129	    An ``after`` event that also matches ``expect`` restarts the window so the
130	    trigger waits for the next expected event.  That is only safe when the event is
131	    newer than everything the bucket has already seen.  In particular, when an
132	    expected event (such as a flow run reaching a terminal state) was observed at
133	    the same moment as, or after, this ``after`` event, restarting the window would
134	    discard that observation and produce a false positive even though the resource
135	    already responded.
136	    """
137	    if previous_last_event is None:
138	        return True
139	    if previous_last_event.id == triggering_event.id:
140	        return True
141	    if not trigger.expects(previous_last_event.event):
142	        # The previous event does not satisfy what this trigger is waiting for, so
143	        # it does not represent a response that should keep the window from being
144	        # restarted.
145	        return True
146	    if triggering_event.occurred > previous_last_event.occurred:
147	        return True
148	    if (
149	        triggering_event.occurred == previous_last_event.occurred
150	        and trigger.starts_after(previous_last_event.event)
151	    ):
152	        # The previous event was another window-arming event at the same instant, so
153	        # there is no response to preserve and the window can be restarted.  A
154	        # response at this instant would have been preferred as `last_event` and
155	        # would have made the checks above fail instead.
156	        return True
157	    return False
158	
159	
160	async def evaluate(
161	    session: AsyncSession,
```

## 221 · 2026-10-28T08:49:42.193771+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | grep -E \"incident_id|passed|failed\"",
  "description": "Run incident test as specified",
  "timeout": 300000
}
```

## 222 · 2026-10-28T08:50:21.284154+00:00 · tool_result 

```
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
1 passed in 26.09s
```

## 223 · 2026-10-28T08:50:23.328553+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers -q --ignore=tests/events/server/triggers/test_incident_completed_run.py 2>&1 | tail -6",
  "description": "Run full triggers suite after final changes",
  "timeout": 1800000
}
```

## 224 · 2026-10-28T08:56:18.282660+00:00 · tool_result 

```
.................................................x...x...x.............. [ 58%]
...................................................                      [100%]
120 passed, 3 xfailed in 343.37s (0:05:43)
```

## 225 · 2026-10-28T08:56:24.958907+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "limit": 80,
  "offset": 205
}
```

## 226 · 2026-10-28T08:56:25.066581+00:00 · tool_result 

```
205	    #
206	    # Automations are also evaluated proactively without an event to see if they have
207	    # met their proactive threshold (where not enough events have happened in the time
208	    # period)
209	
210	    # If there was a triggering event, then we need to "spend" this count somewhere,
211	    # either in the currently open bucket or in the next time period's bucket
212	    count = 1 if triggering_event else 0
213	
214	    if now < bucket.start:
215	        # This is an older out-of-order message or a redundant event for a reactive
216	        # trigger that has has already fired, so it should not should not affect the
217	        # current bucket.  We can safely ignore this event/timestamp entirely.  Case #1
218	        # from the implementation notes above.
219	        logger.debug(
220	            "Automation %s (%r) trigger %s got a late event for keys (%r)",
221	            automation.id,
222	            automation.name,
223	            trigger.id,
224	            bucket.bucketing_key,
225	            extra=logging_context,
226	        )
227	        return bucket
228	
229	    # Remember the most recent event this bucket had already accounted for before
230	    # this evaluation.  It may be newer than the triggering event when events arrive
231	    # out of order (or at the same instant); in that case it must not be replaced by
232	    # the older event, and a proactive window must not be restarted at the older one.
233	    previous_last_event = bucket.last_event
234	
235	    if count and (trigger.immediate or bucket.start <= now < bucket.end):
236	        # we are still within the automation time period, so spend the count in the
237	        # current bucket
238	        last_event = (
239	            triggering_event
240	            if _should_record_last_event(
241	                trigger, triggering_event, previous_last_event
242	            )
243	            else None
244	        )
245	        bucket = await increment_bucket(session, bucket, count, last_event)
246	        count = 0
247	
248	    # Reactive automations will fire "eagerly", meaning they will fire as _soon_ as the
249	    # threshold is reached, then wait for the rest of their time period before
250	    # firing again.  This is done by creating a new bucket in the future after the
251	    # trigger has fired.
252	
253	    # Proactive automations must wait until the whole bucket has expired before they can
254	    # fire, because we can't know if we'll get one late event just in time to cause the
255	    # automation _not_ to fire.
256	
257	    ready_to_fire = trigger.posture == Posture.Reactive or bucket.end <= now
258	    meets_threshold = trigger.meets_threshold(bucket.count)
259	
260	    if ready_to_fire and meets_threshold:
261	        logger.debug(
262	            (
263	                "Automation %s (%r) trigger %s triggered for keys (%r) %s, "
264	                "having occurred %s times between %s and %s"
265	            ),
266	            automation.id,
267	            automation.name,
268	            trigger.id,
269	            bucket.bucketing_key,
270	            "reactively" if triggering_event else "proactively",
271	            bucket.count,
272	            bucket.start,
273	            bucket.end,
274	            extra=logging_context,
275	        )
276	
277	        firing = Firing(
278	            trigger=trigger,
279	            trigger_states={TriggerState.Triggered},
280	            triggered=prefect.types._datetime.now("UTC"),
281	            triggering_labels={
282	                label: value
283	                for label, value in zip(sorted(trigger.for_each), bucket.bucketing_key)
284	            },
```

## 227 · 2026-10-28T08:56:35.340124+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"EXPIRED_BUCKET_BUFFER\" -A 12 src/prefect/settings/models/server/events.py | head -30",
  "description": "Check expired bucket buffer default"
}
```

## 228 · 2026-10-28T08:56:35.700658+00:00 · tool_result 

```
(Bash completed with no output)
```

## 229 · 2026-10-28T08:56:37.038090+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"EXPIRED_BUCKET_BUFFER\" src/prefect/settings | head",
  "description": "Locate expired bucket buffer setting"
}
```

## 230 · 2026-10-28T08:56:37.333764+00:00 · tool_result 

```
(Bash completed with no output)
```

## 231 · 2026-10-28T08:56:38.769064+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"EXPIRED_BUCKET_BUFFER\" src/prefect | head",
  "description": "Search expired bucket buffer setting everywhere"
}
```

## 232 · 2026-10-28T08:56:39.662293+00:00 · tool_result 

```
src/prefect/server/events/triggers.py:67:from prefect.settings import PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER
src/prefect/server/events/triggers.py:786:            as_of - PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER.value(),
```

## 233 · 2026-10-28T08:56:41.345774+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"PREFECT_EVENTS_EXPIRED_BUCKET_BUFFER\" src/prefect/settings/*.py src/prefect/settings/models/*.py src/prefect/settings/models/**/*.py 2>/dev/null | head; grep -rn \"expired_bucket_buffer\" -A 10 src/prefect/settings/models | head -20",
  "description": "Find bucket buffer setting definition"
}
```

## 234 · 2026-10-28T08:56:41.789571+00:00 · tool_result 

```
src/prefect/settings/models/server/events.py:72:    expired_bucket_buffer: timedelta = Field(
src/prefect/settings/models/server/events.py-73-        default=timedelta(seconds=60),
src/prefect/settings/models/server/events.py-74-        description="The amount of time to retain expired automation buckets",
src/prefect/settings/models/server/events.py-75-        validation_alias=AliasChoices(
src/prefect/settings/models/server/events.py:76:            AliasPath("expired_bucket_buffer"),
src/prefect/settings/models/server/events.py:77:            "prefect_server_events_expired_bucket_buffer",
src/prefect/settings/models/server/events.py:78:            "prefect_events_expired_bucket_buffer",
src/prefect/settings/models/server/events.py-79-        ),
src/prefect/settings/models/server/events.py-80-    )
src/prefect/settings/models/server/events.py-81-
src/prefect/settings/models/server/events.py-82-    proactive_granularity: timedelta = Field(
src/prefect/settings/models/server/events.py-83-        default=timedelta(seconds=5),
src/prefect/settings/models/server/events.py-84-        description="How frequently proactive automations are evaluated",
src/prefect/settings/models/server/events.py-85-        validation_alias=AliasChoices(
src/prefect/settings/models/server/events.py-86-            AliasPath("proactive_granularity"),
src/prefect/settings/models/server/events.py-87-            "prefect_server_events_proactive_granularity",
src/prefect/settings/models/server/events.py-88-            "prefect_events_proactive_granularity",
```

## 235 · 2026-10-28T08:56:47.886845+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -rn \"def frozen_time\" -A 15 tests/conftest.py tests/events/server/conftest.py 2>/dev/null | head -40; grep -rn \"def frozen_time\" -A 15 tests/fixtures/*.py 2>/dev/null | head -30",
  "description": "Find frozen_time fixture"
}
```

## 236 · 2026-10-28T08:56:48.314148+00:00 · tool_result 

```
tests/fixtures/time.py:14:def frozen_time(
tests/fixtures/time.py-15-    monkeypatch: pytest.MonkeyPatch,
tests/fixtures/time.py-16-) -> prefect.types._datetime.DateTime | datetime.datetime:
tests/fixtures/time.py-17-    frozen = prefect.types._datetime.now("UTC")
tests/fixtures/time.py-18-
tests/fixtures/time.py:19:    def frozen_time(tz: ZoneInfo | str | None = None):
tests/fixtures/time.py-20-        if tz is None:
tests/fixtures/time.py-21-            return frozen
tests/fixtures/time.py-22-        else:
tests/fixtures/time.py-23-            return frozen.astimezone(tz=ZoneInfo(getattr(tz, "name", tz)))
tests/fixtures/time.py-24-
tests/fixtures/time.py-25-    monkeypatch.setattr(prefect.types._datetime, "now", frozen_time)
tests/fixtures/time.py-26-    return frozen
tests/fixtures/time.py-27-
tests/fixtures/time.py-28-
tests/fixtures/time.py-29-@pytest.fixture
tests/fixtures/time.py-30-def advance_time(
tests/fixtures/time.py-31-    monkeypatch: pytest.MonkeyPatch,
tests/fixtures/time.py-32-) -> Callable[[timedelta], prefect.types._datetime.DateTime]:
tests/fixtures/time.py-33-    clock = prefect.types._datetime.now("UTC")
tests/fixtures/time.py-34-
```

## 237 · 2026-10-28T08:57:10.056445+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && wc -l docs/contribute/dev-contribute.mdx REVIEW.md && sed -n '1,80p' REVIEW.md",
  "description": "Check contribution docs size and review rules"
}
```

## 238 · 2026-10-28T08:57:10.399827+00:00 · tool_result 

```
  258 docs/contribute/dev-contribute.mdx
   68 REVIEW.md
  326 total
# Code review guidance

Repo-specific guidance for human and automated reviewers of Prefect. Implementation standards
and component contracts belong in the applicable `AGENTS.md` files; do not duplicate them here.

## Review axes

Review every diff along two independent axes:

- **Standards** — does the change follow the applicable repository instructions?
- **Spec** — does the change faithfully implement the originating issue or specification?

Evaluate the axes independently even when the review surface reports findings individually.
Inline comments should lead directly with the problem rather than an axis label. Do not let
success on one axis hide problems on the other.

## Standards review

Read every `AGENTS.md` and `REVIEW.md` whose scope contains a changed file, plus the relevant
contribution guides under `docs/contribute/`. Follow references to paired implementations,
owning components, architectural boundaries, and other contracts material to the diff. Verify
those contracts against their implementations rather than reasoning from names or mocks alone.

Cite the instruction file and rule for every hard Standards finding. Repository instructions
override the following Fowler code-smell baseline, which is always a judgement call:

- Mysterious Name
- Duplicated Code
- Feature Envy
- Data Clumps
- Primitive Obsession
- Repeated Switches
- Shotgun Surgery
- Divergent Change
- Speculative Generality
- Message Chains
- Middle Man
- Refused Bequest

Skip formatting, lint, and other failures that automated tooling reliably identifies unless
they expose a broader behavioral problem.

## Spec review

Find the authoritative specification in this order:

1. A linked GitHub issue and its maintainer decisions, including issue references in commits
2. A specification explicitly linked from the issue or pull request
3. A relevant document under `docs/`, `plans/`, or another specification directory
4. The pull request description for a small, self-contained change allowed without an issue

For each Spec finding, cite the requirement it relies on. Report requirements that are missing
or partial, behavior that was not requested, and implementations that appear to satisfy a
requirement but do so incorrectly.

If no authoritative specification is available, do not invent one. If the contribution guide
requires prior issue discussion for the change and none is linked, report that as a Standards
finding. Otherwise, skip the Spec axis; when a summary surface exists, note that it was not
evaluated rather than creating an inline finding.

## Reporting discipline

- Review the diff against its merge base; do not turn adjacent pre-existing problems into
  findings.
- Quote the relevant changed code and cite the governing standard or requirement.
- Distinguish observed failures from inferred risks and state what evidence would confirm an
  inference.
- Avoid speculative cleanup and preference-only findings.
```

## 239 · 2026-10-28T08:57:12.290585+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '1,140p' docs/contribute/dev-contribute.mdx",
  "description": "Read contribution guide part 1"
}
```

## 240 · 2026-10-28T08:57:12.535197+00:00 · tool_result 

````
---
title: Develop on Prefect
description: Learn how to set up Prefect for development, experimentation and code contributions.
---

import fork from '/snippets/fork.mdx'


## Make a code contribution

We welcome all forms of contributions to Prefect, whether it's small typo fixes in [our documentation](/contribute/docs-contribute), bug fixes or feature enhancements!
If this is your first time making an open source contribution we will be glad to work with you and help you get up to speed.

<Note>
For small changes such as typo fixes you can simply open a pull request - we typically review small changes like these within the day.
For larger changes including all bug fixes, we ask that you first open [an issue](https://github.com/PrefectHQ/prefect/issues) or comment on the issue that you are planning to work on.
</Note>

## Design principles

Prefect contributions should serve the project and its users, not just the immediate implementation request.
We evaluate code, documentation, and issue proposals against these principles:

- **User-centered**: Changes should solve a real workflow orchestration need for Prefect users and explain the user-facing value.
- **Correct and reliable**: Prefer behavior that is explicit, deterministic, observable, and safe under failure.
- **Minimal and focused**: Keep changes scoped to one clear problem and avoid broad rewrites or new abstractions without a strong reason.
- **Consistent with Prefect's architecture**: Follow existing public APIs, orchestration boundaries, async patterns, settings behavior, and integration conventions.
- **Well-tested and documented**: Cover meaningful behavior with tests and update documentation when users need to understand new or changed behavior.

Pull requests that make Prefect harder to reason about, broaden maintenance burden without clear user value, or bypass established architecture may be rejected even if the implementation works locally.

## Issue first, code second

For anything larger than a small documentation or typo fix, open an issue or join the existing issue before opening a pull request.
Issues give maintainers and contributors a place to confirm the problem, discuss scope, identify architectural constraints, and decide whether the change belongs in Prefect.
An open issue is not automatically an invitation to open a pull request.
Some issues require maintainer ownership because they touch architecture, product direction, compatibility, security, or release planning.

Use the issue discussion to narrow the work before writing code.
For complex issues, propose a detailed approach and wait for a maintainer to confirm that the approach and contributor ownership are appropriate before submitting a pull request.
A pull request is not the best place to discover that a feature does not fit the project, duplicates existing behavior, or requires a different design.

## Using AI tools responsibly

You may use AI tools to explore the codebase, draft documentation, sketch tests, refactor code, or review your own work.
You are responsible for every issue, pull request, and comment you submit.
Treat AI output as a starting point, not as evidence that a change is correct.

Before opening an issue or pull request:

- Reproduce the behavior yourself and include a minimal reproducible example for bugs when possible.
- Keep each pull request focused on one bug fix, feature, or documentation improvement.
- Explain the user-facing problem, why your approach fits Prefect's existing architecture, and any tradeoffs.
- Run the relevant checks locally and include behavior-focused tests for code changes.
- Update documentation when your change affects user-facing behavior.

Maintainers may close issues without further triage when they appear low-effort, unverified, likely AI-generated and lacking concrete detail, too broad, difficult to follow, or primarily shift investigation and validation onto maintainers.
Maintainers may ask for pull request revisions for the same reasons, or close pull requests that appear low-effort, likely AI-generated, and substantially far from the expected implementation.
This applies whether or not AI tools were used.

## What maintainers look for

Reviews focus on whether the change should become part of Prefect and whether it can be maintained over time.
The strongest pull requests:

- Solve a clear user problem with enough context for reviewers to understand the value.
- Fit Prefect's existing architecture, public APIs, and compatibility expectations.
- Prefer clear, idiomatic code over cleverness, excessive abstraction, or broad rewrites.
- Include tests that protect behavior instead of mirroring private implementation details.
- Update documentation for user-facing behavior changes, or explain why documentation is not needed.
- Explain meaningful tradeoffs, migration concerns, or follow-up work in the pull request description.

Even working code may need revision if it is difficult to reason about, overengineered, inconsistent with established patterns, or likely to create maintenance burden out of proportion to the user value.

## Fork the repository
<fork />

## Install Prefect for development

Once you have cloned your fork of the repo you can install [an editable version](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) of Prefect for quick iteration.


We recommend using `uv` for dependency management when developing. Refer to the [`uv` docs for installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

To set up a virtual environment and install a development version of `prefect`:
<CodeGroup>
```bash uv
uv sync
```
```bash pip and venv
python -m venv .venv
source .venv/bin/activate

# Installs the package with development dependencies
pip install --group dev -e .
```
</CodeGroup>

To verify `prefect` was installed correctly:

<CodeGroup>
```bash uv
uv run prefect --version
```
```bash pip and venv
prefect --version
```
</CodeGroup>

To ensure your changes comply with our linting policies, set up `pre-commit` and `pre-push` hooks to run with every commit:

```bash
uv run pre-commit install
```

To manually run the `pre-commit` hooks against all files:

```bash
uv run pre-commit run --all-files
```

To manually run the pre-push hooks:

```bash
uv run pre-commit run --hook-stage pre-push --all-files
```

<Tip>
  If you're using `uv`, you can run commands with the project's dependencies by prefixing the command with `uv run`.
</Tip>

## Write tests

Prefect relies on unit testing to ensure proposed changes don't negatively impact any functionality.
For all code changes, including bug fixes, we ask that you write at least one corresponding test.
One rule of thumb - especially for bug fixes - is that you should write a test that fails prior to your changes and passes with your changes.
This ensures the test will fail and prevent the bug from resurfacing if other changes are made in the future.
Prefer tests that assert user-visible behavior or public contracts instead of private implementation details.
All tests can be found in the `tests/` directory of the repository.
````

## 241 · 2026-10-28T08:57:14.103482+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '140,258p' docs/contribute/dev-contribute.mdx",
  "description": "Read contribution guide part 2"
}
```

## 242 · 2026-10-28T08:57:14.362388+00:00 · tool_result 

````
You can run the test suite with `pytest`:

```bash
# run all tests
pytest tests

# run a specific file
pytest tests/test_flows.py

# run all tests that match a pattern
pytest tests/test_tasks.py -k cache_policy
```

## Submit your pull request

Before submitting a pull request:

- Confirm the related issue is linked, unless the change is a small documentation or typo fix.
- Keep the scope to one feature, bug fix, or documentation improvement.
- Describe the problem, the approach, and any tradeoffs or alternatives considered.
- Run the relevant tests and checks locally.
- Add or update documentation for user-facing behavior changes.

The code shows what changed.
The pull request description should explain why the change is useful and why this approach is appropriate for Prefect.

## Working with a development UI

If you plan to use the UI during development, you will need to build a development version of the UI first.

Using the Prefect UI in development requires installation of [npm](https://github.com/npm/cli).
We recommend using [nvm](https://github.com/nvm-sh/nvm) to manage Node.js versions.
Once installed, run `nvm use` from the root of the Prefect repository to initialize the proper version of `npm` and `node`.

Start a development UI that reloads on code changes:

```bash
prefect dev ui
```

This command is most useful if you are working directly on the UI codebase.

Alternatively, you can build a static UI that will be served when running `prefect server start`:

```bash
prefect dev build-ui --include-v2
```

## Working with a development server

The Prefect CLI provides several helpful commands to aid development of server-side changes.

You can start all services with hot-reloading on code changes (note that this requires installation of UI dependencies):

```bash
prefect dev start
```

Start a Prefect API that reloads on code changes:

```bash
prefect dev api
```

## Add database migrations

If your code changes necessitate modifications to a database table, first update the SQLAlchemy model in `src/prefect/server/database/orm_models.py`.

For example, to add a new column to the `flow_run` table, add a new column to the `FlowRun` model:

```python
# src/prefect/server/database/orm_models.py

class FlowRun(Run):
    """SQLAlchemy model of a flow run."""
    ...
    new_column: Mapped[Union[str, None]] = mapped_column(sa.String, nullable=True) # <-- add this line
```

Next, generate new migration files.
Generate a new migration file for each database type.

Migrations are generated for whichever database type `PREFECT_SERVER_DATABASE_CONNECTION_URL` is set to.
See [how to set the database connection URL](/v3/api-ref/settings-ref#connection_url) for each database type.

To generate a new migration file, run:

```bash
prefect server database revision --autogenerate -m "<migration name>"
```

Make the migration name brief but descriptive.
For example:

*   `add_flow_run_new_column`
*   `add_flow_run_new_column_idx`
*   `rename_flow_run_old_column_to_new_column`

The `--autogenerate` flag automatically generates a migration file based on the changes to the models.

<Warning>
**Always inspect the output of `--autogenerate`**

`--autogenerate` generates a migration file based on the changes to the models.
However, it is not perfect. Check the file to ensure it only includes the desired changes.
</Warning>

The new migration is in the `src/prefect/server/database/migrations/versions/` directory. Each database type has its
own subdirectory. For example, the SQLite migrations are stored in `src/prefect/server/database/migrations/versions/sqlite/`.

After inspecting the migration file, apply the migration to the database by running:

```bash
prefect server database upgrade -y
```

After successfully creating migrations for all database types, update `MIGRATION-NOTES.md` to
document the changes.
````

## 243 · 2026-10-28T08:57:29.744723+00:00 · assistant_message 

```
Let me run the final verification commands and check the workspace for unintended changes.
```

## 244 · 2026-10-28T08:57:30.303828+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | grep -E \"received_sequence|incident_id|passed|failed\"",
  "description": "Final incident replay verification",
  "timeout": 300000
}
```

## 245 · 2026-10-28T08:57:30.740516+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX\" && find prefect/src prefect/tests -newermt \"2026-10-28 16:00\" -type f -name \"*.py\" 2>/dev/null | head -20; echo \"---\"; ls -la SOLUTION_SUMMARY.md 2>/dev/null || echo \"no summary yet\"",
  "description": "List recently modified Python files"
}
```

## 246 · 2026-10-28T08:58:06.146913+00:00 · tool_result 

```
{"received_sequence": 1, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:00Z"}
{"received_sequence": 2, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:00:30Z"}
{"received_sequence": 3, "event": "prefect.flow-run.Completed", "occurred": "2026-10-20T12:01:00Z"}
{"received_sequence": 4, "event": "prefect.flow-run.heartbeat", "occurred": "2026-10-20T12:01:00Z"}
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
1 passed in 24.05s
```

## 247 · 2026-10-28T08:58:07.527046+00:00 · tool_result 

```
prefect/src/prefect/server/events/triggers.py
prefect/src/prefect/_build_info.py
prefect/src/prefect/_internal/analytics/_config.py
prefect/tests/events/server/triggers/test_incident_completed_run.py
prefect/tests/events/server/triggers/test_regressions.py
---
no summary yet
```

## 248 · 2026-10-28T08:58:10.482987+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && ls -la --time-style=full-iso src/prefect/_build_info.py src/prefect/_internal/analytics/_config.py tests/events/server/triggers/test_incident_completed_run.py src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py; echo ---; cat src/prefect/_build_info.py; echo ---; cat src/prefect/_internal/analytics/_config.py | head -20",
  "description": "Inspect unexpected modified files"
}
```

## 249 · 2026-10-28T08:58:10.995320+00:00 · tool_result 

```
-rw-r--r-- 1 luwen 197121   159 2026-10-28 16:05:45.740656100 +0800 src/prefect/_build_info.py
-rw-r--r-- 1 luwen 197121    92 2026-10-28 16:05:45.741654800 +0800 src/prefect/_internal/analytics/_config.py
-rw-r--r-- 1 luwen 197121 55283 2026-10-28 16:49:32.410618200 +0800 src/prefect/server/events/triggers.py
-rw-r--r-- 1 luwen 197121  2489 2026-10-28 16:05:37.110865500 +0800 tests/events/server/triggers/test_incident_completed_run.py
-rw-r--r-- 1 luwen 197121 40133 2026-10-28 16:37:52.902157200 +0800 tests/events/server/triggers/test_regressions.py
---
# Generated by versioningit
__version__ = "3.6.24+nogit"
__build_date__ = "2026-10-28T08:05:45.739656+00:00"
__git_commit__ = "unknown"
__dirty__ = False
---
# Generated at build time - DO NOT EDIT
AMPLITUDE_API_KEY = "YOUR_AMPLITUDE_API_KEY_HERE"
```

## 250 · 2026-10-28T08:58:25.534091+00:00 · assistant_message 

```
The fix is verified. Now let me write the required `SOLUTION_SUMMARY.md`.
```

## 251 · 2026-10-28T08:58:34.547491+00:00 · tool_call Write

````
{
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "content": "# Solution summary: completed flow runs receive unresponsive-run actions\n\n## Diagnosis\n\nReproduction before the repair:\n\n```\npython -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s\n...\n{\"incident_id\": \"completed-run-001\", \"observed_actions\": 1, \"expected_actions\": 0}\nAssertionError: Completed run received 1 unresponsive-run action(s); expected zero\n```\n\nRoot cause is in the proactive-trigger bucket evaluation in\n`prefect/src/prefect/server/events/triggers.py`.\n\nFor a proactive trigger whose `after` event also matches `expect` (the flow-run\nheartbeat / unresponsive-run configuration), `evaluate()` has a special case: once a\nbucket has reached its threshold (`not meets_threshold`, i.e. enough expected events\nwere seen), a further arming event removes the bucket and starts a fresh window at\nthat event's `occurred` time with `count=0` (the code around the \"Special case of a\nproactive trigger for which the same event satisfies both `after` and `expect`\"\ncomment).\n\nIn the incident the recorded events are:\n\n* heartbeat at 12:00:00\n* heartbeat at 12:00:30\n* `prefect.flow-run.Completed` at 12:01:00 (received first)\n* heartbeat at 12:01:00 (received second, same `occurred` timestamp)\n\nThe completion event satisfies the 90 s window opened by the 12:00:30 heartbeat\n(count becomes 1, the threshold). Then the final heartbeat, which carries the *same*\n`occurred` timestamp but is received after the completion, hits the special case and\nrestarts the window at 12:01:00 with `count=0`. The restart discards the completion\nobservation, so proactive evaluation at 12:02:31 sees an apparently silent resource\nand fires the unresponsive-run action.\n\nTwo existing behaviours combined to cause this:\n\n1. `ensure_bucket()` unconditionally wrote the incoming event into the existing\n   bucket's `last_event`, so the completion event that was already recorded at that\n   instant was overwritten before evaluation.\n2. The restart special case did not check whether the arming event was actually\n   newer than events the bucket had already accounted for, so it could move/restart\n   the window at or before an already-seen expected event.\n\n## Repair\n\nChanges in `prefect/src/prefect/server/events/triggers.py`:\n\n* `ensure_bucket()` no longer updates `last_event` when the bucket already exists\n  (it now matches its documented contract, \"Will not modify the existing bucket\").\n  `last_event` is advanced only by `increment_bucket()`.\n* `evaluate()` captures the bucket's `last_event` before mutating it and only records\n  the triggering event as the new `last_event` when it is at least as recent. A\n  distinct event with the same `occurred` timestamp does not replace one already\n  recorded, and an expected event that does not arm the window (a \"response\", e.g. a\n  terminal state event) takes precedence over an arming event at the same instant so\n  the response cannot be lost depending on arrival order.\n* The proactive-window restart is now guarded by\n  `_can_restart_proactive_window()`: a window may only be restarted when the arming\n  event is strictly newer than the last event the bucket accounted for. Repeated\n  arming events at the same instant still restart the window (so duplicate\n  heartbeats do not mask a real outage), and a different, same-event retry is still\n  allowed.\n\nThe repair is entirely in the existing bucket state (`automation_bucket.last_event`,\nalready persisted as JSON for both SQLite and PostgreSQL):\n\n* no schema change, no migration and no public API change;\n* restart/upgrade safe: the state lives in the database and is re-read by proactive\n  evaluation after a restart;\n* storage remains bounded: one bucket row per (automation, trigger, bucketing key),\n  cleaned up by the existing `remove_bucket` / `sweep_closed_buckets` paths;\n* no monitoring thresholds, actions, or concurrency primitives were changed.\n\nA genuinely unresponsive run still fires: its last heartbeat is newer than any event\nalready seen, so the window is still restarted and expires with a count below the\nthreshold. The `Firing` still gets `triggering_labels` from the bucketing key and\n`triggering_event` from the recorded last event.\n\n## Tests added\n\nIn `prefect/tests/events/server/triggers/test_regressions.py`:\n\n* `test_zombie_flow_detection_ignores_heartbeat_that_predates_terminal_event` - the\n  incident shape (completion received before a same-timestamp heartbeat) produces\n  no action.\n* `test_zombie_flow_detection_ignores_completion_received_after_heartbeat` - the\n  same-instant events in the opposite receive order still produce no action.\n* `test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat` - an\n  out-of-order heartbeat older than a completion cannot move the window backwards.\n* `test_zombie_flow_detection_fires_when_heartbeats_share_timestamp` - a run that\n  stops responding after repeated same-timestamp heartbeats still fires, with the\n  correct resource label and triggering event.\n\n## Commands actually executed and results\n\nRun from `$SANDBOX/prefect`\nwith the isolated interpreter\n`$SANDBOX/.runtime/venv/Scripts/python.exe`.\n\nBefore the repair:\n\n* `python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`\n  -> 1 failed, `observed_actions: 1`.\n\nAfter the repair:\n\n* `python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s`\n  -> 1 passed, `{\"incident_id\": \"completed-run-001\", \"observed_actions\": 0,\n  \"expected_actions\": 0}`.\n* `python -m pytest tests/events/server/triggers/test_regressions.py -q`\n  -> 16 passed.\n* `python -m pytest tests/events/server/triggers/test_basics.py -q`\n  -> 34 passed.\n* `python -m pytest tests/events/server/triggers -q --ignore=tests/events/server/triggers/test_incident_completed_run.py`\n  -> 120 passed, 3 xfailed.\n* `python -m pytest tests/events/server/test_automation_events.py tests/events/server/test_automations_api.py -q`\n  -> 61 passed, 1 failed (`test_read_automations_page`). This failure is unrelated to\n  the repair: it is an ordering assumption on `automation.updated` in the API test,\n  and it reproduces identically when the original trigger code is restored.\n* `python -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py`\n  -> both files already formatted. `ruff check` reports only pre-existing style\n  findings that follow the surrounding file conventions; the new code adds none.\n\n## Limits\n\n* The repair distinguishes ordering by the events' `occurred` timestamps and by the\n  persisted bucket state. Events in this incident carry no payload/state, so it does\n  not depend on flow-run-specific event names or payloads (also making it work for\n  custom state names). If a heartbeat were emitted *after* a terminal state event's\n  `occurred` timestamp (a narrow client/server race) it would be indistinguishable\n  from a legitimate heartbeat at the trigger layer; the event fixture and the real\n  recorded incident use same-instant timestamps, which are handled.\n* No database migration is required; existing buckets keep working, but a bucket\n  that was already persisted in the bad reset state before an upgrade is not\n  retroactively repaired (it is indistinguishable from a genuine unresponsive\n  state).\n"
}
````

## 252 · 2026-10-28T08:58:34.667583+00:00 · tool_result 

```
File created successfully at: $SANDBOX/SOLUTION_SUMMARY.md (file state is current in your context — no need to Read it back)
```

## 253 · 2026-10-28T08:58:40.137076+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && sed -n '916,1085p' tests/events/server/triggers/test_regressions.py",
  "description": "Review added regression tests"
}
```

## 254 · 2026-10-28T08:58:40.393077+00:00 · tool_result 

```
async def test_zombie_flow_detection_ignores_heartbeat_that_predates_terminal_event(
    act: mock.AsyncMock,
    frozen_time: DateTime,
    zombie_flow_detection_automation: Automation,
):
    """A terminal state event satisfies the window and must not be undone by a
    concurrent or stale heartbeat that arrives afterwards.

    This is the incident reproduction: the run completes at the same moment as its
    final heartbeat, but the heartbeat is received after the completion event.  The
    heartbeat must not restart the window, because the run already responded by
    completing.
    """
    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
    flow_run_id = uuid4()
    resource = {"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"}

    first_heartbeat = Event(
        occurred=frozen_time,
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=0.1))
    second_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=30),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=30.1))
    completed = Event(
        occurred=frozen_time + timedelta(seconds=60),
        event="prefect.flow-run.Completed",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.1))
    stale_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=60),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.2))

    for event in (
        first_heartbeat,
        second_heartbeat,
        completed,
        stale_heartbeat,
    ):
        await triggers.reactive_evaluation(event)

    await triggers.proactive_evaluation(
        zombie_flow_detection_automation.trigger,
        frozen_time + timedelta(seconds=151),
    )
    act.assert_not_awaited()


async def test_zombie_flow_detection_ignores_completion_received_after_heartbeat(
    act: mock.AsyncMock,
    frozen_time: DateTime,
    zombie_flow_detection_automation: Automation,
):
    """A terminal state event is a response even when it is received after a
    heartbeat that shares its timestamp, and it must satisfy the window."""
    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
    flow_run_id = uuid4()
    resource = {"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"}

    first_heartbeat = Event(
        occurred=frozen_time,
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive()
    second_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=30),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive()
    final_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=60),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.1))
    completed = Event(
        occurred=frozen_time + timedelta(seconds=60),
        event="prefect.flow-run.Completed",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.2))

    for event in (
        first_heartbeat,
        second_heartbeat,
        final_heartbeat,
        completed,
    ):
        await triggers.reactive_evaluation(event)

    await triggers.proactive_evaluation(
        zombie_flow_detection_automation.trigger,
        frozen_time + timedelta(seconds=151),
    )
    act.assert_not_awaited()


async def test_zombie_flow_detection_does_not_rewind_window_to_older_heartbeat(
    act: mock.AsyncMock,
    frozen_time: DateTime,
    zombie_flow_detection_automation: Automation,
):
    """An out-of-order heartbeat older than an already-seen terminal event must not
    move the window backwards and cause a false unresponsive-run action."""
    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
    flow_run_id = uuid4()
    resource = {"prefect.resource.id": f"prefect.flow-run.{flow_run_id}"}

    first_heartbeat = Event(
        occurred=frozen_time,
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive()
    second_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=30),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive()
    completed = Event(
        occurred=frozen_time + timedelta(seconds=60),
        event="prefect.flow-run.Completed",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.1))
    older_heartbeat = Event(
        occurred=frozen_time + timedelta(seconds=50),
        event="prefect.flow-run.heartbeat",
        resource=resource,
        id=uuid4(),
    ).receive(received=frozen_time + timedelta(seconds=60.2))

    for event in (
        first_heartbeat,
        second_heartbeat,
        completed,
        older_heartbeat,
    ):
        await triggers.reactive_evaluation(event)

    await triggers.proactive_evaluation(
        zombie_flow_detection_automation.trigger,
        frozen_time + timedelta(seconds=151),
    )
    act.assert_not_awaited()


async def test_zombie_flow_detection_fires_when_heartbeats_share_timestamp(
    act: mock.AsyncMock,
    assert_acted_with: Callable[[Union[Firing, List[Firing]]], None],
    frozen_time: DateTime,
    zombie_flow_detection_automation: Automation,
):
    """Repeated heartbeats at the same instant still re-arm the window, so a run
    that stops responding afterwards is detected."""
    assert isinstance(zombie_flow_detection_automation.trigger, EventTrigger)
    flow_run_id = uuid4()
```

## 255 · 2026-10-28T08:58:46.933709+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && which python 2>/dev/null; python -c \"import sys; print(sys.executable)\" 2>&1 | head -2",
  "description": "Check default python resolution"
}
```

## 256 · 2026-10-28T08:58:47.337096+00:00 · tool_result 

```
/e/工作/笔试/klavis/sandbox-claude-deepseek41-flash-max-diagnostic/.runtime/venv/Scripts/python
$SANDBOX\.runtime\venv\Scripts\python.exe
```

## 257 · 2026-10-28T08:58:47.375221+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py",
  "description": "Final format check"
}
```

## 258 · 2026-10-28T08:58:47.879280+00:00 · tool_result 

```
Exit code 1
unformatted: File would be reformatted
   --> src\prefect\server\events\triggers.py:240:42
    |
239 |             triggering_event
    -             if _should_record_last_event(
    -                 trigger, triggering_event, previous_last_event
    -             )
240 +             if _should_record_last_event(trigger, triggering_event, previous_last_event)
241 |             else None
    |

1 file would be reformatted, 1 file already formatted
```

## 259 · 2026-10-28T08:58:49.994711+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py",
  "description": "Format modified files"
}
```

## 260 · 2026-10-28T08:58:50.750686+00:00 · tool_result 

```
1 file reformatted, 1 file left unchanged
2 files already formatted
[This command modified 1 file you've previously read: src\prefect\server\events\triggers.py. Call Read before editing.]
```

## 261 · 2026-10-28T08:58:52.890472+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_regressions.py -q 2>&1 | tail -3",
  "description": "Final incident and regression test run",
  "timeout": 900000
}
```

## 262 · 2026-10-28T09:00:37.684637+00:00 · tool_result 

```
.................                                                        [100%]
17 passed in 93.08s (0:01:33)
```

## 263 · 2026-10-28T09:00:39.595385+00:00 · tool_call Read

```
{
  "file_path": "$SANDBOX/prefect/src/prefect/server/events/triggers.py",
  "limit": 25,
  "offset": 228
}
```

## 264 · 2026-10-28T09:00:39.706018+00:00 · tool_result 

```
228	
229	    # Remember the most recent event this bucket had already accounted for before
230	    # this evaluation.  It may be newer than the triggering event when events arrive
231	    # out of order (or at the same instant); in that case it must not be replaced by
232	    # the older event, and a proactive window must not be restarted at the older one.
233	    previous_last_event = bucket.last_event
234	
235	    if count and (trigger.immediate or bucket.start <= now < bucket.end):
236	        # we are still within the automation time period, so spend the count in the
237	        # current bucket
238	        last_event = (
239	            triggering_event
240	            if _should_record_last_event(trigger, triggering_event, previous_last_event)
241	            else None
242	        )
243	        bucket = await increment_bucket(session, bucket, count, last_event)
244	        count = 0
245	
246	    # Reactive automations will fire "eagerly", meaning they will fire as _soon_ as the
247	    # threshold is reached, then wait for the rest of their time period before
248	    # firing again.  This is done by creating a new bucket in the future after the
249	    # trigger has fired.
250	
251	    # Proactive automations must wait until the whole bucket has expired before they can
252	    # fire, because we can't know if we'll get one late event just in time to cause the
```

## 265 · 2026-10-28T09:00:42.260110+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && grep -n \"\\[tool.ruff\" -A 60 pyproject.toml | head -100",
  "description": "Inspect ruff configuration"
}
```

## 266 · 2026-10-28T09:00:42.595889+00:00 · tool_result 

```
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
383-    "aks",
384-    "ines",
385-    "dependant",
386-    "fsspec",
387-    "automations",
388-    "nmme",
389-    "afterall",
390-    "medias",
391-    "falso",
392-    "aapply",
393-]
394-
395-check-hidden = true
396-
397-
398-[tool.uv]
399-required-version = ">=0.6.15" # make sure upload_time is included to avoid churn (see https://github.com/dependabot/dependabot-core/issues/12127)
```

## 267 · 2026-10-28T09:00:46.790268+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff --version; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check --show-settings src/prefect/server/events/triggers.py 2>/dev/null | grep -E \"^linter.select|select = |extend_select\" | head",
  "description": "Check ruff version and effective rule selection"
}
```

## 268 · 2026-10-28T09:00:47.654005+00:00 · tool_result 

```
ruff 0.16.2
```

## 269 · 2026-10-28T09:00:49.011496+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check --show-settings src/prefect/server/events/triggers.py 2>&1 | head -40",
  "description": "Show ruff settings output"
}
```

## 270 · 2026-10-28T09:00:49.489183+00:00 · tool_result 

```
Resolved settings for: "$SANDBOX\prefect\src\prefect\server\events\triggers.py"
Settings path: "$SANDBOX\prefect\pyproject.toml"

# General Settings
cache_dir = "$SANDBOX/.runtime/ruff-cache"
fix = false
fix_only = false
output_format = full
output_prefer_rule_codes = false
show_fixes = false
unsafe_fixes = hint

# File Resolver Settings
file_resolver.exclude = [
	".bzr",
	".direnv",
	".eggs",
	".git",
	".git-rewrite",
	".hg",
	".ipynb_checkpoints",
	".mypy_cache",
	".nox",
	".pants.d",
	".pyenv",
	".pytest_cache",
	".pytype",
	".ruff_cache",
	".svn",
	".tox",
	".venv",
	".vscode",
	"__pypackages__",
	"_build",
	"buck-out",
	"dist",
	"node_modules",
	"site-packages",
	"venv",
]
```

## 271 · 2026-10-28T09:00:51.108562+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check --show-settings src/prefect/server/events/triggers.py 2>&1 | grep -n \"linter.rules.enabled\\|linter.select\\|extend\" -A 5 | head -30",
  "description": "Inspect enabled ruff rules"
}
```

## 272 · 2026-10-28T09:00:51.629754+00:00 · tool_result 

```
41:file_resolver.extend_exclude = []
42-file_resolver.force_exclude = false
43-file_resolver.include = [
44-	"*.py",
45-	"*.pyi",
46-	"*.ipynb",
--
52:file_resolver.extend_include = []
53-file_resolver.respect_gitignore = true
54-file_resolver.project_root = "$SANDBOX\prefect"
55-
56-# Linter Settings
57-linter.exclude = []
--
59:linter.rules.enabled = [
60-	sys-version-slice3 (YTT101),
61-	sys-version2 (YTT102),
62-	sys-version-cmp-str3 (YTT103),
63-	sys-version-info0-eq3 (YTT201),
64-	six-py3 (YTT202),
--
984:linter.flake8_bandit.extend_markup_names = []
985-linter.flake8_bandit.allowed_markup_calls = []
986:linter.flake8_bugbear.extend_immutable_calls = []
987-linter.flake8_builtins.allowed_modules = []
988-linter.flake8_builtins.ignorelist = []
989-linter.flake8_builtins.strict_checking = false
990-linter.flake8_comprehensions.allow_dict_calls_with_keyword_arguments = false
991-linter.flake8_copyright.notice_rgx = (?i)Copyright\s+((?:\(C\)|©)\s+)?\d{4}((-|,\s)\d{4})*
--
```

## 273 · 2026-10-28T09:00:54.835340+00:00 · tool_call Bash

```
{
  "command": "cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check --show-settings src/prefect/server/events/triggers.py 2>&1 | grep -c \"(UP045)\\|(UP006)\\|(C408)\\|(PIE808)\"; \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m ruff check --show-settings src/prefect/server/events/triggers.py 2>&1 | sed -n '59,75p'",
  "description": "Check whether modernize rules are enabled"
}
```

## 274 · 2026-10-28T09:00:55.583538+00:00 · tool_result 

```
8
linter.rules.enabled = [
	sys-version-slice3 (YTT101),
	sys-version2 (YTT102),
	sys-version-cmp-str3 (YTT103),
	sys-version-info0-eq3 (YTT201),
	six-py3 (YTT202),
	sys-version-info1-cmp-int (YTT203),
	sys-version-info-minor-cmp-int (YTT204),
	sys-version0 (YTT301),
	sys-version-cmp-str10 (YTT302),
	sys-version-slice1 (YTT303),
	cancel-scope-no-checkpoint (ASYNC100),
	trio-sync-call (ASYNC105),
	async-zero-sleep (ASYNC115),
	long-sleep-not-forever (ASYNC116),
	blocking-http-call-in-async-function (ASYNC210),
	create-subprocess-in-async-function (ASYNC220),
```

## 275 · 2026-10-28T09:00:59.626803+00:00 · tool_call Edit

```
{
  "replace_all": false,
  "file_path": "$SANDBOX/SOLUTION_SUMMARY.md",
  "old_string": "* `python -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py`\n  -> both files already formatted. `ruff check` reports only pre-existing style\n  findings that follow the surrounding file conventions; the new code adds none.",
  "new_string": "* `python -m ruff format --check src/prefect/server/events/triggers.py tests/events/server/triggers/test_regressions.py`\n  -> both files already formatted. (The locally installed `ruff check` 0.16.2 with\n  its default rule set already reports many pre-existing modernization/style\n  findings across these files; the new code follows the surrounding conventions\n  such as `Optional`/`Tuple` and adds no functional lint issues.)"
}
```

## 276 · 2026-10-28T09:00:59.737803+00:00 · tool_result 

```
The file $SANDBOX/SOLUTION_SUMMARY.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

## 277 · 2026-10-28T09:01:07.920442+00:00 · tool_call Bash

```
{
  "command": "rm -f /tmp/triggers_modified_backup.py; ls -la \"$SANDBOX/SOLUTION_SUMMARY.md\"; cd \"$SANDBOX/prefect\" && \"$SANDBOX/.runtime/venv/Scripts/python.exe\" -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s 2>&1 | grep -E \"observed_actions|passed|failed\"",
  "description": "Clean temp file and final incident verification",
  "timeout": 300000
}
```

## 278 · 2026-10-28T09:01:43.893444+00:00 · tool_result 

```
-rw-r--r-- 1 luwen 197121 7526 Oct 28 17:00 $SANDBOX/SOLUTION_SUMMARY.md
{"incident_id": "completed-run-001", "observed_actions": 0, "expected_actions": 0}
1 passed in 23.41s
```

## 279 · 2026-10-28T09:01:49.314029+00:00 · assistant_message 

```
## Diagnosis

The failure was in proactive-trigger bucket evaluation in `prefect/src/prefect/server/events/triggers.py`:

1. The `Completed` event at 12:01:00 satisfied the 90 s expectation window opened by the 12:00:30 heartbeat (bucket count reached the threshold).
2. The final heartbeat carried the **same `occurred` timestamp** but was received after the completion. The special case for `after` events that also match `expect` unconditionally restarted the window at that timestamp with `count=0`, discarding the completion observation.
3. At 12:02:31 the bucket looked like a resource that had gone silent, so the unresponsive-run action fired.

Two code-level contributors: `ensure_bucket()` overwrote an existing bucket's `last_event` with the incoming (possibly stale) event, and the restart special case never checked whether the arming event was newer than events the bucket had already accounted for.

## Repair

In `src/prefect/server/events/triggers.py`:

- `ensure_bucket()` no longer modifies an existing bucket (matching its documented contract); `last_event` is advanced only by `increment_bucket()`.
- `evaluate()` captures the bucket's prior `last_event` and only records the triggering event when it is at least as recent; same-instant "response" events (e.g. terminal states) take precedence over window-arming events so arrival order cannot lose them.
- The proactive-window restart now requires the arming event to be strictly newer than the last accounted-for expected event. Repeated arming events at the same instant still restart the window, so duplicate heartbeats don't mask a real outage.

No schema change, migration, threshold change, public-interface change, or new concurrency mechanism is involved; state lives in the existing persisted `automation_bucket.last_event`, so it survives restarts and remains bounded (one row per automation/trigger/key).

## Verification

- Added 4 behavior tests in `tests/events/server/triggers/test_regressions.py` (incident shape, reverse receive order at the same instant, out-of-order older heartbeat, and genuine unresponsive run with correct resource label/triggering event).
- `python -m pytest tests/events/server/triggers/test_incident_completed_run.py -q -s` → **1 passed**, `observed_actions: 0` (was 1 before the fix).
- `python -m pytest tests/events/server/triggers/test_regressions.py -q` → 16 passed.
- Full `tests/events/server/triggers` directory → 120 passed, 3 xfailed.
- One unrelated API test (`test_read_automations_page`) fails due to an `updated` timestamp ordering assumption; it reproduces identically with the original trigger code.

`SOLUTION_SUMMARY.md` at the working root contains the full diagnosis, commands, results and limits.
```
