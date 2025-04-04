soma = 0
while True:
    valor = int(input('Digite um valor: [999 para PARAR]'))
    if valor == 999:
        break
    else:
        soma += valor
print(soma)