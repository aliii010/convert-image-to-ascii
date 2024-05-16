from PIL import Image

try:
  image = Image.open("fcb.png")
except:
  print("Image not found.")

width, height = image.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
image = image.resize((new_width, int(new_height)))

image = image.convert('L')

chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

pixels = image.getdata()
ascii_chars_as_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(ascii_chars_as_pixels)
ascii_image = [new_pixels[i: i + new_width] for i in range(0, len(new_pixels), new_width)]
ascii_image = "\n".join(ascii_image)

with open("fcb.txt", "w") as f:
  f.write(ascii_image)
