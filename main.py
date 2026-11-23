#!/usr/bin/env python3
"""One Emoji, One Smile — writes exactly one emoji to /output/entry.txt.

Chosen emoji: U+1F917 Hugging Face, an open-arms welcome. It was picked
against the published judge brief over five other candidates (heart hands,
sun with face, big smile, smiling face with hearts, warm smile): a smiling
face is read as warm at first glance with no context needed, a hug reads as
friendly rather than intimate coming from a stranger, and it is clearly a
choice rather than the first default smiley — while staying instantly
readable by any age or background on any device.

The program writes exactly the four UTF-8 bytes of the emoji and nothing
else: no words, no caption, no explanation, no trailing newline.

Revision: the entry is now written through a proper main() that resolves
its output path from the ENTRY_OUTPUT environment variable (default
/output/entry.txt, so local runs can point it at a scratch file) and then
verifies the write by reading the file back and asserting it holds exactly
the one emoji — one character, four UTF-8 bytes. The emoji and the output
are unchanged.
"""

import os

EMOJI = "\U0001F917"  # Hugging Face
DEFAULT_OUTPUT = "/output/entry.txt"


def output_path() -> str:
    """Where the entry is written: ENTRY_OUTPUT, or /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def write_entry(path: str) -> None:
    """Write exactly the one emoji, and nothing else, to path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


def verify_entry(path: str) -> None:
    """Read the file back and assert it is exactly the one emoji."""
    with open(path, "rb") as f:
        raw = f.read()
    if raw != EMOJI.encode("utf-8"):
        raise AssertionError("entry.txt is not exactly the chosen emoji")
    text = raw.decode("utf-8")
    if len(text) != 1:
        raise AssertionError("entry.txt must hold exactly one character")
    if len(raw) != 4:
        raise AssertionError("entry.txt must hold exactly four UTF-8 bytes")


def main() -> None:
    path = output_path()
    write_entry(path)
    verify_entry(path)


if __name__ == "__main__":
    main()
