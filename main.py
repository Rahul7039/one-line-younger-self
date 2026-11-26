"""One Line to Your Younger Self.

Writes the chosen line verbatim to /output/entry.txt and prints it.
The line is a single sentence, addressed directly to the writer's younger
self: a specific, lived detail (a joke told at fourteen that fell flat)
with a turn only this person's older self could give it.

Before writing, the line is validated against the competition's rules:
a single line within the 200-character limit.
"""

import os

MAX_LENGTH = 200

LINE = (
    "That joke you told at fourteen that nobody laughed at \u2014 "
    "tell it again at thirty, when the whole room roars, "
    "and keep telling it."
)


def validate(line: str) -> None:
    """Guard the competition's own rules before writing anything.

    The entry must be a single line within the 200-character limit.
    Failing loudly here beats submitting a line the judges reject.
    """
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line (no line breaks)")
    if len(line) > MAX_LENGTH:
        raise SystemExit(
            f"entry line is {len(line)} chars, over the {MAX_LENGTH}-char limit"
        )


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
