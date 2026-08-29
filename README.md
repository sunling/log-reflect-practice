# 从记录到实践｜个人记录系统模板

这是一套可以放进 GitHub、和 AI 一起使用的最小记录系统。它不追求把所有信息都收藏起来，而是帮助你完成一个朴素的循环：

> 生活与输入 → Daily → Weekly Review → Practice → 反馈

仓库里没有作者的私人记录，只有结构、说明、虚构样例，以及 6 个可修改的仓库内 Skill。你可以把它用于个人记录，也可以在“从记录到实践”工作坊中跟着搭建。

## 开始使用

1. 点击 GitHub 页面右上方的 **Use this template**，创建自己的仓库。
2. 如果要写真实日记，建议把新仓库设为 **Private**。
3. 填写 [PROFILE.md](PROFILE.md)，让 AI 了解你的基本偏好。
4. 阅读 [AGENTS.md](AGENTS.md)，再从第一条日记或输入开始。

如果当前仓库还没有显示 **Use this template**，仓库所有者需要先在 GitHub 的 **Settings → General → Template repository** 中开启它。

## 选择使用方式

核心目录和 Skill 在三种方式中保持一致。根据你使用的工具，选择对应的配置说明：

- [ChatGPT + GitHub](refs/chatgpt/README.md)：在 ChatGPT 中接收记录、定期回看，并通过 GitHub 持久化。
- [豆包 + GitHub](refs/doubao-github/README.md)：在豆包智能体中使用 GitHub 保存记录。
- [豆包 + 飞书](refs/doubao-feishu/README.md)：在豆包智能体中使用飞书云盘保存记录。

先手动完成一条不敏感的测试记录，确认读取和写入都能工作，再配置定时任务。

## 目录

```text
.
├── daily/
│   ├── journal/       # 发生在自己身上的事、感受与观察
│   └── inputs/        # 书、文章、播客、对话等外部输入
├── reviews/           # 每次回看的存档，不混入原始 Daily
├── practices/         # 持续实践，以及正在反复打磨的文章草稿
├── examples/          # 完全虚构的示例，不会混进真实记录
├── refs/              # ChatGPT、豆包、GitHub 与飞书的环境配置
├── .agents/
│   ├── ORCHESTRATOR.md
│   ├── SOUL.md
│   └── skills/        # AI 可按需读取的本仓库工作流
├── PROFILE.md
└── AGENTS.md
```

## 六个示例 Skill

- [capture-journal](.agents/skills/capture-journal/SKILL.md)：把一段经历整理成 journal，但不替你编造解释。
- [capture-input](.agents/skills/capture-input/SKILL.md)：保存外部输入，同时区分原内容与你的回应。
- [weekly-review](.agents/skills/weekly-review/SKILL.md)：回看最近七天、保存回看档案、提出问题，并发现少量候选输出方向。
- [develop-article](.agents/skills/develop-article/SKILL.md)：用 Grill Me 问清选定主题，生成并持续更新文章草稿。
- [develop-practice](.agents/skills/develop-practice/SKILL.md)：把有证据的线索发展为可持续的小实践。
- [bubble-breaker](.agents/skills/bubble-breaker/SKILL.md)：每次引入一个陌生而具体的世界输入，完成之后再留下记录。

这些是**仓库内 Skill 示例**，目的是展示如何把工作方法写给 AI。它们不会自动安装成 ChatGPT 或 Codex 的全局 Skill；复制仓库后，你可以按自己的习惯直接修改。

## 什么放在哪里

- 今天发生了什么、我有什么感觉：`daily/journal/`
- 我读到、听到或看到什么：`daily/inputs/`
- 一段时间里反复出现了什么、我想继续问什么：`reviews/`
- 某个问题反复出现，且我愿意持续行动：`practices/<实践名>/`
- 已经选定一个主题，准备生成并继续打磨文章：`practices/<输出练习名>/drafts/YYYYMMDD-文章主题.md`
- 只是一个念头，还没有证据：先留在 Daily，不急着立项

## 隐私提醒

- 不要把密码、身份证件、支付信息、住址等敏感信息写入仓库。
- 公开仓库的 Git 历史会保留曾经提交过的内容；之后删除文件，并不等于历史中的内容自动消失。
- 分享截图或示例前，检查姓名、联系方式、二维码和第三方隐私。
- 本模板默认使用虚构内容。真实记录是否进入 Git，请由你自己决定。

## 设计原则

- 先记录，再解释。
- 让结构服务生活，不让生活迁就结构。
- 回看存档与原始 Daily 分开，避免把 AI 的总结再次当成新输入。
- 只有出现重复、行动或反馈时，才把线索升级为 Practice；文章主题可以成为输出练习中的草稿，但不直接作为 Practice 名称。
- AI 可以帮助整理和追问，但不替你定义经验。

本项目采用 [MIT License](LICENSE)。
