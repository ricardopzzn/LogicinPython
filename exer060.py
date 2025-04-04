def factorial():
    fatorial = 1
    num = int(input('Você quer o fatorial de qual número: '))
    original = num
     
    while num > 1:
        fatorial *= num
        num -= 1
    return f'O fatorial do número {original} é o {fatorial}'

print(factorial())