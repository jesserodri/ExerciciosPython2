lista  = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    esc=input("Deseja continuar[S/N]: ").upper()
    if esc in 'sS':
        continue
    if esc in 'nN':
        break
    else:
        print(("Você digitou algo de errado, Tente novamente!"))
        esc = ("Deseja continuar[S/N]: ").upper()
listaPar = []
for c in lista:
    if c % 2 == 0:
        listaPar.append(c)

listaImpar = []
for c in lista:
    if c % 2 == 1:
        listaImpar.append(c)


print(f"Lista completa {lista}")
print(f"Lista dos pares{listaPar}")
print(f"Lista dos impares{listaImpar}")