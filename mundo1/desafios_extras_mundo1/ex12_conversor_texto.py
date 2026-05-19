# * =============================================================
# * EXERCICIO 12 - CONVERSOR DE TEXTO
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * テキスト変換 (tekisuto henkan) = conversao de texto
# * =============================================================


# ? ENUNCIADO:
# Crie um programa que funcione como uma ferramenta de transformacao
# de texto, com varios modos de conversao que o usuario pode escolher.


# ! O MENU DEVE OFERECER AS SEGUINTES CONVERSOES:
# TODO: 1. MAIUSCULAS      -> transforma todo o texto em maiusculo
# TODO: 2. minusculas      -> transforma todo o texto em minusculo
# TODO: 3. Capitalizado    -> Primeira Letra De Cada Palavra Em Maiusculo
# TODO: 4. Invertido       -> escreve o texto completamente de tras pra frente
# TODO: 5. snake_case      -> substitui espacos por underline, tudo minusculo
#                            exemplo: "meu texto aqui" -> "meu_texto_aqui"
# TODO: 6. Contar chars    -> exibe quantos caracteres o texto possui (com e sem espacos)

# ! REGRAS:
# O programa deve continuar rodando ate o usuario escolher sair
# Se o usuario digitar uma opcao invalida, avise e peca novamente


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Digite o texto: hello world python
#   Opcao: 5
#
# Output:
#   Resultado: hello_world_python
#
# Input:
#   Digite o texto: Python e demais
#   Opcao: 6
#
# Output:
#   Com espacos: 16 caracteres
#   Sem espacos: 14 caracteres


# * DICAS - ヒント (hint):
# .upper()              -> MAIUSCULAS
# .lower()              -> minusculas
# .title()              -> Capitalizado
# texto[::-1]           -> Invertido (slicing reverso)
# .replace(" ","_").lower() -> snake_case
# len(texto)            -> conta todos os chars
# len(texto.replace(" ", "")) -> conta sem espacos


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
