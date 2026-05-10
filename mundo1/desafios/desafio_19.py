# * ============================================================
# * DESAFIO 19 — Sorteando um item na lista
# * リストからランダムに選ぶ (Risuto kara random ni erabu)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que tenha uma lista com 5 nomes de
# ? amigos e sorteie um deles para descobrir quem vai
# ? pagar o almoço hoje.
# ?
# ? A lista deve ser definida diretamente no código.
# ? O programa deve exibir o nome sorteado.
# ?
# ? Dica: use random.choice(lista)
# ? ヒント: random.choice() でリストから1つ選べます！
# ? ─────────────────────────────────────────────────────────────

import random
import time

separador = "─" * 40
lista = ["Manoel", "Lidio", "Gosalan", "Dos", "Santos",]
sorteio = random.choice(lista)

print(f"\n{separador}")
print("Sorteando...")
time.sleep(3)
print(f"{separador}")
print(f"\n{separador}")
print(f"Após o Sorteio quem ira pagar a conta é: {sorteio}")
print(f"{separador}")

# * がんばって！🎌
