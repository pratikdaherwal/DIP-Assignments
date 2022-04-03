import cv2
import numpy as np

inpimg = cv2.imread('stock-snap.jpg')

l = len(inpimg)
b = len(inpimg[0])

grey = np.zeros((l, b), dtype=np.uint8)

for i in range(0, l):
    for j in range(0, b): 
        grey[i][j] = int(inpimg[i][j][0] * 0.2126 + inpimg[i][j][1] * 0.7152 + inpimg[i][j][2] * 0.0722)

sb = np.zeros((l, b), dtype=np.uint8)

for i in range(0, l):
    for j in range(0, b):
        sb[i][j] = int(inpimg[i][j][0] * 0.2126 + inpimg[i][j][1] * 0.7152 + inpimg[i][j][2] * 0.0722)

for i in range(200, l-200):
    for j in range(200, b-200):
        sb[i][j] = int(inpimg[i][j][0] * 0 + inpimg[i][j][1] * 0 + inpimg[i][j][2] * 0)


cv2.imshow('Input Image', inpimg)              
cv2.imshow('Grey Image', grey)
cv2.imshow('Inner Black', sb)  
cv2.imshow('Sub',grey-sb)            
cv2.waitKey(0)