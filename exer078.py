lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}:\n')))
    if c == 0:
        maior = menor = lista[c]
    else: 
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]    


print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O Maior valor digitado foi {maior} nas posições', end='')
for index, c in enumerate(lista):
    if lista[index] == maior:
        print(f'{index}...')
print(f'O Menor valor digitado foi {menor} nas posições', end='')
for index, c in enumerate(lista):
    if lista[index] == menor:
        print(f'{index}...')