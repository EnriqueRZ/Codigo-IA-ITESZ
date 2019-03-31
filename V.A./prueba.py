#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:13:26 2019

@author: rocker
"""

from miLibreria import MiLibreria
from multiprocessing import Process

ruta = '/home/rocker/Documents/I.A./V.A./'
nombreColor = [ 'azul', 'verde', 'rojo']

objeto = MiLibreria(ruta+'fig-p.png')

hilo1 = Process(target=objeto.limpiarImagenM2, args=(0, nombreColor[0], ))
hilo2 = Process(target=objeto.limpiarImagenM2, args=(1, nombreColor[1], ))
hilo3 = Process(target=objeto.limpiarImagenM2, args=(2, nombreColor[2], ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
"""

"""
hilo1 = Process(target=objeto.metodos, args=(0, nombreColor[0], ))
hilo2 = Process(target=objeto.metodos, args=(1, nombreColor[1], ))
hilo3 = Process(target=objeto.metodos, args=(2, nombreColor[2], ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()


