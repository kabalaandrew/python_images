from PIL import Image

img = Image.open("funny2.jpg")

img1 = Image.open("logo.jpg")

area = (100, 100, 315, 260)

img.paste(img1, area)

img.show()