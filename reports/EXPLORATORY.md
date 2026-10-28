# 冻结封装前的探索性模型试验

日期：2026-10-28。这些结果来自原工作区保留的独立验收记录；并非本包的 Harbor `/run`、`/cheat` 或当前 verifier 结果。

| 配置 | 求解用时 | 公开复现 | 当时 35 个历史实例 | 四个 retry 回归 |
|---|---|---|---|---|
| GPT-6.1-sol / xhigh | 41.1 分钟 | 通过 | 26 通过、9 失败 | 通过 |
| Claude Code / DeepSeek V4.1 Flash / max | 50.3 分钟 | 通过 | 18 通过、17 失败 | 通过 |

每个配置只运行一次。两个模型都修好了公开症状，却仍在窗口边界、多事件阈值、重复事件、滚动后的动作上下文等行为上出现失败；这说明只看公开 replay 无法判断一般性修复是否正确。

原验收中有一项内部 bucket 表示断言需审核，本包已移除该中间断言、保留最终动作检查。新增的三个兼容实例和跨进程检查也不在旧模型验收中，因此原始数字不得直接当作本包的成绩，不能据此断言已达到“两组各三次语义失败”。

旧 session 标识为 GPT `01a18191-47b9-71a1-a13c-29a4bdb90948`、Claude Code `55214eff-0884-4b79-a3a2-b90b27256548`。

2026-10-29 已补充[两组脱敏的可见操作轨迹及证据](trajectories/README.md)：公开消息、工具调用与结果、输入题面、配置、模型自述、最终生产代码补丁及对应独立验收日志。内部推理、原始 session/stream、凭据和本地通用技能正文没有上传。

- [GPT-6.1-sol / xhigh 可见轨迹](trajectories/gpt61-sol-xhigh/trajectory.md)
- [Claude Code + DeepSeek 可见轨迹](trajectories/claude-deepseek41-flash-max/trajectory.md)

补充证据不等于重新运行正式试验，旧版测试与当前 verifier 的差异仍按上文处理。
