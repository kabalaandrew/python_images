from PIL import Image
img = Image.open('funny2.jpg')

#print img.size()

#print img.format()

#img.show()

area = (100, 100, 200, 200)

cropped_img = img.crop(area)

cropped_img.show()