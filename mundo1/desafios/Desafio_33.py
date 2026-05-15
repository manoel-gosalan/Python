# * ============================================================
# * DESAFIO 33 — MAIOR E MENOR VALORES
# * 最大値と最小値 (Saidai-chi to Saishō-chi)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Faça um programa que leia três números
# ? e mostre:
# ?
# ? → qual é o MAIOR
# ? → qual é o MENOR
# ? ─────────────────────────────────────────────
titulo    = " Maior e Menor ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

A = int(input("Digite o 1º valor: "))
B = int(input("Digite o 2º valor: "))
C = int(input("Digite o 3º valor: "))

print(f"\n{titulo}")

if A == B or A == C or B == C:
    print(separador)
    print("  Valores iguais detectados!")
    print("  Os tres numeros precisam ser diferentes.")
else:
    if A > B and A > C:
        maior = A
    elif B > A and B > C:
        maior = B
    else:
        maior = C

    if A < B and A < C:
        menor = A
    elif B < A and B < C:
        menor = B
    else:
        menor = C

    print(f"  {'Valor A':<10}: {A}")
    print(f"  {'Valor B':<10}: {B}")
    print(f"  {'Valor C':<10}: {C}")
    print(separador)
    print(f"  {'Maior':<10}: {maior}")
    print(f"  {'Menor':<10}: {menor}")

print(footer)