# -*- coding: latin-1
#X=41 Y=21
#X=2 Y=37
#X=23 Y=30
#X=58 Y=11
#X=50 Y=16
#X=9 Y=35
#x=55 y=13
#x=60 y=10
import random
import math

porGana = 0
cont = 0
x = 0
y = 0
lx = []
ly = []
fenoX = []
fenoY = []
resL = []
ganadores = []
gx = []
gy = []
gr = []
bandera = False
    """
        Método ordenar arreglo
    """
def ordenar_min():
  for xd in range(len(resL)):
    for m in range(len(resL)):
      if resL[xd] < resL[m]:
        tmp = resL[m]
        resL[m] = resL[xd]
        resL[xd] = tmp

        tmp1 = lx[m]
        #print str(len(resL))
        #print "error "+str(m)+"-"+str(xd)
        lx[m] = lx[xd]
        lx[xd] = tmp1

        tmp2 = ly[m]
        ly[m] = ly[xd]
        ly[xd] = tmp2

def seleccion():
    dif = []
    ganadores = []
    gx = []
    gy = []
    gr = []
    global resL, cont
    print ('Seleccion')
    #print str(len(resL))
    for i in range(len(resL)):
        if(resL[i] < 150):
            dif.append(150-resL[i])
        else:
            dif.append(resL[i])

    for i in range(numIndividuos):
        #print 'Diferencia = '+str(dif[i])
        if(dif[i] > 150):
            for j in range(10):
                i = i-1
                tem = dif[i]
                ganadores.append(tem)
                tem = lx[i]
                gx.append(tem)
                fenoX.append(binarizar(tem))
                tem = ly[i]
                gy.append(tem)
                fenoY.append(binarizar(tem))
                tem = resL[i]
                gr.append(tem)
                
            break
    for i in range(len(ganadores)):
        print ('Ganadores='+str(ganadores[i])+" : "+str(gx[i])+"-"+str(gy[i])+"-"+str(fenoX[i])+"-"+str(fenoY[i])+"-"+str(gr[i]))

    #resL = []
    for i in range(numIndividuos):
        uno = random.randint(0, 9)
        if(len(gx) == 0):
            print ('Algo')
        #print "error : "+str(uno)+str(len(gx))
        dos = random.randint(0, 9)
        #print str(dos)+str(len(gy))
        tem = gx[uno]
        lx[i] = tem
        tem = gy[dos]
        ly[i] = tem
        resL[i] = (operacion(int(lx[i]), int(ly[i])))

    #print "Tamñ "+str(len(resL))
    cont += 1
    print ('Población '+str(cont))
    ordenar_min()

#def cruza():
 #   lx = []
  #  ly = []
   # resL = []
    #global gx
    
def porcentajePoblacion(numIndividuos):
    porGana = int(.30 * numIndividuos)

def operacion(x, y):
    result = int(x + (3*y) + (math.sqrt(x**2 + y**2)))
    return result

def evaluar():
    global resL, bandera
    for i in range(len(resL)):
        if resL[i] == 150:
            print ('Solución x = '+str(lx[i])+" y = "+str(ly[i]))
            bandera = True
            break

def indiviuos(min, max):
    x = random.randint(min, max)

    return x

def binarizar(num):
    xs = str("{0:b}".format(int(num)))
    d = xs.zfill(8)

    return d

def generarPoblacion():
    global cont, resL, lx, ly
    resL = []
    lx = []
    ly = []
    for y in range(numIndividuos):
        n = indiviuos(1, 60)
        lx.append(n)
        #fenoX.append(m)
        n = indiviuos(1, 60)
        ly.append(n)
        #fenoY.append(m)
        resL.append(operacion(int(lx[y]), int(ly[y])))

    cont += 1
    print ('Población '+str(cont))
    ordenar_min()
    imprimir()

def main():
    global bandera
    generarPoblacion()
    if(evaluar() == True):
        bandera == True
    for i in range(numPoblaciones):
        imprimir()
        if(cont == numPoblaciones):
            print ('Solución no encontrada')
            break
        seleccion()
        #cruza()
        evaluar() 
        print ('Evaluar = '+str(bandera))
        if(bandera == True):
            break


def imprimir():
    for i in range(numIndividuos):
       print (str(lx[i])+"-"+str(ly[i])+"-"+str(resL[i]))

print ('BIENVENIDO')
print ('Ingresa el número de individuos por población: ')
numIndividuos = int(input())
print ('Ingresa el número de poblaciones: ')
numPoblaciones = int(input())

main()


