# ==================================================
# ! Desafio 14 — Conversor de Temperatura
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler uma temperatura em graus Celsius e mostrar a temperatura convertida em graus Fahrenheit
# --------------------------------------------------

# ? Entrada de Dados
celcius = float(input("Digite a temporatura em graus Celsius: "))

# ? Processamento de Dados
fahrenheit = (celcius * 9/5) + 32

# ? Saída de Dados
print(f"\nA temperatura de {celcius:.2f}°C é equivalente a {fahrenheit:.2f}°F.")

# NOTE: 
# A fórmula para converter Celsius para Fahrenheit é: F = (C * 9/5) + 32




