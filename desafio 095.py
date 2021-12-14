time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = input("Nome do jogador: ")
    tot = int(input(f"Quantas partidas o {jogador['nome']} jogou: "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"    Quantos gols na partida {c}: ")))
    jogador['gols'] = partidas[:] # como partidas é uma lista da para usar [:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy()) # como jogador é um dicionario entao tem que usar .copy
    while True:
        resp = input("Quer continuar [S/N]: ").upper()[0]
        if resp in 'SN':
            break
        print("Opa. Somente Sim ou Não")
    if resp == 'N':
        break
print('-=' * 50)

#cabeçalho da tabela
print("cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()

print('-=' * 50)
for i, j in enumerate(time):
    print(f"{i:>2} ", end="")
    for d in j.values():
        print(f"{str(d):<15}", end='')
    print()
while True:
    busca= int(input("Mostrar dados de qual jogador ?"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe o jogador com o codigo {busca}")
    else:
        print(f" -- levantamento do jogador {time[busca]['nome']}:  ")
        for i, g in enumerate(time[busca]['gols']):
            if g == 0:
                print(f"    no jogo {i+1} Não fez nenhum Gol")
            if g == 1:
                print(f"    no jogo {i + 1}  fez {g} gol")
            else:
                print(f"    No jogo {i+1} Fez {g} gols")
        print("--"*60)
print("volte sempre")