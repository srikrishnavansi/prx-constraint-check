# prx-constraint-check

Does Photoroom's open PRX model do what a product-photo prompt asks?

40 prompts, each with one thing you can check: an exact count ("exactly 5 lemons"), no text ("a watch with a blank dial"), two colours on two objects ("a red mug next to a blue plate"), or a position ("a candle in front of a vase"). Every prompt also asks for a pure white background.

PRX (`Photoroom/prx-512-t2i-sft-distilled`, 8 steps, seed = case number) ran locally on an Apple Silicon Mac, about 7 s per image. Claude Haiku 5.5 judged each image twice. A plain pixel rule checked the background (90% of the border at RGB 235 or brighter).

| | run 1 | run 2 |
|---|---|---|
| colour binding | 10/10 | 10/10 |
| position | 9/10 | 9/10 |
| no text | 8/10 | 7/10 |
| exact count | 7/10 | 7/10 |
| all | 34/40 | 33/40 |

The judge agreed with itself on 39 of 40. White background, by pixels: 23 of 40, and only 3 of 10 on the counting prompts. Every count miss added objects (7 lemons for 5, about 10 macarons for 6). Ask for several things and it builds a styled scene. Judging cost $0.011.

Limits: one seed per prompt, the small distilled checkpoint, my prompts and my pixel threshold. colour00 passed even though the mug sits on the plate, not next to it.

```
pip install diffusers transformers torch ftfy beautifulsoup4 anthropic numpy pillow
python gen.py                                     # images into img/
ANTHROPIC_API_KEY=... python judge.py             # results.json
```
