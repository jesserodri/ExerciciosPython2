ficha= list()

while True:

    nome= str(input("digite o nome do aluno: "))
    not1 = float(input("digite a primeira nota: "))
    not2 = float(input("digite a segunda nota: "))
    media = (not1 + not2) / 2
    ficha.append([nome,[not1,not2],media])
    resp= str(input("quer continuar S/N: "))
    if resp in 'nN':
        break

print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input("mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]:1.f}')

