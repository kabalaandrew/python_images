from PIL import Image

img = Image.open('funny2.jpg')

r, g, b = img.split()


new_img = Image.merge("RGB", (r,g,b))

# shuffle these channels
new_img2 = Image.merge("RGB", (b,g,b))

new_img.show()
new_img2.show()