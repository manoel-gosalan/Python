# ==================================================
# ! Desafio 12 — Desconto em Produto
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler o preço de um produto e mostrar o preço com desconto de 5%
# --------------------------------------------------

# ? Entrada de Dados
preco = float(input("Digite o preço do produto: € "))

#? Processamento
desconto = preco *0.05
preco_com_desconto = preco - desconto

# ? Saída de Dados
print(f"\nPreço original: € {preco:.2f}")
print(f"Desconto de 5%: € {desconto:.2f}")
print(f"Preço com desconto: € {preco_com_desconto:.2f}")

