#usuario colocar um numero entre 0 e 20 e o programa escreve qual foi que ele escreveu
cont = ('zero', 'um', 'dois','três','Quatro','Cinco','seis','sete','oito','nove','dez','onze','doze','treze',
'catorze','quinze','desseceis','dessesete','dezoito','dezenove','vinte')
esc=''
while True:
    while True: # validar se o numero que o usuario digitou esta dentro do que pedi
        num = int(input("Digite um numero entre 0 e 20: "))
        if 0 <= num <=20: # condição entre 0 a 20
            break # para o esse while True pois a condição está certa
        print("Tente Novamente.", end='')
    print(f" voce digitou o numero {cont[num]}") # cont é a tupla e vai mostrar o indice que o usuario digitou no num
    esc=input("Você deseja continuar [S/N]: ").upper().strip()[0]
    if esc in 'sS':
        continue
    elif esc in 'nN':
        print("PROGRAMA FINALIZADO!")
        break