#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:13:26 2019

@author: rocker
"""

from miLibreria import MiLibreria
from multiprocessing import Process

ruta = '/home/rocker/Documents/I.A./V.A./'
ruta1 = '/home/rocker/Documents/I.A./V.A./Pruebas/'
nombreColor = [ 'azul', 'verde', 'rojo']
extension = '.png'
k = 1

objeto = MiLibreria(ruta1+'ima3'+extension)

hilo1 = Process(target=objeto.limpiarImagenM2, args=(0, ruta1, nombreColor[0], ))
hilo2 = Process(target=objeto.limpiarImagenM2, args=(1, ruta1, nombreColor[1], ))
hilo3 = Process(target=objeto.limpiarImagenM2, args=(2, ruta1, nombreColor[2], ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
"""

"""
hilo1 = Process(target=objeto.metodos, args=(ruta1+str(nombreColor[0])+extension, k, nombreColor[0], ))
hilo2 = Process(target=objeto.metodos, args=(ruta1+str(nombreColor[1])+extension, k, nombreColor[1], ))
hilo3 = Process(target=objeto.metodos, args=(ruta1+str(nombreColor[2])+extension, k, nombreColor[2], ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()


