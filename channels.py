from PIL import Image

img = Image.open("funny2.jpg")

r, g, b = img.split()


r.show()
g.show()
b.show()
