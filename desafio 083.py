expr = input('digite a expressão: ')
pilha = list()

for simb in expr: #varre para achar o simbolo
    if simb == '(': # se tem um ( abrindo
        pilha.append('(') #  coloque-a em uma lista chamada pilha
    elif simb ==')':# se tem um ) fechando..
        if len(pilha) > 0: #se a pilha for acima de 0
            pilha.pop() # voce fecha ela
        else:# se nao (tiver nada na lista)
            pilha.append(')')# coloca ) e para o programa
            break
if len(pilha) == 0: # se a pilha estiver em com nenhum item, ela é valida
    print("sua expressão está valida!")
else: # se não, ela está errada
    print("sua expressão não está valida!")