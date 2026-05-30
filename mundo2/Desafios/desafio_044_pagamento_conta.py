# * =============================================================
# * EXERCICIO 44 - GERENCIADOR DE PAGAMENTOS
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 支払い管理 (shiharai kanri) = gerenciamento de pagamentos
# * =============================================================


# ? ENUNCIADO:
# Uma loja deseja automatizar o calculo de pagamentos dos clientes.
# O sistema deve aplicar descontos ou juros dependendo da forma
# escolhida pelo usuario.


# ! REGRAS DE PAGAMENTO:
#
# [ 1 ] A vista no dinheiro/PIX
#       -> 10% de desconto
#
# [ 2 ] A vista no cartao
#       -> 5% de desconto
#
# [ 3 ] Em ate 2x no cartao
#       -> preco normal
#
# [ 4 ] 3x ou mais no cartao
#       -> 20% de juros


# ! O PROGRAMA DEVE:
# TODO: 1. Ler o preco do produto
# TODO: 2. Mostrar menu de formas de pagamento
# TODO: 3. Calcular o valor final
# TODO: 4. Caso seja parcelado em 3x ou mais:
#             - pedir quantidade de parcelas
#             - mostrar valor de cada parcela
# TODO: 5. Exibir resumo final da compra


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
#
# Input:
#   Preco do produto: R$1000
#   Forma de pagamento: 4
#   Quantidade de parcelas: 5
#
# Output:
#   Total com juros: R$1200.00
#   Sua compra sera parcelada em 5x de R$240.00


# =============================================================
# ? DESAFIO EXTRA (OPCIONAL)
# =============================================================
#
# Adicione validacoes:
#
# - impedir parcelas menores que 1
# - impedir opcoes invalidas
# - impedir valores negativos
#
# BONUS:
# Crie um pequeno "recibo" visual no terminal.
#
# Exemplo:
#
# ==============================
#         LOJA PYTHON
# ==============================
# Produto: ........ R$1000.00
# Pagamento: ...... 5x CARTAO
# Total Final: .... R$1200.00
# ==============================


# ? HABILIDADES TREINADAS:
#
# - if / elif / else
# - operadores matematicos
# - porcentagem
# - validacao de entrada
# - formatacao monetaria
# - menus no terminal
#
# =============================================================

separador = "=" * 30
titulo = "LOJA PYTHON".center(30, " ")
produto = float(input("Valor do produto: "))
alerta_valor_produto = """
O valor do produto não pode ser 0 ou negativo.
"""

if produto <= 0:
    print(alerta_valor_produto)

else:
    while True:
        print("Formas de pagamento: ")
        print("1 - A vista Pix")
        print("2 - A vista no Cartão")
        print("3 - Em até 2x no Cartão")
        print("4 - 3x ou mais no Cartão")
        print("5 - Sair")

        escolha = input("\nEscolha uma das opções acima: ").lower()

        if escolha == "5":
            print("\nMuito bom, té logo! すごくよかった、またね！")
            break
        elif escolha not in ["1", "2", "3", "4"]:
            print("Opção inválida, tente outra vez! もう一度！(mou ichido = de novo!)")
            continue

        print(separador)
        print(titulo)
        print(separador)

        if escolha == "1":
            percentual = 0.10
            preco_final = produto - (produto * percentual)
            print(f"Produto: ........ €{produto:.2f}")
            print("Pagamento: ...... PIX")
            print(f"Total Final: .... €{preco_final:.2f}")

        elif escolha == "2":
            percentual = 0.05
            preco_final = produto - (produto * percentual)
            print(f"Produto: ........ €{produto:.2f}")
            print("Pagamento: ...... CARTÃO")
            print(f"Total Final: .... €{preco_final:.2f}")

        elif escolha == "3":
            print(f"Produto: ........ €{produto:.2f}")
            print("Pagamento: ...... 2x CARTÃO")
            print(f"Total Final: .... €{produto:.2f}")

        elif escolha == "4":
            x = int(input("\nNúmero de parcelas (mínimo 3x): "))

            if x <= 2:
                print("Tem que ser em 3 vezes ou mais!")
                continue
            else:
                percentual_de_juros = 0.20
                preco_final = produto + (produto * percentual_de_juros)
                valor_parcela = preco_final / x
                print(f"Produto: ........ €{produto:.2f}")
                print(f"Pagamento: ...... {x}x CARTÃO")
                print(f"Total Final: .... €{preco_final:.2f}")
                print(f"Parcela: ........ €{valor_parcela:.2f}")

        print(separador)