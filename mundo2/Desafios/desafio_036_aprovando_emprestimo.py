
# * =============================================================
# * DESAFIO 036 - APROVANDO EMPRÉSTIMO
# * Mundo 2 - Curso em Vídeo | Python
# * =============================================================

# ? ENUNCIADO:
# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
#
# O programa vai perguntar:
# - valor da casa
# - salário do comprador
# - em quantos anos ele vai pagar
#
# Calcule o valor da prestação mensal.
#
# A prestação não pode exceder 30% do salário,
# senão o empréstimo será negado.

# TODO: Entrada de dados
casa = float(input("Valor da casa: €"))
salario = float(input("Salário do comprador: €"))
anos = int(input("Quantos anos para pagar: "))

# TODO: Cálculo da prestação
prestacao = casa / (anos * 12)

print(f"Prestação: €{prestacao:.2f}")

# TODO: Validação do empréstimo
if prestacao <= salario * 0.30:
    print("Empréstimo APROVADO")
else:
    print("Empréstimo NEGADO")
