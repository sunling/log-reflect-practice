# Doubao + Feishu 环境配置库

本目录为主仓库六个核心工作流提供豆包 + 飞书变体。记录与回看通过飞书云盘插件持久化。

## 包含的 Skills

- `capture-journal`：记录亲历事件、感受和身体经验，写入 `daily/journal/`。
- `capture-input`：保存文章、播客、书、视频和对话等外部输入，写入 `daily/inputs/`。
- `bubble-breaker`：发现一个陌生资源，完成后留下轻量记录。
- `weekly-review`：读取最近七天两类 Daily，保存 Review、提出问题，并发现少量候选输出方向。
- `new-article`：跨时间召回选定主题的相关素材，再用 Grill Me 问清表达，并把草稿持续更新在已立项输出练习的 `drafts/` 中。
- `develop-practice`：把有重复、行动或反馈证据的线索发展为持续 Practice。

## 使用指南

1. 为豆包智能体挂载支持文件操作的飞书插件，并完成认证授权。
2. 在飞书云盘准备 `daily/journal/`、`daily/inputs/`、`reviews/` 与 `practices/`，或允许 Bot 首次使用时创建。
3. 将 `skills/` 中的内容复制到智能体对应技能提示词。
4. 先用一条不敏感记录验证读取、创建和更新，再建立计划任务。
5. 计划任务的用途、选择和复制方式见 [`scheduled-task-prompt/README.md`](scheduled-task-prompt/README.md)；建立任务前先手动运行一次。
6. 飞书允许同名文件夹并存。任何 Skill 创建目录前都必须完整列出父目录子项并精确匹配名称：1 个则复用，0 个才创建，多个则停止并消歧。
