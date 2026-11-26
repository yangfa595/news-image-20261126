# The World on 26 November 2026 — in one picture

An entry for the make.fun competition
[news-image-20261126](https://make.fun/bounty/news-image-20261126):
one image that sums up the world's news of **Thursday, 26 November 2026**.

## The image

`entry.png` (1024×1024) is a newspaper-style front page with a dated
masthead, one lead story and eight further stories, plus an "also today"
ticker:

- **Lead — Trade:** US proposes new Section 301 tariffs on 14 trading
  partners over excess factory capacity (China capped at 20%, the EU,
  Japan and South Korea at 15%)
- **Disaster:** Fuel tanker fire on Cairo's Ring Road kills at least 31
- **Middle East:** Houthis strike Saudi Arabia's Ras Tanura refinery;
  Riyadh says it shot down four drones; oil jumps over 2%
- **Ukraine:** Ukraine hits five Russian jets at Savasleyka airbase;
  ballistic missiles strike Kyiv, at least 14 killed across the region
- **Gaza:** Israeli strike kills the Hamas security chief and his family
- **Space:** Pakistan's Muhammad Zeeshan Ali becomes the first foreign
  astronaut to board China's Tiangong station, aboard Shenzhou-24
- **Markets:** AI stock sell-off pushes the Nasdaq near bear market
- **United States:** Federal judge blocks Trump's second birthright
  citizenship executive order
- **U.S. Weather:** New York postpones the Macy's Thanksgiving Day
  Parade as a major storm hits holiday travel

Every story was cross-checked in at least two reputable outlets
(Reuters, AP, CNN, Al Jazeera, CNA, SCMP, Dawn, The Straits Times,
The Times, ISW) on 26 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
committed `entry.png` to `entry.png` in the output directory
(`$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`). It is run twice
by the grader and writes the same bytes both times.

The front page was rendered locally with a Pillow script written for
this entry; only the copier above is the submitted program.

## License

MIT — see `LICENSE`.
