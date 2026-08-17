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

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        errors.append(".agents/skills/ 中没有 SKILL.md")
        return

    for path in skill_files:
        relative = path.relative_to(ROOT)
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


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_skills(errors)
    check_markdown_links(errors)
    check_machine_paths(errors)

    if errors:
        print("检查未通过：")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = len(list(SKILLS_DIR.glob("*/SKILL.md")))
    print(f"检查通过：基本结构完整，{skill_count} 个仓库内 Skill 格式正常。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
