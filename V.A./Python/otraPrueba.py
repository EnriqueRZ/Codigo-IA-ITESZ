import cv2
import numpy as np
import time 
import matplotlib.pyplot as plt
from multiprocessing import Process
print(cv2.useOptimized())

class MiLibreria:

    def __init__(self, ruta):
        self.img = cv2.imread(ruta)
        self.img2 = self.img
        self.tam = np.size(self.img, 0), np.size(self.img, 1)

    def limpiarImagen(self, titulo):
        inicio = time.time()
        #self.img.sort()
        """
        #if(self.img[:, :, 0].all() != 0 and self.img[:, :, 1].all() != 0 and self.img[:, :, 2].all() != 255):
        #if(self.img[:, :, 0].any() != 0 and self.img[:, :, 1].any() != 0 and self.img[:, :, 2].any() != 255):
        if(self.img[:, :, 0:0:0].any() != 0):
            self.img[:, :, 0] = 255
        if(self.img[:, :, 1].any() != 0):
            self.img[:, :, 1] = 255    
        if(self.img[:, :, 2].any() != 255):
            self.img[:, :, 2] = 255
        #if(self.img[:, :, 1].any() != 0):
        #    self.img[:, :, 1] = 255
        #if(self.img[:, :, 2].any() != 255):
        #    self.img[:, :, 2] = 255
            #self.img[:, :, 1] = 0
            #self.img[:, :, 2] = 0
        """
        c = (0, 0, 255)
        indices = np.where(np.all(self.img == c, axis=-1))
        print(indices)

        for i in indices:
            for j in indices:
                print(self.img[i, j])
        
        if()
       # uno = self.img[:,:,0:1]
        #self.img[self.img[:, :, 0] < 255, 0] = 255
        #self.img[self.img[:, :, 1] < 255, 1] = 255
        #self.img[self.img[:, :, 2] != 255, 2] = 255

        cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/'+str(titulo)+'.png', self.img)
        fin = time.time()
        print(str(fin-inicio))

obejto = MiLibreria('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
obejto.limpiarImagen('12345')