listagem = ('lápis', 1.75,
            'boracha', 2,
            'caderno',15,
            'caneta', 2.90,
            'estoujo', 4.50,
            'mochila', 50)
print("-"*40)
print(f"{'LISTAGEM DE PREÇO':^40}")# :^40 (CENTRALIZA E 40 DE ESPAÇAMENTO)
print("-"*40)
for item in range(0, len(listagem)):
    if item % 2 == 1:
        listagem[item]
    if item % 2 == 0:
        print(f"{listagem[item]:.<30}", end='')# :.<30(PONTOS ANTES DO ESPAÇAMENTO DE 30 A ESQUERDA)
    else :
        print(f"R${listagem[item]:>7.2f}")# :>7 (A DIREITA 7 DE ESPAÇAMENTO ) .2f(DUAS CASAS DECIMAIS)
