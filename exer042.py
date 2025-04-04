print('           Analisando Triangulos')
lado_A = int(input('Primeiro lado: '))
lado_B = int(input('Segundo lado: '))
lado_C = int(input('Terceiro lado: '))

if lado_A < lado_B + lado_C and lado_B < lado_A + lado_C and lado_C < lado_A + lado_B:
    print('Os segmentos acima PODEM formar triângulo ', end='')
    if lado_A == lado_B == lado_C:
        print('EQUILÁTERO')
    elif lado_A != lado_B != lado_C != lado_A:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um TRIANGULO')