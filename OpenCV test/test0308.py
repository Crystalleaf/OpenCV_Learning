import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread("d:\\1.jpg",0)

# display image
#cv2.imshow("image", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#cv2.imshow("image", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.imwrite("D:\\2.png", img)

plt.imshow(img, cmap = "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()