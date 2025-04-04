print('Vários números com flag')
cont = soma = 0
while True:
    try:
        number = int(input(f'Digite número: [999 para PARAR] '))
        if number == 999:
            break
        else:
            cont += 1
            soma += number
                    
    except ValueError as erro:
        print(f'ERRO {erro}')
        

print(f'Você digitou {cont}x e a soma dos números foi {soma}')


    