from time import sleep

def contador(i,f,p):
    if p==0:
        p=1
    elif p < 0:
        p*=p
    cont = i
    if cont < f:
        while cont <= f:
            print(cont, end=' ')
            cont+=p
            sleep(0.3)
        print('FIM')
    elif cont > f:
        while cont >=f:
            print(cont, end=" ")
            cont-=p
            sleep(0.3)
        print('FIM')



contador(1,10,1)
contador(10,0,2)
print("Sua vez agora, informe o inicio:")
ini = int(input("> "))
print("Informe o fim:")
fim = int(input("> "))
print("informe o passo:")
pas = int(input("> "))
contador(ini, fim, pas)