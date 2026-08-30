# ChatGPT｜长期 Project 设置

这里保存可以复制到 ChatGPT **Project Instructions** 的三个入口配置。它们负责告诉 Project 何时启动一条工作流、从哪个 GitHub 仓库读取 Skill，以及内容最终写到哪里；具体整理、追问和写入规则仍以目标仓库中的 `.agents/skills/` 为准。

## 当前配置

| Project Instructions | 建议的 Project 名称 | 主要用途 | 默认去向 |
| --- | --- | --- | --- |
| [`new-journal.md`](new-journal.md) | 随时日记 | 随时记录亲历事件、感受和身体经验 | `daily/journal/` |
| [`new-input.md`](new-input.md) | 输入笔记 | 保存文章、播客、书、视频和对话带来的触动 | `daily/inputs/` |
| [`new-article.md`](new-article.md) | 文章工作台 | 接住选定主题，召回素材、Grill Me 并持续打磨草稿 | `practices/<输出练习名>/drafts/` |

三个 Project 是三个长期入口，不代表所有 Skill 都需要创建 Project。Weekly Review 和 Bubble Breaker 更适合在专用聊天中测试后建立定时任务，详见 [`../scheduled-task-prompt/README.md`](../scheduled-task-prompt/README.md)。

## 创建方法

1. 先用模板仓库创建自己的记录仓库，填写根目录 `PROFILE.md`，并在 ChatGPT 中连接和授权 GitHub。
2. 打开所需配置，在 GitHub 文件页切换到 **Code / Raw（原始 Markdown）**，或使用 **Copy raw file** 复制完整内容。
3. 在 ChatGPT 新建 Project，把复制内容粘贴到 **Project Instructions**。
4. 把 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的完整仓库名。
5. 使用 `new-article.md` 时，还要把 `YOUR_OUTPUT_PRACTICE_NAME` 替换为已经立项的输出练习名；如果还没有，首次使用时让 AI 先协助建立 Practice。这个名称描述长期在练什么，不是某一篇文章的主题。
6. 先用一条不敏感内容测试 GitHub 读取和写入，再开始保存真实记录。

## 使用边界

- Project Instructions 只提供稳定入口，不复制或覆盖 Skill 的完整规则；两者冲突时以 Skill 为准。
- Journal 和 Input 默认直接保存；文章工作台只发展已经选定的主题，未确定主题时请使用者先提供或确认，不在文章工作台中调用 Weekly Review 替其选题。
- 文章草稿进入 `practices/` 不等于已经公开，任何外部发布都需要使用者明确要求。
- 如果 GitHub 只能读取、不能写入，应明确说明未持久化并返回建议路径与完整内容，不能把对话结果误报为已经保存。
- 真实记录建议放在 Private 仓库，并在授权范围中明确包含该仓库。
