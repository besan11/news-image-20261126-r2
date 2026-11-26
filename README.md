# news-image-20261126-r2

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/besan11/news-image-20261126-r2/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/besan11/news-image-20261126-r2/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Thursday 26 November 2026 in one picture: 40 stories across 9 regions, led by the first-ever postponement of the 100th Macy's Thanksgiving Day Parade, India marking 18 years since the 26/11 Mumbai attacks, and Gukesh–Sindarov Game 3 ending in a 60-move draw. A one-page newspaper front page with a big-numbers strip, a region bar, drawn scenes for the top three stories, a UTC timeline, a numbered world map, and a dated DATE CHECK that names what was deliberately left out.

## Run it

```sh
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`render.py` draws `entry.png` (1024×1024, Pillow only, Liberation fonts from the system); `main.ts` copies it to the grading output directory and verifies the PNG magic bytes. See `NOTES.md` for the story list, the sources, and what this round fixed versus round 1.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jpgk45b3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
