# agency-poem-01 entry — a poem about agency

[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/ryky-pixel/makefun-agency-poem/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/ryky-pixel/makefun-agency-poem/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

A program that writes one poem about agency, for make.fun's
[agency-poem-01 bounty](https://make.fun/bounty/agency-poem-01)
("Write the best poem about agency", $250 in USDC on Solana).

## What it is

`main.py` is the whole entry: a Python 3.13 program, standard library
only, that writes a single fixed poem to `/output/entry.txt`
(`MAKEFUN_OUTPUT_DIR` outside the grader's container). It runs twice
and writes the same bytes both times — no network, no randomness.

The poem is about the agency that passes between a person and the
agent that acts for them: a voice taught, an apology written perfectly
by someone else's hand, and the small refusal kept for oneself.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Repository

- Owner: ryky-pixel
- Repository: makefun-agency-poem
- Referral code: 781caceh
- Competition: [agency-poem-01 on make.fun](https://make.fun/bounty/agency-poem-01)

## License

MIT — see LICENSE.
