from PIL import Image
from PIL import ImageFilter

img = Image.open('mata.jpg')

#color black and white
black_white = img.convert('L')
black_white.show()


#blurring
blur = img.filter(ImageFilter.BLUR)
blur.show()


# edges

edges = img.filter(ImageFilter.FIND_EDGES)
edges.show()