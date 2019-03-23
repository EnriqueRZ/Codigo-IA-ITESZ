# -*- coding: utf-8 -*-
#'/home/rocker/Pictures/fig_2.png'

"""
Created on Wed Mar 13 18:17:42 2019

@author: rocker
"""
import cv2
import numpy as np
import time 
import matplotlib.pyplot as plt
from multiprocessing import Process

class MiLibreria:

    def __init__(self, ruta):
        self.img = cv2.imread(ruta)
        self.tam = np.size(self.img, 0), np.size(self.img, 1)

    """
        MÉTODO QUE RECIBE UNA CADENA EN CÓDIGO RGB "[R G B]" Y UN TÍTULO PARA 
        ALMACENAR LA IMAGEN. 

        BÁSICAMENTE LIMPIA LA IMAGEN DEJANDO SOLO EL COLOR DADO EN LA CADENA Y 
        CUBRIENDO TODO LO DEMÁS CON BLANCO    
    """
    def limpiarImagen(self, cadena, titulo):
        inicio = time.time()
        self.img.sort()
        for i in range(self.tam[0]):
            for j in range(self.tam[1]):
                
                if(str(self.img[i, j]) != cadena):
                    self.img[i, j] = [255, 255, 255]
                    
        cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/'+str(titulo)+'.png', self.img)
        fin = time.time()
        print(str(fin-inicio))
        #plt.imshow(self.img, cmap='gray')
        #plt.show()

    def limpiarImagenMejorada(self, cadena, titulo):
        target_BGR = [[255, 0, 0], [0, 255, 255], [0, 0, 255]]
        inicio = time.time()

        for i in range(self.tam[0]):
            for j in range(self.tam[1]):
                if not np.array_equal(target_BGR[cadena], self.img[i, j]):
                    self.img[i, j] = [255, 255, 255]

        cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/'+str(titulo)+'.png', self.img)

        print(time.time()-inicio)

    """
        MÉTODO PARA OBTENER "A MANO" LA CANTIDAD DE REPETICIONES DE LOS
        VALORES RGB EN UNA IMAGEN, PARA POSTERIORMENTE GENERAR UN HISTOGRAMA
    """
    def numRepeticiones(self):
        diccionario = {}
        for i in range(self.tam[0]):
            for j in range(self.tam[1]):

                rgb = str(self.img[i, j])
                if(rgb in diccionario):
                    diccionario[rgb] += 1
                else:
                    diccionario[rgb] = 1

        self.generarHistrograma(diccionario)
    
    def generarHistrograma(self, diccionario):
        plt.bar(list(diccionario.keys()), diccionario.values(), color='g')
        plt.savefig('/home/rocker/Documents/I.A./Vision Artificial/histo.png')

    def histogramaOpenCV(self):
        color = ('b','g','r')
        for i,col in enumerate(color):
            histr = cv2.calcHist([self.img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        plt.show()


lista = ['[255   0   0]', '[  0 255 255]', '[  0   0 255]']

objeto = MiLibreria('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
#objeto.histogramaOpenCV()

hilo1 = Process(target=objeto.limpiarImagenMejorada, args=(0, 'uno', ))
hilo2 = Process(target=objeto.limpiarImagenMejorada, args=(1, 'dos', ))
hilo3 = Process(target=objeto.limpiarImagenMejorada, args=(2, 'tres', ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
