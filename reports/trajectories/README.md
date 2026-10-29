# 两组模型各三次求解证据

**先看 [六次结果汇总](repeats/RESULTS.md)**，包含当前同一个 Docker 验证器下的六次成绩，以及每次轨迹和日志链接。也可下载 [JSON](repeats/results.json) 或 [CSV](repeats/results.csv)。

2026-10-29 按招聘方追补要求，保留此前每组一次结果，新增各两次独立求解。模型总次数为每组三次；补丁统一重验不是新模型运行。启动与隔离边界见 [运行协议](repeats/PROTOCOL.md) 和 [新增启动记录](repeats/launch-record.md)。这些是本地 agent 运行和直接 Docker 复核，不是正式 Harbor `/run` 或 `/cheat`。

验证六次公开证据的调用配对、日志计数、补丁重现和当前 Docker 记录：

```sh
python authoring/verify_trajectories.py --include-current
python -m unittest discover -s authoring -p 'test_trajectory_evidence.py' -v
```

检查记录见 [verification-public.json](repeats/verification-public.json)。中英文回复草稿见 [中文](repeats/recruiter-reply-zh.md)、[English](repeats/recruiter-reply-en.md)。

## 2026-10-28 的原始两次运行

以下部分保留最初每组一次的历史记录及其原有验收口径；当前同口径成绩请看上面的六次汇总。

| 模型/客户端 | 可见轨迹 | 配置 | 模型最终生产补丁 | 独立验收 |
|---|---|---|---|---|
| GPT-6.1-sol / xhigh，Codex app 子代理 | [阅读版](gpt61-sol-xhigh/trajectory.md) · [JSONL](gpt61-sol-xhigh/trajectory.jsonl) | [run-config](gpt61-sol-xhigh/run-config.json) | [7 个生产文件](gpt61-sol-xhigh/candidate-production.patch) | [结果](gpt61-sol-xhigh/evaluation/result.json) · [行为日志](gpt61-sol-xhigh/evaluation/behavior.log) · [retry 日志](gpt61-sol-xhigh/evaluation/retry.log) |
| Claude Code 2.1.312 + DeepSeek V4.1 Flash / max | [阅读版](claude-deepseek41-flash-max/trajectory.md) · [JSONL](claude-deepseek41-flash-max/trajectory.jsonl) | [run-config](claude-deepseek41-flash-max/run-config.json) · [客户端设置](claude-deepseek41-flash-max/client-settings.json) | [1 个生产文件](claude-deepseek41-flash-max/candidate-production.patch) | [结果](claude-deepseek41-flash-max/evaluation/result.json) · [行为日志](claude-deepseek41-flash-max/evaluation/behavior.log) · [retry 日志](claude-deepseek41-flash-max/evaluation/retry.log) |

## 如何阅读

每组从 `input-task.md` 开始，沿 `trajectory.md` 查看公开进度、实际工具调用及工具返回。GPT 保留 11 条公开消息、47 次编排调用和 47 次返回；DeepSeek 保留 11 条公开消息、134 次工具调用和 134 次返回。两种客户端记录粒度不同，不能据此直接比较效率。

`model-summary.md` 是模型当时的自述；作者侧结论以 `evaluation/` 为准。两组均通过公开 replay，但在当时的 35 个历史行为实例中分别是 26/9 和 18/17（通过/失败），四个 retry 回归均通过。日志中的 behavior 组还包含一个通过的公开 replay，因此原始汇总分别为 27 通过/9 失败、19 通过/17 失败。

## 版本和适用范围

- 基线均为 `71d1906204dfca1bd2dff36b57bcfc46dd7a2dd8`；两份 TASK 文件在替换沙盒路径后相同，原始比较记录见 [comparison-protocol.json](comparison-protocol.json)。
- 两组使用独立 Windows 源码副本与明确的访问范围指令，未提供作者参考解、其他模型答案或上游 Git 历史；当时没有 OS/容器级强隔离。
- 独立验收复制模型最终生产源码，使用基线 fixture 和作者冻结测试。补丁从该独立快照导出，逐个改动生产文件核对当时记录的 SHA-256；只规范化 CRLF 为 LF，排除生成的 build/analytics 元数据，不包含模型测试、运行时或整个工作目录。
- 本目录保留历史测试版本，包含后来被移除的中间 bucket 表示断言。因此原始失败数不能直接作为当前题目的分数，也不能把该结构断言失败单独认定为错误修复。具体失败名称及原始日志均保留。
- 当前 task 的题面增加了输出 artifact 契约，verifier 增加了三个兼容实例和跨进程/升级检查，故本目录不能冒充当前冻结题目的正式重跑。
- GPT 使用 Codex app 子代理，并非一条 `codex`/`harbor` CLI 命令；DeepSeek 的实际 CLI 参数及附加提示见 [launch-record.md](launch-record.md)。

## 公开处理

可见工具操作和结果来自真实记录。未公开原始 session/stream、内部推理/thinking、系统/开发者消息、内部 metadata、协作消息正文、凭据或本地通用技能正文。读取通用技能的调用保留，其返回明确标注为省略。

路径占位符：`$SANDBOX` 为该组工作目录，`$EVALUATION` 为独立验收副本，`$WORKSPACE` 为作者工作区，`$USER_HOME` 为用户目录。它们用于脱敏，不表示轨迹代码可直接复制执行。原始文件哈希、导出计数和变换统计见各组 `export-audit.json`。

## 复核旧版验收

使用基线自己的锁定依赖和 SQLite，在基线的独立副本中应用某组 `candidate-production.patch`，再覆盖 [historical-evaluation/overlay](historical-evaluation/overlay) 中的旧测试。不要覆盖或连接现有用户数据库。使用原有 fixture，模型自写测试不用于这次独立评分。

```sh
# 从干净基线源码根目录运行，路径替换为本仓库的绝对路径：
git apply /absolute/path/to/reports/trajectories/gpt61-sol-xhigh/candidate-production.patch
cp -R /absolute/path/to/reports/trajectories/historical-evaluation/overlay/. .
python -m pytest tests/events/server/triggers/test_incident_completed_run.py tests/events/server/triggers/test_early_expect_events.py tests/events/server/triggers/test_proactive_terminal_events.py -q --tb=short
python -m pytest tests/server/orchestration/test_core_policy.py -k 'test_in_process_retry_transition_does_not_release_concurrency_slots or test_scheduled_transition_without_retry_releases_concurrency_slots or test_rescheduled_retry_transition_releases_concurrency_slots or test_direct_reschedule_after_automatic_retry_releases_concurrency_slots' -q --tb=short
```

上述命令给出当时测试目标的可复核写法，并未在本次导出中重新运行模型或声称重新取得相同历史成绩。可先运行 `python authoring/verify_trajectories.py` 检查调用/返回配对、结果与日志一致、补丁适用性及改动文件哈希。
