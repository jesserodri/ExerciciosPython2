def soma(l,c):
    lin()
    print("Dimensões do terreno definidas: ")
    print(f"Largura: {l}")
    print(f"Comprimento: {c}")
    r = l * c
    lin()
    print(f"O Resultado foi : {r}m²")

def lin():
    print('-'*30)
lin()
print('Controle de terreno')
lin()


l = float(input("Largura(m): "))
c = float(input("Comprimento(m): "))
soma(a,l)

