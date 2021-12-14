numeros = list()
maior = menor = 0
for c in range(0,5):
    n =int(input("Digite um valor: "))
    if c == 0 or n > numeros[len(numeros)-1]: #1 opção
        numeros.append(n)
        print("adicionado ao final da lista")
   #elif n > numeros[len(numeros)-1]: # ultimo elemente len(numeros)-1   # 2opção
     #   list.append(n)
    else:
        pos = 0  # serve para varrer o vetor inteiro(o for)
        while pos < len(numeros): # vai de pos(0) ate a ultima posição
            if n <= numeros[pos]:# se o n for menorOUigual a numeros[pos]
                print(f"adicionado na posição{pos} da lista...")
                numeros.insert(pos, n) # insere na pos, valor n
                break
            pos += 1
print(f"os valores digitados em ordem foram {numeros}")



