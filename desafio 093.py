import os
jogadores = dict()
qtd_gols = list()
gols_total = 0
jogadores['nome']= input("Informe o nome do jogador: ")
jogadores['qtd_partidas'] = int(input("informe o numero de partidas desse jogador: "))
for i in range(1,jogadores['qtd_partidas']+1):
    c = int( input(f"Informe a quantidade de gols no {i}º jogo: "))
    qtd_gols.append(c)
jogadores['gols'] = qtd_gols

for v,i in enumerate(qtd_gols):
    gols_total+=i


jogadores['total'] = gols_total
print(jogadores)
print("-="*50)
print(f'no campo nome tem o valor {jogadores["nome"]}')
print(f'o campo gols tem o valor {jogadores["gols"]}')
print(f'o campo total tem o valor {jogadores["total"]}')
print("-="*50)
print(f"O jogador {jogadores['nome']} jogou {jogadores['qtd_partidas']} Partidas.")
for c,v in enumerate(qtd_gols):
    if v == 1:
        print(f"    =>  Na partida {c+1}, fez {v} gol.")
    elif v < 1:
        print(f"    =>  Na partida {c+1}, fez Nenhum gol.")
    else:
        print(f"    =>  Na partida {c + 1}, fez {v} gols.")
print(f"Foi um total de {jogadores['total']} gols ")

''' prof guanabara fez
jogador = dict()
partidas = list()

jogador['nome'] = input("Nome do jogador: ")
tot = int(input(f"Quantas partidas o {jogador['nome']} jogou: "))
for c in range(1, tot+1):
    partidas.append(int(input(f"    Quantos gols na partida {c}: ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*50)
print(jogador)
print('-='*50)
#a partir daqui vai apresentar os valores detalhadamente.
for k, v  in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print('-=' * 50)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for i, v in enumerate(jogador['gols']):
    print(f"      => Na partida {i+1}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")
'''