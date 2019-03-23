# -*- coding: latin-1
# ----------------------------------------------------------------- #
# -------		UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO		 ------ #
# -------				FACULTAD DE INGENIERIA				 ------ #
# -------													 ------ #
# ------- 						Vixo						 ------ #
# ----------------------------------------------------------------- #
# -------													 ------ #
# -------  Programa que simula un algoritmo genético simple  ------ #
# -------													 ------ #
# ------- El algoritmo busca el valor mínimo para la funcion ------ #
# -------						y = x^2						 ------ #
# -------		 se busca que y = 0 o lo más cercano 		 ------ #
# -------	el genotipo se forma de la siguiente manera:     ------ #
# -------													 ------ #
# -------		|signo|2^5|2^4|2^3|2^2|2^1|0.5|0.25|		 ------ #
# -------													 ------ #
# ------- se busca que el algoritmo no realice mas de 100 	 ------ #
# ------- iteraciones en caso de no encontrar la solución,	 ------ #
# ------- 			se mostrará la mejor opcion				 ------ #
# ----------------------------------------------------------------- #

import math
import random

# Contador que analiza el numero de iteraciones
v = 0

# Función de seleccion
def seleccion(arg):
	args = arg[:]
	dic = {}
	#Función para evaluar a la población
	for i in xrange(0,len(args)):
		x = 0.0
		ine = -3
		pot = 1
		for s in xrange(1,len(args[i])-2):
			if args[i][ine] == 1:
				x += math.pow(2,pot)
			pot += 1
			ine -= 1
		ine = -1
		for s in xrange(0,2):
			if args[i][ine] == 1 and ine == -1:
				x += 0.25
			if args[i][ine] == 1 and ine == -2:
				x += 0.5
			ine -= 1
		if args[i][0] == 1:
			x *= -1
		dic[i] = x
		print "En " + str(args[i]) + " El valor de x es " + str(dic[i])
	tablaordenada = ordenar(args,dic)
	#Revisamos si se encontró la solución
	if abs(dic[0]) == 0:
		print "------- La ultima poblacio es: -------------------"
		for i in args:
			print i
		print "El mejor valor fue: " + str(args[0]) + " x = " + str(dic[0])
		print "---------------------------------------------------"
		return
	return args
		
#Función para cruzar la población
def cruzar(poblacion):
	tabla = poblacion[:]
	nueva = []
	for i in xrange(0,len(tabla)-1,2):
		aux1 = tabla[i][0:4]
		aux1 += tabla[i+1][4:8]
		aux2 = tabla[i+1][0:4]
		aux2 += tabla[i][4:8]
		nueva.append(aux1)
		nueva.append(aux2)
	return nueva

#Funcion para hacer la mutación en la población
def mutar(poblacion):
	tabla = poblacion[:]
	for i in xrange(0,len(tabla)):
		#Generamos un número al azar para ver si se muta o no el genotipo
		if random.random() < .2 :
			#Generamos otro número al azar para saber que atributo será modificado
			r = random.randint(0,7)
			if tabla[i][r] == 1:
				tabla[i][r] = 0
			else:
				tabla[i][r] = 1
	return tabla

def aptitud(padres,hijos):
	poblacion = len(padres)
	poblacionTotal = padres[:]
	poblacionTotal += hijos[:]
	dic = {}
	for i in xrange(0,len(poblacionTotal)):
		x = 0.0
		ine = -3
		pot = 1
		for s in xrange(1,len(poblacionTotal[i])-2):
			if poblacionTotal[i][ine] == 1:
				x += math.pow(2,pot)
			pot += 1
			ine -= 1
		ine = -1
		for s in xrange(0,2):
			if poblacionTotal[i][ine] == 1 and ine == -1:
				x += 0.25
			if poblacionTotal[i][ine] == 1 and ine == -2:
				x += 0.5
			ine -= 1
		if poblacionTotal[i][0] == 1:
			x *= -1
		dic[i] = x
	tablaordenada = ordenar(poblacionTotal,dic)
	for i in tablaordenada:
		print i
	nueva = []
	for i in xrange(0,poblacion):
		nueva.append(tablaordenada[i])
	return nueva

#Función para ordenar la tabla
def ordenar(tablaParaOrdenar,ordenamiento):
	tabla = tablaParaOrdenar[:]
	ordenado = False
	j = []
	while not ordenado:
		ordenado = True
		for i in xrange(0,len(ordenamiento)-1):
			if abs(ordenamiento[i]) > abs(ordenamiento[i+1]):
				ordenado = False
				aux = ordenamiento[i+1]
				j = tabla[i+1]
				ordenamiento[i+1] = ordenamiento[i]
				tabla[i+1] = tabla[i]
				tabla[i] = j
				ordenamiento[i] = aux
	return tabla


# Poblacion inicial
t=[
	[1,0,1,0,0,1,1,0],
	[1,1,1,0,0,1,1,0],
	[1,0,1,1,0,1,1,0],
	[1,0,1,0,0,0,1,0],
	[1,0,1,0,0,1,1,1],
	[1,1,1,1,1,1,1,1]
]

padres = t[:]
#El algoritmo comienza
while(True):
	padres = seleccion(padres)
	#comprobamos que no se ha encontrado la solución
	if not padres:
		print v
		exit()
	#Comprobamos que no se ha llegado al número máximo de iteraciones
	if v > 15:
		print v
		print "La mejor solucion es: "
		print padres[0]
		exit()
	hijos = cruzar(padres)
	hijos = mutar(hijos)
	padres = aptitud(padres,hijos)
	print "--------------------------------------------------"
	v += 1