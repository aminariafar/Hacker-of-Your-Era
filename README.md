# 🛡️ CAPTCHA Research Demo (Educational)

This repository contains a small Python prototype that demonstrates **image preprocessing** and a simple **OCR-style approach** applied to CAPTCHA images. **This README frames the project for ethical, research, and defensive purposes only.**

> ⚠️ **Ethics & Legal:** Do **not** use this code to attack, bypass, or break into systems you do not own or do not have explicit permission to test. Use it only on datasets you own or in controlled environments for research, learning, or accessibility testing.

## ✨ What this demonstrates
- Basic image loading and preprocessing with **Pillow (PIL)**.  
- Simple segmentation and digit recognition heuristics.  
- Use of `requests` / `Session` can be adapted for **authorized** data collection for research (with permission).

## 🧱 Project Structure
```
hacker.py   # Prototype image-processing + OCR-ish functions (educational)
```

## 🔧 Requirements
- Python 3.8+
- pip install pillow requests

```bash
pip install pillow requests
```

## 🚀 How to use (safe mode)
1. **Do not** point this at a live service you don't control. Instead, run locally on saved CAPTCHA images.  
2. Save sample CAPTCHA images to a folder `samples/` (create it yourself).  
3. Edit `hacker.py` to load images from `samples/` instead of fetching from the web, or extract the image-processing functions and call them directly.  
4. Run in an isolated environment (virtualenv) and inspect outputs.

Example (conceptual):
```python
# safe_test.py (conceptual)
from hacker import getCaptcha  # or the image processing function inside
img = Image.open("samples/example1.png")
result = getCaptcha_from_image(img)   # adapt the code to accept PIL Image
print("Predicted:", result)
```

## ✅ Recommended ethical uses
- Accessibility research (e.g., alternatives for CAPTCHAs)  
- Studying image preprocessing / segmentation techniques  
- Teaching demonstrations in classroom / lab with synthetic data  
- Developing defensive measures (rate-limiting, improved CAPTCHAs)  

## ❌ Prohibited uses (do NOT do)
- Automated unauthorized login attempts  
- Bypassing access controls on third-party services  
- Any activity that violates terms of service or local laws
