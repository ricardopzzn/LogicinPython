from uteis.modulos import *
"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


valor = float(input('Digite um valor R$: '))
print(f'A metade de R${valor:.2f} é R${metade(valor)}')
print(f'O dobro de R${valor:.2f} é R${dobro(valor)}')
print(f'Aumentando 10%, temos R${aumentar(valor)}')
print(f'Diminuindo 10%, temos R${diminuir(valor)}')