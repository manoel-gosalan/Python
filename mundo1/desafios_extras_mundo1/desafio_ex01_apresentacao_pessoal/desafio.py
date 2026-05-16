# ============================================================
# ! DESAFIO EX01 — Apresentação Pessoal
# ============================================================

# ? Conceitos treinados:
# ? input(), f-string, print()

# TODO:
# Descrição:
# Peça nome, idade e cidade do usuário e exiba uma apresentação formatada.

titulo    = " Apresentação Pessoal ".center(40, "\u2550")
footer    = "\u2550" * 40

nome      = str(input("Qual é seu nome: "  ))
idade     = int(input("Qual é sua idade: " ))
cidade    = str(input("Qual é sua Cidade: "))

print(titulo)
print(f"Olá eu me chamo {nome}, é um prazer conhecer vocês.")
print(f"eu tenho {idade} anos.\nSou de {cidade}")
print(footer)


