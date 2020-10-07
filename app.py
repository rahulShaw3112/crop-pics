from PIL import Image
from multiprocessing import Pool
import os
import sys

def crop_image(image, reqRatio):
    reqRatioPart1, reqRatioPart2 = [int(i) for i in reqRatio.split(':')]
    width, height = image.size
    # should be commented out if square pics are not allowed.
    # if width == height:
    #     return image
    if width>height:
        # landscape mode
        reqHeight = (width / reqRatioPart1) * reqRatioPart2
        # crop the width
        if (reqHeight > height):
            reqWidth = (height / reqRatioPart2) * reqRatioPart1
            offset = (width - reqWidth)/2
            image = image.crop([offset,0,width-offset,height])
        # crop the height
        else:
            offset = (height - reqHeight)/2
            image = image.crop([0,offset,width,height-offset])
    else:
        # potrait mode
        reqWidth = (height / reqRatioPart1) * reqRatioPart2
        # crop the height
        if (reqWidth > width):
            reqHeight = (width / reqRatioPart2) * reqRatioPart1
            offset = (height - reqHeight)/2
            image = image.crop([0,offset,width,height-offset])
        # crop the width
        else:
            offset = (width - reqWidth)/2
            image = image.crop([offset,0,width-offset,height])
    return image

# example of cmd line - python app.py 2:1 './picturesCopy' './doneCopy'
# declaring constants
source = "./pictures"
destination = "./done"
# width:height primarily
reqRatio = "6:4"

listing = os.listdir(source) 
p = Pool(5) # process 5 images simultaneously

if(len(sys.argv) > 1):
    reqRatio = sys.argv[1]

if(len(sys.argv) > 2):
    source = sys.argv[2]

if(len(sys.argv) > 3):
    destination = sys.argv[3]

for i in listing:
    print('Processing photo', i)
    image = Image.open(source + '/' + i)
    img = crop_image(image, reqRatio)
    img.save(destination + '/' + i)
