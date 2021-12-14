# FATORIAR UM NUMERO

num = int(input("Escolha um numero para fatoriar: "))
numInicial = num
resul = num * (num - 1)
while num != 2:
    num -= 1
    resul = resul * (num - 1)

print("O RESULTADO DO FATORIAL DE {} É {}".format(numInicial,resul))


# VEJA O 60B QUE É MUITO MAIS FACIL




