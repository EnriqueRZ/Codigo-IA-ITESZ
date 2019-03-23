import cv2
import numpy as np
import time

start_time = time.time()
img = cv2.imread('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
tam = np.size(img, 0), np.size(img, 1)
target_BGR = [255, 0, 0]

for i in range(tam[0]):
    for j in range(tam[1]):
        if not np.array_equal(target_BGR, img[i, j]):
            img[i, j] = [255, 255, 255]

cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/out.png', img)

print(time.time() - start_time)

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
data = np.array(img)

r1, g1, b1 = 0, 255, 255 # Original value
r2, g2, b2 = 255, 255, 255 # Value that we want to replace it with

red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
data[:,:,:3][mask] = [r2, g2, b2]

r1, g1, b1 = 0, 0, 255 # Original value
r2, g2, b2 = 255, 255, 255 # Value that we want to replace it with

red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
mask = (red == r1) & (green == g1) & (blue == b1)
data[:,:,:3][mask] = [r2, g2, b2]

plt.imshow(data, interpolation='nearest')
plt.show()
#im = Image.fromarray(data)
#im.save('fig1_modified.png')
"""