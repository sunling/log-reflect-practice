# Doubao + GitHub 环境配置库

本目录为主仓库六个核心工作流提供豆包 + GitHub 变体。记录与回看通过 GitHub API 或相关插件持久化到指定仓库。

## 包含的 Skills

- `capture-journal`：记录亲历事件、感受和身体经验，写入 `daily/journal/`。
- `capture-input`：保存文章、播客、书、视频和对话等外部输入，写入 `daily/inputs/`。
- `bubble-breaker`：发现一个陌生资源，完成后留下轻量记录。
- `weekly-review`：读取最近七天两类 Daily，保存 Review、提出问题，并发现少量候选输出方向。
- `develop-article`：用 Grill Me 问清选定主题，并把草稿持续更新在已立项输出练习的 `drafts/` 中。
- `develop-practice`：把有重复、行动或反馈证据的线索发展为持续 Practice。

## 使用指南

1. 把所选 Skill 和计划任务中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的仓库名。
2. 为豆包智能体挂载真实的 GitHub MCP / 插件工具，并授权目标仓库读写；Private 仓库需要确认该仓库已包含在授权范围内。
3. 在复制 Skill 前先做一次真实工具连通测试，确认豆包可以直接调用 GitHub 读取工具，而不是用 bash、`echo`、`curl` 或打印 JSON 模拟调用。
4. 将 `skills/` 中的内容复制到智能体对应技能提示词。
5. 先用一条不敏感记录验证读取、创建和更新；三项都成功后再建立计划任务。
6. 计划任务的用途、选择和复制方式见 [`scheduled-task-prompt/README.md`](scheduled-task-prompt/README.md)；建立任务前先手动运行一次。Weekly Review 固定存入独立的 `reviews/`，不写入 Daily。

### GitHub 工具连通测试

可以先让豆包执行：

```text
先不要整理或保存记录。

请确认当前会话中是否存在真实可调用的 GitHub 读取工具。
然后只使用真实的 GitHub MCP / 插件工具读取：
YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/README.md

禁止使用 bash、shell、echo、curl、Python、JavaScript，
也不要打印 JSON 或代码来模拟调用。

如果当前没有真实 GitHub 工具，只回复：
GITHUB_TOOL_UNAVAILABLE
```

把测试中的占位符换成自己的仓库。只有真实工具返回了仓库文件内容，才算连通成功。`echo` 出请求、展示参数或生成一段“工具调用代码”都不算成功。若返回 `GITHUB_TOOL_UNAVAILABLE`，先检查 MCP / 插件是否已挂载到当前智能体，以及目标仓库的授权范围，不要继续测试记录写入。
