
# ============================================================
# ! DESAFIO EX05 — Tabuada até 10
# ============================================================

# ? Conceitos treinados:
# ? int(), operadores

# TODO:
# Descrição:
# Mostre a tabuada de um número.

titulo    = " Tabuada até 10 ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

valor     = int(input("Digite o valor para ver sua tabuada: "))

print(f"\n{titulo}")
print(f"Analisando o {valor}, sua tabuada é:")
print(separador)
for i in range(1, 11):
    print(f"{valor:>4} x {i:>2} = {valor * i:>3}")
print(footer)


