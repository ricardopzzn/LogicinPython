while True:
    sexo = str(input('Digite o sexo [M/F]')).upper().strip()[0]
    if sexo not in 'FM':
        print('Digite a opção correta novamente: ')
    else:
        if sexo == 'F':
            print(f'Sexo feminino Cadastrado com sucesso')
        elif sexo == 'M':
            print(f'Sexo masculino Cadastrado com sucesso')
    
    
        