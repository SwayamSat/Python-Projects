from PIL import Image
import sys
import os

try:
  for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.jpg'):
          im = Image.open(filename).convert("RGB")
          im.save(filename.replace('jpg', 'png'), "png")
          print(f"Converted {filename} to PNG")
        elif filename.endswith('.png'):
          im = Image.open(filename).convert("RGB")
          im.save(filename.replace('png', 'jpg'), "jpeg")
          print(f"Converted {filename} to JPG")
except IOError:
  print('directory empty!')
  sys.exit()