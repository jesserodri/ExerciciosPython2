s = ''
c = True
cont = 1
while c == True:  # iniciei com uma variavel qualquer
    print("{} Pessoa: ".format(cont))
    s = str(input("digite o seu sexo [M/F]: ")).lower().strip()[0] # o [0] pega somente a primeira letra
    if s == 'm': # esse if é para o sexo masculino
        cont += 1
        print("você é do sexo masculino")
        continue        # para continuar o programa sem precisar reiniciar
    if s == 'f': # esse if é para o sexo feminino
        cont += 1
        print("você é do sexo feminino")
        continue        # para continuar o programa sem precisar reiniciar
    if s != 'm' or 'f': # esse if é para quando for digitado algo errado
        print("voce digitou errado, por favor tente novamente!")
        # não precisa colocar continue aqui pois a condição está como falsa ou seja ela vai repetir