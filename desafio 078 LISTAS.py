#acrescenta valores em uma lista e...
valores = [] #lista criada
maior = menor = 0 #criando variavel simples para guardar os dados
print('-_'* 25)
for v in range(0, 5): #for para repetir 5 valores digitados pelo usuario
   valores.append(int(input((f"Digite um valor para a posição {v}: ")))) # o que foi lido append(vai guardar na lista)
   if v == 0:
      maior = menor = valores[v]
   else:
      if valores[v] > maior:
         maior = valores[v]
      if valores[v] < menor:
         menor = valores[v]

print('-_'* 25)
print('voce digitou os valores:', valores)

print(f'O maior valor digitado foi {maior} e apareceu na posição', end=" ")
for i, va in enumerate(valores): # faz a varredura e verifica as informações na variavel valores
   if va == maior: # condição para mostrar somente o valor que for maior da varredura
      print(f" {i}..", end=" ")
print()
print(f" O menor valor digitado foi {menor} e está na posição ", end=" ")
for i, va in enumerate(valores): # mesma coisa que acima, porem para o menor valor
   if va == menor:
      print(f"{i}..", end=" ")
      print


