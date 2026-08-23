# Doubao + GitHub 环境配置库

本目录为主仓库五个核心工作流提供豆包 + GitHub 变体。记录与回看通过 GitHub API 或相关插件持久化到指定仓库。

## 包含的 Skills

- `capture-journal`：记录亲历事件、感受和身体经验，写入 `daily/journal/`。
- `capture-input`：保存文章、播客、书、视频和对话等外部输入，写入 `daily/inputs/`。
- `bubble-breaker`：发现一个陌生资源，完成后留下轻量记录。
- `weekly-review`：读取最近七天两类 Daily，保存 Review、提出问题，并在确认后发展文章。
- `develop-practice`：把有重复、行动或反馈证据的线索发展为持续 Practice。

## 使用指南

1. 把所选 Skill 和计划任务中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名。
2. 为豆包智能体挂载 GitHub 插件或等效代码库能力，并授权目标仓库读写。
3. 将 `skills/` 中的内容复制到智能体对应技能提示词。
4. 先用一条不敏感记录验证读取、创建和更新，再建立计划任务。
5. Weekly Review 的计划任务使用 `scheduled-task-prompt/weekly-review.md`，Review 固定存入独立的 `reviews/`，不写入 Daily。
