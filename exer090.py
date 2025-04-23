'''Exercício Python 090: Faça um programa que leia nome e média de um aluno
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

notas = {}

try:
    notas['Nome'] = str(input('Digite um nome: '))
    notas['Nota'] = float(input('Digite a nota: '))
    

    for c in notas.values():
        if type(c) != float:
            nome = c
        else:
            if c < 7:
                print(f'{nome} ficou de recuperação')
            elif c < 5:
                print(f'{nome} ficou de Exame')
            else:
                print(f'{nome} foi Aprovado! Parabéns!!!!')
except ValueError:
    print('Por favor, digite um número valido.')
