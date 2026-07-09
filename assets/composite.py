from PIL import Image, ImageDraw, ImageFilter
import os

HERE = os.path.dirname(__file__)
balloon = Image.open(os.path.join(HERE, "..", "..", "dji", "dji-360-deck", "assets", "concept-3-balloon.jpg")).convert("RGBA")
logo = Image.open(os.path.join(HERE, "ebay-logo.png")).convert("RGBA")
logo = logo.crop(logo.getbbox())  # trim transparent padding so it centers
truck = Image.open(os.path.join(HERE, "truck.png")).convert("RGBA")
W, H = balloon.size  # 1536 x 1024

def branded(base):
    img = base.copy()
    # white branding banner on the envelope face
    banner = Image.new("RGBA", img.size, (0,0,0,0))
    bd = ImageDraw.Draw(banner)
    cx, cy = 1140, 355
    bw, bh = 430, 150
    bd.rounded_rectangle([cx-bw//2, cy-bh//2, cx+bw//2, cy+bh//2], radius=28, fill=(255,255,255,205))
    banner = banner.filter(ImageFilter.GaussianBlur(0.6))
    img = Image.alpha_composite(img, banner)
    # eBay logo on the banner
    lw = 360
    lh = int(logo.height * lw / logo.width)
    lg = logo.resize((lw, lh), Image.LANCZOS)
    img.alpha_composite(lg, (cx - lw//2, cy - lh//2))
    return img

# Frame A: eBay balloon, real sky
frameA = branded(balloon)
# crop to a tighter cinematic 16:10 around the balloon
cropA = frameA.crop((640, 20, 1536, 580)).convert("RGB")
cropA.save(os.path.join(HERE, "concept-1.jpg"), quality=92)

# Frame B: suspended truck beneath the basket
frameB = branded(balloon)
d = ImageDraw.Draw(frameB)
basket = (1090, 852)
tw = 230
th = int(truck.height * tw / truck.width)
tk = truck.resize((tw, th), Image.LANCZOS)
tx, ty = basket[0]-tw//2, 905
# suspension cables basket -> truck rig
for dx in (-70, -25, 25, 70):
    d.line([basket[0]+dx*0.3, basket[1], tx+ (tw//2)+dx, ty+6], fill=(20,25,40,235), width=3)
frameB.alpha_composite(tk, (tx, ty))
cropB = frameB.crop((720, 60, 1460, 1024).__class__((720,60,1460,1024))).convert("RGB") if False else frameB.crop((720,60,1460,1024)).convert("RGB")
cropB.save(os.path.join(HERE, "concept-2.jpg"), quality=92)
print("saved concept-1.jpg", cropA.size, "concept-2.jpg", cropB.size)
