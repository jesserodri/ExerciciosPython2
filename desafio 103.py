def ficha(nomeJogador='', gols = 0):

    if nomeJogador == '':
        nomeJogador = '<DESCONHECIDO>'
        if gols == 0:
            return f'O jogador {nomeJogador} não tem nenhum gol no campeonato'
        elif gols >= 1:
            return f'O jogador {nomeJogador} tem {gols} gols feitos no campeonato'
    else:
        nomeJogador = nome
        if gols == 0:
            return f'O jogador {nomeJogador} Não tem nenhum gol feito no campeonato'
        elif gols >= 1:
            return  f'O jogador {nomeJogador} tem {gols} gols feitos no campeonato'

nome = input("informe o nome: ")
gols = int(input("informe os gols: "))
print(ficha(nome, gols))