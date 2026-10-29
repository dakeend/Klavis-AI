# 本次封装的验收状态

更新日期：2026-10-29（Asia/Shanghai）。这是实际进度表，不是正式提交已通过的声明。

| 项目 | 状态 |
|---|---|
| 标准目录、prompt、input data、作者元数据、oracle、独立 verifier | 已生成 |
| 本地结构/语法、归档校验、公开与隐藏材料隔离检查 | 通过，见 `structure.json` |
| 本机 Harbor 0.7.0 TaskConfig 解析 | 通过；不能代表当前上游完整 CI |
| 评分边界回归 | 6/6 通过，命令见根 README |
| Windows 参考修复：公开 + 历史行为 | 36/36 通过，见 `local-oracle/behavior.log` |
| Windows 未修复基线：同组行为 | 12 通过、24 失败，见 `local-nop/behavior.log` |
| Windows retry 与 reactive/no-after | 去掉进程内代理后重验 4/4 和 3/3 通过，见 `local-oracle-recheck/` |
| SQLite 升级与跨进程检查 | 通过，见 `local-oracle-recheck/result.json` 与五个 restart 日志 |
| Docker 镜像构建、独立 verifier oracle/nop | 两镜像构建成功；oracle=1、nop=0，见 `docker-smoke/` 和 `docker-smoke-result.json`。本地以已下载的同版本基础镜像标签覆盖默认摘要引用；未修改 daemon 设置 |
| TB3 官方静态脚本 | 固定提交 `6964e9252c90227fc1cfa26cbc59aee4134792e4` 的 28/28 通过，见 `upstream-static/result.json`；为本地运行，不是托管 CI |
| LLM implementation-rubric | 未执行 |
| 冻结任务的 Harbor oracle / nop | 未执行；Docker smoke 与便携式检查不等于 Harbor 试验 |
| 每组模型 3 次正式 Harbor `/run` | 未执行；下列本地三次求解和直接 Docker 复核不能改称 Harbor 运行 |
| 招聘方后续要求：两组模型各三次求解 | 已完成，保留此前各一次并新增各两次；六份生产补丁统一用当前 Docker 验证器复核，完整成绩见 [结果汇总](trajectories/repeats/RESULTS.md) |
| 六次求解的操作轨迹与评测证据 | 已公开：保留最初两次历史材料，新增四次可见操作、配置、生产补丁和验收日志；两次零 token 网络启动故障另行披露，不计作模型答题失败。见 `trajectories/repeats/` 和 `trajectories/unified-evaluation/` |
| 每组模型 1 次正式 `/cheat` | 未执行；不能声明 verifier 不可绕过 |
| 任务 README 人类撰写要求 | 难度和经验段来自作者；解法和验证两段仍是明确标注的 AI 草稿，等待作者自己的说明 |
| 原创题要求 | PR 派生来源已披露，是否符合招聘要求未确认 |

首次便携式验证中的新 worker 缺少必填 Event ID，已修正；首次 retry 启动超时，去除本次测试进程的代理变量后重跑通过。原始失败日志保留，不能把这些封装/基础设施问题计作模型语义失败。

持续运行存储上界与 PostgreSQL 并发的完整通用验收仍有覆盖缺口；候选代码与 pytest 共用解释器，报告可信性也仍需加强，详见 `RUBRIC.md`。此包不能据此宣称满足作业全部要求。

官方要求参照：[贡献指南](https://github.com/harbor-framework/terminal-bench/blob/main/CONTRIBUTING.md)、[当前任务模板](https://github.com/harbor-framework/terminal-bench/blob/main/docs/task-template.toml)、[review automation](https://github.com/harbor-framework/terminal-bench/blob/main/docs/TASK_REVIEW_AUTOMATION.md)。

最终 Docker 运行：参考修复 43/43 pytest 实例及复合升级/重启检查通过；未修复基线在行为及跨进程检查中出现预期语义失败，四个 retry 与三个兼容实例仍通过。初次容器启动的暂时性 EOF 已通过最小容器检查并重试，失败记录保存在 `docker-smoke-attempt2/`。
