import cv2
from matplotlib import pyplot as plt
import utils

img = cv2.imread('/Users/jimmy_tsai/projects/car-behavioral-cloning/data/IMG/right_2018_07_22_15_46_36_005.jpg')
# img = cv2.imread('/Users/jimmy_tsai/projects/car-behavioral-cloning/data_hard/IMG/center_2018_08_03_10_36_10_295.jpg')
img = utils.random_brightness(img)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
plt.imshow(img)
plt.show()

"""
import cv2
from matplotlib import pyplot as plt

def invert_img(img):
    img = (255-img)
    return img


img = cv2.imread('/Users/jimmy_tsai/Downloads/example.png')
yuvimg = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
plt.imshow(yuvimg)

# gray = cv2.cvtColor(yuvimg, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# thresh = invert_img(thresh)

# yuvimg = cv2.cvtColor(thresh, cv2.COLOR_RGB2YUV)

# plt.imshow(thresh)
# plt.imshow('yuvimg', yuvimg)

plt.show()
"""
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('./data/IMG/right_2018_07_22_15_46_36_005.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (0,65,320,160)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
plt.imshow(img),plt.colorbar(),plt.show()
"""
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./data/IMG/center_2018_07_22_15_45_17_671.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
plt.imshow(thresh),plt.colorbar(),plt.show()
"""
