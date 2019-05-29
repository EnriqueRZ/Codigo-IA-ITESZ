# coding=utf-8
import numpy as np 

class RedNeuronal:

    def __init__(self):
        #Datos datos como input y lo esperado
        self.datos_in = np.array([[0,0], [0,1], [1,0], [1,1]])
        self.datos_out = np.array([[0], [1], [1], [0]])

        self.wi = np.random.uniform(size=(1, 3))
        self.wj = np.random.uniform(size=(1, 3))
        self.wk = np.random.uniform(size=(1, 3))
        self.biasj = np.random.uniform(size=(1, 3))
        self.biask = np.random.uniform(size=(1, 1))

        self.iteraciones = 80000
        self.lr = 0.1

    def sigmoide(self, x):
        return 1 / (1 + np.exp(-x))

    def derivada_sigmoide(self, x):
        return x * (1 - x)
    
    def calculoNet(self, wi, wj, x, y, bias):
        return ((wi * x) + (wj * y)) + bias 

    def entrenar(self):
        print('WI')
        print(*self.wi)
        print('WJ')
        print(*self.wj)
        print('BIAS J')
        print(*self.biasj)
        print('W K')
        print(*self.wk)
        print('BIAS K')
        print(*self.biask)
        for i in range(self.iteraciones):
            #print('Iteración #'+str(i))
            for j in range(4):
                #Parte 1
                red11 = self.calculoNet(self.wi[0][0], self.wj[0][0], self.datos_in[j][0],
                                    self.datos_in[j][1], self.biasj[0][0])
                red12 = self.calculoNet(self.wi[0][1], self.wj[0][1], self.datos_in[j][0],
                                    self.datos_in[j][1], self.biasj[0][1])
                red13 = self.calculoNet(self.wi[0][2], self.wj[0][2], self.datos_in[j][0],
                                    self.datos_in[j][1], self.biasj[0][2])
                #Parte 2
                sig11 = self.sigmoide(red11)
                sig12 = self.sigmoide(red12)
                sig13 = self.sigmoide(red13)
                
                #Parte 3
                red14 = (sig11 * self.wk[0][0]) + (sig12 * self.wk[0][1]) + (sig13 * self.wk[0][2]) + self.biask
                sig14 = self.sigmoide(red14)

                #B.P.
                error = self.datos_out[j] - sig14
                errorglobal = error * (sig14 * (1 - sig14))
                if(i == 0 or i == self.iteraciones-1):
                    #print('Iteración #'+str(i))
                    print('Error: '+str(self.datos_in[j][0])+"-"+str(self.datos_in[j][1])+' = '+str(error))
                
                #deltas
                delta11 = (sig11 * (1 - sig11)) * (errorglobal * self.wk[0][0]) 
                delta12 = (sig12 * (1 - sig12)) * (errorglobal * self.wk[0][1]) 
                delta13 = (sig13 * (1 - sig13)) * (errorglobal * self.wk[0][2]) 

                self.wk[0][0] += errorglobal * sig11 * self.lr
                self.wk[0][1] += errorglobal * sig12 * self.lr
                self.wk[0][2] += errorglobal * sig13 * self.lr
                self.biask += errorglobal * self.lr

                self.wi[0][0] += delta11 * self.datos_in[j][0] * self.lr
                self.wi[0][1] += delta12 * self.datos_in[j][0] * self.lr
                self.wi[0][2] += delta13 * self.datos_in[j][0] * self.lr

                self.wj[0][0] += delta11 * self.datos_in[j][1] * self.lr
                self.wj[0][1] += delta12 * self.datos_in[j][1] * self.lr
                self.wj[0][2] += delta13 * self.datos_in[j][1] * self.lr
                
                self.biasj[0][0] += delta11 * self.lr
                self.biasj[0][1] += delta12 * self.lr
                self.biasj[0][2] += delta13 * self.lr

        print('WI')
        print(*self.wi)
        print('WJ')
        print(*self.wj)
        print('BIAS J')
        print(*self.biasj)
        print('W K')
        print(*self.wk)
        print('BIAS K')
        print(*self.biask)

    def probar(self, x, y):
        red11 = self.calculoNet(self.wi[0][0], self.wj[0][0], x,
                            y, self.biasj[0][0])
        red12 = self.calculoNet(self.wi[0][1], self.wj[0][1], x,
                            y, self.biasj[0][1])
        red13 = self.calculoNet(self.wi[0][2], self.wj[0][2], x,
                            y, self.biasj[0][2])

        sig11 = self.sigmoide(red11)
        sig12 = self.sigmoide(red12)
        sig13 = self.sigmoide(red13)
    
        red14 = (sig11 * self.wk[0][0]) + (sig12 * self.wk[0][1]) + (sig13 * self.wk[0][2]) + self.biask
        sig14 = self.sigmoide(red14)
        print(str(x)+"-"+str(y)+" = "+str(sig14))

    def imprimir(self):
        print(str(self.datos_in))
        print(str(self.datos_in[1][1]))
        print(str(self.wi[0][0]))
        print(str(self.wj))
        print(str(self.biasj))
        print(str(self.biask))
        

obj = RedNeuronal()
obj.entrenar()
while True:
    print("Ingrese x, y = ")
    x = float(input())
    y = float(input())
    obj.probar(x, y)
#print(obj.derivada_sigmoide(2.21))     