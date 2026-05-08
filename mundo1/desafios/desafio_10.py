# ==================================================
# ! Desafio 10 — Conversor de Moedas
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler um valor em euro e mostrar quantos ienes ele pode comprar
# --------------------------------------------------

# ? Entrada de Dados
euro = float(input("Digite a Quantidade em Euro: "))

# ? Processamento e Saída de Dados
print(f"A quantidade de ienes que é possivel comprar com € {euro:.2f} é: ¥ {euro * 183.97:.2f}")

# TODO:
# aqui podemos utilizar uma api para pegar a cotação do euro, mas para facilitar, vamos usar um valor fixo
# 1 euro = 183.97 ienes (2026-05-08)


