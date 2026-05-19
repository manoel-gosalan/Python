# * =============================================================
# * EXERCICIO 17 - DETECTOR DE PALINDROMO
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 回文 (kaimon) = palindromo (palavra que le igual dos dois lados)
# * =============================================================


# ? ENUNCIADO:
# Um palindromo e uma palavra ou frase que pode ser lida da mesma
# forma tanto da esquerda pra direita quanto da direita pra esquerda.
# Crie um programa robusto que detecte palindromos, ignorando
# espacos, pontuacao e diferenca entre maiusculas e minusculas.


# ! EXEMPLOS DE PALINDROMOS:
# Palavras: arara | radar | ana | ovo | civic
# Frases:   "A sacada da casa"  -> limpo: "asacadadacasa"  -> palindromo
#           "Socorram-me subi no onibus em Marrocos" -> palindromo


# ! O PROGRAMA DEVE:
# TODO: 1. Receber uma PALAVRA ou FRASE do usuario
# TODO: 2. LIMPAR o texto: remover espacos, pontuacao, deixar tudo minusculo
# TODO: 3. Verificar se o texto limpo E ou NAO E um palindromo
# TODO: 4. Exibir o TEXTO LIMPO que foi analisado (para o usuario entender)
# TODO: 5. Continuar pedindo novas entradas ate o usuario digitar "sair"


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:  arara
#   Texto analisado: arara
#   "arara" E um palindromo!
#
# Input:  A sacada da casa
#   Texto analisado: asacadadacasa
#   "A sacada da casa" E um palindromo!
#
# Input:  python
#   Texto analisado: python
#   "python" NAO e um palindromo.
#
# Input:  sair
#   Encerrando...


# * DICAS - ヒント (hint):
# Para verificar palindromo: texto_limpo == texto_limpo[::-1]
#
# Para limpar o texto (metodo 1 - mais simples):
#   texto_limpo = ""
#   for char in texto.lower():
#       if char.isalpha():
#           texto_limpo += char
#
# Para limpar o texto (metodo 2 - mais avancado, com regex):
#   import re
#   texto_limpo = re.sub(r'[^a-zA-Z]', '', texto).lower()
#   (obs: o metodo 2 nao funciona bem com acentos - tente o metodo 1 primeiro)


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
