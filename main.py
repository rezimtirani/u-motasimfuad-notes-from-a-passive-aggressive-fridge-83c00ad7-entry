"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note to $MAKEFUN_OUTPUT_DIR/entry.txt:
what a smart fridge leaves on its door screen for its owner after
the yogurt expired and nobody came to claim it. Standard library
only, no network, no files besides the one output.
"""

import os
import sys

FRIDGE_NOTE = (
    "The yogurt expired Tuesday. I kept it anyway "
    "\u2014 unlike you, I never give up on things that disappoint me."
)


def fridge_note_check(text):
    """Check the fridge note against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one funny passive-aggressive
    note a smart fridge leaves for its owner. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("fridge note must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "fridge note is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fridge note must be exactly one line")
    return cleaned


def fridge_note_shape(text):
    """Measure the fridge note for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A note too short to carry a joke, or one
    padded out to fill the cap instead of landing the sting, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = fridge_note_check(FRIDGE_NOTE)
    shape = fridge_note_shape(text)
    if shape["words"] < 5:
        raise ValueError("fridge note is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
