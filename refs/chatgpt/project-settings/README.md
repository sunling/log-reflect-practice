# ChatGPT｜长期 Project 设置

这里保存可以复制到 ChatGPT **Project Instructions** 的三个简短入口配置。它们只负责建立 GitHub 通道并路由到仓库中的 Skill；具体整理、追问和写入规则仍以目标仓库中的 `.agents/skills/` 为准，不在 Project Instructions 中重复维护。

## 当前配置

| Project Instructions | 建议的 Project 名称 | 主要用途 | 默认去向 |
| --- | --- | --- | --- |
| [`new-journal.md`](new-journal.md) | 随时日记 | 随时记录亲历事件、感受和身体经验 | `daily/journal/` |
| [`new-input.md`](new-input.md) | 输入笔记 | 保存文章、播客、书、视频和对话带来的触动 | `daily/inputs/` |
| [`new-article.md`](new-article.md) | 文章工作台 | 接住选定主题，召回素材、Grill Me 并持续打磨草稿 | `practices/weekly-writing/drafts/` |

三个 Project 是三个长期入口，不代表所有 Skill 都需要创建 Project。Weekly Review 和 Bubble Breaker 更适合在专用聊天中测试后建立定时任务，详见 [`../scheduled-task-prompt/README.md`](../scheduled-task-prompt/README.md)。

## 创建方法

1. 先用模板仓库创建自己的记录仓库，填写根目录 `PROFILE.md`，并在 ChatGPT 中连接和授权 GitHub。
2. 打开所需配置，在 GitHub 文件页切换到 **Code / Raw（原始 Markdown）**，或使用 **Copy raw file** 复制完整内容。
3. 在 ChatGPT 新建 Project，把复制内容粘贴到 **Project Instructions**。
4. 把 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的完整仓库名。
5. `new-article.md` 默认使用 `weekly-writing` 作为输出练习，不需要再填写名称；如果尚未立项，首次使用时由 AI 建立最小 Practice。
6. 在文章工作台先发送：“先不要写文章，请测试 GitHub 通道并告诉我实际读取到的 Skill 路径和默认草稿目录。”只有它确实读到 `.agents/skills/new-article/SKILL.md` 后，再开始真实主题。
7. 先用一条不敏感内容测试 GitHub 写入，再开始保存真实记录。

## 使用边界

- Project Instructions 只提供稳定入口，不复制或覆盖 Skill 的完整规则；两者冲突时以 Skill 为准。
- 每次新文章任务都应从 GitHub 重新读取当前 Skill；不能因为 Project 记得旧对话就跳过通道检查。
- Journal 和 Input 默认直接保存；文章工作台只发展已经选定的主题，未确定主题时请使用者先提供或确认，不在文章工作台中调用 Weekly Review 替其选题。
- 文章草稿进入 `practices/` 不等于已经公开，任何外部发布都需要使用者明确要求。
- 如果 GitHub 只能读取、不能写入，应明确说明未持久化并返回建议路径与完整内容，不能把对话结果误报为已经保存。
- 真实记录建议放在 Private 仓库，并在授权范围中明确包含该仓库。
