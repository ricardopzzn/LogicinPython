def information():
    while True:
        listanome = {}
        try:
            listanome['Nome'] = str(input('Qual o nome? '))
            listanome['Idade'] = int(input('Qual a idade? '))
            while True:
                listanome['Sexo'] = str(input('Qual o sexo? [M/F]')).strip().upper()
                if listanome['Sexo'] in ('M', 'F'):
                    break
                else:
                    print('Sexo não correponde ao correto, digite apenas M ou F')
                    
            # 2 Tratamento de exceção
        
        except TypeError:
            print('Erro de tipo de entrada!')
        except SyntaxError:
            print('Erro de Sextaxe!')
        except ValueError:
            print('Erro de entrada de valor!')
        finally:
            print('Dados cadastrado com sucesso.')
            return listanome
              
           
def main():           
    list_add = []
    list_feminina = []
    list_acima = []

    # 1 - Opção para continuação do programa

    while True:
        cadastro = information()
        list_add.append(cadastro.copy())
        
        if cadastro['Sexo'] == 'F':
            list_feminina.append(cadastro.copy())
            
        if cadastro['Idade'] > 25:
            list_acima.append(cadastro.copy())
        
        option = str(input('Deseja continuar? S/N')).strip().upper()
        if option == 'N':
            break
    soma = 0
    for pessoas in list_add:
        soma += pessoas['Idade']
    
    media = soma / len(list_add)
    print(f'Foram cadastradas {len(list_add)} pessoas!')
    print(f'A media de idade é {media}')
    if len(list_feminina) == 0:
        print('Não teve nenhuma mulher cadastrada na lista.')
    else:
        print(f'A lista das mulheres {list_feminina}')
    if len(list_acima) == 0:
        print(f'Lista de pessoa acima da média está vazia')
    else:
        print(f'Lista com pessoas acima de 25 anos {list_acima}')
    
    
if __name__=="__main__":
    main()