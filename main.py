"""The 3 AM Excuse — a make.fun entry.

Prints exactly one line of under 200 characters, in the voice of a
hardware wallet that will not sign a transaction at 3 AM.
"""

LINE = (
    "It is 3 a.m. and I refuse to sign anything neither of us "
    "will remember approving after sunrise."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
