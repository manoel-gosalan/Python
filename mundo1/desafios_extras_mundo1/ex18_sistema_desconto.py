# * =============================================================
# * EXERCICIO 18 - SISTEMA DE DESCONTO
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 割引システム (waribiki shisutemu) = sistema de desconto
# * =============================================================


# ? ENUNCIADO:
# Crie um sistema de calculo de preco para uma loja que aplica
# descontos progressivos com base no valor total da compra
# e na categoria do cliente.


# ! TABELA DE DESCONTO POR VALOR DE COMPRA:
# Subtotal abaixo de R$ 100.00  ->  0% de desconto
# Subtotal de R$ 100 a R$ 299   ->  5% de desconto
# Subtotal de R$ 300 a R$ 499   -> 10% de desconto
# Subtotal de R$ 500 a R$ 999   -> 15% de desconto
# Subtotal de R$ 1000 ou mais   -> 20% de desconto

# ! BONUS POR CATEGORIA DE CLIENTE:
# Cliente VIP    -> +5% de desconto adicional sobre o percentual acima
# Cliente comum  -> sem bonus adicional


# ! O PROGRAMA DEVE:
# TODO: 1. Permitir adicionar varios ITENS com nome e preco (ate digitar "fim")
# TODO: 2. Calcular o SUBTOTAL de todos os itens
# TODO: 3. Aplicar o DESCONTO correto com base no subtotal
# TODO: 4. Perguntar se o cliente e VIP e aplicar o bonus se necessario
# TODO: 5. Exibir um CUPOM com itens, percentual de desconto e valor final

# ! REGRAS:
# Preco de item nao pode ser negativo ou zero
# O desconto VIP e somado ao desconto de valor (nao e multiplicado)
# Exiba o percentual total de desconto aplicado no cupom


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Nome do item: Camiseta
# Preco: 89.90
# Nome do item: Tenis
# Preco: 250.00
# Nome do item: fim
#
# Cliente VIP? (s/n): s
#
# === Cupom Fiscal ===
# Camiseta ................. R$ 89.90
# Tenis .................... R$ 250.00
# Subtotal: R$ 339.90
# Desconto aplicado (15%): - R$ 50.99
# TOTAL: R$ 288.92


# * DICAS - ヒント (hint):
# Guarde os itens em uma lista de dicionarios:
#   itens = []
#   itens.append({"nome": "Camiseta", "preco": 89.90})
#
# Use if/elif para determinar o percentual:
#   if subtotal < 100:
#       percentual = 0
#   elif subtotal < 300:
#       percentual = 5
#   ...
#
# Calculo do desconto:
#   valor_desconto = subtotal * (percentual / 100)
#   total_final    = subtotal - valor_desconto


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
