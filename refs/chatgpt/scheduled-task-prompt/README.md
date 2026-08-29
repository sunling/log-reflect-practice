# ChatGPT｜计划任务 Prompt

这里保存需要由 ChatGPT 按时间主动触发的任务 Prompt。计划任务负责定义触发时间和目标仓库，具体执行方式仍以仓库中的对应 Skill 为准。

## 当前任务

- [`weekly-review.md`](weekly-review.md)：每周回看最近七天的 Journal 和 Inputs，保存 Review，并把问题与可能发展的方向返回同一聊天；不会在定时运行中直接生成文章或创建 Practice。
- [`break-bubble.md`](break-bubble.md)：定期推荐一个经过核实、与现有关注有距离的资源；完成前不入库。已连接并授权 Gmail 时，也可以按需把任务发送到指定邮箱。

## 使用前

1. 先按照[上一级 README](../README.md) 连接并授权 GitHub，确认 ChatGPT 可以读取和写入自己的记录仓库。
2. 把 Prompt 中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的完整仓库名。
3. 新建一个专用聊天，先手动运行所需工作流，确认它能读取正确的 Skill、仓库和分支。
4. 在同一聊天中粘贴 Prompt，再设置星期、时间、频率和时区；后续任务结果会回到这里，方便继续回答和选择方向。
5. 如果使用 Private 仓库，确认它已包含在 GitHub 的授权范围内。

## 如何选择

- 想让过去一周的记录定期回来，使用 `weekly-review.md`。
- 想定期接触现有信息源之外的内容，使用 `break-bubble.md`。

计划任务只是触发器。如果要改变如何回看、如何筛选资源或如何写入仓库，应修改对应 Skill，而不是把整套工作流重复写进 Prompt。
