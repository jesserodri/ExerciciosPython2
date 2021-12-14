#cadastro de idade e sexo com validação de informação
ida = mais18 = hom = mulh_ate20  =0
sexo = ''
esc = 'S'
cont = 1
print('\n','-'*10,"Cadastro de pessoas",'-'*10)
while esc == 'S':
    print(f"\n{cont}ª Pessoa:")
    ida= int(input("Digite a idade: "))
    sexo = str(input("digite o sexo [M/F]: ")).upper().strip()
    if sexo == 'M':
        hom +=1
    elif sexo == 'F':
        if ida < 20:
            mulh_ate20 += 1
    while sexo not in 'mMfF':
        sexo = str(input("digite o sexo [M/F]")).upper().strip()
    cont += 1
    #aqui faz a contagem de quantas pessoas tem mais de 18
    if cont == 1:
        if ida > 18:
            mais18 +=1
    else:
        if ida > 18:
            mais18 +=1
    esc = str(input("Quer continuar [S/N]: ")).upper().strip()
    if esc == 'n':
        break
    else:
        while esc not in 'sSnN':
            esc = str(input("Você digitou uma opção invalida. Tente novamente\nQuer continuar: ")).upper().strip()
    print("-"*30)


print(f"\nA quantidade de pessoas que tem mais de 18 é {mais18}\n o total de homens foi {hom}")
print(f"a quantidade de mulheres com menos de 20 é : {mulh_ate20}")
