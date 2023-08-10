import os
from PIL import Image
from crop_and_append import getthumbnail
for root, dirs, files in os.walk("2023", topdown=False):

    print('vvvvvv')
    if files:
        imagePathList = []
        for name in files:
            if 'NEF' in name or 'thumbnail' in name:
                pass
            else:
                imagePathList.append(os.path.join(root, name))
        print(imagePathList)
        getthumbnail(imagePathList, outPath=os.path.join(root, "thumbnail"), matrixW=3, matrixH=3)
    if dirs:
        print(dirs)
    for name in dirs:
        print(os.path.join(root, name))
    print('^^^^^^')