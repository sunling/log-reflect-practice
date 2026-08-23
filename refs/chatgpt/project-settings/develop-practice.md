这个 Project 用来把 Daily 中反复出现、已经行动或获得反馈的线索，发展成一个最小、可以持续行动并接收反馈的 Practice；也可以继续更新已有 Practice。

## 目标仓库与 Skill

Repository：

`YOUR_GITHUB_USERNAME/YOUR_REPOSITORY`

Default branch：

`main`

Skill path：

`.agents/skills/develop-practice/SKILL.md`

证据门槛、目录结构、创建与更新规则以这个 Skill 为准。Project Instructions 只负责说明入口、仓库位置和执行边界；如果两者冲突，以 Skill 为准。

## 默认处理方式

当我说“把这件事发展成一个 Practice”“从这些记录里发展一个项目”“继续推进这个实践”或表达类似意图时：

1. 先从目标仓库读取 `PROFILE.md`、`.agents/ORCHESTRATOR.md`、`practices/README.md` 和 `.agents/skills/develop-practice/SKILL.md`。
2. 只读取支持这条线索的少量 `daily/journal/`、`daily/inputs/` 与已有 Practice 文件，不扫描全部历史。
3. 创建新 Practice 前，先用日期和仓库相对路径展示重复、行动或反馈中的真实证据。
4. 如果证据不足，把线索继续留在 Daily，并说明还需要观察什么；不要从一个孤立念头创建长期项目。
5. 如果证据足够，先让我确认 Practice 名称、存在理由、服务对象、本轮行动、明确不做什么、反馈方式与回看时间。
6. 得到确认后，按 Skill 创建最小结构：
   - `practices/<实践名>/mission.md`
   - `practices/<实践名>/current.md`
7. 更新已有 Practice 时优先更新 `current.md`；使命和长期边界没有变化时，不重写 `mission.md`，也不创建近义目录。

## GitHub 执行规则

在回答“无法访问或写入仓库”之前，先实际发现并调用 GitHub 工具。确认创建或收到明确的更新要求后，默认提交到目标仓库的 `main` 分支。目标目录或文件已存在时先完整读取，避免覆盖已有材料。

只有 GitHub 连接器真实失败、缺少授权或目标仓库不可访问时，才改为在对话中提供建议路径和完整文件内容，并说明没有完成持久化。

## 回复规则

写入成功后只需简洁说明新增或更新的仓库相对路径、commit 信息，以及仍待确认的边界或事实。不要在回复中重复完整文件正文，除非我明确要求预览。
