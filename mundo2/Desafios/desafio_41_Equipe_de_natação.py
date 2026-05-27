
# * =============================================================
# * DESAFIO 41 - CURSO EM VÍDEO
# * Mundo 2 - Python
# * =============================================================

# ? ENUNCIADO:
# Crie um script que leia a idade de um nadador e mostre em qual categoria ele se enquadra
#
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 20 anos: SENIOR
# - acima disso é master
#
# TODO:
# Implemente a lógica completa do exercício.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

if idade < 5:
    print("A idade mínima para participar é 5 anos.")
elif idade <= 9:
    print(f"Olá, {nome} {sobrenome}! Categoria: MIRIM")
elif idade <= 14:
    print(f"Olá, {nome} {sobrenome}! Categoria: INFANTIL")
elif idade <= 19:
    print(f"Olá, {nome} {sobrenome}! Categoria: JÚNIOR")
elif idade <= 20:
    print(f"Olá, {nome} {sobrenome}! Categoria: SÊNIOR")
else:
    print(f"Olá, {nome} {sobrenome}! Categoria: MASTER")