from random import randint
from time import sleep
from operator import itemgetter
ranking = dict()
jogo = {'JOGADOR 1': randint(1, 6),
        'JOGADOR 2': randint(1, 6),
        'JOGADOR 3': randint(1, 6),
        'JOGADOR 4': randint(1, 6)}

print('valores sorteados: ')
for k, v in jogo.items():
    print(f' {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True) # itemgetter vai classificar pelo que voce escolher
for i, v in enumerate(ranking):
    print(f" {i+1}º Lugar: {v[0]} com {v[1]}. ")
    sleep(1)
