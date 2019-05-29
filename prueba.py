lista = [10, 12, 4, 90, 23, 34, 12, 56, 1, 0]
print(lista)
for j in range(len(lista)):
    for i in range(len(lista)-1): 
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
        print(lista)