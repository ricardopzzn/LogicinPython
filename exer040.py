print('                          Média Final')
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1 + nota2) / 2
print(f'Sua nota final foi {media:.1f}')
if media < 5.0:
    print('\033[0;31mREPROVADO\033[m') 
elif media <= 6.9:
    print('\033[0;33mRECUPERAÇÃO\033[m')
else:
    print('\033[0;32mAPROVADO\033[m')