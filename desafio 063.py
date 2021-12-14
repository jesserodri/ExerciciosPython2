cont = 3                        # PRECISEI DE AJUDA PARA TERMINAR
n = int(input("digite quantos elementos voce deseja ver: "))
n1 = 0
n2 = 1

print("{} > {}".format(n1,n2), end=' > ')
while cont <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(n3, end=' > ')
print("FIM")