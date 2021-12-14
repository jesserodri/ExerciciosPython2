def fatorial(num, show=False):
    '''
    > calula o fatorial de um numero.
    param n: o numero a ser calculado
    param show: mostra ou nao a conta
    return: mostra o valor da conta
    '''
    f = 1
    for i in range(num,0,-1):
        if show:
            print(i, end=" ")
            if i>1:
                print(f' x ', end="")
            else:
                print(" = ", end='')
        f*=i
    return f




n = int(input("informe :"))
print(fatorial(n, show=False))