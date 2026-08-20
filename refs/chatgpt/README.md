# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）包含了为主仓库核心工作流在 **ChatGPT** 环境上运行所专门设计的变体。

与针对豆包/Coze 等纯云端智能体的设定不同，ChatGPT 环境下的设定主要侧重于项目的全局预设提示词（Project Settings）以及配合本地代码库（如 GitHub 同步、或直接在工作区内操作）使用的计划任务。

## 目录结构

- `project-settings/`：供你在 ChatGPT 的“Project”功能中（或自定义指令中）复制粘贴的预设环境配置。这些配置帮助 ChatGPT 理解整个仓库的日记结构、命名规范以及任务去向。
- `scheduled-task-prompt/`：供在配合系统自动化或计划任务时使用的系统 Prompt，用于触发周期性的动作（例如每日回看、信息茧房探索等）。

## 使用指南

1. **复制模板仓库**：先用仓库根目录的 **Use this template** 创建自己的仓库；真实记录建议放在 Private 仓库。
2. **替换配置占位符**：把所选配置文件中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名，例如 `ling/my-recording-system`。不要保留占位符，也不要使用示例仓库。
3. **填写个人偏好**：在仓库根目录的 `PROFILE.md` 中填写时区、主要语言和隐私边界。日期相关任务优先读取这里的时区；没有填写时，AI 应先询问，不要猜测。
4. **连接 GitHub**：在 ChatGPT 中连接并授权 GitHub，确认当前对话既能读取目标仓库，也能在需要时写入。先用一条不敏感的测试记录验证完整流程。
5. **项目配置**：在 ChatGPT 中创建 Project，根据用途选择 `project-settings/` 中的一个配置粘贴到 Project Instructions。日记、外部输入和 New Bubble 可以分别建立 Project，也可以按自己的习惯合并。
6. **计划任务**：只有在对应流程已经手动运行成功后，再使用 `scheduled-task-prompt/` 创建定时任务。通知到邮箱是可选能力，不是记录系统的必要部分。

Project Instructions 负责说明入口、仓库和执行边界；具体的整理、命名与写入规则仍以目标仓库中的 `.agents/skills/` 为准。
