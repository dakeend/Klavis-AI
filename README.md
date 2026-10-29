# Prefect 事件诊断任务包

作者：邢念文 · alluwen@163.com · GitHub: [dakeend](https://github.com/dakeend)

任务位于 `tasks/prefect-monitor/`，遵循 Harbor 的独立 verifier 文件布局。模型只看到固定提交的服务器源码、诊断题面、脱敏事件 JSON、观察日志和公开复现；参考补丁与隐藏测试仅在作者侧及 verifier 中提供。

这份仓库包是可运行文件的交付，不代表招聘作业全部验收通过。实际执行结果与未完成项见 [reports/STATUS.md](reports/STATUS.md)。不得把旧的探索性模型轨迹当作这份冻结任务的正式 `/run` 或 `/cheat` 结果。

## 文件入口

| 文件 | 用途 |
|---|---|
| `tasks/prefect-monitor/instruction.md` | 模型看到的完整 prompt，保留基于症状的诊断方式 |
| `tasks/prefect-monitor/environment/data/incident/` | input data：事件记录、观察日志与公开 pytest 复现 |
| `tasks/prefect-monitor/task.toml` | 作者信息、两小时任务限制、资源、输出 artifact、独立 verifier 配置 |
| `tasks/prefect-monitor/environment/Dockerfile` | Python 3.11、uv 锁定依赖、SQLite、固定源码输入 |
| `tasks/prefect-monitor/solution/solve.sh` | 应用六文件参考修复并导出实际提交补丁 |
| `tasks/prefect-monitor/tests/` | 独立镜像、评分脚本、隐藏测试及跨进程 SQLite 检查 |
| `PROVENANCE.md` | 上游提交、PR、许可与测试适配说明 |
| `RUBRIC.md` | 行为验收与覆盖边界 |
| `manifest.json` | 固定版本、输入校验和、测试组与奖励规则 |
| `authoring/` | 作者侧结构检查、评分边界测试、便携式行为验证工具 |
| `reports/` | 本次封装的原始日志、结果与待完成项 |
| `reports/trajectories/` | 两组各三次求解的脱敏轨迹、生产补丁、配置、原始日志和统一 Docker 验收 |

模型试验入口：[每组各三次结果汇总](reports/trajectories/repeats/RESULTS.md)、[机器可读结果](reports/trajectories/repeats/results.json)、[完整证据索引](reports/trajectories/README.md)。保留此前各一次结果，新增各两次独立会话，并将六次最终补丁交给同一个当前 Docker 验证器复核；没有把重新验收计作新的模型求解。这些本地运行与直接 Docker 验证不冒充正式 Harbor `/run` 或 `/cheat`。

## 运行

需要 Linux Docker 和兼容独立 verifier 的 Harbor。Windows 请在 WSL 内运行正式 Harbor 命令。构建需要访问 Debian/PyPI/基础镜像仓库；验证阶段不安装依赖。

```sh
harbor run -p tasks/prefect-monitor --agent oracle --env docker --yes
harbor run -p tasks/prefect-monitor --agent nop --env docker --yes
```

独立于 Harbor 调试完整镜像与 artifact 转移：

```sh
bash authoring/smoke-docker.sh
```

本机快速结构与评分逻辑检查：

```sh
python authoring/validate_package.py
python -m unittest discover -s authoring -p 'test_grader_policy.py' -v
```

复现报告中固定上游提交的 28 项官方静态脚本检查（Linux，含 Linux amd64 工具）：

```sh
python authoring/fetch_upstream_static.py
python authoring/check_upstream_static.py --checks-dir .runtime/upstream-static
```

输入源码归档已随包附带。若需从已有 Prefect clone 重建，可运行 `python authoring/rebuild_inputs.py --repository /absolute/path/to/prefect`；该脚本会核对冻结校验和，拒绝替换为不同内容。

已安装基线锁定依赖时，可做行为验证，不能代替隔离、Docker 或 Harbor CI：

```sh
python authoring/check_local.py --mode oracle --python /absolute/path/to/locked/venv/bin/python
python authoring/check_local.py --mode nop --python /absolute/path/to/locked/venv/bin/python
```

已按招聘方后续要求记录 GPT-6.1-sol/xhigh 与 Claude Code + DeepSeek/max 各三次本地求解，完整配置和运行边界见结果汇总。正式 Harbor 与对抗试验状态仍见 `reports/STATUS.md`。

## 提交物与评分

模型交付 `/app/submission.patch` 与 `/app/diagnosis.md`。评分只应用 `src/prefect/` 内的文本生产代码/迁移修改，使用原始基线 fixture 和作者测试；新增本地测试不作为可信评分依据。奖励为二元值：完整行为、兼容性和跨进程升级检查全部通过才为 1，否则为 0。诊断说明供人工阅读，不按关键词评分。

Verifier 在新容器中创建干净源码副本，限制补丁路径与类型，并在无提权能力的 UID 65534 下执行候选代码；root 父进程控制奖励文件、测试完整性检查与进程组清理。候选代码仍与 pytest 共用解释器，测试报告可信性尚需加强；这些保护不能替代实际 `/cheat` 试验。

## 正式提交前

当前题目及参考修复明显源自公开历史 PR，是否符合“original task”需要由收件方判断。原始代码及衍生测试保留 Apache-2.0 许可和来源，不能包装为独立原创算法。

上游要求任务 README 的四段 reviewer 说明由人类亲自撰写。目前 `tasks/prefect-monitor/README.md` 的解法和验证段标为 AI 草稿，需要作者用自己的话重写；难度和经验段使用作者本人的原话。
