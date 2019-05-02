import numpy as np
import time 
import matplotlib.pyplot as plt
from multiprocessing import Process
from colorama import init, Fore, Back, Style
import matplotlib.animation as animation

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
        self.flores = np.random.randint(0,1000, size=(self.n_fuentes, 2), dtype=int)

    def funcionAptitud(self):
        """Calcular la función de aptitud para todas las (x,y)
        """
        x = self.flores[:,0]
        y = self.flores[:,1]
        for i in range(self.n_fuentes):
            self.aptitud[i] = x[i] + y[i]

    def c_probabilidad(self):
        suma = self.aptitud.sum()
        self.probabilidad = np.divide(self.aptitud, suma)
        
        self.sum_probabilidad[:,0] = self.probabilidad[:,0]
        for i in range(self.n_fuentes):
            self.sum_probabilidad[i][1] = i

        self.sum_probabilidad = self.sum_probabilidad[np.argsort(self.sum_probabilidad[:,0])] 
        
        aux = 0
        for i in range(self.n_fuentes):
            self.sum_probabilidad[i][0] = aux + self.sum_probabilidad[i][0]
            aux = self.sum_probabilidad[i][0]

        np.set_printoptions(suppress=True)     

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
        arraySelecionados = []
        self.arrayColores = []
        bandera = False
        for i in range(abejas):
            while True:
                posible = np.random.uniform(0,1)
                for j in range(self.n_fuentes-1):
                    if self.sum_probabilidad[j][0] >= posible <= self.sum_probabilidad[j+1][0]:
                        aux = (int(self.sum_probabilidad[j][1]))

                        if not aux in arraySelecionados:
                            arraySelecionados.append(aux)
                            bandera = True
                            break
                        else:
                            bandera = False
                            break

                if bandera == True:
                    break
                    
        fi = np.random.uniform(-1, 1)
        for i in range(len(arraySelecionados)):
            
            distinto = self.xKG(i)
            flor = int(arraySelecionados[i])
            
            xN = self.flores[flor][0] + (fi * (self.flores[flor][0] - self.flores[distinto][0]))
            yN = self.flores[flor][1] + (fi * (self.flores[flor][1] - self.flores[distinto][1]))
            aN = int(xN + yN)

            if aN > int(self.aptitud[flor]):
                self.flores[flor][0] = abs(xN)
                self.flores[flor][1] = abs(yN)
                self.arrayColores.append(flor)
                #print('si ',aN,"+",self.aptitud[flor])

    def xKG(self, omitir):
        """
        while True:
            posible = np.random.uniform(0,1)
            for j in range(self.n_fuentes-1):
                if self.sum_probabilidad[j][0] >= posible <= self.sum_probabilidad[j+1][0]:
                    aux = (int(self.sum_probabilidad[j][1]))
                    #print('aux'+str(aux))
                    return aux
              
            
        """
        while True:
            aux = np.random.randint(0, self.n_fuentes-1)
            if aux != omitir:
                return aux
        
    
    def checarLimite(self):
        for i in range(self.n_fuentes):
            if not i in self.arrayColores:
                self.contador[i] = int(self.contador[i]) - 1
            if int(self.contador[i]) == 0:
                fi = np.random.uniform(-1, 1)
                distinto = self.xKG(i)

                xN = self.flores[i][0] + (fi * (self.flores[i][0] - self.flores[distinto][0]))
                yN = self.flores[i][1] + (fi * (self.flores[i][1] - self.flores[distinto][1]))
                aN = int(xN + yN)

                self.flores[i][0] = abs(xN)
                self.flores[i][1] = abs(yN)
                self.contador[i] = self.n_limite


    def main(self):
        self.llenarFlores()
        self.funcionAptitud()
        self.c_probabilidad()
        self.imprimir()
        #plt.figure(figsize=(10,10))
        for i in range(1, self.n_repeticiones):
            plt.clf()
            plt.plot(self.flores[:,0], self.flores[:,1], '+', color='red', markersize=5)
            plt.savefig('/home/rocker/Documents/I.A./S.I./'+str(i)+'.png')
            
            print('Repetición '+str(i+1))
            self.nuevasSoluciones()
            self.funcionAptitud()
            self.c_probabilidad()
            self.checarLimite()
            self.funcionAptitud()
            self.c_probabilidad()
            self.imprimir()

        #ani = animation.ArtistAnimation(self.fig, ims, interval=50, blit=True,
         #                       repeat_delay=1000)
        #ani.save('/home/rocker/Documents/I.A./S.I./dynamic_images.mp4')
        #plt.show()

obj = Abejas(100, 50, 5)
obj.main()
