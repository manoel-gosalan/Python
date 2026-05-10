# * ============================================================
# * DESAFIO 20 — Sorteando uma ordem na lista
# * リストをシャッフルする (Risuto wo shaffuru suru)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que tenha uma lista com 5 nomes de
# ? amigos e mostre na tela uma ordem de apresentação
# ? ALEATÓRIA para todos eles.
# ?
# ? Todos os nomes devem aparecer — apenas em ordem
# ? diferente a cada execução.
# ?
# ? Dica: use random.shuffle(lista)
# ? ヒント: shuffle() はリストを直接変更します！
# ?
# ? ! Atenção: shuffle() modifica a lista in-place e retorna None
# ? ! Não faça:  lista = random.shuffle(lista)  ← isso quebra!
# ? ─────────────────────────────────────────────────────────────

import random
import time
separador = "─" * 40
lista = ["Manoel", "Lidio", "Gosalan", "Dos", "Santos"]
random.shuffle(lista)

# TODO: mostre a ordem de apresentação
print(f"\n{separador}")
print("Sorteando os Alunos...")
print(separador)
time.sleep(5)
print(f"\n{separador}")
print("Apos o sorteio dos Alunos a apresenatação será feita na seguinte ordem: ")
print(separador)
print(f"\n{lista}")
print(f"\n{separador}\n")




# * がんばって！🎌
