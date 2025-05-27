import sys, os
from PIL import Image, ImageOps


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith(".jpg") == False:
    sys.exit("Invalid output")
path1,ext1 = os.path.splitext(sys.argv[1])
path2,ext2 = os.path.splitext(sys.argv[2])
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    photo = Image.open(sys.argv[1])
    size = shirt.size
    resized = ImageOps.fit(photo, size)
    resized.paste(shirt, shirt)
    resized.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")