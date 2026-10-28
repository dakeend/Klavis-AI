# Prefect monitoring incident

Reviewer note: Solution explanation and Verification explanation below are AI-assisted factual drafts, not a claim of compliance with the upstream human-written-prose requirement. The author must replace those two paragraphs with their own text before formal submission. The difficulty and experience text are the author's own supplied words.

## Task Metadata

- **Author:** 邢念文 (alluwen@163.com)
- **Category:** `Software`
- **Tags:** <code>python</code> <code>sqlite</code> <code>debugging</code> <code>event-processing</code> <code>migrations</code>
- **Expert time:** 4 hours
- **Agent timeout:** 2 hours
- **CPUs:** 2
- **Memory:** 8 GB

## Difficulty explanation

作者原话：“这个题是出自一个成熟的github仓库中的一个真实负责的修复pr，首先代码量很多，需要模型先定位问题，第二点就是有成熟的历史测试案例，同时测试任务足够难。”

## Solution explanation

AI draft: The reference retains scoped, durable event evidence, uses event-time window membership and deduplicates identities when windows are opened or rolled. It supplies migrations for both database backends and bounds retained evidence; alternative implementations are allowed.

## Verification explanation

AI draft: A separate verifier applies only the production patch to a pristine commit and runs the public replay, 35 adapted historical cases, four retry regressions and three existing reactive/no-after compatibility cases. An additional controller seeds a real baseline SQLite database and checks upgrade preservation, resource separation, duplicate identity and expected action results across fresh processes.

## Relevant experience

作者原话：“我有一定的python经验，开发过数据库之类的图书馆管理系统，出题的思路主要是看之前的benchmark构建方式，从历史pr中找高质量的问题。”

Source disclosure and licensing: see the repository's `PROVENANCE.md`. The oracle is derived from Prefect PR #23445; PR #22886 is already present in the baseline. Originality is not certified.
