# leia um numero e mostre sua tabuada (loop ate usuario digirar numero negativo)
n = e = s = cont=0

while True:
    # aqui vou pedir para o usuario informar o numero que deseja
    n = int(input("Digite o numero que deseja exibir sua tabuada: "))
    if n < 0:
        print("Programa finalizado!")
        break
    #for c in range(1,11) tambem funciona assim
    while cont <= 10:
        s = n * cont
        print(f"{n}x{cont} = {s}")
        cont += 1
#a incrementação aqui está sendo usada para "resetar" a variavel cont para que no proximo laço ele faça tudo de novo
    cont -= 10