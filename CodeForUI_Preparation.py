import os
import numpy as np
import cv2
# import matplotlib.pyplot as plt
from utility import *


dir_path = "./images/"

original_images =[]
NUCE_images =[]

img_w = 350 #image width
img_h = 350 #image height

img = cv2.imread(dir_path+'1.jpeg')
	# img = cv2.resize(img,(img_w,img_h))
# original_images.append(img)

nuce_img = NUCE(img)  
cv2.imshow('output',nuce_img)
cv2.waitKey(0)
# NUCE_images.append(nuce_img)

# for im in os.listdir(dir_path):

	

# 	cv2.imwrite("./results/"+im.split('/')[-1], nuce_img)


# fig, ax = plt.subplots(4,2,figsize=(6, 9), constrained_layout = False)
# ax[0][0].set_title("Original Image")
# ax[0][1].set_title("NUCE Image")

# for i in range(4):

# 	ax[i][0].imshow(cv2.cv2tColor(original_images[i], cv2.COLOR_BGR2RGB),cmap='gray')
# 	ax[i][0].axis('off')

# 	ax[i][1].imshow(cv2.cv2tColor(NUCE_images[i], cv2.COLOR_BGR2RGB), cmap='gray')
# 	ax[i][1].axis('off')

# fig.tight_layout()
# plt.savefig("./results/output.jpg")
# plt.show()
print('done')
