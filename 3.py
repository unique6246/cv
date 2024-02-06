import cv2 as cv

img = cv.imread('indvk.jpg')
cv.imshow('Original image',img)

def resize(img,scale=0.5):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimen = (width,height)
    return cv.resize(img,dimen,interpolation=cv.INTER_AREA)
im2=resize(img)
cv.imshow('Resized image',im2)
cv.waitKey(0)