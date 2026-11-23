"""One Letter: Coffee or Tea.

Writes exactly one letter, "A" (A = coffee), to /output/entry.txt:
one byte, no trailing newline, no extra whitespace. The letter is
validated before writing, so only "A" or "B" can ever be emitted.
"""

import os
from pathlib import Path


def validate_letter(letter: str) -> str:
    """Guard: the entry must be exactly one letter, "A" or "B"."""
    if len(letter) != 1 or letter not in ("A", "B"):
        raise ValueError("letter must be exactly one of 'A' or 'B'")
    return letter


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    letter = validate_letter("A")
    entry_path.write_bytes(letter.encode("ascii"))


if __name__ == "__main__":
    main()
