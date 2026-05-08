# ==================================================
# ! Desafio 13 — Aumento Salarial
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler o salário de um funcionário e mostrar o novo salário com aumento de 15%
# --------------------------------------------------

# ? Entrada de Dados
salario = float(input("Digite o salário do funcionário: € "))

# ? Processamento
aumento = salario * 0.15
novo_salario = salario + aumento

# ? Saida de Dados
print(f"\nSalário original: € {salario:.2f}")
print(f"Aumento de 15%: € {aumento:.2f}")
print(f"Novo salário: € {novo_salario:.2f}")




