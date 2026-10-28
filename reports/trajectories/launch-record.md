# 已记录的启动方式

这是 2026-10-28 的历史配置记录，不是正式 Harbor 启动日志或本次新运行。

## GPT-6.1-sol / xhigh

通过 Codex desktop 的子代理接口启动，原 session context 确认为 `model=gpt-6.1-sol`、`effort=xhigh`。输入要求在指定根目录读取 TASK.md 并独立解决问题。没有可据实提供的 `codex exec` 或 `harbor run` 启动命令；不为方便复现而编造这些命令。公开工具操作已导出，完整系统/开发者上下文未导出。

## Claude Code + DeepSeek

原生 Claude Code 版本为 2.1.312。下面是启动脚本使用的 CLI 参数，只有本地路径和 session UUID 用占位符表示：

```sh
"$CLAUDE_CODE" --print --verbose --output-format stream-json \
  --model 'deepseek-flash[1m]' --effort max --session-id "$SESSION_ID" \
  --restricted --tools Read,Edit,Write,Glob,Grep,Bash,PowerShell,TodoWrite \
  --permission-mode acceptEdits \
  --allowedTools Read,Edit,Write,Glob,Grep,Bash,PowerShell,TodoWrite \
  --disallowedTools Agent,Task,WebSearch,WebFetch \
  --strict-mcp-config --mcp-config "$EMPTY_MCP_JSON" \
  --setting-sources '' --settings "$CLIENT_SETTINGS_JSON"
```

`$EMPTY_MCP_JSON` 的内容为 `{"mcpServers": {}}`，客户端设置随该组 `client-settings.json` 提供。凭据仅由父进程通过环境传递，未导出其值。其他关键环境配置为：

```text
ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
ANTHROPIC_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-flash[1m]
ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-flash
CLAUDE_CODE_SUBAGENT_MODEL=deepseek-flash
CLAUDE_CODE_EFFORT_LEVEL=max
CLAUDE_CODE_AUTO_COMPACT_WINDOW=786432
DISABLE_AUTOUPDATER=1
DISABLE_NONESSENTIAL_TRAFFIC=1
```

使用独立 `CLAUDE_CONFIG_DIR`，并移除了进程中的 `ANTHROPIC_API_KEY` 和 `CLAUDE_CODE_OAUTH_TOKEN`。设置的 API 模型标识为 `deepseek-flash`，客户端选择器带 `[1m]` 后缀；实际初始化与观察到的模型值见该组 `run-config.json`。`max` 表示当时请求的客户端配置，不导出服务端私有推理。

输入经 stdin 传入，内容为该组 `input-task.md` 的原始 TASK 文件，加上下列操作提示（路径已脱敏）：

```text
Operational note: Read AGENTS.md and applicable source instructions. Do not inspect credentials or authentication environment variables. Use the installed Python at $SANDBOX/.runtime/venv/Scripts/python.exe. Runtime environment variables are already set for this process. Do not delegate, read other attempts or retrieve task-specific online answers. Implement the repair and write SOLUTION_SUMMARY.md.
```
