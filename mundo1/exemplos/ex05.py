# * ============================================================
# * AULA 09 — MANIPULANDO TEXTO EM PYTHON
# * 文字列操作 (Mojiretsu Sōsa)
# * Prof. Gustavo Guanabara | Curso em Vídeo
# * ============================================================


# ? ─────────────────────────────────────────────
# ? O QUE É UMA STRING? / 文字列とは？
# ? ─────────────────────────────────────────────
# ? String = sequência de caracteres (texto)
# ? Python trata textos como OBJETOS.
# ? 文字列は文字の並びです。
#
# Exemplos:
nome = "Gosalan"
frase = "Curso em Vídeo Python"

print(nome)
print(frase)


# * ─────────────────────────────────────────────
# * FATIAMENTO DE STRING / スライス
# * ─────────────────────────────────────────────
#
# Cada caractere possui um índice:
#
#  G  o  s  a  l  a  n
#  0  1  2  3  4  5  6
#
# Sintaxe:
#   texto[inicio:fim:passo]
#
# OBS:
# → o último índice NÃO entra
# → fim é EXCLUSIVO

texto = "CursoPython"

print(texto[0])        # C
print(texto[0:5])      # Curso
print(texto[5:11])     # Python
print(texto[:5])       # Curso
print(texto[5:])       # Python
print(texto[::2])      # CroPto (pulando de 2 em 2)


# ? ─────────────────────────────────────────────
# ? ANALISANDO STRINGS / 文字列解析
# ? ─────────────────────────────────────────────

frase = "Curso em Vídeo Python"

# len() → tamanho da string
print(len(frase))

# count() → conta quantas vezes aparece algo
print(frase.count("o"))

# find() → encontra posição
print(frase.find("Vídeo"))

# in → verifica se existe
print("Python" in frase)

# lower() → tudo minúsculo
print(frase.lower())

# upper() → tudo maiúsculo
print(frase.upper())

# capitalize() → primeira letra maiúscula
print(frase.capitalize())

# title() → primeira letra de cada palavra maiúscula
print(frase.title())


# * ─────────────────────────────────────────────
# * REMOVENDO ESPAÇOS / 空白を削除する
# * ─────────────────────────────────────────────

frase2 = "   Python Sensei   "

# strip() → remove espaços dos lados
print(frase2.strip())

# rstrip() → remove espaços da direita
print(frase2.rstrip())

# lstrip() → remove espaços da esquerda
print(frase2.lstrip())


# ? ─────────────────────────────────────────────
# ? DIVIDINDO STRINGS / 分割
# ? ─────────────────────────────────────────────

frase3 = "Curso em Vídeo Python"

# split() → divide em lista
lista = frase3.split()

print(lista)
print(lista[0])
print(lista[2])


# * ─────────────────────────────────────────────
# * JUNTANDO STRINGS / 結合
# * ─────────────────────────────────────────────

palavras = ["Curso", "em", "Vídeo"]

# join() → junta usando separador
junto = "-".join(palavras)

print(junto)


# ? ─────────────────────────────────────────────
# ? SUBSTITUINDO TEXTO / 置換
# ? ─────────────────────────────────────────────

frase4 = "Curso em Vídeo"

# replace() → troca partes da string
nova = frase4.replace("Vídeo", "Python")

print(nova)


# * ─────────────────────────────────────────────
# * STRINGS SÃO IMUTÁVEIS
# * 文字列は変更できない
# * ─────────────────────────────────────────────
#
# Isso aqui NÃO altera a string original:
#
# frase.replace("Python", "Java")
#
# Você precisa salvar:
#
# frase = frase.replace("Python", "Java")


# ? ─────────────────────────────────────────────
# ? MULTILINE / TEXTO GRANDE
# ? 複数行テキスト
# ? ─────────────────────────────────────────────

texto_grande = """
Python é muito usado
em automação, backend,
IA, dados e games.
"""

print(texto_grande)


# * ─────────────────────────────────────────────
# * ESCAPE CHARACTERS / 特殊文字
# * ─────────────────────────────────────────────
#
# \n → quebra linha
# \t → tabulação
# \\ → barra invertida
# \' → aspas simples
# \" → aspas duplas

print("Linha 1\nLinha 2")
print("Python\tSensei")


# ? ─────────────────────────────────────────────
# ? FORMATANDO STRINGS / フォーマット
# ? ─────────────────────────────────────────────

nome = "Gosalan"
idade = 20

# Forma antiga
print("Meu nome é {} e tenho {} anos".format(nome, idade))

# f-string (mais moderna e usada hoje)
print(f"Meu nome é {nome} e tenho {idade} anos")


# * ─────────────────────────────────────────────
# * COMPARAÇÃO DE STRINGS
# * 文字列比較
# * ─────────────────────────────────────────────

print("Python" == "python")   # False
print("Python".lower() == "python")  # True


# ? ─────────────────────────────────────────────
# ? DICAS IMPORTANTES DA AULA
# ? 重要ポイント
# ? ─────────────────────────────────────────────
#
# ✔ Strings funcionam como arrays/listas de letras
# ✔ Índices começam no 0
# ✔ O último índice do slice NÃO entra
# ✔ Métodos NÃO alteram a string original
# ✔ Strings são MUITO usadas em backend e APIs
# ✔ Saber manipular texto é skill obrigatória pra DEV
#
# Exemplos reais:
#   → validar email
#   → tratar entrada do usuário
#   → parser de arquivos
#   → chatbot
#   → automação
#   → scraping
#   → APIs REST


# * ─────────────────────────────────────────────
# * RESUMO RÁPIDO / クイックサマリー
# * ─────────────────────────────────────────────
#
#   texto[0]        → pega caractere
#   texto[1:5]      → fatia string
#   len(texto)      → tamanho
#   texto.count()   → contar
#   texto.find()    → encontrar
#   texto.replace() → substituir
#   texto.split()   → dividir
#   "-".join(lista) → juntar
#   texto.upper()   → maiúsculo
#   texto.lower()   → minúsculo
#   texto.strip()   → remover espaços
#
# Métodos MUITO usados no mercado:
#   ┌──────────────────────┬────────────────────┐
#   │ lower()              │ minúsculo          │
#   │ upper()              │ maiúsculo          │
#   │ split()              │ dividir texto      │
#   │ join()               │ juntar texto       │
#   │ replace()            │ substituir         │
#   │ strip()              │ limpar espaços     │
#   │ find()               │ encontrar posição  │
#   └──────────────────────┴────────────────────┘
#
# * がんばって！ (Ganbatte!) 🎌
#
# Manipulação de texto é uma das skills MAIS importantes
# para backend, automação e desenvolvimento profissional.
#
# Quem domina string domina metade do backend.