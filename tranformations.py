from PIL import Image

img = Image.open('mata.jpg')

#square = img.resize((250,250))

#square.show()


#flip = img.transpose(Image.FLIP_LEFT_RIGHT)

flip = img.transpose(Image.FLIP_TOP_BOTTOM)

spin = img.transpose(Image.ROTATE_90)


spin.show()
flip.show()