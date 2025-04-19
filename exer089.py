print('Boletim de notas'.center(60))
notas = []

while True:
    # 1 - Solicitando entrada do usuário de nome e notas e adicionado dentro da lista notas
    try:
        nomes = str(input('Qual o nome do aluno para cadastro?\n'))
        nota1 = float(input('Qual a primeira nota:\n'))
        nota2 = float(input('Qual a segunda nota:\n'))
        notas.append([nomes, nota1, nota2][:])
    
        
        # 2 - Condição de continuação do programa
        option = str(input('Deseja continuar o cadastro? [S/N]\n')).strip().upper()
        if option == 'S':
            continue
        if option == 'N':
            break
    # Tratamendo de exceção
    except ValueError as errovalor:
        print(f'Erro de entrada de valor {errovalor}')
    except SyntaxError as sintaxe:
        print(f'Erro de sintaxe de linguagem {sintaxe}')
    else:
        pass
    finally:
        print()
        print('Nomes e notas adicionados a lista com sucesso')
        print()
    
# 3 - Loop for para soma das notas e criação do indice 
print('NUM',  'NOME', 'NOTA'.center(30))
for i, sublista in enumerate(notas):
    nome = sublista[0]
    resutlado = sublista[1:]
    soma = sum(resutlado) / 2
    
    print(f'{i}   {nome}'.center(5), end=' ' )
    print(f'{soma:.2f}'.center(30))
    
# 4 - Mostrar as notas conforme o indice do aluno criado a partir da lista notas    
while True:
    try:    
        indice = int(input('Qual nota deseja ver: '))
        print(notas[indice])
    except IndexError:
        print(f'Indique o indice correto entre 0 e {len(notas)}')
    except ValueError:
        print(f'Entrada de valor errada, por favor digite apenas números entre{len(notas)}')
    option = str(input('Deseja continuar consultando a lista de notas? ')).strip().upper()
    if option == 'S' or option != 'S':
        pass
    if option == 'N':
        break