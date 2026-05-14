# * ============================================================
# * AULA — TIPOS PRIMITIVOS EM PYTHON
# * 基本データ型 (Kihon Dēta-gata)
# * Prof. Gustavo Guanabara | Curso em Vídeo
# * ============================================================


# ? ─────────────────────────────────────────────
# ? O QUE SÃO TIPOS PRIMITIVOS?
# ? 基本型とは？
# ? ─────────────────────────────────────────────
# ? Tipos primitivos são os tipos básicos de dados
# ? que o Python consegue armazenar.
# ? Pythonが扱う基本データ型です。
#
# Os principais da aula:
#
#   int   → números inteiros
#   float → números reais/quebrados
#   bool  → verdadeiro ou falso
#   str   → textos/string


# * ─────────────────────────────────────────────
# * TIPO INT / 整数型
# * ─────────────────────────────────────────────
#
# int = integer (número inteiro)

idade = 20
ano = 2026
temperatura = -5

print(type(idade))  # <class 'int'>


# ? ─────────────────────────────────────────────
# ? TIPO FLOAT / 小数型
# ? ─────────────────────────────────────────────
#
# float = números com ponto flutuante
# (números decimais)

altura = 1.80
saldo = 2500.75

print(type(altura))  # <class 'float'>


# * ─────────────────────────────────────────────
# * TIPO BOOL / 真偽値型
# * ─────────────────────────────────────────────
#
# bool = boolean
#
# Só possui 2 valores:
#   True
#   False

aprovado = True
banido = False

print(type(aprovado))  # <class 'bool'>


# ? ─────────────────────────────────────────────
# ? TIPO STR / 文字列型
# ? ─────────────────────────────────────────────
#
# str = string (texto)

nome = "Gosalan"
anime = "One Piece"

print(type(nome))  # <class 'str'>


# * ─────────────────────────────────────────────
# * O INPUT() SEMPRE RETORNA STRING
# * input()は常に文字列を返す
# * ─────────────────────────────────────────────
#
# Mesmo digitando número,
# o Python recebe TEXTO.

valor = input("Digite algo: ")

print(type(valor))  # str


# ? ─────────────────────────────────────────────
# ? CONVERTENDO TIPOS / 型変換
# ? ─────────────────────────────────────────────
#
# Conversão = casting
#
# MUITO usado no backend.

numero_int = int(input("Digite um número inteiro: "))
numero_float = float(input("Digite um decimal: "))

print(type(numero_int))
print(type(numero_float))


# * ─────────────────────────────────────────────
# * CONVERSÕES MAIS USADAS
# * よく使う型変換
# * ─────────────────────────────────────────────
#
# int()   → converte para inteiro
# float() → converte para decimal
# str()   → converte para texto
# bool()  → converte para boolean

numero = 10

print(float(numero))   # 10.0
print(str(numero))     # "10"


# ? ─────────────────────────────────────────────
# ? FUNÇÃO TYPE()
# ? type()関数
# ? ─────────────────────────────────────────────
#
# Mostra o tipo da variável.

nome = "Python"
idade = 20
altura = 1.75

print(type(nome))
print(type(idade))
print(type(altura))


# * ─────────────────────────────────────────────
# * OPERAÇÕES ENTRE TIPOS
# * 型同士の演算
# * ─────────────────────────────────────────────

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

soma = n1 + n2

print(f"A soma é {soma}")

# ! Sem converter:
#
# input() → str
#
# "10" + "10" = "1010"
#
# Isso se chama CONCATENAÇÃO.


# ? ─────────────────────────────────────────────
# ? CONCATENAÇÃO / 文字列連結
# ? ─────────────────────────────────────────────

nome = "Go"
sobrenome = "salan"

print(nome + sobrenome)  # Gosalan


# * ─────────────────────────────────────────────
# * MÉTODOS ÚTEIS PARA STRING
# * 便利な文字列メソッド
# * ─────────────────────────────────────────────
#
# isalpha()  → só letras?
# isnumeric() → só números?
# isalnum()  → letras e números?
# isupper()  → maiúsculas?
# islower()  → minúsculas?
# istitle()  → título?

texto = "Python"

print(texto.isalpha())  # True
print(texto.isupper())  # False


# ? ─────────────────────────────────────────────
# ? DICAS IMPORTANTES DA AULA
# ? 重要ポイント
# ? ─────────────────────────────────────────────
#
# ✔ input() SEMPRE retorna str
# ✔ type() mostra o tipo da variável
# ✔ int() converte para inteiro
# ✔ float() converte para decimal
# ✔ bool() trabalha com True/False
# ✔ str() representa textos
#
# Skills fundamentais:
#   → entrada de dados
#   → APIs
#   → backend
#   → automação
#   → validação de formulários
#   → banco de dados


# * ─────────────────────────────────────────────
# * RESUMO RÁPIDO / クイックサマリー
# * ─────────────────────────────────────────────
#
#   int    → inteiro
#   float  → decimal
#   bool   → True/False
#   str    → texto
#
# Conversões:
#
#   int("10")      → 10
#   float("5.5")   → 5.5
#   str(100)       → "100"
#   bool(1)        → True
#
# Funções importantes:
#
#   input() → recebe entrada
#   type()  → mostra tipo
#
# Conceito EXTREMAMENTE importante:
#
#   input() → sempre retorna str
#
# Isso é base para praticamente TODO backend.
#
# * がんばって！ (Ganbatte!) 🎌
#
# Entender tipos primitivos é o primeiro passo
# para começar a pensar como DEV de verdade.