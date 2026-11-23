"""One Letter: Coffee or Tea.

Writes exactly one letter, "A" (A = coffee), to /output/entry.txt:
one byte, no trailing newline, no extra whitespace.
"""

import os
from pathlib import Path


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_bytes(b"A")


if __name__ == "__main__":
    main()
