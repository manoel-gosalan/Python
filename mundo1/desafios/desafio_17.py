# * ============================================================
# * DESAFIO 17 — Catetos e Hipotenusa
# * 直角三角形 (Chokaku sankakkei)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que leia o valor dos dois catetos
# ? de um triângulo retângulo e calcule o valor da
# ? hipotenusa.
# ?
# ?   Fórmula (Teorema de Pitágoras):
# ?   h = √(a² + b²)
# ? ─────────────────────────────────────────────────────────────

import math

cateto_A = float(input("\nDigite o valor do Cateto A: "))
cateto_B = float(input("Digite o valor do Cateto B: "))

hipotenusa = math.hypot(cateto_A, cateto_B)

print(f"\nA hypotenusa se baseando no Cateto A '{cateto_A}' e Cateto B '{cateto_B}' é: {hipotenusa:.2f}")
print("\n")

# * がんばって！🎌
