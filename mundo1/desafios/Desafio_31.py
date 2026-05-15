# * ============================================================
# * DESAFIO 31 — CUSTO DA VIAGEM
# * 旅行費用 (Ryokō Hiyō)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Desenvolva um programa que pergunte a distância
# ? de uma viagem em Km.
# ?
# ? Calcule o preço da passagem:
# ?
# ? → €0,50 por Km para viagens até 200Km
# ? → €0,45 para viagens mais longas
# ? ─────────────────────────────────────────────

titulo    = " Custo da Viagem ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

viagem = int(input("Digite a distancia da viagem em km: "))

if viagem <= 200:
    tarifa = 0.50
else:
    tarifa = 0.45

total = viagem * tarifa

print(f"\n{titulo}")
print(f"  {'Distancia':<18}: {viagem} km")
print(f"  {'Tarifa por km':<18}: EUR {tarifa:.2f}")
print(separador)
print(f"  {'Total da viagem':<18}: EUR {total:.2f}")
print(footer)