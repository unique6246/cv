import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("BLANK",blank)
# blank[50:100,100:150]=255,0,0
# cv.imshow("Square",blank)
# cv.rectangle(blank,(0,0),(200,100),(0,0,255),thickness=4)
# cv.rectangle(blank,(0,0),(200,100),(0,0,255),thickness=cv.FILLED)#or thickness=-1
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//3),(0,0,255),thickness=-1)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(255,0,0),thickness=-1)
cv.line(blank,(100,200),(180,200),(255,255,0),thickness=5)
cv.imshow("Rect",blank)
cv.waitKey(0)