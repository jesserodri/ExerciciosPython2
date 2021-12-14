import random
from time import sleep
numeros = list()

def sorteia():
    for i in range(0,5):
        numeros.append(random.randint(1,101))
    print("SORTEANDO 5 VALORES NA LISTA:", end=' ')
    for i in numeros:
        print(i, end=' ')
        sleep(0.3)
    print("pronto!")

def somaPar():
    par = 0
    for i in numeros:
        if i % 2 == 0:
            par+=i
    print("SOMANDO OS VALORES PARES DA LISTA",numeros, end=' ')
    print("TEMOS: ",par)


sorteia()
somaPar()
