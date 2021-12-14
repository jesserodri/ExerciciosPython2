def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("voce nao digitou um numero.")
        if ok:
            break
    return valor


n = leiaInt("informe apenas um numero inteiro: ")
print(f'Voce acabou de digitar o numero {n}')



