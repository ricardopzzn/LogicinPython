print('           Tabuada')
print(20 * '-=')
n = int(input('Digite um número que deseja a tabuada: '))
for c in range(11):
    soma = n * c
    print(f'{n} x {c} = {soma}')