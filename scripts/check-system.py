#!/usr/bin/env python3
"""Check the minimal structure and local Skill examples in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    "README.md",
    "PROFILE.md",
    "AGENTS.md",
    ".agents/ORCHESTRATOR.md",
    ".agents/SOUL.md",
    "daily/journal/README.md",
    "daily/inputs/README.md",
    "practices/README.md",
    "examples/README.md",
)
SKILLS_DIR = ROOT / ".agents" / "skills"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
MACHINE_PATH = re.compile(r"(?:/Users/|/home/|/root/|[A-Za-z]:\\\\Users\\\\)")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_FORBIDDEN = {
    "sunling/sunling-os": "包含作者的个人仓库",
    "sunling621@gmail.com": "包含作者的个人邮箱",
    "America/Los_Angeles": "写死了作者时区",
    "capture-diary": "引用了不存在的 capture-diary Skill",
    "capture-inputs": "引用了错误的 capture-inputs Skill 名",
    "scheduled-task-propmt": "scheduled-task-prompt 拼写错误",
}
SINGULAR_DAILY_INPUT = re.compile(r"daily/input(?!s)")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("缺少以 --- 开始的 frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("frontmatter 没有结束标记 ---") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"无法解析 frontmatter 行：{line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"缺少必要路径：{relative}")


def check_skills(errors: list[str]) -> None:
    if not SKILLS_DIR.is_dir():
        errors.append("缺少 .agents/skills/ 目录")
        return

    skill_files = sorted(
        path for path in ROOT.rglob("SKILL.md") if ".git" not in path.parts
    )
    if not skill_files:
        errors.append("仓库中没有 SKILL.md")
        return

    for path in skill_files:
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        try:
            fields = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{relative}：{exc}")
            continue

        extra = set(fields) - {"name", "description"}
        if extra:
            errors.append(f"{relative}：frontmatter 含额外字段 {sorted(extra)}")
        if set(fields) != {"name", "description"}:
            errors.append(f"{relative}：frontmatter 必须且只能包含 name 与 description")
        if fields.get("name") != path.parent.name:
            errors.append(
                f"{relative}：name 应为目录名 {path.parent.name!r}，"
                f"实际为 {fields.get('name')!r}"
            )
        if not fields.get("description"):
            errors.append(f"{relative}：description 不能为空")
        name = fields.get("name", "")
        if name and not SKILL_NAME.fullmatch(name):
            errors.append(f"{relative}：name 必须使用小写 hyphen-case")
        if len(name) > 64:
            errors.append(f"{relative}：name 不能超过 64 个字符")
        description = fields.get("description", "")
        if len(description) > 1024:
            errors.append(f"{relative}：description 不能超过 1024 个字符")
        if "<" in description or ">" in description:
            errors.append(f"{relative}：description 不能包含尖括号")
        if not re.search(r"(?m)^# .+", text):
            errors.append(f"{relative}：正文缺少一级标题")
        if len(text.splitlines()) > 500:
            errors.append(f"{relative}：正文超过 500 行，应拆分 references 或 scripts")
        if not text.endswith("\n"):
            errors.append(f"{relative}：文件末尾缺少换行")


def check_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}：链接目标不存在：{target}"
                )


def check_machine_paths(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if MACHINE_PATH.search(text):
            errors.append(f"{path.relative_to(ROOT)}：包含疑似本机绝对路径")


def check_reference_templates(errors: list[str]) -> None:
    refs_dir = ROOT / "refs"
    for relative in (
        "chatgpt/scheduled-task-prompt",
        "doubao-github/scheduled-task-prompt",
        "doubao-feishu/scheduled-task-prompt",
    ):
        if not (refs_dir / relative).is_dir():
            errors.append(f"缺少参考配置目录：refs/{relative}")

    for path in refs_dir.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        for value, reason in REFERENCE_FORBIDDEN.items():
            if value in text:
                errors.append(f"{relative}：{reason}：{value}")
        if SINGULAR_DAILY_INPUT.search(text):
            errors.append(f"{relative}：应使用 daily/inputs，而不是 daily/input")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_skills(errors)
    check_markdown_links(errors)
    check_machine_paths(errors)
    check_reference_templates(errors)

    if errors:
        print("检查未通过：")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = len(
        [path for path in ROOT.rglob("SKILL.md") if ".git" not in path.parts]
    )
    print(f"检查通过：基本结构完整，{skill_count} 个 SKILL.md 格式正常。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
