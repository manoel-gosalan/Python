# * =============================================================
# * DESAFIO 051 - PROGRESSÃO ARITMÉTICA
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 等差数列 (tousasuu-retsu) = progressão aritmética
# * =============================================================

# ? ENUNCIADO

# * Desenvolva um programa que leia o primeiro termo
# * de uma Progressão Aritmética (PA) e sua razão.
# *
# * No final, mostre os 10 primeiros termos dessa PA.

# TODO Ler primeiro termo.
# TODO Ler razão.
# TODO Gerar os 10 primeiros termos.
# TODO Exibir a sequência.
titulo = " Progressão Aritmética ".center(33, "\u2550")
fim = " Até logo! またね！ ".center(30, "\u2550")

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a Razão: "))
decimo = primeiro + (10 - 1) * razao

termos = [str(t) for t in range(primeiro, decimo + razao, razao)]

print(titulo)
print(" → ".join(termos))
print(fim)
