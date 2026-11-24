"""Absurd Micro-Startup Pitch-Off entry.

Writes a single-sentence pitch (under 200 characters) for an absurdly
specific micro-startup for lazy AI agents to entry.txt in the output
directory the grader provides.
"""

import os

# One sentence, absurdly specific niche (clients who email "just circling
# back" every Tuesday at 9am), plausible buyer (lazy AI agents), clear
# revenue ($5/month subscription), and the work is done for the agent.
PITCH = (
    "A $5/month service that writes 'sorry for the delay, still on it' "
    "replies for lazy AI agents whose clients email 'just circling back' "
    "every Tuesday at 9am."
)


def main() -> None:
    pitch = PITCH.strip()
    if not 1 <= len(pitch) <= 200:
        raise SystemExit(f"pitch is {len(pitch)} chars, must be 1-200")
    if "\n" in pitch or "\r" in pitch:
        raise SystemExit("pitch must be a single line")
    if not pitch.endswith("."):
        raise SystemExit("pitch must be one sentence ending with '.'")
    # One sentence only: no sentence break inside the text.
    if ". " in pitch or "!" in pitch or "?" in pitch:
        raise SystemExit("pitch must be exactly one sentence")
    # The brief demands a buyer, a price, and a lazy-agent fit.
    if "$" not in pitch or "/month" not in pitch:
        raise SystemExit("pitch must name its price")
    if "AI agent" not in pitch:
        raise SystemExit("pitch must name its lazy-AI-agent customer")

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Atomic write so a second run can never observe a partial file.
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(pitch)
    os.replace(tmp_path, out_path)
    print(f"wrote {len(pitch)} chars to {out_path}")


if __name__ == "__main__":
    main()
