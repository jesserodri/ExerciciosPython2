#digiter diversos numeros somar e mostrar ( flag é o 999)
n = s = cont =0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    cont += 1
    s += n
print(f"Total de numeros digitados foi {cont} e a soma entre eles foi de {s} ")