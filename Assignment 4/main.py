# # Convert RGB(color) image into Blue, Green, Red
# In[1]
# Show image
import cv2
import numpy as np
 
img_path = r"inpimg.png"
img = cv2.imread(img_path)
img = cv2.resize(img, (1280, 720))
cv2.imshow("Color Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
# In[2]:
img.shape
 
 
# # Blue Image
# In[4]:
 
b, g, r = cv2.split(img)
zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
blue_img = cv2.merge([b, zeros_ch, zeros_ch])
cv2.imshow("Blue Image", blue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Green Image
# In[5]:
green_img = cv2.merge([zeros_ch, g, zeros_ch])
cv2.imshow("Green Image", green_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# # Red Image
# In[6]:
 
red_img = cv2.merge([zeros_ch, zeros_ch, r])
cv2.imshow("Red Image", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# # Show Image using Index spliting and 4 image in One Window
# In[7]:
 
img = cv2.resize(img, (400,300))
red_array = np.zeros(img.shape, dtype="uint8")
red_array[:,:,2] = img[:,:,2]
green_array = np.zeros(img.shape, dtype="uint8")
green_array[:,:,1] = img[:,:,1]
blue_array = np.zeros(img.shape, dtype="uint8")
blue_array[:,:,0] = img[:,:,0]
ht1 = np.hstack((red_array, green_array))
ht2 = np.hstack((blue_array, img))
img_4 = np.vstack((ht1, ht2))
 
cv2.imshow("RGB Images", img_4)
cv2.waitKey(0)
cv2.destroyAllWindows()
