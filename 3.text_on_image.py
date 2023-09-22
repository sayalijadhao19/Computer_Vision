
import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
img=cv.putText(img,'Sayali',(10,500), font, 5,(255,255,255),2,cv.LINE_AA)

cv.imshow('sa',img)
cv.waitKey(100000)
