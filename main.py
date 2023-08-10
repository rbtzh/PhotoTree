import os
import random
from PIL import Image
from crop_and_append import getthumbnail
from matrixsize import get_size
#TODO: Let user choose which path as root filder

#config
ROOTPATH = "2023"
ALLOWED_MATRIXSIZES = [1,2,3,4,5,6]
RAW_FILE_NEEDED_TO_PASS = ".NEF"
CAMERA_IMAGE_SIZE = (6000,4000)
PREFIX="thumbnail-"

for root, dirs, files in os.walk(ROOTPATH, topdown=False):
    if files:
        imagePathList = []
        for name in files:
            if RAW_FILE_NEEDED_TO_PASS in name:
                pass
            else:
                imagePathList.append(os.path.join(root, name))

        #find the right matrix size.
        (matrixSize, needSample) = get_size(ALLOWED_MATRIXSIZES, len(imagePathList))
        print(matrixSize, needSample)
        #if imagePathList contains too many images, randomly choose some out of them.
        if needSample:
            imagePathList = random.sample(imagePathList, ALLOWED_MATRIXSIZES[-1]**2)
            
        outpath=os.path.abspath(os.path.join(root, 
                                             os.pardir, 
                                             PREFIX + str(os.path.basename(root))))
        print(imagePathList)

        thumbnail_size= (int(6000/matrixSize),int(4000/matrixSize))
        getthumbnail(imagePathList=imagePathList, 
                     outPath=outpath, 
                     thumbnailSize=thumbnail_size, 
                     matrixW=matrixSize, 
                     matrixH=matrixSize)
        