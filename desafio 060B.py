# RESOLVENDO O DESAFIO 60 METODO DO PROFESSOR (2 FORMAS)
'''     1 forma MAIS FACIL
from math import factorial
n = int(input("digite um numero para calcular seu fatorial: "))
f = factorial(n)
print('o fatorial de {} é {}'.format(n,f))
'''
f = 1 # corresponde ao fatorial, precisa começar com 1 pois 0 ele nao multiplica por nada
n = int(input("digite um numero para calcular seu fatorial: "))
c = n
print("Calculando {}! = ".format(n), end='')
while c > 0:
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')# if simplicado
    f *= c
    c -=1
print('{}'.format(f))