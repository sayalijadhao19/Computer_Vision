import numpy as np
import cv2
import numpy as np
import cv2 as cv

# Create a black image as base
img11 = np.zeros((512,512,3), np.uint8)
img22 = np.zeros((512,512,3), np.uint8)
img33 = np.zeros((512,512,3), np.uint8)
img44 = np.zeros((512,512,3), np.uint8)
img55 = np.zeros((512,512,3), np.uint8)


# void cv::line	(	InputOutputArray 	img,
# Point 	pt1,
# Point 	pt2,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0 
# )	
img1=cv.line(img11,(0,0),(511,511),(255,0,0),5)


# void cv::rectangle	(	InputOutputArray 	img,
# Rect 	rec,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0 
# )	
img2=cv.rectangle(img22,(384,0),(510,128),(0,255,0),3)

# void cv::circle	(	InputOutputArray 	img,
# Point 	center,
# int 	radius,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0 
# )	
img3=cv.circle(img33,(447,63), 63, (0,0,255), -1)


# void cv::ellipse	(	InputOutputArray 	img,
# Point 	center,
# Size 	axes,
# double 	angle,
# double 	startAngle,
# double 	endAngle,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0 
# )	
img4=cv.ellipse(img44,(256,256),(100,50),0,0,180,255,-1)


# void cv::polylines	(	InputOutputArray 	img,
# const Point *const * 	pts,
# const int * 	npts,
# int 	ncontours,
# bool 	isClosed,
# const Scalar & 	color,
# int 	thickness = 1,
# int 	lineType = LINE_8,
# int 	shift = 0 
# )	
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img5=cv.polylines(img55,[pts],True,(0,255,255))



cv2.imshow('line',img1)
cv2.imshow('rectangle',img2)
cv2.imshow('circle',img3)
cv2.imshow('elipse',img4)
cv2.imshow('polylines',img5)
cv2.waitKey(100000)

