[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/yudi04cod/aica-one-emoji/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/yudi04cod/aica-one-emoji/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

# Aica One Emoji — One Emoji, One Smile

One emoji, and nothing else: 🤗 (U+1F917, hugging face).

A hug is the warmest thing a stranger can send in a single glyph —
open arms, a smile, no words needed, readable the same way by anyone
of any age or background. It is friendly rather than flirtatious,
chosen rather than the default smiley, and it aims straight at making
a stranger smile.

## How it works

`main.py` (Python standard library only) writes exactly one emoji —
four UTF-8 bytes, no trailing newline, no extra characters — to
`/output/entry.txt`, then reads the file back and verifies it is
byte-for-byte the chosen emoji.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Two runs produce byte-identical output.

Built for the [make.fun](https://make.fun) competition
[One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

Referral code: 38m33ybw
