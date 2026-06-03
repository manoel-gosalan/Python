# * =============================================================
# * DESAFIO 052 - NÚMERO PRIMO
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 素数 (sosuu) = número primo
# * =============================================================

# ? ENUNCIADO

# * Faça um programa que leia um número inteiro
# * e diga se ele é ou não um número primo.

# TODO Ler um número.
# TODO Verificar quantas divisões exatas ele possui.
# TODO Determinar se é primo.
# TODO Mostrar o resultado.

titulo = " Verificador de Número Primo ".center(40, "\u2550")
fim = " Até logo! またね！ ".center(40, "\u2550")

numero = int(input("Digite um valor: "))
contador = 0

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        contador += 1

print(titulo)
if contador == 2:
    print(f"\033[32m{numero} É um número primo! 素数です！\033[0m")
else:
    print(f"\033[31m{numero} NÃO é um número primo.\033[0m")
    print(f"  Possui \033[33m{contador}\033[0m divisor(es).")
print(fim)
