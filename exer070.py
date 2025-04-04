print('Estatística em produtos '.center(55))

product_name = ''
produto_low = None
soma_total = 0
soma = 0

while True:
    product = str(input('Nome do produto: '))
    price = int(input('Preço: '))
    soma_total += price
    if price > 1000:
        soma += 1
        
    
    if produto_low is None or price < produto_low:
        produto_low = price
        product_name = product
           
    exit_code = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if exit_code == 'N':
        break
    
print(f'{soma} produtos estão acima de 1.000R$')
print(f'O valor total da compra ficou {soma_total:.2f}R$')
print(f'O produto mais barato foi {product_name}')
        
        