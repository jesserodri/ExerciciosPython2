soma=0
lista=[[],[]]
'''num = [[],[]] # lista com duas listas dentro
valor = 0# variavel serve para pegar o valor cadastrado
for c in range(0,8):
    valor = int(input(f"digite o {c}º valor: "))
    if valor % 2 ==0: # se o valor for par
        num[0].append(valor) # ele manda para a lista [0] da lista num
    else:
        num[1].append(valor) # aqui ele manda para a lista [1] da lista num
print(f'todos os valores : {num}')
num[0].sort()
num[1].sort()
print(f'os valores pares digitados foram{num[0]}')
print(f'os valores impares digitados foram {num[1]}')

'''
for n in range(1, 5):
    lista[0].append(int(input(f"Digite a {n}ª nota: ")))
for i, c in enumerate(lista[0]):# maneira mais facil de fazer
    print(f" A {i+1}ªNota  é: {c}")
    soma +=c
resul = soma / 4
lista[1] = resul
# maneira mais longa de fazer
#lista[1] = (lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3]) / 4
print(f' A média das notas cadastradas é: {lista[1]}')