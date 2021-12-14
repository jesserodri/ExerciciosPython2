#adiciona valor a uma lista mas nao repete o valor (como se fosse uma ID)
lista=[]
while True:
    n = int(input("Digite um valor: "))
    if n not in lista: # se n(valor que colocou) not in (não estiver em) lista:
        lista.append(n) #adiciona n em lista
        print("adicionado com sucesso")
    else:
        print("Ja possui esse valor, Não vou adicionar")
    esc = input("Deseja continuar[S/N]").upper()
    if esc in 'Ss':
        continue
    if esc in 'Nn':
        break
    else:
        esc= input("Digitou algo errado, Tente novamente: ")
lista.sort()
print(f"{lista}")