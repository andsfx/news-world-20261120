# news-world-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/andsfx/news-world-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/andsfx/news-world-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One 1024x1024 newspaper front page, "The World Today", that sums up Friday, 20 November 2026. It carries 37 stories researched and double-sourced that day, spread over six continents (Americas 11, Asia 9, Middle East 5, Africa 5, Europe 5, Oceania 2), led by Russia's overnight missile and drone attack on Kyiv, the UK-EU summit deal in Brussels, and Donald Trump's return from the Shenzhen talks with Xi and Putin. A masthead, a large dateline, a region strip, a strip of six verified numbers from the day (9 killed in Kyiv, the 51-48 Senate Iran vote, 589M children in conflict zones, the 17-billion-pound UK GDP boost, $93 Brent, $48bn Iran war cost), three illustrated lead cards, a ten-card news grid, a world map with twelve numbered hotspots keyed to a story list, a dense "also today" block and a source footer all make the day readable from the image alone. The page is self-contained (inline CSS, inline SVG, no fonts or images fetched); render.py draws it with headless Chrome, twice, and commits the byte-identical PNG. main.ts simply copies the committed entry.png to /output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Rebuild the image:

```sh
python3 render.py   # renders app/index.html -> entry.png (deterministic, verified twice)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=andsfx&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
