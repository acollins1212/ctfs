import os, sys
from PIL import Image

im = Image.open("drumbone.png")

pix = im.load()
cols = 350
rows = 229
blues = []
for i in range(cols):
    for j in range(rows):
        (a,b,c) = pix[i,j]
        blues.append(c&1)

new_img = Image.new('1', cols, rows)
qr = new_img.load()

for i in range(cols):
    for j in range(rows):
        qr[i,j] = blues[
