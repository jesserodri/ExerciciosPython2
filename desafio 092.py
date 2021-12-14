from datetime import datetime
dici = dict()




dici['nome'] = str(input("Digite seu nome: "))
nasc=int(input("Digite seu ano de nascimento: "))
dici['idade'] = datetime.now().year - nasc
dici['carte_trab'] = int(input("Digite carteira de trabalho: "))

if dici['carte_trab'] == 0:
    print(' '*10,"Dados")
    print("*"*50)
    print(dici)
    print("*" * 50)
if dici['carte_trab'] != 0:
    dici['ano_contr'] = int(input("Digite o ano de contratação"))
    dici['salario'] = int(input("digite o salario"))
    dici['aposentadoria'] = datetime.now().year + 35
if dici['salario'] > 0 :
    dici['contribuição_mensal'] = dici['salario'] * 11 / 100
if dici['salario'] > 1000:
    dici['contribuição_mensal'] = dici['salario'] *20 / 100
#__________________________________________________________
print(dici)
print()
print(f'Nome tem o valor:{dici["nome"]}' )
print(f"Idade tem o  valor {dici['idade']}")
print(f'CTPS tem o valor de {dici["carte_trab"]}')
print(f'Ano de contratação tem o valor de {dici["ano_contr"]}')
print(f"salario tem o valor de R${dici['salario']}")
print(f"A sua contribuição mensal com base em seu salario é: R${dici['contribuição_mensal']}")
print(f'Aposentadoria tem o valor de {(dici["aposentadoria"])}')