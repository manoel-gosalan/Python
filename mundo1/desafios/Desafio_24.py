# * ============================================================
# * DESAFIO 24 — Verificando as Primeiras Letras
# * 文字列検証 (Mojiretsu Kenshō)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Crie um programa que leia o nome de uma cidade
# ? e diga se ela começa ou não com o nome "SANTO".
# ? ─────────────────────────────────────────────

titulo    = " Verificando as Primeiras Letras ".center(42, "\u2550")
separador = "─" * 42

cidade = str(input("Digite o nome da cidade: "))

comeca_com_santo = cidade[0:5].upper() == "SANTO"

print(f"\n{titulo}")
print(f"  {'Cidade':<20}: {cidade}")
print(separador)
print(f"  Começa com Santo  : {comeca_com_santo}")
print(separador)