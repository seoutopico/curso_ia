#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "01-fundamentos.md",
    "02-syllabus.md",
    "03-lecciones.md",
]

SYLLABUS_GROUPS = {
    "what_we_are_doing": ["What we are doing", "Que estamos haciendo"],
    "why_it_matters": ["Why it matters", "Por que importa"],
    "example": ["Example", "Ejemplo"],
    "template": ["Template", "Plantilla"],
    "deliverable": ["Deliverable", "Entregable"],
}

LESSON_GROUPS = {
    "objective": ["Objective", "Objetivo"],
    "why_it_matters": ["Why it matters", "Por que importa"],
    "worked_example": ["Worked example", "Ejemplo trabajado", "Ejemplo"],
    "template": ["Template", "Plantilla"],
    "accumulated_result": ["Accumulated result", "Resultado acumulado"],
    "quality_check": ["Quality check", "Criterio de calidad", "Criterios de calidad", "Checklist de calidad", "Checklist final de calidad", "Chequeo de calidad"],
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def missing_groups(text: str, groups: dict[str, list[str]]) -> list[str]:
    lower = text.lower()
    missing = []
    for group, variants in groups.items():
        if not any(variant.lower() in lower for variant in variants):
            missing.append(group)
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a modular AI term course directory.")
    parser.add_argument("module_dir", help="Path to doc/modulos/<term>")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    module_dir = Path(args.module_dir).resolve()
    issues = []
    warnings = []

    if not module_dir.exists() or not module_dir.is_dir():
        issues.append(f"Module directory does not exist: {module_dir}")
    else:
        for rel in REQUIRED_FILES:
            if not (module_dir / rel).is_file():
                issues.append(f"Missing required file: {rel}")

        sources_dir = module_dir / "00-fuentes"
        if not sources_dir.is_dir():
            issues.append("Missing required directory: 00-fuentes")
        else:
            source_files = sorted(sources_dir.glob("*.md"))
            if not source_files:
                issues.append("00-fuentes contains no .md source analyses")

        syllabus = module_dir / "02-syllabus.md"
        if syllabus.is_file():
            text = read_text(syllabus)
            missing = missing_groups(text, SYLLABUS_GROUPS)
            if missing:
                warnings.append("Syllabus may be missing block fields: " + ", ".join(missing))
            if len(re.findall(r"^##\s+", text, flags=re.MULTILINE)) < 3:
                warnings.append("Syllabus has fewer than 3 H2 blocks")

        lessons = module_dir / "03-lecciones.md"
        if lessons.is_file():
            text = read_text(lessons)
            missing = missing_groups(text, LESSON_GROUPS)
            if missing:
                warnings.append("Lessons may be missing lesson fields: " + ", ".join(missing))
            if len(re.findall(r"^##\s+", text, flags=re.MULTILINE)) < 3:
                warnings.append("Lessons has fewer than 3 H2 lessons")

        for path in module_dir.rglob("*.md"):
            text = read_text(path)
            if any(ord(ch) > 127 for ch in text):
                warnings.append(f"Non-ASCII characters found in {path.relative_to(module_dir)}")
                break

    result = {
        "valid": not issues,
        "module_dir": str(module_dir),
        "issues": issues,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("valid:", str(result["valid"]).lower())
        for issue in issues:
            print("ISSUE:", issue)
        for warning in warnings:
            print("WARNING:", warning)

    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())