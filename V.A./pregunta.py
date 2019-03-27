import numpy as np
import cv2
from matplotlib import pyplot as plt

def sobelOperator(img):
    container = np.copy(img)
    size = container.shape
    for i in range(1, size[0] - 1):
        for j in range(1, size[1] - 1):
            gx = (img[i - 1][j - 1] + 2*img[i][j - 1] + img[i + 1][j - 1]) - (img[i - 1][j + 1] + 2*img[i][j + 1] + img[i + 1][j + 1])
            gy = (img[i - 1][j - 1] + 2*img[i - 1][j] + img[i - 1][j + 1]) - (img[i + 1][j - 1] + 2*img[i + 1][j] + img[i + 1][j + 1])
            container[i][j] = min(255, np.sqrt(gx**2 + gy**2))
    return container

img = cv2.cvtColor(cv2.imread('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png'), cv2.COLOR_BGR2GRAY)
img = sobelOperator(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
plt.imshow(img)
plt.show()
"""
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

start_time = time.time()
img = cv2.imread('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
tam = np.size(img, 0), np.size(img, 1)
target_BGR = [255, 0, 0]


for i in range(tam[0]):
    for j in range(tam[1]):
        if not np.array_equal(target_BGR, img[i, j]):
            img[i, j] = [255, 255, 255]


lower = np.array([0, 0, 255], dtype = "uint8")
upper = np.array([0, 0, 255], dtype = "uint8")
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)

#img[mask == 255] = (255, 255, 255)

print(time.time() - start_time)

##laplacian = cv2.Laplacian(output,cv2.CV_64F)
#sobelx = cv2.Sobel(output,cv2.CV_64F,1,0,ksize=5)  # x
#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/out.png', output)
plt.imshow(output)
plt.show()
plt.scatter(..)
plt.contour(..)
"""