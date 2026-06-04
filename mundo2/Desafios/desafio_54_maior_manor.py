# * =============================================================
# * DESAFIO 055 - MAIOR E MENOR DA SEQUÊNCIA
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 最大 (saidai) = maior
# * 最小 (saishou) = menor
# * =============================================================

# ? ENUNCIADO

# * Faça um programa que leia o peso de cinco pessoas.
# *
# * No final, mostre:
# *
# * O maior peso informado.
# * O menor peso informado.

# TODO Ler 5 pesos.
# TODO Identificar maior peso.
# TODO Identificar menor peso.
# TODO Exibir resultados.
pessoas = []
nome_usuario = input("Qual é seu nome: ")

for p in range(1, 6):
    nome = input(f"\033[33mDigite o nome da {p}º pessoa:\033[0m ")
    kg   = float(input(f"\033[31mDigite o peso da {p}º pessoa:\033[0m "))
    pessoas.append({"nome": nome, "peso": kg})

mais_pesada = max(pessoas, key=lambda p: p["peso"])
mais_leve   = min(pessoas, key=lambda p: p["peso"])


print(f"\nMaior peso: {mais_pesada['peso']}kg — {mais_pesada['nome']}")
print(f"Menor peso: {mais_leve['peso']}kg — {mais_leve['nome']}")


while True:
    print("\n" + "=" * 35)
    print("        MENU DE OPÇÕES")
    print("=" * 35)
    print("1 - Ver dados do MAIS PESADO")
    print("2 - Ver dados do MAIS LEVE")
    print("3 - Mostrar lista completa")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print(f"\n  Mais pesado(a): {mais_pesada['nome']} "
                f"com {mais_pesada['peso']}kg")

    elif escolha == "2":
        print(f"\n  Mais leve: {mais_leve['nome']} "
                f"com {mais_leve['peso']}kg")

    elif escolha == "3":
        print("\n  Lista completa:")
        print("-" * 30)
        for pessoa in pessoas:
            print(f"  {pessoa['nome']:<15} {pessoa['peso']}kg")

    elif escolha == "4":
        print(" Até logo! またね！")
        break

    else:
        print(f" Opção inválida, tente de novo {nome_usuario}.")


    