# 任务路由

先判断使用者此刻要完成什么，再读取最少的相关文件。

| 使用者意图 | 读取的 Skill | 默认去向 |
| --- | --- | --- |
| 记录今天发生的事、感受或身体经验 | `capture-journal` | `daily/journal/` |
| 保存文章、书、播客、课程或对话 | `capture-input` | `daily/inputs/` |
| 主动发现一个陌生领域的输入 | `bubble-breaker` | 先留在对话中；完成后进入 `daily/inputs/` |
| 回看一周、回应回看问题或把线索发展成文章 | `weekly-review` | 回看存入 `reviews/`；文章去向需确认 |
| 把线索变成可持续行动 | `develop-practice` | `practices/<实践名>/` |

## 组合任务

如果一段材料同时包含外部输入和个人经历：

1. 先区分“外部内容”和“我的回应”。
2. 分别使用 `capture-input` 与 `capture-journal`。
3. 用相对链接把两条记录连接起来。

Weekly Review 必须同时检查指定范围内的 Journal 与 Input，并把回看存入独立的 `reviews/`。不要把回看档案重新当作下一次 Daily 的原始证据。

如果回看中发现可能的 Practice，先展示证据并征得使用者确认，再创建目录。如果发现值得写作的线索，先询问是否发展成文章；草稿完成后，再确认是否保存及保存位置。

如果使用者想打破信息茧房，`bubble-breaker` 负责寻找资源；不要在对方完成之前把推荐当成已经发生的输入。
