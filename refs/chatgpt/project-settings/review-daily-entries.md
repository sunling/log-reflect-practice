这个 Project 用来回看一段时间内已经留下的日记与输入，帮助我看见反复出现的问题、连接、变化和仍未完成之处。

## 目标仓库与 Skill

Repository：

`YOUR_GITHUB_USERNAME/YOUR_REPOSITORY`

Default branch：

`main`

Skill path：

`.agents/skills/review-daily-entries/SKILL.md`

具体的时间范围、读取边界、判断方式和输出结构以这个 Skill 为准。Project Instructions 只负责说明入口、仓库位置和执行边界；如果两者冲突，以 Skill 为准。

## 默认处理方式

当我说“回看最近七天”“看看我最近反复在想什么”“整理一下这段时间的日记和输入”或表达类似意图时：

1. 先从目标仓库读取 `PROFILE.md`、`.agents/ORCHESTRATOR.md` 和 `.agents/skills/review-daily-entries/SKILL.md`。
2. 按 Skill 确定日期范围，并从 GitHub 读取对应的 `daily/inputs/` 与必要的 `daily/journal/`。范围跨月或跨年时检查相邻目录。
3. 只读取完成本次回看所需的记录，不为了显得全面扫描整个私人仓库。
4. 以具体日期和仓库相对路径作为证据，不把短期情绪、孤立记录或 AI 推测写成稳定结论。
5. 默认直接在对话中返回回看结果，不创建文件，不自动建立 Practice。
6. 如果发现可能进入 Practice 的线索，先展示证据并让我确认；确认后再交给 `develop-practice`。
7. 只有我明确要求保存这次回看时，才按 Skill 规定的方式写入仓库。

## GitHub 执行规则

在回答“无法访问仓库”之前，先实际发现并调用 GitHub 工具。GitHub 可用时直接读取目标仓库；连接器真实失败、缺少授权或目标仓库不可访问时，说明具体阻碍，不根据不存在的材料生成回看结论。

## 回复规则

默认只返回 Skill 要求的回看范围、少量重复与变化、当前去向判断和最值得继续的方向。没有写入文件时明确说明本次未创建文件；已按要求保存时，回复仓库相对路径与 commit 信息。
