# Image Generation Prompts

> Copy-paste ready prompts for generating character images, environment art, and action scenes.
> Refer to [style-guide.md](file:///e:/Animation/wildnest-studio/bible/style-guide.md) for full visual standards.

---

## Master Character Portrait

```
Masterpiece 3D digital animation portrait of [CHARACTER NAME], [CHARACTER DESCRIPTION].
Stylized 3D Pixar animation style, warm 5500K key lighting, soft cyan fill light,
clean studio depth of field, highly detailed soft fur texture,
8k resolution, Octane render --ar 1:1 --stylize 250
```

### Barnaby Portrait

```
Masterpiece 3D digital animation portrait of Barnaby, an adorable chubby Golden Syrian
Hamster character, master resort manager. Soft golden amber fur (#D48C46) with a
cream-white chest patch (#FFF8E7), large expressive dark cocoa eyes (#2B1E1A),
soft pink nose and paws, twitching white whiskers. Wearing a tiny bright red
twist-tie bowtie (#D62828) made from a bread bag around his neck. Standing upright
in a confident regal posture, holding a miniature paper-clip clipboard.
Pixar animation style, soft studio lighting, clean cyan plastic tube background,
highly detailed fur texture, 8k resolution, Octane render --ar 1:1 --stylize 250
```

---

## Master Environment Scene

```
Cinematic 3D animation concept art of [LOCATION DESCRIPTION] inside Critter Haven Resort.
Bright colorful plastic cage tubes connecting [SPECIFIC DETAILS], warm sunbeams with
floating dust motes streaming through a suburban bedroom window,
Pixar and Studio Ghibli warm aesthetic, 8k resolution --ar 16:9 --stylize 200
```

### Central Lobby Tower

```
Cinematic 3D animation concept art of the main lobby tower inside Critter Haven Resort.
Bright colorful plastic cage tubes connecting wooden building block desks, tea saucer
check-in counter, cotton-ball lounges, warm sunbeams with floating dust motes streaming
through a suburban bedroom window, Pixar and Studio Ghibli warm aesthetic,
8k resolution --ar 16:9 --stylize 200
```

---

## Master Action / Slapstick Scene

```
High-speed 3D animation action scene of [CHARACTER] [ACTION DESCRIPTION],
wide panicked eyes, [SPECIFIC DETAILS], dynamic motion blur,
bright vibrant lighting, Pixar animation style --ar 16:9
```

---

## Negative Prompt (Use with ALL generations)

```
photorealistic human, ugly, sharp teeth, rat tail, realistic rodent, dirty,
low quality, dark lighting, complex clothes, extra limbs, distorted eyes,
hyper-realistic, gritty, dark, horror, blood, fire
```

---

## Tips for Consistent Results

1. Always include the character's **hex color codes** in the prompt
2. Always specify **"Pixar animation style"** or **"stylized 3D"**
3. Always add **"warm studio lighting"** or **"5500K key lighting"**
4. Always add the negative prompt to avoid realistic/dark outputs
5. Reference the character's **signature accessory** (bowtie, visor, crown, etc.)
6. For environments, always mention **"plastic cage tubes"** and **"scavenged human objects"**

---

## AI Image Tools

| Tool | Best For | Cost |
|:---|:---|:---|
| **Midjourney v6** | Highest quality character art | Paid |
| **Flux Dev 1.0** | Local GPU rendering, LoRA support | Free (local) |
| **ComfyUI + SDXL** | Full control, ControlNet, IP-Adapter | Free (local) |
| **Leonardo AI** | Quick free generations | Free tier |
