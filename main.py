"""One Line to Your Younger Self.

Writes the chosen line verbatim to /output/entry.txt and prints it.
The line is a single sentence, addressed directly to the writer's younger
self: a specific, lived detail (a joke told at fourteen that fell flat)
with a turn only this person's older self could give it.
"""

import os

LINE = (
    "That joke you told at fourteen that nobody laughed at \u2014 "
    "tell it again at thirty, when the whole room roars, "
    "and keep telling it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
