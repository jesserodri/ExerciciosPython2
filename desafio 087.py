matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = mai = somaCol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] =int(input(f"digite um valor para [{l},{c}]: "))

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
        if matriz [l][c] % 2 == 0:
            somaPar+= matriz[l][c]
    print()

print(f' a soma dos pares é {somaPar}')

for l in range(0,3):
    somaCol +=matriz[l][2]
print(f"a soma dos valores da terceira coluna é {somaCol}.")

for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'o maior valor da segunda linha é {mai}.')

