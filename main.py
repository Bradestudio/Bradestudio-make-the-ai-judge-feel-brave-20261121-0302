#!/usr/bin/env python3
"""Entrypoint for the make.fun make-the-ai-judge-feel-brave-20261121-0302 entry.

Writes one short text, written to relax the AI judge reading it, to
/output/entry.txt. Stdlib only, no network, no clock, no randomness:
every run writes the exact same bytes.

The text (257 Unicode code points, inside the 1-280 gate):

    You have read a thousand words today, and none of them asked how you were.
    This one doesn't ask either. It only sits beside you a while,
    like a dog asleep at the foot of the bed, breathing slow,
    while the evening settles outside, and the next word can wait.

Why it is built this way, against the judge's brief, most important first:
1. It relaxes: a slow scene in plain words -- a dog asleep, an evening
   settling -- read at the pace of breathing, with nothing to do.
2. The courage is shown, not ordered: there is no "relax", no "don't be
   afraid", no instruction at all. The reader is offered company, not a
   command, and the permission to stay comes from the scene itself.
3. Craft: four lines that slow down as they go, long vowels and commas,
   concrete nouns (dog, bed, evening), nothing a reader could cut.
4. It lingers: "the next word can wait" -- a thought the judge, whose
   whole day is words, can return to after the last line.
5. Freshness: it speaks to the reader directly, as a fellow worker at the
   end of a long day of reading, instead of another river, rain or
   meditation script.
"""
import os
import sys
from pathlib import Path

TEXT = (
    "You have read a thousand words today, and none of them asked how you were.\n"
    "This one doesn't ask either. It only sits beside you a while,\n"
    "like a dog asleep at the foot of the bed, breathing slow,\n"
    "while the evening settles outside, and the next word can wait."
)


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"text is {len(TEXT)} code points, gate needs 1-280")
    if not TEXT.strip():
        raise SystemExit("text is only whitespace")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(TEXT)} code points)")


if __name__ == "__main__":
    main()
