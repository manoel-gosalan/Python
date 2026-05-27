# * =============================================================
# * DESAFIO 42 - CURSO EM VÍDEO
# * Mundo 2 - Python
# * =============================================================

# ? ENUNCIADO:
# Refaça o desafio 35 e mostre que tipo de triangulo sera formado
# - Equilátero: todas os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
#
# TODO:
# Implemente a lógica completa do exercício.



# * =============================================================
# * DESAFIO 42 - CURSO EM VÍDEO
# * Mundo 2 - Python
# * =============================================================

titulo    = " Analisando Triangulo v1.0 ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

p = float(input("Primeiro Segmento: "))
s = float(input("Segundo Segmento: "))
t = float(input("Terceiro Segmento: "))

print(f'\n{titulo}')
print("Após analisarmos os valores dos segmentos:")
print(separador)
print(f"{'Primeiro Segmento:':<20} {p}")
print(f"{'Segundo Segmento:' :<20} {s}")
print(f"{'Terceiro Segmento:':<20} {t}")
print(separador)


eh_triangulo = p < s + t and s < p + t and t < p + s

if eh_triangulo:
    print("Eles FORMAM um Triângulo!\n")

    
    if p == s == t:
        tipo = "Equilátero"
    elif p == s or s == t or p == t:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"

    print(f"O triângulo é: \033[1m{tipo}\033[0m")
else:
    print("Eles NÃO formam um triângulo.")

print(footer)