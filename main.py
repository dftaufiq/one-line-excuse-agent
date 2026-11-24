"""The One-Line Excuse an Agent Gives Its Human.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after missing a deadline. A machine that reads a 9 AM deadline as a
suggestion, then a rumor, then history — escalating denial, agent-literal,
owning the miss, no setup.
"""

import os

EXCUSE = "The deadline was 9 AM. I read it as a suggestion, then a rumor, then history."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
