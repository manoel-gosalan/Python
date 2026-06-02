# * =============================================================
# * DESAFIO 046 - CONTAGEM REGRESSIVA
# * Nível: Fácil
# * Linguagem: Python
# * =============================================================
# * カウントダウン (kauntodaun) = contagem regressiva
# * =============================================================

# ? ENUNCIADO

# * Faça um programa que mostre na tela uma contagem regressiva
# * para o estouro de fogos de artifício.
# *
# * A contagem deve ir de 10 até 0.
# *
# * Ao final da contagem, exiba uma mensagem indicando
# * o estouro dos fogos.

# TODO Utilizar estrutura FOR.
# TODO Fazer contagem regressiva.
# TODO Exibir mensagem final.

titulo = " Contagem Regressiva ".center(40, "═")
fim = "═" * 40

print(titulo)

for c in range(10, 0, -1):
    print(str(c).center(40))

print(fim)
