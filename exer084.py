"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas 
 guardando tudo em uma lista. No final, mostre: 
 A) Quantas pessoas foram cadastradas. 
 B) Uma listagem com as pessoas mais pesadas. 
 C) Uma listagem com as pessoas mais leves.


"""
listas = []
triagem = []
maior = 0
menor = 2000

while True:
    listas.append(str(input('Qual o nome? ')))
    listas.append(int(input('Qual o peso? ')))
    triagem.append(listas[:])
    listas.clear()
    
    option = str(input('Deseja continuar [S/N]')).strip().upper()
    if option == 'N':
        break
    
for c in triagem:
    if c[1] > 65:
        print(f'{c[0]} está acima do peso {c[1]}KGs')
        
    else:
        print(f'{c[0]} está abaixo do peso {c[1]}KGs')
        
        
print(f'A quantidade de pessoas cadastradas é {len(triagem)}')
for peso in triagem:
    if peso[1] > maior:
        maior = peso[1]
    if peso[1] is None or peso[1] < menor:
        menor = peso[1]    

print(f'O menor peso é {menor}')
print(f'O maior peso é {maior}')