# gera 5 numeros e mostra o menor e o maior
from random import randint
menor = maior = 0
cont = 1
num= (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
#exemplo (8,0,2,3,7)

for n in num:
    print(n)
    if cont == 1:
        menor = maior = n

    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
    cont += 1
print("menor:",menor)
print("maior:",maior)

#outra maneira BEM MAIS FACIL É USAR O MIN e MAX
print(f"O menor valor é {min(num)}")
print(f"O maior  valor é {max(num)}")



