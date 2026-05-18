# ============================================================
# ! DESAFIO EX08 — Sorteio de Times
# ============================================================

# ? Conceitos treinados:
# ? listas, random.shuffle()

# TODO:
# Descrição:
# Embaralhe jogadores e divida em times.
import random

titulo = " Sorteio de times ".center(40, "\u2550")
separador = "─" * 40
fim    = "\u2550" * 40

entrada = str(input("Digite o nome dos times (separados por , ): "))
times = [t.strip() for t in entrada.split(",")]
sorteio = times.copy()
random.shuffle(sorteio)

print(titulo)
print("Os times para o sorteio são:")
for t in times:
    print(f"  - {t}")

print(separador)
print("Após embaralhar:")
for t in sorteio:
    print(f"  - {t}")
print(fim)

