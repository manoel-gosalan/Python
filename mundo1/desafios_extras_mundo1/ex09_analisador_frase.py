# * =============================================================
# * EXERCICIO 09 - ANALISADOR DE FRASES
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * 分析器 (bunsekiki) = analisador
# * =============================================================


# ? ENUNCIADO:
# Crie um programa que receba uma frase digitada pelo usuario
# e exiba um relatorio completo sobre ela.


# ! O PROGRAMA DEVE FAZER (na ordem):
# TODO: 1. Contar quantas PALAVRAS tem a frase
# TODO: 2. Contar quantas LETRAS tem a frase (sem contar espacos)
# TODO: 3. Contar quantas VOGAIS existem na frase (a, e, i, o, u - maiusculas e minusculas)
# TODO: 4. Exibir qual e a PALAVRA MAIS LONGA da frase
# TODO: 5. Exibir a frase em MAIUSCULAS e depois em minusculas

# * DICAS - ヒント:
# Use .split() para separar as palavras em uma lista
# Use um loop for e cheque se cada char esta em "aeiouAEIOU" para contar vogais
# Use max(palavras, key=len) para achar a palavra mais longa
titulo = " Relatório da Frase ".center(40, "\u2550")
frase = input("Digite uma frase: ")


palavras = frase.split()
total_palavras = len(frase)

so_letras = frase.replace(" ", "-")
total_letras = len(so_letras)

# 3. Vogais - loop verificando cada caractere
total_vogais = 0
for letra in "aiueo":
    if letra.lower() in "aeiou":
        total_vogais += 1

# 4. Palavra mais longa - max com key=len (mágica do Python! ✨)
mais_longa = max(frase, key=len)

# 5. Upper e lower - direto e simples
em_maiuscula = frase.upper()
em_minuscula = frase.lower()

# Relatório final
print(f"\n{titulo}")
print(f"Palavras:          {total_palavras}")
print(f"Letras:            {total_letras}")
print(f"Vogais:            {total_vogais}")
print(f"Palavra mais longa: {mais_longa}")
print(f"Maiúsculas:        {em_maiuscula}")
print(f"Minúsculas:        {em_minuscula}")