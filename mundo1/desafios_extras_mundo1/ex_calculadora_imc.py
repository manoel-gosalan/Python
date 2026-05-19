# ============================================================
# ! DESAFIO EX02 — Calculadora de IMC
# ============================================================

# ? Conceitos treinados:
# ? float(), operadores aritméticos

# TODO:
# Descrição:
# Peça peso e altura e calcule o IMC.

titulo    = " Calculadora de IMC ".center(40, "═")
separador = "─" * 40
footer    = "═" * 40

altura = float(input("Digite sua altura em metros (ex: 1.73): "))
peso   = float(input("Digite seu peso em kg (ex: 70): "))

imc = peso / (altura ** 2)

# Cabeçalho e contexto
print(titulo)
print(f" Peso: {peso}kg | Altura: {altura}m ".center(40, " "))
print(separador)
print("De acordo com a OMS:")

# Apenas o resultado muda
if imc < 18.5:
    print("Abaixo do peso ideal.")
elif imc < 25:
    print("Peso ideal para sua altura.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")

print(footer)