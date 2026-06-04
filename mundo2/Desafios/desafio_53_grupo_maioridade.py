# * =============================================================
# * DESAFIO 054 - GRUPO DA MAIORIDADE
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 成年 (seinen) = maior de idade
# * 未成年 (miseinen) = menor de idade
# * =============================================================

# ? ENUNCIADO

# * Crie um programa que leia o ano de nascimento
# * de sete pessoas.
# *
# * No final, mostre:
# *
# * Quantas pessoas já atingiram a maioridade.
# * Quantas ainda não atingiram a maioridade.

# TODO Ler 7 anos de nascimento.
# TODO Calcular idade de cada pessoa.
# TODO Contar maiores e menores de idade.
# TODO Mostrar os totais.
from datetime import date

titulo = " Grupo de Maioridade ". center(30, "\u2550")
atual = date.today().year
total_acima = 0
total_abaixo = 0 



for pessoa in range(1, 8):
    nascimento = int(input(f"{pessoa} / 7 Digite o ano de nascimento: "))
    idade = atual - nascimento
    

    if idade >= 18:
        total_acima += 1
    else:
        total_abaixo += 1
print(f"\n{titulo}")
while True:
    print("\n1 - Ver total de Pessoas maior de idade.")
    print("2 - Ver total de Pessoas menores de idade.")
    print("3 - Sair.")

    escolha = input("\nEscolha um o que deseja fazer: ")
    if escolha == "1":
        print(f"\n{total_acima} pessoas são maiores de idade")
    elif escolha == "2":
        print(f"\n{total_abaixo} pessoas são menores de idade.")
    elif escolha == "3":
        print("\nAté logo! またね！".center(30, "\u2550"))
        break
    else:
        print("\nEscolha invalida! selecione 1, 2 ou 3!")




