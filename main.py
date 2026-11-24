"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to $MAKEFUN_OUTPUT_DIR/entry.txt.

Judge fit: the tip speaks to a stressed developer and to an AI coding
agent at once (the agent Googles the error; the human asked the question),
lands its turn in the last words (the question is the developer's own,
unanswered since 2019), and stays well inside the 200-character gate.
"""

import os

ENTRY = "Tip: while this loads, your agent is Googling your error message \u2014 and finding your own unanswered question from 2019."

MAX_CHARS = 200


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
