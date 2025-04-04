masc, fem, age_cont, age_low = 0, 0, 0, 0
while True:
    print('Cadastro de pessoas'.center(50))
    print()
    age = int(input('Digite a idade: '))
    print()
    sexo = str(input('Qual o sexo: [F/M]')).upper().strip()[0]
    print()
    if age > 18:
        age_cont += 1
    if sexo == 'F':
        fem += 1
        if age < 20:
            age_low += 1
    if sexo == 'M':
        masc += 1
    
            
    
    option = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if option == 'S':
        continue
    else:
        break    
    
print(f'Total de pessoas +18 anos: {age_cont}')
print(f'Ao todo temos {masc} Homens cadastrados')
print(f'Ao todo temos {fem} Mulheres cadastrados')
print(f'E temos {age_low} Mulher com menos de 20 anos.')