import numpy as np
import time 
import matplotlib.pyplot as plt
from multiprocessing import Process
from colorama import init, Fore, Back, Style

class Abejas:

    def __init__(self, n_Fuentes, n_Repeticiones, n_limite):
        """ Constructor. Inicializar variabes
            self.n_fuentes = SN
            self.n_repeticiones = MCN
            self.n_limite = limit
        """
        self.n_fuentes = n_Fuentes
        self.n_repeticiones = n_Repeticiones
        self.n_limite = n_limite
        
        self.flores = np.zeros((self.n_fuentes, 2), dtype=np.int64)
        self.aptitud = np.zeros((self.n_fuentes, 1), dtype=int)
        self.probabilidad = np.zeros((self.n_fuentes, 1), dtype=int)
        self.sum_probabilidad = np.zeros((self.n_fuentes, 2), dtype=float)
        self.arrayAbejas = np.zeros((int(self.n_fuentes*.45), 1), dtype=float)
        self.arrayColores = []

        self.contador = np.zeros((self.n_fuentes, 1), dtype=int)
        self.contador[:,0] = self.n_limite
        

    def llenarFlores(self):
        """ llenar las fuentes de alimento
            con un tamaño igual a n_fuentes, con (x,y)
            desde -10 hasta 100
        """ 
        self.flores = np.random.randint(0,100, size=(self.n_fuentes, 2), dtype=int)
        #print(str(self.flores[0][0])+str(self.flores[1][0]))
        #plt.plot(self.flores[:,0], self.flores[:,1], 'ro')
        #plt.show()
        #print(self.flores)

    def funcionAptitud(self):
        x = self.flores[:,0]
        y = self.flores[:,1]
        for i in range(self.n_fuentes):
            self.aptitud[i] = x[i] + y[i]
        #print(self.aptitud)

    def c_probabilidad(self):
        suma = self.aptitud.sum()
        #print('suma'+str(suma))
        self.probabilidad = np.divide(self.aptitud, suma)
        
        self.sum_probabilidad[:,0] = self.probabilidad[:,0]
        for i in range(self.n_fuentes):
            self.sum_probabilidad[i][1] = i

        self.sum_probabilidad = self.sum_probabilidad[np.argsort(self.sum_probabilidad[:,0])] 
        #print(self.sum_probabilidad)
        
        aux = 0
        for i in range(self.n_fuentes):
            self.sum_probabilidad[i][0] = aux + self.sum_probabilidad[i][0]
            aux = self.sum_probabilidad[i][0]

        np.set_printoptions(suppress=True)     
        #print(self.sum_probabilidad)
        
        #print(self.probabilidad)

    def imprimir(self):
        print(Fore.GREEN+'FLORES--APTITUD--PROBABILIDAD--CONTADOR'+Fore.RESET)
        for i in range(self.n_fuentes):
            if i in self.arrayColores:
                print(Fore.YELLOW+str(self.flores[i])+"--"+str(self.aptitud[i])+"--"
                    +str(self.probabilidad[i])+"--"+str(self.contador[i])+Fore.RESET)
            else:
                print(str(self.flores[i])+"--"+str(self.aptitud[i])+"--"
                    +str(self.probabilidad[i])+"--"+str(self.contador[i]))

    def nuevasSoluciones(self):
        abejas = int(self.n_fuentes * .45)
        self.arrayAbejas = np.random.uniform(0,1, size=(abejas))
        arraySelecionados = np.zeros((int(abejas), 1), dtype=int)
        self.arrayColores = []
        #print(self.arrayAbejas)
        #print(str(abejas))

        cont = -1
        print(self.sum_probabilidad[:,1])
        for i in self.arrayAbejas:
            for j in range(self.n_fuentes-1):
                if self.sum_probabilidad[j][0] >= i <= self.sum_probabilidad[j+1][0]:
                    cont += 1
                    aux = (int(self.sum_probabilidad[j][1]))
                    if not aux in arraySelecionados:
                        arraySelecionados[cont] = aux
                        break
                    else:
                        x = cont
                        k = 0
                        while True:
                            aux = (int(self.sum_probabilidad[k][1]))
                            if not aux in arraySelecionados:
                                arraySelecionados[x] = aux
                                break
                            else:
                                k += 1
        print(arraySelecionados)

        for i in range(abejas):
            fi = np.random.uniform(-1, 1)
            #print(str(fi))
            distinto = self.xKG(i)
            flor = int(arraySelecionados[i])
            #print('x-y'+str(distinto)+"."+str(flor))
            xN = self.flores[flor][0] + (fi * (self.flores[flor][0] + self.flores[distinto][0]))
            yN = self.flores[flor][1] + (fi * (self.flores[flor][1] + self.flores[distinto][1]))
            aN = int(xN + yN)
            if aN > int(self.aptitud[flor]):
                self.flores[flor][0] = xN
                self.flores[flor][1] = yN
                self.arrayColores.append(flor)
                print('si ',aN,"+",self.aptitud[flor])
            #else:
                #print(str('no ')+str(aN)+"+"+str(self.aptitud[flor]))

    def xKG(self, omitir):
        while True:
            aux = np.random.randint(0, self.n_fuentes-1)
            if aux != omitir:
                return aux
    
    def checarLimite(self):
        for i in range(self.n_fuentes):
            if not i in self.arrayColores:
                self.contador[i] = int(self.contador[i]) - 1
            if int(self.contador[i]) == 0:
                self.flores[i][0] = np.random.randint(0,100, dtype=int)
                self.flores[i][1] = np.random.randint(0,100, dtype=int)
                self.contador[i] = self.n_limite

    def main(self):
        self.llenarFlores()
        self.funcionAptitud()
        self.c_probabilidad()
        self.imprimir()

        for i in range(1, self.n_repeticiones):
            plt.plot(self.flores[:,0], self.flores[:,1], 'ro')
            plt.savefig('/home/rocker/Documents/I.A./S.I./'+str(i)+'.png')
            print('Repetición '+str(i+1))
            self.nuevasSoluciones()
            self.funcionAptitud()
            self.c_probabilidad()
            self.checarLimite()
            self.funcionAptitud()
            self.c_probabilidad()
            self.imprimir()


obj = Abejas(10, 20, 10)
obj.main()
