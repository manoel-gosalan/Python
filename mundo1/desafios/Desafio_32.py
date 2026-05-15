# * ============================================================
# * DESAFIO 32 — ANO BISSEXTO
# * うるう年 (Urū-doshi)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Faça um programa que leia um ano qualquer
# ? e mostre se ele é BISSEXTO.
# ? ─────────────────────────────────────────────
from datetime import date
titulo    = " Ano Bissexto ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40


ano = int(input("Digite o Ano: "))
if ano == 0:
    ano = date.today().year

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print(f"\n{titulo}")
print(f"  {'Ano analisado':<18}: {ano}")
print(separador)

if bissexto:
    print(f"  {ano} E um ano bissexto!")
else:
    print(f"  {ano} NAO e um ano bissexto.")

print(footer)