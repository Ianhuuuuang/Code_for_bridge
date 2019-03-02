import cv2.cv as cv
import numpy as np
 
orig = cv.LoadImage('D:/test.png')
b = cv.CreateImage(cv.GetSize(orig), orig.depth, 1)
g = cv.CloneImage(b)
r = cv.CloneImage(b)
cv.Split(orig, b, g, r, None)
 
merged = cv.CreateImage(cv.GetSize(orig), 8, 3)
cv.Merge(g, b, r, None, merged)
 
cv.ShowImage("Image", orig)
cv.ShowImage("Blue", b)
cv.ShowImage("Green", g)
cv.ShowImage("Red", r)
cv.ShowImage("Merged", merged)
 
cv.WaitKey(0)