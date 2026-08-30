# Doubao + Feishu 环境配置库

本目录为主仓库六个核心工作流提供豆包 + 飞书变体。豆包不依赖 ChatGPT Project；先把需要的 Skill 完整安装到智能体，再在普通对话中调用 Skill，通过飞书云盘插件读取和持久化文件。

## 包含的 Skills

- `capture-journal`：记录亲历事件、感受和身体经验，写入 `daily/journal/`。
- `capture-input`：保存文章、播客、书、视频和对话等外部输入，写入 `daily/inputs/`。
- `bubble-breaker`：发现一个陌生资源，完成后留下轻量记录。
- `weekly-review`：读取最近七天两类 Daily，保存 Review、提出问题，并发现少量候选输出方向。
- `new-article`：跨时间召回选定主题的相关素材，再用 Grill Me 问清表达，并把草稿持续更新在已立项输出练习的 `drafts/` 中。
- `develop-practice`：把有重复、行动或反馈证据的线索发展为持续 Practice。

## 使用指南

1. 为豆包智能体挂载支持文件操作的飞书插件，并完成认证授权。
2. 把准备使用的 `skills/<skill-name>/SKILL.md` 完整安装为豆包 Skill。不要改用 ChatGPT 的 Project Setting；豆包没有这层入口。
3. 在飞书云盘准备 `daily/journal/`、`daily/inputs/`、`reviews/` 与 `practices/`，或允许 Bot 首次使用时创建。
4. 在普通对话中明确调用已安装的 Skill。例如 Demo 文章流程时，调用 `new-article` 并提供一个已经选定的主题；后续读取、追问和飞书写入都由该 Skill 决定。
5. 先用一条不敏感内容测试：确认 Skill 能列出目标飞书目录、读取相关文件，并把结果上传回正确目录。只有返回真实飞书链接才算通道成功。
6. 计划任务的用途、选择和复制方式见 [`scheduled-task-prompt/README.md`](scheduled-task-prompt/README.md)；建立任务前先手动运行一次。
7. 飞书允许同名文件夹并存。任何 Skill 创建目录前都必须完整列出父目录子项并精确匹配名称：1 个则复用，0 个才创建，多个则停止并消歧。
