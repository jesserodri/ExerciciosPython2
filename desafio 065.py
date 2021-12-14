cont = n = soma= maior = menor = 0 # precisei de ajuda
esc = 'S'
while esc == 'S':
    n =  int(input("digite um numero: "))
    esc = str(input('deseja continuar ? [S/N] ')).upper().strip()
    soma += n # realizar a soma dos numeros digitados no loop
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print("A media dos {} numeros foi {}".format(cont,media))
print(" O menor numero digitado foi {} e o maior foi {}".format(menor, maior))