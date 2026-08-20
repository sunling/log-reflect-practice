# Doubao + GitHub 环境配置库

本目录（`refs/doubao-github/`）包含了为主仓库核心工作流在 **豆包（Doubao）智能体平台** 上运行所专门设计的变体。

此环境下的核心特点是：**系统依赖于 GitHub API 或相关插件进行最终的文件持久化存储**。所有的记录、任务会直接通过 Commit 的形式推送到指定的 GitHub 仓库（默认目标：`sunling/sunling-os`）。

## 目录结构

- `skills/`：供在豆包 Bot 中创建具体“技能（Skill）”时复制粘贴的 Prompt。所有的写入、读取步骤都已被改写为 GitHub API 的执行逻辑，且内置了特定的仓库约束。
- `scheduled-task-propmt/`：供豆包创建定时任务、计划任务时参考和复制的系统 Prompt。

## 包含的 Skills

目前本目录下包含以下核心功能的适配：

- **`capture-journal`**：用于将口语化、碎片化的语音转录或随手记录，整理为真实自然的个人日记（存入GitHub 仓库的 `daily/journal/` 目录）。
- **`capture-input`**：用于将文章、播客、视频等外部输入，以及读书闪念等低摩擦地整理归档（存入GitHub 仓库的 `daily/inputs/` 目录）。
- **`bubble-breaker`**：用于主动推荐并记录与现有 feed 不同的陌生领域高质量资源，打破信息茧房（完成的记录存入GitHub 仓库的 `daily/inputs/` 目录）。
- **`review-daily-entries`**：用于回看近期（如最近七天）在GitHub 仓库上的输入和日记，识别反复出现的线索、触动和变化，给出继续行动的方向。
- **`develop-practice`**：用于将日常记录中反复出现的线索，转化为最小可持续的长期实践（存入GitHub 仓库的 `practices/` 目录）。


## 使用指南
在使用本目录下的配置时，请确保你的智能体：
0. **修改目标仓库（必做）**：当前所有的 Skill 提示词中默认绑定的目标仓库为 `sunling/sunling-os`。在使用前，**请务必将各个文件中的 `sunling/sunling-os` 批量替换为你自己的 GitHub 仓库名**（例如 `your-username/your-repo`）。
1. 挂载了**GitHub 插件**或拥有类似的代码库操作能力。
2. 已经授权允许 Bot 对指定的仓库进行内容读写。
3. 请将目录下的 `skills/` 中的内容复制到智能体技能对应的提示词输入框内，以覆盖本地端默认的 `SKILL.md` 逻辑，确保它不会在云端迷失存储方向。
