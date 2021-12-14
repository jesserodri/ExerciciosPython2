
din  = 0
ced = 50
totalced = 0
din = int(input(" que valor deseja sacar :"))
total = din

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f"total de {totalced} celulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break




