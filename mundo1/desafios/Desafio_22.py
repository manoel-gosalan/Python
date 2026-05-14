# * ============================================================
# * DESAFIO 22 — Analisador de Texto
# * 文字列解析 (Mojiretsu Kaiseki)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Crie um programa que leia o nome completo
# ? de uma pessoa e mostre:
# ?
# ? - O nome com todas as letras maiúsculas
# ? - O nome com todas as letras minúsculas
# ? - Quantas letras ao todo (sem considerar espaços)
# ? - Quantas letras tem o primeiro nome
# ? ─────────────────────────────────────────────

titulo = " ANALISADOR DE TEXTO ".center(42, "═")

nome = input("Digite seu nome completo: ")
sem_espacos = "".join(nome.split())
primeiro_nome = nome.split()[0]

print(f"\n{titulo}")
print(f"  {'Maiúsculas':<26}: {nome.upper()}")
print(f"  {'Minúsculas':<26}: {nome.lower()}")
print(f"  {'Total letras sem espaços':<26}: {len(sem_espacos)}")
print(f"  {'Primeiro nome':<26}: {primeiro_nome} ({len(primeiro_nome)} letras)")
print(f"{'═' * 42}\n")