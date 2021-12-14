#Jogo Adivinhação 2.0    #feito pelo professor (incrementei algumas coisas )
import random
import time
acertou = False
palp = 1
computador = random.randint(0,10)

print("Olá sou seu computador.. Acabei de pensar em um numero entre 0 e 10")
time.sleep(0.5)
print("Será que voce consegue adivinha ?")

while not acertou: # usando operador logico para inicar o enquanto
    jogador = int(input("Qual é o seu palpite: "))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente novamente.")
        elif jogador > computador:
            print("menos... Tente novamente. ")

        palp += 1
if palp == 1:
    print("Acertou com {} tentativa, Parabens".format(palp))
else:
    print("Acertou com {} tentativas, Parabens".format(palp))