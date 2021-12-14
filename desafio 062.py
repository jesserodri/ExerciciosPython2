t = int(input("digite o primeiro termo: "))         #precisei de ajuda para fazer esse
r = int(input("digite a razão: "))
cont = 1
total = 0
mais = 10

print("\033[0:31m {} \033[0;0m".format(t), end='> ')
while mais !=0:
    total = total + mais
    while cont <= total:
        t = t + r
        cont += 1
        print(t,  end=' > ')
    print("\033[0:31mPausa \033[0;0m")
    mais = int(input("Você quer ver mais quantos termos: "))
print("total de termos mostrados foram {} termos".format(total))






