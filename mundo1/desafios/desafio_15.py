# ==================================================
# ! Desafio 15 — Aluguel de Carros
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler a quantidade de dias e a quantidade de quilômetros percorridos por um carro alugado, e mostrar o preço a pagar.
# ? sabendo que o preço do aluguel é € 60 por dia e € 0,15 por km rodado
# --------------------------------------------------

# ? Entrada de Dados
dias = int(input("Digite a quantidade de dias que ficou com o carro: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))

# ? Processamento
preco_dias = dias * 60
preco_km = km * 0.15
preco_total = preco_dias + preco_km

# ? Saída de Dados
print(f"\nPreço pelo aluguel dos dias é de: € {preco_dias:.2f}")
print(f"Preço pelos quilômetros rodados é de: € {preco_km:.2f}")
print(f"Preço total a pagar: € {preco_total:.2f}")


