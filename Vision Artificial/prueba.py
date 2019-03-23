#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:13:26 2019

@author: rocker
"""

from miLibreria import MiLibreria
from multiprocessing import Process

lista = ['[255   0   0]', '[  0 255 255]', '[  0   0 255]']

objeto = MiLibreria('/home/rocker/Documents/I.A./Vision Artificial/fig_2.png')
objeto.histogramaOpenCV()

"""
hilo1 = Process(target=objeto.limpiarImagen, args=(lista[0], 'uno', ))
hilo2 = Process(target=objeto.limpiarImagen, args=(lista[1], 'dos', ))
hilo3 = Process(target=objeto.limpiarImagen, args=(lista[2], 'tres', ))
    
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
"""

print('ya')