#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:17:42 2019

@author: rocker
INTENTANDO USAR HILOS DEMONIOS
"""
import threading, time
import cv2
import numpy as np
from multiprocessing import Process

inicio = time.time()

img = cv2.imread('/home/rocker/Pictures/fig_2.png')
tam = np.size(img, 0), np.size(img, 1)
lista = ['[255   0   0]', '[  0 255 255]', '[  0   0 255]']

def recorrer(cadena, nHilo):
    for i in range(tam[0]):
        for j in range(tam[1]):
            if(str(img[i, j]) != cadena):
                img[i, j] = [255, 255, 255]
                
    cv2.imwrite('/home/rocker/Pictures/figura_prueba'+str(nHilo)+'.png', img)
    fin = time.time()
    print(fin-inicio)
    

hilo1 = Process(target=recorrer, args=(lista[0], 'uno'))

hilo2 = Process(target=recorrer, args=(lista[1], 'dos'))

hilo3 = Process(target=recorrer, args=(lista[2], 'tres'))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
