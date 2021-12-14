import random
from time import sleep

numeros = list()

def maior(*num):
    '''for i in range(0,5):
        numeros.append(random.randint(1,101))'''
    print("ANALISANDO OS NUMEROS..")
    for i in num:
        print(i, end=' ')
        sleep(0.3)
    print(f"foram informados {len(num)} numeros.")

    mai = 0
    for i, v in enumerate(num):
        if i == 1:
            mai = v
        else:
            if v > mai:
                mai = v
    print(f"O maior numero informado foi: {mai}")
    print("-="*20)


maior(20,30,25,102,85)
maior(20,10)
maior(86,103,1102)