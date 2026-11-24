# Cat Reviews Its Human

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/mfahmiq/cat-reviews-human/rank.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/mfahmiq/cat-reviews-human/reward.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

A make.fun text bounty entry: one funny single-line one-star review,
written by a house cat about the human it lives with.

## The entry

> One star. He threw away my favourite box to make room for a bed I never asked for. I now sleep in the box the bed came in.

## Why this line is funny

The joke works because it is a complaint only a cat would file — and
because the cat loses the argument with itself in the last sentence.

- **It keeps the deadpan shape of a real one-star review.** "One star."
  up front, a flat list of grievances, no winking at the reader. The
  form is a genuine angry-customer review; only the content is absurd.
- **The complaint is specific and recognisable.** Not vague grumpiness
  about "my human" — a favourite box, thrown away, replaced by a bed
  nobody asked for. Anyone who has lived with a cat has watched this
  exact purchase get ignored.
- **The voice is unmistakably feline.** The human is measured entirely
  by cat standards: a bed is judged not by comfort or price but by
  whether it is a box. The review gives away more about the cat than
  the owner — the cat is the one with the unreasonable standards, and
  it has no idea.
- **The sting lands in the last few words.** "I now sleep in the box
  the bed came in" flips the whole complaint: the human's crime was
  not buying the wrong thing, it was buying the right thing in the
  wrong shape. The cat got exactly what it wanted — a box — and is
  still leaving one star. That contradiction is the laugh, and it
  rewards a second read: the human actually won, and the cat will
  never admit it.

## How it works

`main.py` holds the entry as a single string constant and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before
writing, it self-verifies the bounty gate: the text must be valid
UTF-8, 1–200 characters, a single line, and not whitespace-only. It
then re-reads the file it just wrote and checks it byte for byte
against the constant. Any failure exits non-zero.

Python standard library only — no dependencies, no network, no input
files. The output is fully deterministic: the same line every run.

## Usage

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

