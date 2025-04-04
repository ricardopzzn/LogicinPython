from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 100 or ano % 400 == 0:
    print(f'Esse ano {ano} é BISSEXTO')
else:
    print(f'Esse ano {ano} não é BISSEXTO')