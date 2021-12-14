pessoas = list()
dados = list() #dados temporarios
tot = mai = men = 0

while True:
    tot += 1
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        mai = men = 0
    else:
        if dados[1] > mai:
            mai= dados[1]       # pega o maior peso com base nos dados informados
        if dados[1] < men:
            men = dados[1]       # pega o menor peso com base nos dados informados
    pessoas.append(dados[:]) # coloquei uma copia em pessoas
    dados.clear()# importante
    resp = input("Deseja continuar[S/N]: ").upper()
    if resp in 'S':
        continue
    if resp in 'N':
        break

print(f"o maior peso foi de {mai}KG. peso de ", end= ' ')
for p in pessoas:
    if p[1] == mai:#p1 são os pesos
        print(f'[{p[0]}]', end = ' ') #p0 são os nomes

print()

print(f'o menor peso foi de {men}KG')
for p in pessoas:
    if p[1] == men:
        print(f"[{p[0]}]", end=' ')





