import datetime

#busca o ano atual do sistema
date = datetime.date.today()
ano = int(date.strftime("%Y"))

def voto(anoNasc):
    idade =  ano - anoNasc
    if idade >=18 and idade < 65 :
        return f"Pessoas com {idade} anos, VOTO OBRIGATORIO"
    elif idade < 18:
        return f"{idade}anos, Não tem idade para votar"
    else:
        return f"{idade} anos, VOTO OPCIONAL"
print("--------------------------------------")
Nasc = int(input("Digite em que ano nasceu: "))
print(voto(Nasc))
