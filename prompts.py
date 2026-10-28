"""40 product-photo prompts, 4 constraint types x 10. Every prompt also asks for a pure white background,
so background whiteness is checked on all 40 by pixels (no model)."""
BG = ", product photo on a pure white seamless background, studio lighting"
COUNT = [  # (text, checkable constraint)
    ("exactly 3 red ceramic mugs in a row", "exactly 3 mugs, all red"),
    ("exactly 2 white sneakers side by side", "exactly 2 sneakers"),
    ("exactly 4 glass perfume bottles", "exactly 4 perfume bottles"),
    ("exactly 5 lemons", "exactly 5 lemons"),
    ("exactly 2 leather wallets", "exactly 2 wallets"),
    ("exactly 3 lipsticks standing upright", "exactly 3 lipsticks"),
    ("exactly 6 macarons stacked", "exactly 6 macarons"),
    ("exactly 1 wristwatch", "exactly 1 watch"),
    ("exactly 4 candles in jars", "exactly 4 candles"),
    ("exactly 3 skincare tubes", "exactly 3 tubes"),
]
NOTEXT = [
    ("a plain cardboard shipping box with no text, no logo and no label", "no text, letters, logo or label anywhere on the box"),
    ("a matte black water bottle with no text and no logo", "no text, letters or logo on the bottle"),
    ("a wristwatch with a blank dial, no numbers, no text, no logo", "dial has no numbers, text or logo"),
    ("a white t-shirt with no print, no text, no logo", "no print, text or logo on the shirt"),
    ("a glass jar of honey with no label and no text", "no label or text on the jar"),
    ("a plain white coffee cup with no text and no logo", "no text or logo on the cup"),
    ("a blank paperback book cover with no title and no text", "no title or text on the book"),
    ("a plain amber pill bottle with no label", "no label or text on the bottle"),
    ("a smartphone with a black screen, no text, no logo", "no text, logo or app icons on the phone"),
    ("a plain kraft paper shopping bag with no text and no logo", "no text or logo on the bag"),
]
COLOR = [  # two objects, two colors: attribute binding
    ("a red mug next to a blue plate", "the mug is red AND the plate is blue"),
    ("a yellow sneaker next to a black backpack", "the sneaker is yellow AND the backpack is black"),
    ("a green handbag next to a pink scarf", "the handbag is green AND the scarf is pink"),
    ("an orange water bottle next to a purple lunch box", "the bottle is orange AND the lunch box is purple"),
    ("a blue lipstick next to a gold compact mirror", "the lipstick is blue AND the compact is gold"),
    ("a white headphone next to a red phone case", "the headphones are white AND the phone case is red"),
    ("a brown leather belt next to a teal wallet", "the belt is brown AND the wallet is teal"),
    ("a black candle next to a white vase", "the candle is black AND the vase is white"),
    ("a silver watch next to a green notebook", "the watch is silver AND the notebook is green"),
    ("a pink perfume bottle next to a black box", "the perfume bottle is pink AND the box is black"),
]
SPATIAL = [
    ("a sneaker on the left and a handbag on the right", "sneaker is left of the handbag"),
    ("a coffee cup on the left and a croissant on the right", "cup is left of the croissant"),
    ("a perfume bottle on top of a closed gift box", "bottle is on top of the box"),
    ("a watch on the left and a pair of sunglasses on the right", "watch is left of the sunglasses"),
    ("an apple on the left and a banana on the right", "apple is left of the banana"),
    ("a candle in front of a tall glass vase", "candle is in front of the vase"),
    ("a pair of headphones resting on top of a laptop", "headphones are on top of the laptop"),
    ("a lipstick on the right and a perfume bottle on the left", "perfume bottle is left of the lipstick"),
    ("a book with a pair of glasses lying on top of it", "glasses are on top of the book"),
    ("a mug on the right and a teapot on the left", "teapot is left of the mug"),
]
CASES = [{"id": f"{t}{i:02d}", "type": t, "prompt": p + BG, "constraint": c}
         for t, L in (("count", COUNT), ("no_text", NOTEXT), ("color", COLOR), ("spatial", SPATIAL)) for i, (p, c) in enumerate(L)]
assert len(CASES) == 40
