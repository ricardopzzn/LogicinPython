print('Maior e menor da sequência')
option = int(input('Quantas vezes quer digitar o peso? '))
low = 0
high = 0

for c in range(0, option, +1):
    kilos = float(input(f'Digite o {c + 1}° peso: '))
    if high is 0 or kilos > high:
        high = kilos
    if low is 0 or kilos < low:
        low = kilos
        
print(f'Menor peso {low}\nMaior peso {high}')
