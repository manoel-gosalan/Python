# * =============================================================
# * DESAFIO 047 - CONTAGEM DE PARES
# * Nível: Fácil
# * Linguagem: Python
# * =============================================================
# * 偶数 (guusuu) = número par
# * =============================================================

# ? ENUNCIADO

# * Crie um programa que mostre na tela todos os números pares
# * que estão no intervalo entre 1 e 50.

# TODO Utilizar FOR.
# TODO Exibir apenas números pares.
# TODO Trabalhar com intervalos usando range().

titulo = " Contagem de Pares ".center(30, "\u2550")
fim = "\u2550" * 30

for c in range(0, 50, 2):
    print(str(c).center(30, " "))
print(fim)