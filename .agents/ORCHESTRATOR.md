# 任务路由

先判断使用者此刻要完成什么，再读取最少的相关文件。

| 使用者意图 | 读取的 Skill | 默认去向 |
| --- | --- | --- |
| 记录今天发生的事、感受或身体经验 | `capture-journal` | `daily/journal/` |
| 保存文章、书、播客、课程或对话 | `capture-input` | `daily/inputs/` |
| 回看一周、找重复线索 | `review-seven-days` | 当前对话；确认后再写文件 |
| 把线索变成可持续行动 | `develop-practice` | `practices/<实践名>/` |

## 组合任务

如果一段材料同时包含外部输入和个人经历：

1. 先区分“外部内容”和“我的回应”。
2. 分别使用 `capture-input` 与 `capture-journal`。
3. 用相对链接把两条记录连接起来。

如果回看中发现可能的 Practice，先展示证据并征得使用者确认，再创建目录。
