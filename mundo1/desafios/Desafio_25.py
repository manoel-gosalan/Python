# * ============================================================
# * DESAFIO 25 — Procurando uma String Dentro de Outra
# * 文字列検索 (Mojiretsu Kensaku)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Crie um programa que leia o nome de uma pessoa
# ? e diga se ela tem "SILVA" no nome.
# ? ─────────────────────────────────────────────

titulo    = " Procurando String Dentro de Outra ".center(42, "\u2550")
separador = "─" * 42

nome = str(input("Digite seu nome: "))

print(f"\n{titulo}")
print(f"  {'Nome':<20}: {nome}")
print(f"  {'Tem Silva no nome':<20}: {'SILVA' in nome.upper()}")
print(separador)