matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para [{i}, {c}]: "))
print("-=" * 35)
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[i][c]:^5}]", end='')
        if matriz[i][c] % 2 == 0:
           spar += matriz[i][c] 
    print()
print("-=" * 35)
print(f"A soma dos valores PARES é {spar}")
for c in range(0, 3):
    scol += matriz[c][2]
print(f"A soma da terceira coluna é {scol}")
for i in range(0, 3):
    if i == 0:
        mai = matriz[1][i]
    elif matriz[1][i] > mai:
        mai = matriz[1][i]
print(f"A soma da coluna do meio é {mai}")