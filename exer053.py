print('Detector de Palíndromo')
text = str(input('Digite uma palavra: ')).strip().upper()
palavras = text.split()
junto = ''.join(palavras)
inverse = ''
for letra in range(len(junto)-1, -1, -1):
    inverse += junto[letra]
if inverse == junto:
    print('Palíndromo OK')
else: 
    print('Não é Palíndromo')
