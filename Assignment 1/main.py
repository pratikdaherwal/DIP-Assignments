from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

inpimg = imread("stock-snap.jpg")
r,g,b = inpimg[:,:,0], inpimg[:,:,1], inpimg[:,:,2]
gamma: float = 1.04
rconst, gconst, bconst = 0.2026, 0.7152, 0.0772

greyimg = rconst*r**gamma + gconst*g**gamma + bconst*b**gamma
fig = plt.figure(1)

img1 = fig.add_subplot(121)
img2 = fig.add_subplot(122)
img1.imshow(inpimg)
img2.imshow(greyimg, cmap=plt.cm.get_cmap('Greys'))

fig.show()
plt.show()