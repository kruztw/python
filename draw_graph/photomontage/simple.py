# 參考: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

from PIL import Image, ImageDraw, ImageFont

with Image.open("background.png").convert("RGBA") as base:
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype("comic-sans.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, full opacity
    d.text((10,60), "suck", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)

    out.show()
