escola= dict()

escola['nome'] = str(input("Informe o nome do aluno: "))
escola['nota'] = int(input("informe a nota do aluno: "))

if escola['nota'] >= 7:
    escola['aprovação'] = 'Aprovado'
elif escola['nota'] < 7:
    escola['aprovação'] = 'Reprovado'

print(f'O nome do aluno é {escola["nome"]}')
print(f'a nota do aluno é {escola["nota"]}')
print(f'Com base na nota o aluno está {escola["aprovação"]}')