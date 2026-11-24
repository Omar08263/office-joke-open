"""Office Joke Open: write one original office joke to /output/entry.txt.

Stdlib only. No network, no randomness, no time. The output is a fixed
string, so every run writes byte-identical output.
"""

import os

JOKE = "I muted myself on the call to sigh, unmuted to agree, and somehow got promoted for my 'thoughtful pauses'."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUT_PATH, 0o644)
    # Read-back verification: fail loudly on any difference.
    with open(OUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == JOKE, "read-back mismatch"
    assert 1 <= len(written) <= 200, "length out of gate range"
    assert written.strip() == written, "leading/trailing whitespace"
    assert "\n" not in written, "must be a single line"
    print(f"Wrote {len(written)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
