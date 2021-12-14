# digite 4 numeros e trate os dados que foi digitados salvando em uma tupla
contpar = contimpar = 0
num = (int(input("digite um numero:")),
       int(input("digite outro numero:")),
       int(input("digite mais um numero:")),
       int(input("digite o ultimo numero:"))) # foi colocado ( ) a mais para ela virar uma variavel composta(tupla)

print(f"voce digitou os valores{num}")
print(f"O valor 9 apareceu {num.count(9)} vezes ")
if 3 in num:
    print(f"o valor 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("o valor 3 não foi digitado!")
for n in num:
    if n % 2 == 0:
        contpar+=1
    else:
        contimpar+=1

print(f" Tem {contpar} numeros pares.")






