# 豆包 + GitHub｜计划任务 Prompt

这里保存需要由豆包按时间主动触发的任务 Prompt。计划任务负责定义触发时间和目标仓库，具体执行方式仍以仓库中的对应 Skill 为准。

## 当前任务

- [`weekly-review.md`](weekly-review.md)：每周回看最近七天的 Journal 和 Inputs，保存 Review，并返回问题与可能发展的方向；不会在定时运行中直接生成文章或创建 Practice。
- [`break-bubble.md`](break-bubble.md)：每隔一天推荐一个经过核实、与现有关注有距离的资源；完成前不入库，等用户明确说“完成了”后再执行记录流程。

## 使用前

1. 先按照[上一级 README](../README.md) 完成 GitHub 工具连通测试，确认豆包可以真实读取和写入目标仓库。
2. 把 Prompt 中的 `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` 替换为自己的完整仓库名。
3. 将所需 Prompt 的完整内容复制给豆包，并按自己的需要调整星期、时间、频率和时区。
4. 建立计划任务前先手动运行一次，确认它读取的是正确的 Skill、仓库和分支。
5. 如果使用 Private 仓库，确认它已包含在 GitHub 工具的授权范围内。

## 如何选择

- 想让过去一周的记录定期回来，使用 `weekly-review.md`。
- 想定期接触现有信息源之外的内容，使用 `break-bubble.md`。

计划任务只是触发器。如果要改变如何回看、如何筛选资源或如何写入仓库，应修改对应 Skill，而不是把整套工作流重复写进 Prompt。
