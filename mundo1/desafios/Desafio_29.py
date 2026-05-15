# * ============================================================
# * DESAFIO 29 — RADAR ELETRÔNICO
# * スピード違反 (Supīdo Ihan)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Leia a velocidade de um carro.
# ?
# ? Se ele ultrapassar 80Km/h,
# ? mostre uma mensagem dizendo que ele foi multado.
# ?
# ? A multa vai custar €7,00 por cada Km acima
# ? do limite.
# ? ─────────────────────────────────────────────
from random import randint

titulo    = " Radar Eletronico ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

velocidade = int(input("Digite a velocidade em km/h: "))
multa      = 7
excesso    = velocidade - 80

print(f"\n{titulo}")

if velocidade > 80:
    print(f"  {'Velocidade':<18}: {velocidade} km/h")
    print(f"  {'Limite':<18}: 80 km/h")
    print(f"  {'Excesso':<18}: {excesso} km/h")
    print(separador)
    print(f"  {'Situacao':<18}: MULTADO")
    print(f"  {'Valor da multa':<18}: EUR {excesso * multa:.2f}")
else:
    print(f"  {'Velocidade':<18}: {velocidade} km/h")
    print(f"  {'Limite':<18}: 80 km/h")
    print(separador)
    print("  Sem infracao. Bom condutor!")

print(footer)