galera = list()
pessoa = dict()
cont = media = soma =  0
while True:
    cont+=1
    pessoa.clear()
    pessoa["nome"] = input(f"Digite o nome da {cont}ª pessoa:")
    while True:
        pessoa["sexo"] = input(f"Digite o seu sexo [M/F]").upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print("voce Digitou algo de errado, tente novamente!")
    pessoa["idade"] = int(input("Digite a idade : "))
    soma+= pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = input("Deseja continuar [S/N]: ").upper()[0]
        if resp in 'SN':
            break
        print("RESPONDA SOMENTE S OU N. TENTE NOVAMENTE!")
    if resp == 'N':
         break
print(galera)
print("-="*40)
print(f"Ao todo foram cadastrados {len(galera)} pessoas.")
media = soma / len(galera)
print(f"a media de idade é de {media:5.2f} anos.")
print("as mulheres cadastradas foram: ",end= ' ')
for p in galera:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('lista de pessoas que estão acima da media:')
for p in galera:
    if p['idade']>=media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< encerrado>>")