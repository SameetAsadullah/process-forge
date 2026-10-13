#!/usr/bin/env python3
"""Validate layout, generated files, and C/C++ syntax for the systems lab."""

from __future__ import annotations

import platform
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXERCISES = (
    "processes/command-line-arguments", "processes/fork-factorial",
    "processes/fork-array-sorting", "processes/exec-string-reversal",
    "ipc/unnamed-pipes", "ipc/named-pipes",
    "concurrency/producer-consumer", "concurrency/ticket-selling",
    "concurrency/withdraw-deposit", "concurrency/thread-joins",
    "concurrency/threaded-sudoku-validator", "shell/gbsh",
)


def tracked_files() -> list[Path]:
    output = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True)
    return [ROOT / line for line in output.splitlines()]


def main() -> int:
    errors: list[str] = []
    compiler = shutil.which("c++")
    if not compiler:
        errors.append("no C++ compiler found")

    for relative in EXERCISES:
        directory = ROOT / relative
        if not (directory / "README.md").is_file():
            errors.append(f"missing README: {relative}")

    for path in tracked_files():
        if path.suffix.lower() in {".exe", ".o", ".out"}:
            errors.append(f"generated binary is tracked: {path.relative_to(ROOT)}")

    if compiler:
        for source in sorted(ROOT.glob("**/*.cpp")):
            if platform.system() != "Linux" and source == ROOT / "shell/gbsh/src/gbsh.cpp":
                continue
            result = subprocess.run(
                [compiler, "-std=c++17", "-pthread", "-fsyntax-only", str(source)],
                cwd=source.parent,
                text=True,
                capture_output=True,
            )
            if result.returncode:
                errors.append(f"syntax check failed: {source.relative_to(ROOT)}\n{result.stderr}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(EXERCISES)} systems exercises.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
