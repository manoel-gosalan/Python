# ==================================================
# ! Desafio 08 — Conversor de Medidas
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler uma distancia em metros e mostra essa distancia convertida em:
# ? - Km -> quilômetros
# ? - Hm -> hectômetros
# ? - Dam -> decâmetros
# ? - Dm -> decímetros
# ? - Cm -> centímetros
# ? - Mm -> milímetros
# --------------------------------------------------

distancia = float(input("Digite a Distancia em metros que deseja converter: "))

print(f"Analisando a distancia de {distancia} metros suas conversões são:")

print(f"Em quilômetros -> km é: {distancia / 1000}")

print(f"Em hectômetros -> hm é:  {distancia / 100}")

print(f"Em Decâmetro -> dam é: {distancia / 10}")

print(f"Em Decimetro -> dm é: {distancia * 10}")

print(f"Em Centimetro -> cm é: {distancia * 100}")

print(f"Em Milimetro -> mm é: {distancia * 1000}")




