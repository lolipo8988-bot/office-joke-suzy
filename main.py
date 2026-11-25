"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

JOKE = "HR told me to bring my whole self to work, so I brought my resignation too."


def main() -> None:
    # Gate check: entry must be 1-200 chars, a single line, not blank.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
