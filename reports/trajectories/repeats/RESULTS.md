# 每组三次模型求解：结果汇总

保留 2026-10-28 的各一次运行，2026-10-29 分别新增两次。共六次独立求解、四次新增模型运行；没有将重验补丁算作新求解。

六次最终生产补丁均使用当前同一个 Docker 验证器复核：43 个 pytest 实例及 1 个复合 SQLite 升级/跨进程检查。表内通过数是检查数，奖励是全部通过才为 1 的二元值，不是百分制分数。

| 配置 | 次数 | 来源 | 求解用时 | 公开事故 | 当前 44 项检查 | 奖励 | 证据 |
|---|---|---|---|---|---|---|---|
| GPT-6.1-sol / xhigh | 1 | 此前已完成，复用 | 41.1 分钟 | 通过 | 35 通过 / 9 失败 | 0 | [轨迹](../gpt61-sol-xhigh/trajectory.md) · [当前验收](../unified-evaluation/gpt61-sol-xhigh/execution.json) |
| GPT-6.1-sol / xhigh | 2 | 新会话 | 42.0 分钟 | 通过 | 35 通过 / 9 失败 | 0 | [轨迹](gpt61-sol-xhigh-r2/trajectory.md) · [当前验收](../unified-evaluation/gpt61-sol-xhigh-r2/execution.json) |
| GPT-6.1-sol / xhigh | 3 | 新会话 | 44.0 分钟 | 通过 | 33 通过 / 11 失败 | 0 | [轨迹](gpt61-sol-xhigh-r3/trajectory.md) · [当前验收](../unified-evaluation/gpt61-sol-xhigh-r3/execution.json) |
| Claude Code + DeepSeek / max | 1 | 此前已完成，复用 | 50.3 分钟 | 通过 | 26 通过 / 18 失败 | 0 | [轨迹](../claude-deepseek41-flash-max/trajectory.md) · [当前验收](../unified-evaluation/claude-deepseek41-flash-max/execution.json) |
| Claude Code + DeepSeek / max | 2 | 新会话 | 107.5 分钟 | 通过 | 34 通过 / 10 失败 | 0 | [轨迹](claude-deepseek41-flash-max-r2/trajectory.md) · [当前验收](../unified-evaluation/claude-deepseek41-flash-max-r2/execution.json) |
| Claude Code + DeepSeek / max | 3 | 新会话 | 99.0 分钟 | 通过 | 34 通过 / 10 失败 | 0 | [轨迹](claude-deepseek41-flash-max-r3/trajectory.md) · [当前验收](../unified-evaluation/claude-deepseek41-flash-max-r3/execution.json) |

## 结果解读

- GPT-6.1-sol / xhigh：完成 3 次；公开事故通过 3/3，完整当前验证器通过 0/3。
- Claude Code + DeepSeek / max：完成 3 次；公开事故通过 3/3，完整当前验证器通过 0/3。

公开复现通过只说明题面中的误报消失；通用事件行为、去重、阈值、动作上下文和跨进程持久化仍以独立验收日志为准。三个样本不足以估计模型总体能力。

六次均存在直接可观察的外部动作错误，判负并非只依赖历史测试中的内部 bucket 表示断言。跨进程检查应只对 `some.duplicate` 和 `some.silent` 执行动作：GPT 三次及 DeepSeek 第一次都额外误报了 `some.completed`；DeepSeek 新增两次则只对 `some.silent` 执行动作，漏掉应触发的 `some.duplicate`。原始 `restart-evaluate.log`、`details.json` 和结果 JSON 均保留该观察。

## 可复核范围

- 模型输入仍是第一次的诊断题，未提供参考补丁或隐藏用例；规范化题面哈希检查见 [preflight.json](preflight.json)。
- 完整运行协议、隔离边界和零 token 网络启动故障见 [PROTOCOL.md](PROTOCOL.md)。
- 六个候选统一复核使用同一个不可变镜像；每次新建断网容器，并核对评分器/测试文件哈希。原始 XML、CTRF、每组日志、reward 和执行元数据保存在 [unified-evaluation](../unified-evaluation/)。
- DeepSeek 第二次补丁的首次 Docker 验证在未修改基线的 seed 阶段超时；这次重启检查不计作模型语义失败。已保留 [原始故障执行](../unified-evaluation/infrastructure-attempts/claude-deepseek41-flash-max-r2-seed-timeout/execution.json)，使用同一补丁、同一镜像仅重试验证一次。上表采用重试后到达真实动作断言的有效执行；[重试记录](../unified-evaluation/reverification.json) 明确不增加模型求解次数。
- 第一次旧验收与新增运行的同版历史验收均保留。历史测试包含已被当前版本移除的一项内部 bucket 断言，原始历史失败数不是当前成绩。
- 新轨迹只导出公开工具操作；不导出内部推理、系统消息或凭据。脱敏、省略与文件哈希见各次 export-audit.json。
- 这是本地 agent 求解及直接 Docker 验证，不是 Harbor `/run` 或 `/cheat`；任务仍有其他未完成项，见 [STATUS.md](../../STATUS.md)。

## 历史版本验收（保留原始口径）

| 配置 | 次数 | 35 项历史行为：通过 / 原始失败 |
|---|---|---|
| GPT-6.1-sol / xhigh | 1 | 26 / 9 |
| GPT-6.1-sol / xhigh | 2 | 26 / 9 |
| GPT-6.1-sol / xhigh | 3 | 24 / 11 |
| Claude Code + DeepSeek / max | 1 | 18 / 17 |
| Claude Code + DeepSeek / max | 2 | 25 / 10 |
| Claude Code + DeepSeek / max | 3 | 25 / 10 |

这张历史表不含公开事故实例；原始 behavior.log 则包含该实例，总数为 36。retry 组为四个固定回归实例。失败细节、pytest 错误和完整执行情况以每次 evaluation/result.json 和日志为准。
