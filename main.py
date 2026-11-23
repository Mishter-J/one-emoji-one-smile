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
"""

import os

EMOJI = "\U0001F917"  # Hugging Face


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
