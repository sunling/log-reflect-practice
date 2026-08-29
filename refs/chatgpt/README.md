# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）提供在 ChatGPT 中使用这套记录系统的参考配置。

这里的三类文件承担不同职责：

- **Project Settings**：为需要长期积累上下文的练习保留稳定入口；
- **Scheduled Task Prompt**：按时间主动触发一次工作流，不要求额外建立 Project；
- **Skill**：定义具体怎么读取、存档、追问和写入，是实际执行规则。

## 六个 Skill 如何使用

| 核心 Skill | 推荐承载方式 | 配置文件 |
| --- | --- | --- |
| `capture-journal` | 长期 Project | [new-journal.md](project-settings/new-journal.md) |
| `capture-input` | 长期 Project | [new-input.md](project-settings/new-input.md) |
| `weekly-review` | 专用聊天中的定时任务 | [weekly-review.md](scheduled-task-prompt/weekly-review.md) |
| `bubble-breaker` | 定时任务 | [break-bubble.md](scheduled-task-prompt/break-bubble.md) |
| `develop-article` | 选定主题后按需调用 | 直接读取仓库中的 `.agents/skills/develop-article/SKILL.md` |
| `develop-practice` | 需要时调用 | 直接读取仓库中的 `.agents/skills/develop-practice/SKILL.md` |

六个 Skill 是六条完整工作流，不需要对应六个 Project。

Journal 与 Input 适合保留独立 Project，方便在手机或网页中随时记录。Weekly Review 不需要单独的 Project：先在一个专用聊天中测试流程，再从同一聊天创建定时任务。每次运行都回到这个聊天，用户可以直接回答问题、更新同一档案，并选择是否继续某个输出方向。选定主题后，再按需读取 `develop-article` 逐个追问并整理文章。

## 目录结构

- `project-settings/`
  - `new-journal.md`
  - `new-input.md`
- `scheduled-task-prompt/`
  - `README.md`
  - `break-bubble.md`
  - `weekly-review.md`

## 使用前替换仓库占位符

凡配置文件中出现 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY`，无论是 Project Setting 还是 Scheduled Task Prompt，都要在使用前替换为自己的 GitHub 用户名和仓库名，例如 `ling/my-recording-system`。可以先在自己的仓库文件中替换，也可以复制粘贴后再替换；如果是定时任务 Prompt，必须在创建任务前完成替换。

## 使用指南

1. **复制模板仓库**：先用仓库根目录的 **Use this template** 创建自己的仓库；真实记录建议放在 Private 仓库。
2. **填写个人偏好**：在根目录 `PROFILE.md` 中填写时区、主要语言和隐私边界。
3. **连接 GitHub**：在 ChatGPT 中连接并授权 GitHub。
4. **创建两个长期 Project**：分别打开 [`new-journal.md`](project-settings/new-journal.md) 与 [`new-input.md`](project-settings/new-input.md)，在 GitHub 文件页切换到 **Code / Raw（原始 Markdown）** 视图，或使用 **Copy raw file**，复制完整内容并粘贴到对应 Project 的 **Project Instructions**。粘贴后，将其中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的 GitHub 用户名和仓库名，例如 `ling/my-recording-system`。也可以先在自己的仓库中完成替换再复制，两种方式效果相同。
5. **测试记录入口**：在 Journal 或 Input Project 中保存一条不敏感的测试记录，确认 GitHub 读取与写入都能工作。
6. **测试 Weekly Review**：新建一个专用聊天，先手动要求 ChatGPT 读取你仓库中的 `.agents/skills/weekly-review/SKILL.md` 并执行一次第一阶段，不创建定时任务；确认它能读取两类 Daily 并写入 `reviews/`。
7. **创建定时任务**：先查看 [`scheduled-task-prompt/README.md`](scheduled-task-prompt/README.md) 选择任务。打开对应 Prompt，复制原始 Markdown 并粘贴到刚才的专用聊天，将 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库，再设置执行时间。后续结果会回到同一聊天，方便继续回答问题和选择输出方向。

Project Instructions 只负责 Journal 与 Input 的长期记录入口；Scheduled Task Prompt 负责定期触发；具体规则始终以 `.agents/skills/` 为准。
