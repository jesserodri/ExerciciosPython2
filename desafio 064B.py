# Feito pelo professor ( MAIS PRATICO E FACIL)

n = cont = soma = 0
n = int(input("digite um numero [999 para]: "))  # essa linha foi duplicada pela que tem dentro do while
# -------------------------------------------- # assim 0 999 vai ser considerado pelo while um numero de saida
while n != 999:
    soma += n
    cont += 1
    n = int(input("digite um numero [999 para]: "))
print("voce digitou {} numeros e a soma entre ele foi {}".format(cont, soma))
