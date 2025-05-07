def votacao(nasc):
    """
    Função de votação, criada para calcular idade
    e se pode votar ou não.
    :ano > esta recebendo a data atual, expecifico o ano
    :idade > está recebendo :ano - ano_nascimento do usuario
    
    """
    
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - nasc
    if idade <= 16:
        return print(f'Você tem {idade}! VOTO NEGADO')
    elif idade > 16 and idade <= 50:
        return print(f'Você tem {idade}! VOTO OBRIGATÓRIO')
    else:
        return print(f'Você tem {idade}! VOTO OPCIONAL')
    
nasc = int(input('Qual o ano de nascimento?\n'))
votacao(nasc)

