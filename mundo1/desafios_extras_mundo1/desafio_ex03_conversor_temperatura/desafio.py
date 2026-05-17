# ============================================================
# ! DESAFIO EX03 — Conversor de Temperatura
# ============================================================

# ? Conceitos treinados:
# ? float(), operadores

# TODO:
# Descrição:
# Converta Celsius para Fahrenheit e Kelvin.

titulo = " Conversor de Temperatura 2.0 ".center(40, "\u2550")
separador = "─" * 40
footer = "\u2550" * 40

fahrenheit = float(input("Digite a Temperatura: "))
kelvin = ((fahrenheit - 32)/ 1.8) + 273.15

print(f"\n{titulo}")
print("Bem Vindo ao Conersor de Temperatura de Fº para Kº")
print(separador)
print(f"A temperatura de | {fahrenheit}Fº.")
print(f"{'A temperarua em':<16} | {kelvin:.2f}Kº")
print(footer)

