
# * =============================================================
# * DESAFIO 038 - COMPARANDO NÚMEROS
# * =============================================================

# ? ENUNCIADO:
# Leia dois números inteiros e compare-os.
# Mostre o primeiro é maior
# O segundo é maior
# Não tem valor maior os dois são iguais

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print("O primeiro valor é maior.")
elif n2 > n1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior os dois são iguais.")
