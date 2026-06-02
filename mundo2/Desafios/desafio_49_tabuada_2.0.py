# * =============================================================
# * DESAFIO 049 - TABUADA V2.0
# * Nível: Fácil
# * Linguagem: Python
# * =============================================================
# * 九九 (kuku) = tabuada
# * =============================================================

# ? ENUNCIADO

# * Refaça o desafio da tabuada.
# *
# * O programa deve ler um número inteiro e mostrar
# * sua tabuada utilizando a estrutura FOR.

# TODO Solicitar um número ao usuário.
# TODO Gerar a tabuada usando FOR.
# TODO Exibir os resultados organizadamente.

titulo = " Tabuada v2.0 ".center(30, "\u2550")
fim = "\u2550" * 30

tabuada = int(input("Digite um valor: "))
print(titulo)
for t in range(1, 11):
    print(f"{tabuada:>10} x {t:>2} = {tabuada * t:>2}")
print(fim)
