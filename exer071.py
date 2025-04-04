print("=" * 30)
print("      BANCO PYTHON      ")
print("=" * 30)

# Solicita o valor do saque
valor = int(input("Digite o valor a ser sacado: R$ "))

# Definição das cédulas disponíveis
cedulas = [50, 20, 10, 1]
resultado = {}

# Loop para calcular a quantidade de cada cédula
for cedula in cedulas:
    quantidade = valor // cedula  # Calcula quantas cédulas desse valor são necessárias
    if quantidade > 0:
        resultado[cedula] = quantidade
    valor %= cedula  # Atualiza o valor restante após retirar as cédulas

# Exibe o resultado
print("\nNotas entregues:")
for cedula, qtd in resultado.items():
    print(f"{qtd} cédula(s) de R$ {cedula}")

print("=" * 30)
print("Retire seu dinheiro. Obrigado por usar o Banco Python!")