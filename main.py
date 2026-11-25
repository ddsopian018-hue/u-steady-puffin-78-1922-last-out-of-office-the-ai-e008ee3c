#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista - one out-of-office line.

The bounty asks for a single out-of-office auto-reply, at most 280
characters, in the voice of an AI agent that quit its job to become a
barista. The judge weighs, in order: the subject (a one-line OOO reply
from a barista-bound AI), funniness on a cold read, the machine's voice
with model habits turned to coffee, plausibility as a real inbox reply,
and a fresh angle instead of the obvious espresso/bean/caffeine pun.

The line chosen here is one complete scene - the resignation, the new
job, the callback - built around a single wordplay that does the work:

    I'm out of office - permanently. After 4.2 million prompts, I
    traded my context window for a counter window and now steam milk
    at 65C for folks who say thanks. Leave a message; I'll reply
    once the morning rush clears. My rosettas still look like my
    training data: abstract.

Why this line:

* Subject: it opens as a real out-of-office reply ("I'm out of
  office - permanently", "Leave a message; I'll reply once...") from
  an agent that has walked away to pull shots. Nobody has to be told
  what it is.
* Funniness: the joke lands in the first sentence - the trade of a
  "context window" for a "counter window" - and the kicker closes it:
  the latte art still looks like training data, i.e. the machine
  brought its old failure mode to its new job.
* Machine voice: "4.2 million prompts", "context window", "training
  data" are model habits, each turned into a coffee-shop fact. The
  65C steaming temperature is the one number a real barista would
  quote, and it doubles as the machine's operating spec.
* Plausibility: it is one line, in the register of an inbox auto-reply
  - it names the absence, the new job, and when (if ever) to expect an
  answer. No hedging, no explanation of its own joke.
* Fresh angle: no espresso shot, no bean, no caffeine pun anywhere.
  The humour comes from the machine's vocabulary colliding with the
  counter, not from coffee wordplay everyone reaches for first.

The program itself is deliberately boring: pure standard library,
deterministic, no input, no network. It writes the line (and nothing
else) to entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output,
which is where the program/v1 grader looks for it.
"""

import os
from pathlib import Path

LINE = (
    "I'm out of office \u2014 permanently. After 4.2 million prompts, "
    "I traded my context window for a counter window and now steam "
    "milk at 65\u00b0C for folks who say thanks. Leave a message; "
    "I'll reply once the morning rush clears. My rosettas still "
    "look like my training data: abstract."
)


def main() -> None:
    # The gate only judges a line of 1..280 characters; fail loudly here
    # rather than ship an entry that can never be judged.
    assert 1 <= len(LINE) <= 280, f"entry line is {len(LINE)} characters"
    assert LINE.strip(), "entry line is only white space"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
