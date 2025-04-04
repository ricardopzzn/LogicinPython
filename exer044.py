print('              Loja Online')
price = int(input('Qual o valor das compras? ')) # Solicitando o valor total da compra

print('\033[32mFORMAS DE PAGAMENTO\033[m')

# Manual de opção de pagamento 
print('''
      \033[33m[1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão\033[m
      
      ''')


while True:
    option = int(input('Qual opção você deseja escolher: '))
    if option == 1:
        avista = price - (price * 0.10)
        print(f'para o valor da compra de {price:.2f}R$, com desconto à vista fica {avista}')
        break
    elif option == 2:
        cartao = price - (price * 0.05)
        print(f'para o valor da compra de {price:.2f}R$, com desconto no cartão fica {cartao}')
        break
    elif option == 3:
        print(f'para o valor da compra de {price:.2f}R$, não tem desconto portando o valor fica o mesmo {price:.2f}R$') 
        break
    elif option == 4:
        cartao_3x = price + (price * 0.20)
        num_parc = int(input('Quantas parcelas?'))
        print(f'para o valor da compra de {price:.2f}R$\nnúmero de parcelas {num_parc} x {cartao_3x / num_parc:.2f}R$ COM JUROZ')
        print(f'com juroz da maquina fica o TOTAL {cartao_3x:.2f}R$')
        break
        
    
