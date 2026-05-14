# * ============================================================
# * DESAFIO 27 — Primeiro e Último Nome
# * 名前の分割 (Namae no Bunkatsu)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Faça um programa que leia o nome completo
# ? de uma pessoa mostrando em seguida:
# ?
# ? - O primeiro nome
# ? - O último nome
# ? ─────────────────────────────────────────────

titulo    = " Primeiro e Ultimo Nome ".center(40, "\u2550")
separador = "─" * 40
nome      = str(input("Digite seu nome completo: "))
partes    = nome.split()

print(f"\n{titulo}")
print(f"  {'Nome completo':<15}: {nome}")
print(separador)
print(f"  {'Primeiro nome':<15}: {partes[0]}")
print(f"  {'Ultimo nome':<15}: {partes[-1]}")
print(separador)