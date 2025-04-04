print('         Índice de massa corporal')
print('Bem vindo')
print('Vamos realizar algumas perguntar para calcular o seu IMC OK?')
altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso? [KG]'))
imc = (peso / altura ** 2) 
if imc <= 18.5:
    print(f'Seu IMC {imc:.1f} está indicando ABAIXO DO PESO')
elif imc <= 25:
    print(f'Seu IMC {imc:.1f} está indicando PESO IDEAL')
elif imc <= 30:
    print(f'Seu IMC {imc:.1f} está indicandoSOBREPESO')
else:
    print(f'Seu IMC {imc:.1f} está indicando OBESIDADE MÓRBIDA')