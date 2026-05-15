# * ============================================================
# * DESAFIO 34 — AUMENTOS MÚLTIPLOS
# * 給料アップ (Kyūryō Appu)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Escreva um programa que pergunte o salário
# ? de um funcionário.
# ?
# ? Calcule o aumento:
# ?
# ? → salários acima de R$1250,00 ganham 10%
# ? → salários menores ou iguais ganham 15%
# ? ─────────────────────────────────────────────
titulo    = " Aumento Salarial ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

salario = float(input("Qual e o seu salario: R$ "))

print(f"\n{titulo}")
print(f"  {'Salario atual':<20}: R$ {salario:.2f}")
print(separador)

if salario <= 1250:
    aumento    = salario * 0.15
    novo       = salario + aumento
    percentual = "15%"
else:
    aumento    = salario * 0.10
    novo       = salario + aumento
    percentual = "10%"

print(f"  {'Percentual':<20}: {percentual}")
print(f"  {'Aumento':<20}: R$ {aumento:.2f}")
print(f"  {'Novo salario':<20}: R$ {novo:.2f}")
print(footer)