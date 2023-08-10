from PIL import Image

def getThumbnailsList(imagePathList, thumbnailSize):
    thumbnailsList = []
    for imagePath in imagePathList:
        try:
            with Image.open(imagePath) as im:
                im.thumbnail((thumbnailSize[0], thumbnailSize[1]))
                thumbnailsList.append(im)
        except OSError:
            print("cannot create thumbnail for", imagePath)
    return thumbnailsList


def mergeGivenImageList(thumbnailsList, thumbnailSize, matrixW, matrixH):
    if len(thumbnailsList) > matrixW * matrixH:
        raise Exception("Image list can't fit into given matrix size.")
    w = matrixW * thumbnailSize[0]
    h = matrixH * thumbnailSize[1]
    outIm = Image.new("RGBA", (w,h))
    for index in range(len(thumbnailsList)):
        location = ((int(index % matrixW)*thumbnailSize[0]), (int(index / matrixH)*thumbnailSize[1]))
        print(location)
        outIm.paste(thumbnailsList[index], location)
    return outIm

def getthumbnail(imagePathList, outPath, matrixW, matrixH, thumbnailSize=(1200,800)):
    outfile = outPath + ".png"
    try:
        outIm = mergeGivenImageList(getThumbnailsList(imagePathList, thumbnailSize), thumbnailSize, matrixW, matrixH)
        outIm.save(outfile,optimize=True, quality=95)
    except OSError:
        print(OSError)
        print("cannot convert")