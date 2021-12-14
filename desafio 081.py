lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    esc = input("Deseja continuar[S/N]: ").upper()
    if esc in 'sS':
        continue
    elif esc in 'nN':
        break
    else:
        print("Não reconhecido, Por favor. Tente novamente")
        esc= input("Deseja continuar[S/N]: ")
print('-_'*30)
print("DADOS: ")
if len(lista) == 1:
    print(f'Foi digitado apenas {len(lista)} numero')
else:
    print(f"Foram digitados {len(lista)} numeros")
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print("O valor 5 está na lista,", end=' ')
    for i, c in enumerate(lista):
        if c == 5:
            print(f"Na Posição {i} ")
else:
    print('O valor 5 Não está na lista')

