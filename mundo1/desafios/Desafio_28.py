# * ============================================================
# * DESAFIO 28 — JOGO DA ADIVINHAÇÃO v1.0
# * 数当てゲーム (Kazu Ate Gēmu)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? O computador vai "pensar" em um número entre
# ? 0 e 5.
# ?
# ? Faça um programa para o usuário tentar
# ? descobrir qual foi o número escolhido.
# ?
# ? O programa deve informar se o usuário
# ? venceu ou perdeu.
# ? ─────────────────────────────────────────────
from random import randint

titulo    = " Jogo da Adivinhacao ".center(40, "\u2550")
separador = "─" * 40
footer = "\u2550" * 40

jogador = int(input("Digite um numero de 0 a 5: "))
maquina = randint(0, 5)

print(f"\n{titulo}")
if jogador < 0 or jogador > 5:
    print("  Valor invalido! Digite apenas entre 0 e 5.")
elif jogador == maquina:
    print(f"  {'Seu numero':<15}: {jogador}")
    print(f"  {'Maquina':<15}: {maquina}")
    print(separador)
    print("  PARABENS! Voce acertou! 🎉")
    print(separador)
else:
    print(f"  {'Maquina':<15}: {maquina}")
    print(f"  {'Seu numero':<15}: {jogador}")
    print(separador)
    print("  Que pena! Tente novamente.")
print(footer)



