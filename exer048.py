cont = 0
count = 0
for i in range(1 ,501, 2):
    if i % 3 == 0:
        count += 1
        cont += i
print(f'Quantidade de números multiplo por 3 = {count} e soma de todos eles {cont}')