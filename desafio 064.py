# FUNCIONA MAIS A GAMBIARRA FOI GRANDE
cont = n1 = n2= 0
esc = 0
print("para sair do loop digite 999")
while esc < 999:
    n1= int(input("digite: "))
    esc = n1
    resul = n1 + n2
    n1 = n2
    n2 = resul
    cont += 1
cont -= 1
resul = resul - 999
print("Você colocou {} numeros e o resultado da soma deles foi {}".format(cont, resul))

