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
from scipy.spatial import distance_matrix

class MiLibreria:

    def __init__(self, ruta):
        self.img = cv2.imread(ruta)
        self.tam = np.size(self.img, 0), np.size(self.img, 1)
        self.arraySobel = []

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

    def limpiarImagenMejorada(self, cadena, titulo):
        target_BGR = [[255, 0, 0], [0, 255, 255], [0, 0, 255]]
        inicio = time.time()

        for i in range(self.tam[0]):
            for j in range(self.tam[1]):
                if not np.array_equal(target_BGR[cadena], self.img[i, j]):
                    self.img[i, j] = [255, 255, 255]

        cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/'+str(titulo)+'.png', self.img)

        print(time.time()-inicio)

    def limpiarImagenM2(self, pos, titulo):
        color = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])

        start_time = time.time()
        lower = np.array(color[pos], dtype = "uint8")
        upper = np.array(color[pos], dtype = "uint8")

        mask = cv2.inRange(self.img, lower, upper)
        output = cv2.bitwise_and(self.img, self.img, mask = mask)
        #output[mask == 0] = (255, 255, 255)
        cv2.imwrite('/home/rocker/Documents/I.A./V.A./'+titulo+'.png', output)

        print(time.time() - start_time)

    """
        MÉTODO PARA APLICAR EL OPERADOR DE SOBEL
        NOS REGRESA UNA MATRIZ DONDE ALMACENA LAS POSICIONES 
        DE LOS CIRCULOS
    """
    def sobel(self, img):

        container = np.copy(img)
        size = np.size(container, 0), np.size(container, 1)
        cont = 0

        for i in range(1, size[0]-1):

            for j in range(1, size[1]-1):

                gx = (-img[i-1][j-1]-2*img[i][j-1]-img[i+1][j-1])+(img[i-1][j+1]+2*img[i][j+1]+img[i+1][j+1])
                gy = (-img[i-1][j-1]-2*img[i-1][j]-img[i-1][j+1])+(img[i+1][j-1]+2*img[i+1][j]+img[i+1][j+1])

                if 30 < np.sqrt(gx**2 + gy**2) < 230: 
                    container[i][j] = 255
                    cont += 1

                else:
                    container[i][j] = 0

                if gx > 10 and gy > 10:
                    self.arraySobel.append([i,j])

        return self.arraySobel

    """
        MÉTODO PARA APLICAR EL ALGORITMO DE K-MEANS 
        NOS RETORNA UN ARRAY CON LA POSICIÓN DE LOS CENTROS
        Y UN ARREGLO QUE CLASIFICA QUÉ PUNTOS PERTENECE A CADA CENTRO
    """
    def kmeans(self, data, k):
        x = np.size(data, 0)
        y = np.size(data, 1)

        initial_centroids = np.random.choice(x, k, replace=False)
        centroids = data[initial_centroids]

        centroids_old = np.zeros((k, y))
        cluster_assignments = np.zeros(x)

        while (centroids_old != centroids).any():
            print('si')
            print(str(centroids))
            centroids_old = centroids.copy()

            dist_matrix = distance_matrix(data, centroids, p=2)

            for i in np.arange(x):
                d = dist_matrix[i]
                closest_centroid = (np.where(d == np.min(d)))[0][0]

                cluster_assignments[i] = closest_centroid

            for j in np.arange(k):
                Xj = data[cluster_assignments == j]
                centroids[j] = np.apply_along_axis(np.mean, axis=0, arr=Xj)

        return (centroids, cluster_assignments)

    def calculoArea(self, xC, xData, color):
        radio = 0
        bandera = False
        arrayAreas = []
        for y in range(xC.shape[0]):
            
            for j in xData:
                if j == xC[y]:
                    bandera = True
                    radio += 1

            if bandera == True:
                area = 3.1416 * ((radio/2)**2)
                print('Area '+str(color)+' = '+str(area))
                radio = 0
                bandera = False
    
    def metodos(self, ruta, data, k, color):
        img = cv2.cvtColor(cv2.imread(ruta), cv2.COLOR_BGR2GRAY)
        img = self.sobel(img)

        data = np.copy(img)
        k_means_result = self.kmeans(data, k)
        centroids = k_means_result[0]

        xData = data[:,0]
        yData = data[:,1]

        xData = np.array(xData)
        yData = np.array(yData)

        xC = centroids[:,0]
        yC = centroids[:,1]
        
        self.calculoArea(xC, xData, color)

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
        color = ('b')#,'g','r')
        for i,col in enumerate(color):
            histr = cv2.calcHist([self.img],[i],None,[256],[0,256])
            cv2.imwrite('/home/rocker/Documents/I.A./Vision Artificial/his.png', histr)
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        plt.show()


objeto = MiLibreria('/home/rocker/Documents/I.A./V.A./fig-p.png')
#objeto.histogramaOpenCV()

hilo1 = Process(target=objeto.limpiarImagenM2, args=(0, 'uno', ))
hilo2 = Process(target=objeto.limpiarImagenM2, args=(1, 'dos', ))
hilo3 = Process(target=objeto.limpiarImagenM2, args=(2, 'tres', ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()