#organizar a tupla e mostrar o que eu quero
tabela_brasileirão = ('palmeiras', 'bragantino', 'athletico-PR', 'atletico-MG', 'fortaleza', 'bahia', 'santos',
'atletico-GO','ceara','fluminense','flamengo','juventudo','corinthians','internacional','america-MG', 'são paulo',
'sport recife','cuiába', 'chapecoence','grêmio')
print("\nos 5 primeiros colocados são :")
#print(f"os 5 primeiros times são {times[0:5]}")            #os que estão em comentario é mais simples
for cont in range(0,5):
    print(f"{tabela_brasileirão[cont]}", end=" - " )
    if cont == 4:
        print("fim")

print("\nos 4 Ultimos colocados são:")
#print(f"os 4 ultimos times são {times[-4:]}")
for cont2 in range(16,20):
    print(f"{tabela_brasileirão[cont2]}", end=" - ")
    if cont2 == 19:
        print("fim")

print("\nOs times organizados por ordem alfabetica:")
#print(f"times em ordem alfabética: {sorted(times)}")
for cont3 in range(0, len(tabela_brasileirão)):
     print(f"{sorted(tabela_brasileirão)[cont3]}", end=" - ")

print(f"\n\na Chapecoence está em {tabela_brasileirão.index('chapecoence')+1}  ")