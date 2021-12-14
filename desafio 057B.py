# VALIDAÇÃO DE DADOS                        057B POIS FICOU DIFERENTE DO PROFESSOR
sexo = str(input("informe um sexo: [M/F]")).upper().strip()[0]
while sexo not in 'MmFf': # ENQUANTO NAO TIVER 'MmFf' no sexo repita
    sexo = str(input(" Dados inválidos. Por favor, informe novamente: "))
print("sexo {} foi registrado com sucesso!".format(sexo))