# ============================================================
# ! DESAFIO EX07 — Gerador de Crachá
# ============================================================

# ? Conceitos treinados:
# ? f-string, formatação visual

# TODO:
# Descrição:
# Crie um crachá formatado.

titulo   = " Gerador de Cracha ".center(30, "\u2550")
borda_h = "─" * 30
lateral  = "|"
inferior = "\u2550" * 30
centralizar = 29
nome     = str(input("Digite seu nome: ")).strip().split()
nome_completo = f"{nome[0]} {nome[-1]}"


print(f"\n{titulo}")
print(borda_h)
print(f"{lateral}{' ' * 30}{lateral}")
print(f"{lateral}{nome_completo.center(centralizar)} {lateral}")
print(f"{lateral}{' ' * 30}{lateral}")
print(borda_h)
print(inferior)