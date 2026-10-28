"""Generate the 40 images with Photoroom's open PRX model (prx-512-t2i-sft-distilled, 8 steps) locally on Apple Silicon (MPS).
Resumable: skips images already on disk. Seed = case index, so reruns are reproducible."""
import json, os, time, torch
from diffusers.pipelines.prx import PRXPipeline
from prompts import CASES
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs('img', exist_ok=True)
MODEL = 'Photoroom/prx-512-t2i-sft-distilled'
pipe = PRXPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to('mps')
meta = json.load(open('gen_meta.json')) if os.path.exists('gen_meta.json') else {}
for i, c in enumerate(CASES):
    out = f"img/{c['id']}.png"
    if os.path.exists(out): continue
    t = time.time()
    img = pipe(c['prompt'], num_inference_steps=8, guidance_scale=1.0, generator=torch.Generator('cpu').manual_seed(i)).images[0]
    img.save(out); meta[c['id']] = {'seed': i, 'secs': round(time.time() - t, 1), 'size': img.size}
    json.dump({'model': MODEL, 'steps': 8, 'guidance': 1.0, **meta}, open('gen_meta.json', 'w'), indent=1)
    print(c['id'], meta[c['id']], flush=True)
