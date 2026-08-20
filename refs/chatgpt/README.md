# ChatGPT 环境配置库

本目录（`refs/chatgpt/`）包含了为主仓库核心工作流在 **ChatGPT** 环境上运行所专门设计的变体。

与针对豆包/Coze 等纯云端智能体的设定不同，ChatGPT 环境下的设定主要侧重于项目的全局预设提示词（Project Settings）以及配合本地代码库（如 GitHub 同步、或直接在工作区内操作）使用的计划任务。

## 目录结构

- `project-settings/`：供你在 ChatGPT 的“Project”功能中（或自定义指令中）复制粘贴的预设环境配置。这些配置帮助 ChatGPT 理解整个仓库的日记结构、命名规范以及任务去向。
- `scheduled-task-prompt/`：供在配合系统自动化或计划任务时使用的系统 Prompt，用于触发周期性的动作（例如每日回看、信息茧房探索等）。

## 使用指南

1. **项目配置**：在 ChatGPT 中创建一个新的 Project，并将 `project-settings/` 中的设定内容添加进系统提示词中，以确保 ChatGPT 理解你的个人记录体系。
2. **执行与存储**：配合本地操作环境时，ChatGPT 会生成符合核心 `.agents/skills` 要求的回答与本地文件修改命令；如果你是通过第三方自动化调用 API，请参考 `scheduled-task-prompt/` 中的设定进行集成。
