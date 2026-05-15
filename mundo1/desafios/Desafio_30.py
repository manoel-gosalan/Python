# * ============================================================
# * DESAFIO 30 — PAR OU ÍMPAR
# * 偶数と奇数 (Gūsū to Kisū)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Crie um programa que leia um número inteiro
# ? e mostre na tela se ele é PAR ou ÍMPAR.
# ? ─────────────────────────────────────────────
titulo = "Par ou Impar".center(40, "\u2550")
numero = int(input('Digite um valor: '))
footer = "\u2550" * 40

print(f'\n{titulo}')
if numero % 2 == 0:
    print(f'O numero de {numero} é: PAR')
else:
    print(f'O numero {numero} é: IMPAR')
print(footer)