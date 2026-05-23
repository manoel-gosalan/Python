# * =============================================================
# * EXERCICIO 14 - CIFRA DE CESAR
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 暗号 (angou) = cifra / codigo secreto
# * =============================================================


# ? ENUNCIADO:
# A Cifra de Cesar e uma das tecnicas de criptografia mais antigas
# do mundo. Ela desloca cada letra do texto um numero fixo de
# posicoes no alfabeto. Crie um programa que codifique e
# decodifique mensagens usando essa tecnica.


# ! COMO FUNCIONA A CIFRA:
# Com deslocamento 3:
#   A -> D  |  B -> E  |  C -> F  |  Z -> C  (volta pro inicio)
#   "PYTHON" com deslocamento 3 -> "SBWKRQ"
#
# Ao decodificar, o deslocamento e aplicado ao contrario:
#   "SBWKRQ" com deslocamento 3 -> "PYTHON"
#
# ! IMPORTANTE: numeros, espacos e simbolos NAO sao alterados


# ! O PROGRAMA DEVE:
# TODO: 1. Pedir a MENSAGEM a ser processada
# TODO: 2. Pedir o NUMERO DE DESLOCAMENTO (valor entre 1 e 25)
# TODO: 3. Perguntar se quer CODIFICAR ou DECODIFICAR
# TODO: 4. Exibir o resultado processado
# TODO: 5. Respeitar maiusculas e minusculas (A cifrado != a cifrado)


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Mensagem: Hello World
#   Deslocamento: 3
#   (1) Codificar  (2) Decodificar: 1
#
# Output:
#   Resultado: Khoor Zruog
#
# Input:
#   Mensagem: Khoor Zruog
#   Deslocamento: 3
#   (1) Codificar  (2) Decodificar: 2
#
# Output:
#   Resultado: Hello World


# * DICAS - ヒント (hint):
# ord('A') = 65 | ord('Z') = 90  -> faixa das maiusculas
# ord('a') = 97 | ord('z') = 122 -> faixa das minusculas
#
# Formula para codificar uma letra maiuscula:
#   chr((ord(letra) - 65 + deslocamento) % 26 + 65)
#
# Formula para decodificar: use (26 - deslocamento) no lugar do deslocamento
# Ou simplifique: codificar com deslocamento negativo faz a mesma coisa


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
# * =============================================================
# * EXERCICIO 14 - CIFRA DE CESAR
# * 暗号 (angou) = cifra / codigo secreto
# * =============================================================

# 入力 (nyuuryoku) = entrada de dados
mensagem     = input("Mensagem: ")
deslocamento = int(input("Deslocamento: "))
opcao        = input("(1) Codificar  (2) Decodificar: ")

# Se for decodificar, invertemos o deslocamento
# デコード = decode | エンコード = encode
if opcao == "2":
    deslocamento = -deslocamento  # truque: só inverte o sinal!

resultado = ""  # aqui vamos construindo a resposta letra por letra

# 繰り返し (kurikaeshi) = repetição / loop
for letra in mensagem:

    if letra.isupper():  # Maiúscula? Faixa ASCII 65-90
        # Zera pro alfabeto (A=0), desloca, faz o wrap, volta pro ASCII
        nova = chr((ord(letra) - 65 + deslocamento) % 26 + 65)
        resultado += nova

    elif letra.islower():  # Minúscula? Faixa ASCII 97-122
        nova = chr((ord(letra) - 97 + deslocamento) % 26 + 97)
        resultado += nova

    else:
        # Número, espaço, símbolo? Deixa como está!
        # 変更なし (henkou nashi) = sem alteração
        resultado += letra

print(f"Resultado: {resultado}")