# * ============================================================
# * DESAFIO 23 — Separando Dígitos de um Número
# * 数字を分解する (Sūji wo Bunkai Suru)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Faça um programa que leia um número de 0 a 9999
# ? e mostre na tela cada um dos dígitos separados.
# ?
# ? Exemplo:
# ? Digite um número: 1834
# ?
# ? Unidade: 4
# ? Dezena: 3
# ? Centena: 8
# ? Milhar: 1
# ? ─────────────────────────────────────────────

separador = "─" * 42
titulo = " Separando Dígitos ".center(42, "═")

numero = int(input("Digite um valor de 0 a 9999: "))

milhar  = numero // 1000
centena = numero % 1000 // 100
dezena  = numero % 100  // 10
unidade = numero % 10

print(f"\n{titulo}")
print(f"  {'Valor para analise':<10}: {numero}")
print(separador)
print(f"  {'Milhar':<10}: {milhar}")
print(f"  {'Centena':<10}: {centena}")
print(f"  {'Dezena':<10}: {dezena}")
print(f"  {'Unidade':<10}: {unidade}")
print(separador)