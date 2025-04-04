print('           Maior e menor valores')
print(20 * '-=')
n1 = int(input('Digite o primeiro valor:\n'))
n2 = int(input('Digite o segundo valor:\n'))
n3 = int(input('Digite o terceiro valor:\n'))
# Verificando número maior >
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
#Verificando número menor <
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print(f'{maior} Maior valor')
print(f'{menor} Menor Valor')