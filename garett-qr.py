#!/usr/bin/env python3
import qrcode
from PIL import Image

# Generate QR for dark theme page
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
#qr.add_data("https://garettnell.com?ref=gngm")
qr.add_data("https://garett.xyz?ref=web")

qr.make(fit=True)

# Dark-on-light for the page aesthetic
img = qr.make_image(fill_color="#1b2566", back_color="#ffffff").convert("RGBA")
img = img.resize((256, 256), Image.LANCZOS)
#img.save("/Users/garett/projects/gngm/gngm.xyz/garettnell-qr.png")
img.save("/Users/garett/projects/gngm/gngm.xyz/garettxyz-qr.png")
print("Saved: garettxyz-qr.png (256x256)")
