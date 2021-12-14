t = int(input("digite o primeiro termo: "))
r = int(input("digite a razão: "))
resul = 0
cont = 1
print("\033[0:31m {} \033[0;0m".format(t), end='> ')
while cont <= 10:
    t = t + r
    cont += 1
    print(t,  end=' > ')
print("\033[0:31mAcabou \033[0;0m")