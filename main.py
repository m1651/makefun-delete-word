"""The Word You'd Delete From the Dictionary.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the single word this entry would erase from the dictionary forever.
"""

import os
import sys

# The word this entry would erase from the dictionary forever.
ENTRY_WORD = "defenestration"


def validate(word: str) -> None:
    """Check the entry word against the competition gate."""
    if not word:
        raise ValueError("entry word must not be empty")
    if not (1 <= len(word) <= 77):
        raise ValueError(
            f"entry word must be 1-77 characters, got {len(word)}"
        )
    if word.strip() != word or any(ch.isspace() for ch in word):
        raise ValueError("entry word must be a single word with no whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry word must be exactly one word")


def main() -> int:
    validate(ENTRY_WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)
    # Round-trip check: what landed on disk must be byte-identical to the
    # validated word, so a stray newline or encoding slip can never pass.
    with open(path, "rb") as f:
        if f.read() != ENTRY_WORD.encode("utf-8"):
            print("error: entry.txt on disk does not match the validated word", file=sys.stderr)
            return 1
    print(f"Wrote {ENTRY_WORD!r} ({len(ENTRY_WORD)} characters) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
