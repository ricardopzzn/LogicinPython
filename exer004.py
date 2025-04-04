print('Dissecando uma várialvel') # Nome do desafio.

print(20 * '-=')
pl = input('Digite uma palavra: ')
print(f'O tipo primitivo desse valor é {type(pl)}')
print(f'Só tem espaços? {pl.isspace()}')
print(f'É um número? {pl.isnumeric()}')
print(f'É alfabético? {pl.isalpha()}')
print(f'É alfanúmerico? {pl.isalnum()}')
print(f'Está em Maiúsculas? {pl.isupper()}')
print(f'Está em minúsculas? {pl.islower()}')
print(f'Está capitalizada? {pl.istitle()}')
