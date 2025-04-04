nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.split()
primeiro_nome = pnome[0]
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem o total de {len(nome) - nome.count(' ')} Letras.')
print(f'Seu primerio nome é {primeiro_nome} do tamanho {len(primeiro_nome)}')