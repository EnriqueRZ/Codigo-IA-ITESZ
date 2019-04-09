import cv2
import numpy as np

img = cv2.imread('/home/rocker/Documents/I.A./V.A./uno.png', 0)
ret,thresh = cv2.threshold(img,255,255,255)

image, contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

for i in contours:
    area = cv2.contourArea(i)
    print('AREA='+str(area))
#print('cnt='+str(cnt))
#print(str(np.size(cnt,0)))
#print('M='+str(M))
