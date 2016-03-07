from PIL import Image

img = Image.open('funny2.jpg')

r, g, b = img.split()


img1 = Image.open('funny1.jpg')
r1, g1, b1 = img1.split()


new_img = Image.merge("RGB", (r1, g1, b))

new_img.show()