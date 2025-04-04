print('Analisador completo')

pessoa_velha = ''
maior = 0 
cont = 0 
menor = 0


for c in range(1, 5):
    print(f'====Analisando {c}° Pessoa')
    pessoa = str(input('Qual o nome: '))
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo [F/M]')).strip()[0].upper()
    cont += idade
    if maior is 0 or idade > maior and sexo in ['Mm']:
        maior = idade
        pessoa_velha = pessoa
    if sexo == 'F' and idade < 20:
        menor += 1
          
media_idade = cont / 4

print(f'A media entre a idade de 4 pessoas é {media_idade:.2f}')
print(f'O Homen mais velho tem {maior} e se chama {pessoa_velha}')
print(f'Ao todo são {menor} mulheres com menos de 20 anos')