# * ============================================================
# * DESAFIO 16 — Quebrando um número
# * 数字を分解する (Sūji wo bunkai suru)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que leia um número inteiro e mostre
# ? na tela:
# ?
# ?   → Qual é o antecessor desse número
# ?   → Qual é o sucessor desse número
# ?   → Qual o dobro desse número
# ?   → Qual o triplo desse número
# ?   → Qual é a raiz quadrada desse número
# ?   → Se o número é par ou ímpar
# ?
# ? Dica: use o módulo math para a raiz quadrada!
# ? ヒント: 平方根には math.sqrt() を使いましょう！
# ? ─────────────────────────────────────────────────────────────

import math

numero = int(input("Digite um valor: "))

antecessor = numero - 1
sucessor = numero + 1
triplo = numero * 3
dobro = numero * 2
raiz = math.sqrt(numero)
par_impar = numero % 2

print(f"\nO antecessor de {numero} é: {antecessor} ")

print(f"O sucessor de {numero} é: {sucessor}")

print(f"O dobro de {numero} é: {dobro}")

print(f"O triplo de {numero} é: {triplo}")

print(f"A raiz quadrada de {numero} é: {raiz:.2f}")

# * % 2 retorna 0 se par, 1 se ímpar
if par_impar == 0:
    print(f"Analisando o numero {numero} ele é: PAR")
else:
    print(f"Analisando o numero {numero} ele é: IMPAR")


# * がんばって！🎌
