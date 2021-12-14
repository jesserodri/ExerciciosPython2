#menu de ação para dois numeros

import time

num1 = num2 =0
esc = 0
print("_-"*20)
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
print("_-" * 20)

while esc != 5:

    time.sleep(1)
    print("-="*20)
    print("ESCOLHA UMA OPERAÇÃO")
    print("[1] SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\n")
    print("-=" * 20)
    esc = int(input("ESCOLHA: "))
    if esc == 1:
        print("A SOMA ENTRE  {} e {} É: {}".format(num1, num2, num1 + num2))
    elif esc == 2:
        print("A MULTIPLICAÇÃO ENTRE  {} e {} É: {}".format(num1, num2, num1 * num2))
    elif esc == 3:
        if num1 > num2: #jeito diferente (num1 > num2)
            #maior = num1
            print("O PRIMEIRO NUMERO {} É MAIOR QUE O SEGUNDO NUMERO {} ".format(num1, num2))
        else:
            # maior = num2
            print("O SEGUNDO NUMERO {} É MAIOR QUE O PRIMEIRO NUMERO {}".format(num2 ,num1))
        #print(" entre {} E {} o maior é {}".format()
    elif esc == 4:
        num1 = int(input("digite o primeiro numero: "))
        num2 = int(input("digite o segundo numero: "))
    elif esc == 5:
        print(" O PROGRAMA FOI FINALIZADO!")
        time.sleep(0.5)
        break
    else:
        print("Opção invalida. Por favor, tente novamente.")
        continue
