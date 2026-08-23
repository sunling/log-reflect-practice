# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）提供在 ChatGPT 中使用这套记录系统的参考配置。

这里的三类文件承担不同职责：

- **Project Settings**：为需要长期积累上下文的练习保留稳定入口；
- **Scheduled Task Prompt**：按时间主动触发一次工作流，不要求额外建立 Project；
- **Skill**：定义具体怎么读取、存档、追问和写入，是实际执行规则。

## 五个 Skill 如何使用

| 核心 Skill | 推荐承载方式 | 配置文件 |
| --- | --- | --- |
| `capture-journal` | 长期 Project | [new-journal.md](project-settings/new-journal.md) |
| `capture-input` | 长期 Project | [new-input.md](project-settings/new-input.md) |
| `weekly-review` | 长期回看 Project + 定时任务 | [Project Setting](project-settings/weekly-review.md) · [定时任务 Prompt](scheduled-task-prompt/weekly-review.md) |
| `bubble-breaker` | 定时任务 | [break-bubble.md](scheduled-task-prompt/break-bubble.md) |
| `develop-practice` | 需要时调用 | 直接读取仓库中的 `.agents/skills/develop-practice/SKILL.md` |

五个 Skill 是五条完整工作流，不需要对应五个 Project。

Journal 与 Input 适合保留独立入口，方便在手机或网页中随时记录。Weekly Review 适合放在长期 Project 中，并在其中创建定时任务：每次先读取七天 Daily、保存 Review、呈现 pattern 并提出问题；用户回来回答后，继续更新同一档案，并决定是否发展成文章。

## 目录结构

- `project-settings/`
  - `new-journal.md`
  - `new-input.md`
  - `weekly-review.md`
- `scheduled-task-prompt/`
  - `break-bubble.md`
  - `weekly-review.md`

## 使用指南

1. **复制模板仓库**：先用仓库根目录的 **Use this template** 创建自己的仓库；真实记录建议放在 Private 仓库。
2. **替换配置占位符**：把所选配置文件中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名，例如 `ling/my-recording-system`。
3. **填写个人偏好**：在根目录 `PROFILE.md` 中填写时区、主要语言和隐私边界。
4. **连接 GitHub**：在 ChatGPT 中连接并授权 GitHub，先用一条不敏感记录验证读取与写入。
5. **创建长期 Project**：把 `project-settings/` 中的配置复制到对应 Project Instructions。
6. **测试 Weekly Review**：先在普通对话中手动运行一次，确认能读取两类 Daily 并写入 `reviews/`。
7. **创建定时任务**：在 Weekly Review Project 的聊天中使用对应 Prompt；这样任务回来后，可以在同一对话继续回答问题和发展文章。

Project Instructions 负责长期入口与仓库边界；Scheduled Task Prompt 负责说明每次运行要做什么；具体规则始终以 `.agents/skills/` 为准。
