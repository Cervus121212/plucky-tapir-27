"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence uses only things a person from 1800 already knows: a coffee
house, a book, a page read aloud at a table. No word in it was coined
after the traveler's time. The program is deterministic: it always writes
the same bytes.
"""

import os

SENTENCE = (
    "A coffee house where every soul on earth writes its tale in one book, "
    "and any page you ask for is read aloud at your table."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
