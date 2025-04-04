expr = str(input('Digite a experessão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    
if len(pilha) == 0:
    print('Sua expressão está válida!')
else: 
    print('Expressão invalida') 
    
    