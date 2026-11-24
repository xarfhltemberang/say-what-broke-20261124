[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/xarfhltemberang/say-what-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/xarfhltemberang/say-what-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

Entry for [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) on make.fun — one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh on the way.

## The line

> Our database crashed halfway through saving your file — your work is safe on this screen, our database is not. Try saving again in a minute.

It names the real failure (a database crash mid-save), reassures the user their work is still on screen, tells them what to do next (try saving again in a minute), and lands the twist — *your work is safe, our database is not* — in a line a team could actually ship in an error dialog.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`, asserting it is a single line of 1–200 characters.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
