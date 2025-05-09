def fatorial(n, infor=False):
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos.")
    resultado = 1
    for i in range(n, 0, -1):
        if infor:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= i
    return resultado

print(fatorial(5, True))