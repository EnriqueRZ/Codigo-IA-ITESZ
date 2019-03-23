# -*- coding: latin-1
import random
import math
class Genetic:
    """
        --
    """
    def __init__(self, nPobla, nIndiv):
        self.nPobla = nPobla
        self.nIndiv = nIndiv
        self.pGana = int(.30*nIndiv)
        self.pMutar = math.ceil(.30*self.pGana)
        self.cont = 0
        self.lx = []
        self.ly = []
        self.fenoX = []
        self.fenoY = []
        self.resT = []
        self.resL = []
        self.ganadores = []
        self.gx = []
        self.gy = []
        self.gr = []
        self.pp1 = []
        self.bandera = False

    def ordenar_min(self):
        for xd in range(len(self.resL)):
            for m in range(len(self.resL)):
                if self.resL[xd] < self.resL[m]:
                    tmp = self.resL[m]
                    self.resL[m] = self.resL[xd]
                    self.resL[xd] = tmp

                    tmp1 = self.lx[m]
                    self.lx[m] = self.lx[xd]
                    self.lx[xd] = tmp1

                    tmp2 = self.ly[m]
                    self.ly[m] = self.ly[xd]
                    self.ly[xd] = tmp2
    
    def seleccion(self):
        dif = []
        self.ganadores = []
        self.gx = []
        self.gy = []
        self.gr = []
        print ('Seleccion')
      
        for i in range(self.pGana):
            self.ganadores.append(self.resL[i])
            tem = self.lx[i]
            self.gx.append(tem)
            self.fenoX.append(self.binarizar(tem))
            tem = self.ly[i]
            self.gy.append(tem)
            self.fenoY.append(self.binarizar(tem))
            tem = self.resL[i]
            self.gr.append(tem)
        
        self.mutacion()

        for i in range(len(self.ganadores)):
            print ('Ganador='+str(self.ganadores[i])+" : "+
            str(self.gx[i])+"-"+str(self.gy[i])+"-"+str(self.fenoX[i])+
            "-"+str(self.fenoY[i])+"-"+str(self.gr[i]))

        self.evaluar() 
        self.dividirUno()

        self.cont += 1
        print ('Población '+str(self.cont))
        self.ordenar_min()
        
    def mutacion(self):
        for i in range(self.pMutar):
            num = random.randint(0, self.pGana-1)
            padre = random.randint(0, 1)
            if(padre == 0):
                pos = (len(self.fenoX[num])-1) - random.randint(0, 8)
                saux = self.fenoX[num]
                if(saux[pos] == '0'):
                    cam = '1'
                else:
                    cam = '0'
                aux = saux[:pos-1] + cam + saux[pos+1:]
                self.fenoX[num] = aux
                numN = int(aux, 2)
                self.gx[num] = numN
            else:
                pos = (len(self.fenoY[num])-1) - random.randint(0, 8)
                saux = self.fenoY[num]
                if(saux[pos] == '0'):
                    cam = '1'
                else:
                    cam = '0'
                    aux = saux[:pos-1] + cam + saux[pos+1:]
                    self.fenoY[num] = aux
                    numN = int(aux, 2)
                    self.gy[num] = numN
            
            self.resT[num] = (self.operacion(str(self.gx[num]), str(self.gy[num])))
            self.resL[num] = (abs(150-self.resT[num]))
            self.ganadores[num] = self.resL[num]
            self.gr[num] = self.resL[num]


    def nuevaPoblacion(self):
        self.lx = []
        self.ly = []
        self.resL = []
        self.resT = []
        for i in range(self.nIndiv):
            n = random.uniform(0,1)
            self.lx.append(self.saberPadre(n))
            n = random.uniform(0,1)
            self.ly.append(self.saberPadre(n))

            self.resT.append(self.operacion(str(self.lx[i]), str(self.ly[i])))
            self.resL.append(abs(150-self.resT[i]))

        self.ordenar_min()
     
    def saberPadre(self, num):
        for i in range(len(self.pp1)):
            if(num <= self.pp1[i]):
                aux = random.randint(0, 1)
                if(aux == 0):
                    return self.gx[i]
                else:
                    return self.gy[i]


    def dividirUno(self):
        self.pp1 = []
        suma = self.sumalista(self.ganadores)
        for i in range(len(self.ganadores)):
            aux = ((150-self.ganadores[i])*1)/suma
            if(i > 0):
                self.pp1.append(self.pp1[i-1] + round(aux, 5))
            else:
                self.pp1.append(round(aux, 5))
        print ('--')

    def sumalista(self, lista):
        suma = 0
        for i in lista:
            suma = suma + (150-i)
        return abs(suma)

    def operacion(self, x, y):
        return int(int(x) + (3*int(y)) + int((math.sqrt(int(x)**2 + int(y)**2))))

    def evaluar(self):
        for i in range(len(self.resL)):
            if self.resL[i] == 0:
                print ('Solución x = '+str(self.lx[i])+" y = "+str(self.ly[i]))
                self.bandera = True
                break

    def indiviuos(self, min, max):
        x = random.randint(min, max)

        return x

    def binarizar(self, num):
        xs = str("{0:b}".format(int(num)))
        d = xs.zfill(32)
        auc = len(d)

        return d

    def generarPoblacion(self):
        for y in range(self.nIndiv):
            n = self.indiviuos(1, 150)
            self.lx.append(n)
            n = self.indiviuos(1, 150)
            self.ly.append(n)
            self.resT.append(self.operacion(int(self.lx[y]), int(self.ly[y])))
            self.resL.append(abs(150-self.resT[y]))

        self.cont += 1
        print ('Población '+str(self.cont))
        self.ordenar_min()

    def main(self):
        self.generarPoblacion()
        if(self.evaluar() == True):
            self.bandera == True
        for i in range(self.nPobla):
            if(self.cont == self.nPobla):
                print ('Solución no encontrada')
                break
            self.seleccion()
            print ('Evaluar = '+str(self.bandera))
            if(self.bandera == True):
                break
            else:
                self.nuevaPoblacion()


    def imprimir(self):
        print ("X - Y - DIFERENCIA")
        for i in range(self.nIndiv):
            print (str(self.lx[i])+"-"+str(self.ly[i])+"-"+str(self.resL[i]))

print ('BIENVENIDO')
print ('Ingresa el número de individuos por población: ')
numIndividuos = int(input())
print ('Ingresa el número de poblaciones: ')
numPoblaciones = int(input())

algo = Genetic(numPoblaciones, numIndividuos)
algo.main()
