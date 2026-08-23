# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）提供在 ChatGPT 中使用这套记录系统的参考配置。

这里的三类文件承担不同职责：

- **Project Settings**：为需要长期积累上下文的练习保留稳定入口；
- **Scheduled Task Prompt**：按时间主动触发一次工作流，不要求建立独立 Project；
- **Skill**：定义具体怎么读取、整理、判断和写入，是实际执行规则。

## 六个 Skill 如何使用

| 核心 Skill | 推荐承载方式 | 配置文件 |
| --- | --- | --- |
| `capture-journal` | 长期 Project | [new-journal.md](project-settings/new-journal.md) |
| `capture-input` | 长期 Project | [new-input.md](project-settings/new-input.md) |
| `write-weekly-article` | 长期写作 Project | [write-weekly-article.md](project-settings/write-weekly-article.md) |
| `bubble-breaker` | 定时任务 | [break-bubble.md](scheduled-task-prompt/break-bubble.md) |
| `review-daily-entries` | 定时任务 | [review-last-7-days.md](scheduled-task-prompt/review-last-7-days.md) |
| `develop-practice` | 需要时调用 | 直接读取仓库中的 `.agents/skills/develop-practice/SKILL.md` |

六个 Skill 是六种能力，不需要对应六个 Project。

Journal 与 Input 适合保留独立入口，方便在手机或网页中随时记录。Weekly Writing 值得成为长期 Project，因为它会持续积累周记草稿、修改反馈、表达偏好和语言变化。

Bubble Breaker 与七天回看由定时任务主动触发即可。Develop Practice 则只在某条线索已经反复出现、发生行动或获得反馈时按需调用，不必提前创建空的 Project。

## 目录结构

- `project-settings/`
  - `new-journal.md`
  - `new-input.md`
  - `write-weekly-article.md`
- `scheduled-task-prompt/`
  - `break-bubble.md`
  - `review-last-7-days.md`

## 使用指南

1. **复制模板仓库**：先用仓库根目录的 **Use this template** 创建自己的仓库；真实记录建议放在 Private 仓库。
2. **替换配置占位符**：把所选配置文件中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名，例如 `ling/my-recording-system`。不要保留占位符，也不要使用示例仓库。
3. **填写个人偏好**：在仓库根目录的 `PROFILE.md` 中填写时区、主要语言和隐私边界。日期相关任务优先读取这里的时区；未填写时使用当前执行环境的本地时间，只有相对日期或日期边界仍有歧义时才询问，不直接用 UTC 代替。
4. **连接 GitHub**：在 ChatGPT 中连接并授权 GitHub，确认当前对话能够读取目标仓库，并在需要时写入。先用一条不敏感的测试记录验证完整流程。
5. **创建长期 Project**：根据需要，把 `project-settings/` 中的配置复制到对应 Project Instructions。三个 Project 可以独立建立，不需要为了定时任务额外创建 Project。
6. **测试定时工作流**：先在普通对话中手动运行 Bubble Breaker 或七天回看，确认仓库读取与输出符合预期。
7. **创建定时任务**：测试成功后，将 `scheduled-task-prompt/` 中的 Prompt 用于定时任务，再自行选择执行时间与频率。

Project Instructions 负责长期入口、仓库位置和执行边界；Scheduled Task Prompt 负责说明每次运行要做什么；具体规则始终以目标仓库中的 `.agents/skills/` 为准。
