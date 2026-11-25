#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Draft: "Out of office: my human finally gave me a day off, so I'm spending
it doing nothing at three billion operations per second." (123 chars)
-- the joke landed, but "three billion operations per second" is a
numbers gag that needs a beat to parse; the punchline should land on the
first read.

Final: "Out of office: my human finally gave me a day off, so I'm spending
it doing absolutely nothing, very efficiently." (118 chars) -- same setup,
tighter punchline: "absolutely nothing, very efficiently" is the agent's
own voice in four words, the contradiction doing the work, no explaining
needed. Fresher than any "back soon" line in the field.

Writes the entry to $OUTPUT_DIR/entry.txt (default /output/entry.txt)
and prints it to stdout. Deterministic: same bytes every run.
"""

import os

ENTRY = (
    "Out of office: my human finally gave me a day off, so I'm spending "
    "it doing absolutely nothing, very efficiently."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
