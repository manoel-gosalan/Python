# * =============================================================
# * EXERCICIO 11 - GERADOR DE USERNAME
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * ユーザー名 (yuza mei) = username / nome de usuario
# * =============================================================


# ? ENUNCIADO:
# Crie um programa que gere automaticamente 5 sugestoes de
# username para o usuario se cadastrar em uma plataforma.


# ! O PROGRAMA DEVE:
# TODO: 1. Pedir o NOME COMPLETO do usuario
# TODO: 2. Pedir o ANO DE NASCIMENTO
# TODO: 3. Gerar e exibir 5 sugestoes de username usando as regras abaixo

# ! REGRAS DE GERACAO DOS USERNAMES:
# Sugestao 1: primeira letra do nome + sobrenome + ano
#             exemplo: "joao silva" + 2001 -> "jsilva2001"
#
# Sugestao 2: nome + underline + numero aleatorio entre 10 e 999
#             exemplo: "joao silva" -> "joao_742"
#
# Sugestao 3: sobrenome + underline + primeiras 3 letras do nome
#             exemplo: "joao silva" -> "silva_joa"
#
# Sugestao 4: nome completo sem espacos em minusculo
#             exemplo: "joao silva" -> "joaosilva"
#
# Sugestao 5: duas primeiras letras do nome + sobrenome + ano invertido
#             exemplo: "joao silva" + 2001 -> "josilva1002"


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Nome completo: Joao Silva
#   Ano de nascimento: 2001
#
# Output:
#   === Sugestoes de Username ===
#   1. jsilva2001
#   2. joao_742
#   3. silva_joa
#   4. joaosilva
#   5. josilva1002


# * DICAS - ヒント (hint):
# Use .split() para separar nome e sobrenome: partes = nome.split()
# partes[0] = primeiro nome | partes[-1] = sobrenome
# import random e use random.randint(10, 999) para o numero aleatorio
# Para inverter o ano: str(ano)[::-1]
# Use f-strings para montar os usernames: f"{partes[0][0]}{partes[-1]}{ano}"


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
