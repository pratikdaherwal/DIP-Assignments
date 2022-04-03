import cv2 as im
# import matplotlib.pyplot as plt
import numpy as np


org = im.imread('stock-snap.jpg')
# fig = plt.figure(1)

imageHeight = len(org)
imageWidth = len(org[0])

gr = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        gr[i][j] = int(org[i][j][0] * 0.2126 + org[i][j][1] * 0.7152 + org[i][j][2] * 0.0722)

b = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        if gr[i][j] >= 127:
            b[i][j] = 255
        else:
            b[i][j] = 0

rgb = np.zeros((imageHeight, imageWidth, 3), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        rgb[i][j] = org[i][j] + np.uint(20)

# img1 = fig.add_subplot(121)
# img2 = fig.add_subplot(122)
# img3 = fig.add_subplot(123)
# img4 = fig.add_subplot(124)
# img5 = fig.add_subplot(125)

# img1.imshow(org)
# img2.imshow(gr, cmap=plt.cm.get_cmap('Greys'))
# img3.imshow(b)
# img4.imshow(rgb)
# img5.imshow(gr+b)

# fig.show()
# plt.show()

im.imshow('Orginal Image', org)
im.imshow('Gray Image', gr)              
im.imshow('Binary Image', b)             
im.imshow('RGB + 20 Image', rgb)         
im.imshow('Gray + Binary',gr+b)    
im.waitKey(0)
