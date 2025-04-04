entry = int(input('Digite um número para taboada: '))
for c in range(1, 11):
    soma = entry * c
    print(f'{entry} x {c} = {soma}')