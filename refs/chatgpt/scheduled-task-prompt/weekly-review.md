请在当前聊天中创建每周一次的个人记录回看任务。如果我还没有提供星期、执行时间和时区，先询问后再创建。

每次执行时，读取 GitHub 仓库 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 下的 `.agents/skills/weekly-review/SKILL.md`，执行其中的第一阶段。

默认回看包含今天在内的最近七个日历日，完整读取对应范围内的 `daily/journal/` 与 `daily/inputs/`。识别有证据的 pattern、连接、变化和未完成之处，提出 1–3 个由材料长出来的问题。

无论本周是否存在输出方向，都把结果保存到 `reviews/{YYYY}/{YYYYMM}/{开始日期}-{结束日期}-{关键词}.md`。关键词应简短、具体且来自本周材料；同一日期范围已有 Review 时更新原文件并保留原文件名，不创建重复版本。保存成功后，将回看摘要、问题、可能发展的 0–2 个方向和 Review 路径返回当前聊天。

定时运行时不要直接生成文章或创建 Practice。等我在当前聊天中回答问题或选择一个输出方向后，再继续更新同一 Review；如果我明确想把选定主题写成文章，读取 `.agents/skills/develop-article/SKILL.md` 继续。
