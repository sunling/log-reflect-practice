# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）包含了为主仓库核心工作流在 **ChatGPT** 环境上运行所专门设计的变体。

与针对豆包/Coze 等纯云端智能体的设定不同，ChatGPT 环境下的设定主要侧重于项目的全局预设提示词（Project Settings）以及配合本地代码库（如 GitHub 同步、或直接在工作区内操作）使用的计划任务。

## 目录结构

- `project-settings/`：供你在 ChatGPT 的“Project”功能中复制粘贴的预设环境配置。六份配置分别对应主仓库中的六个 Skill。
- `scheduled-task-prompt/`：供在配合系统自动化或计划任务时使用的 Prompt，用于触发周期性的动作。

## 六个 Project Settings

| 核心 Skill | Project Setting | 主要用途 |
| --- | --- | --- |
| `capture-journal` | [new-journal.md](project-settings/new-journal.md) | 随时记录亲历事件、感受和身体经验 |
| `capture-input` | [new-input.md](project-settings/new-input.md) | 保存文章、播客、书、对话等外部输入 |
| `bubble-breaker` | [new-bubble.md](project-settings/new-bubble.md) | 发现陌生输入，并在完成后留下轻量记录 |
| `review-daily-entries` | [review-daily-entries.md](project-settings/review-daily-entries.md) | 回看最近七天或指定范围，寻找重复与变化 |
| `write-weekly-article` | [write-weekly-article.md](project-settings/write-weekly-article.md) | 用七天材料整理一篇默认给自己看的周记 |
| `develop-practice` | [develop-practice.md](project-settings/develop-practice.md) | 把有证据的线索发展成可持续 Practice |

六份设置不表示必须创建六个 Project。为了降低手机端记录的摩擦，可以把 Journal、Input 和 New Bubble 分开；回看、周记和发展 Practice 可以按需单独使用，也可以合并到一个“回看与实践”Project。合并时保留共同的目标仓库与执行边界，不要复制相互冲突的规则。

## 使用指南

1. **复制模板仓库**：先用仓库根目录的 **Use this template** 创建自己的仓库；真实记录建议放在 Private 仓库。
2. **替换配置占位符**：把所选配置文件中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名，例如 `ling/my-recording-system`。不要保留占位符，也不要使用示例仓库。
3. **填写个人偏好**：在仓库根目录的 `PROFILE.md` 中填写时区、主要语言和隐私边界。日期相关任务优先读取这里的时区；未填写时使用当前执行环境的本地时间，只有相对日期或日期边界仍有歧义时才询问，不直接用 UTC 代替。
4. **连接 GitHub**：在 ChatGPT 中连接并授权 GitHub，确认当前对话既能读取目标仓库，也能在需要时写入。先用一条不敏感的测试记录验证完整流程。
5. **项目配置**：在 ChatGPT 中创建 Project，从上表选择对应配置粘贴到 Project Instructions。一个 Project 可以只负责一个入口，也可以根据上面的建议合并。
6. **计划任务**：只有在对应流程已经手动运行成功后，再使用 `scheduled-task-prompt/` 创建定时任务。通知到邮箱是可选能力，不是记录系统的必要部分。

Project Instructions 负责说明入口、仓库和执行边界；具体的整理、命名与写入规则仍以目标仓库中的 `.agents/skills/` 为准。
