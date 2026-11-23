"""Write one sentence, one journey, to /output/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "I left home at seventeen with a train ticket folded inside my shoe "
    "and a coat two sizes too big, rode three days to a city where nobody "
    "knew my name, and came back at forty to find my mother had pressed "
    "that same ticket, still uncreased, between the pages of her Bible."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
