
# * =============================================================
# * DESAFIO 040 - MÉDIA DO ALUNO
# * =============================================================

# ? ENUNCIADO:
# Crie um programa que leia duas notas de um aluno
# e calcule sua média.
#
# Média abaixo de 5.0 = REPROVADO
# Entre 5.0 e 6.9 = RECUPERAÇÃO
# 7.0 ou superior = APROVADO

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")

if media < 5:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
