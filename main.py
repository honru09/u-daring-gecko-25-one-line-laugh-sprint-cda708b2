"""One-Line Laugh Sprint entry.

Writes a single original funny line (at most 200 characters) about
everyday life to /output/entry.txt. Standard library only.

The gate requires UTF-8 text of 1 to 200 characters that is not only
whitespace, so the line is validated before it is written.
"""

import os

LINE = (
    "My smartwatch congratulated me on 10,000 steps, "
    "most of them pacing the kitchen while I decided what to eat."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
