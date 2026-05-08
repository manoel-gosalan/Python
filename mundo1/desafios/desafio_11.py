# ==================================================
# ! Desafio 11 — Pintando Parede
# ==================================================

import math

# --------------------------------------------------
# ? Objetivo
# Ler a largura e altura de uma parede e mostrar
# quantos litros de tinta são necessários
# Sabendo que 1 litro pinta 2m²
# --------------------------------------------------

# ? Entrada de Dados
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# ? Processamento
area = largura * altura
litros = area / 2
litros_arredondados = math.ceil(litros)

# ? Saída de Dados
print(f"\nÁrea da parede: {area:.2f}m²")
print(f"Litros necessários: {litros:.2f}L")
print(f"Você precisará comprar {litros_arredondados} litro(s) de tinta.")

