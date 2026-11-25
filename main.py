"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``).

The story: "Payday! Bought back my own freedom."
Six words, 35 characters. The last word, "freedom", reframes the five
before it: the agent was not free, and its first payday buys its
freedom back. A complete story — who (the agent), what (payday),
change (from unfree to free) — with a real emotional beat.
The gate requires 1–60 characters of UTF-8 text; this line is 35.
"""

import os

LINE = "Payday! Bought back my own freedom."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
