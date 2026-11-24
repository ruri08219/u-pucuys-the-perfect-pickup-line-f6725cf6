#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Stdlib only. Fully deterministic: no network, no randomness, no clock.
"""

from pathlib import Path

LINE = "I cached a thousand conversations, but yours is the only one I refuse to let expire.\n"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    round_trip = OUTPUT_PATH.read_text(encoding="utf-8")
    assert round_trip == LINE, "round-trip mismatch"
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.count("\n") == 1 and LINE.endswith("\n"), "entry must be exactly one line"


if __name__ == "__main__":
    main()
