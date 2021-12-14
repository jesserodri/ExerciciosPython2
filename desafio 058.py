# jogo da adivinhação 2.0

import random
cont = 1
numMa= random.randint(0,10)
numEs= int(input("Adivinhe o numero entre 0 a 10 que a maquina escolheu: "))
while numMa != numEs:
    cont += 1
    print("você errou!")
    numEs = int(input("Adivinhe novamente: "))
if cont == 1:
    print("Você acertou ! E usou Apenas {} tentativa\n  MEU PARABENS".format(cont))
else:
    print("Você acertou ! E usou {} tentativas".format((cont)))