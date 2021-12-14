#cadastro de nome e preço do produto com validação de informação

nome = nomebara = ""
prec = cont = soma = maisde = barat= 0
esc = "s"
while True:
    cont +=1
    print(f"{cont}º Produto")
    nome = input("digite o nome do produto: ").strip()
    prec = float(input ("Qual é o seu preço: "))
    esc = input("Deseja Cadastrar mais [S/N]").lower().strip()
    soma += prec
    if prec > 1000:
        maisde +=1
    if cont == 1 or prec < barat:
        barat = prec
        nomebara = nome
    else:
        if prec < barat:
            barat = prec
            nomebara = nome
    if esc == 'n':
        break
    elif esc == 's':
        continue
    else :
        while esc not in 'sSnN':
            esc = input("Você digitou uma opção invalida. Por favor, Tente novamente:  ")
print(f"Total de gasto da compra foi R${soma:.2f}")
if maisde == 1:
    print(f"No Total foi {maisde} produto que custou mais de R$1000 Reais.")
else :
    print(f"No Total foram {maisde} produtos que custaram mais de R$1000 Reais.")
print(f" O nome do Produto mais barato é {nomebara} custando R${barat:.2f}.")
