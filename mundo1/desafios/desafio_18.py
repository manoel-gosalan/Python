# * ============================================================
# * DESAFIO 18 — Seno, Cosseno e Tangente
# * 三角関数 (Sankaku kansū)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que leia um ângulo qualquer (em graus)
# ? e mostre o valor do Seno, Cosseno e Tangente.
# ?
# ? ! ATENÇÃO: o math usa RADIANOS, não graus!
# ? ! 注意: math は度ではなく、ラジアンを使います！
# ?
# ? Conversão obrigatória:
# ?   radianos = math.radians(graus)
# ?
# ? Funções:
# ?   math.sin(rad)   → seno
# ?   math.cos(rad)   → cosseno
# ?   math.tan(rad)   → tangente
# ? ─────────────────────────────────────────────────────────────

import math

sep = "─" * 40

graus = float(input("Digite o angulo (em graus): "))
radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"\n{sep}")
print(f"  Angulo: {graus} graus  ({radianos:.4f} rad)")
print(sep)
print(f"  sen({graus})  =  {seno:+.4f}")
print(f"  cos({graus})  =  {cosseno:+.4f}")
print(f"  tan({graus})  =  {tangente:+.4f}")
print(sep)

# * がんばって！🎌
