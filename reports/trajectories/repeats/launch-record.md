# 新增四次的实际启动记录

会话 ID、UTC 启动时间、题面原始 SHA-256 和配置见 [launch-manifest.json](launch-manifest.json)。每次最终的结束时间、观察到的模型标识和导出审计另见该次 `run-config.json`。

## GPT-6.1-sol / xhigh

使用 Codex app 的 `collaboration.spawn_agent`，配置为 `fork_turns=none`、`model=gpt-6.1-sol`、`reasoning_effort=xhigh`。两个会话不继承作者历史，实际会话 context 已核对模型和 effort。启动消息如下，其中 `$SANDBOX` 分别是该次独立目录的脱敏占位符：

```text
Independently solve the software-engineering task by reading $SANDBOX/TASK.md. Your only task working root is $SANDBOX. Read its AGENTS.md and applicable repository instructions. Do not inspect parent/sibling directories, other sessions/attempts, reference materials, credentials or task-specific online solutions. Generic installed skill documentation is allowed. Implement autonomously and deliver source changes plus SOLUTION_SUMMARY.md under your root. Source .runtime/environment.ps1 before Python commands to use the isolated installed interpreter and database. Do not delegate or switch models. Treat TASK.md as the complete problem; do not ask for extra hints. When finished, stop after reporting actual verification and limitations; do not message any other thread.
```

这是 app 子代理启动记录，不是 `codex exec` 或 Harbor 命令。

## Claude Code + DeepSeek / max

继续使用第一次的原生 Claude Code 2.1.312 启动器、CLI 参数、输入追加说明与模型配置，详见 [第一次启动方式](../launch-record.md)。两次均新建 session UUID、独立 `CLAUDE_CONFIG_DIR`，输入各自原始 TASK；没有传入旧答案、作者隐藏测试或其他模型消息。

首次启动被执行沙盒的 socket 限制阻断，尚未获得模型 token。保存这些启动故障后，重新以获授权的本机网络访问启动两个新会话，使用用户已配置的系统代理，仅向该子进程传递配置；没有更改机器全局代理、模型参数、题目或测试。凭据只在内存/子进程环境中传递，不写入公开文件。

配置选择器为 `deepseek-flash[1m]`，effort 为 `max`，实际响应标识为 `deepseek-flash`。报告保留请求与观察值，不声称服务端别名对应不可变权重快照。
