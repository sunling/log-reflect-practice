import os
import re

def update_capture_journal():
    path = '.agents/skills/capture-journal/SKILL.md'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_text = """## 七、 执行环境分支 (Execution Contract)

### 1. 当具备文件系统或 GitHub 写入能力时
优先直接完成文件创建或追加。执行完成后，对话回复只需简洁说明：
- 已写入或已追加；
- 目标文件路径；
- 若通过 GitHub 提交，则附上 commit 信息。

不要在对话回复中重复完整日记正文，除非用户明确要求预览或确认。

### 2. 当不具备文件系统或 GitHub 写入能力时
不要中断流程，也不要要求用户重新提供素材。请输出以下三项：
1. **目标文件路径**；
2. **应写入或追加的 Markdown 日记正文**；
3. **简短说明**：当前环境无法直接写入文件或 GitHub，需要用户手动复制，或在支持写入的环境中执行。

此时输出的 Markdown 日记正文仍必须严格符合「日记文件内容结构」，不要包含要点总结或执行说明。"""

    new_text = """## 七、 执行与输出

### 1. 默认执行（具备本地文件系统操作能力）
优先直接在本地完成文件创建或追加。执行完成后，对话回复只需简洁说明：
- 已写入或已追加；
- 目标文件路径。

不要在对话回复中重复完整日记正文，除非用户明确要求预览或确认。

### 2. 当不具备本地文件写入能力时
不要中断流程，也不要要求用户重新提供素材。请输出以下三项：
1. **目标文件路径**；
2. **应写入或追加的 Markdown 日记正文**；
3. **简短说明**：当前环境无法直接写入文件，需要用户手动复制。

此时输出的 Markdown 日记正文仍必须严格符合「日记文件内容结构」，不要包含要点总结或执行说明。"""
    
    if "GitHub" in content:
        content = content.replace(old_text, new_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

def update_develop_practice():
    path = '.agents/skills/develop-practice/SKILL.md'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_text = "当具备文件系统或 GitHub 写入能力时，直接创建或更新文件，并简短报告相对路径与变更内容。"
    new_text = "默认具备本地文件系统操作能力，直接在本地创建或更新文件，并简短报告相对路径与变更内容。"

    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

update_capture_journal()
update_develop_practice()
