
# * =============================================================
# * DESAFIO 039 - ALISTAMENTO MILITAR
# * =============================================================

# ? ENUNCIADO:
# Faça um programa que leia o ano de nascimento
# de um jovem e informe:
# - se ele ainda vai se alistar
# - se é hora de se alistar
# - ou se já passou do tempo.

from datetime import date

ano = int(input("Ano de nascimento: "))

idade = date.today().year - ano

if idade < 18:
    print(f"Faltam {18 - idade} anos.")
elif idade == 18:
    print("Hora de se alistar.")
else:
    print(f"Passaram {idade - 18} anos.")
