#faça um programa que jogue impar ou par
import time
import random

tot = numJ= cont = 0
esc= ''
print("-_"*20)
print("\t\tJOGO DO IMPAR OU PAR")
print("-_"*20)
while True:
    cont+=1
    esc = int(input("\nEcolha 1-[PAR] OU 2-[IMPAR]: "))
    if esc == 1:
        numJ = int(input("Digite um valor:"))
        numC =random.randint(0,10)
        tot = numC + numJ
        time.sleep(0.5)
        print(f"O computador escolheu {numC} e o total foi {tot}")
        tot = tot % 2
        if tot == 0:
            time.sleep(0.5)
            print("parabens Você ganhou!")
            continue
        if tot == 1:
            time.sleep(0.5)
            print("Não foi dessa vez... Adeus!")
            break
    elif esc == 2:
        numJ = int(input("DIgite um valor:"))
        numC = random.randint(0,10)
        tot = numC + numJ
        time.sleep(0.5)
        print(f"O computador escolheu {numC} e o total foi {tot}")
        tot = tot % 2
        if tot == 0:
            time.sleep(0.5)
            print("Você perdeu, talvez na proxima!")
            break
        if tot == 1:
            time.sleep(0.5)
            print("Parabens VOCE ganhou!")
            continue
    else:
        print("Você digitou errado. Por favor, Tente novamente!")
        continue
cont-=1
if cont == 0:
    print(f"Você Não ganhou nenhuma vez ")
elif cont == 1:
    print(f"voce ganhou {cont} vez ")
else:
    print(f"voce ganhou {cont} vezes ")
