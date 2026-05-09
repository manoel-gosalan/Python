# * ============================================================
# * AULA 08 - MÓDULOS E IMPORTAÇÕES EM PYTHON
# * モジュールとインポート (Mojūru to Inpōto)
# * Prof. Gustavo Guanabara | Curso em Vídeo
# * Resumo feito pelo Sensei Claude 先生 🎌
# * ============================================================


# ? ─────────────────────────────────────────────
# ? O QUE É UM MÓDULO? / モジュールとは何ですか？
# ? ─────────────────────────────────────────────
# ? Um módulo é um arquivo .py que contém funções,
# ? variáveis e classes que podemos REUTILIZAR.
# ? モジュールは再利用できる .py ファイルです。
#
# Tipos de módulos / モジュールの種類:
#   1. Built-in    → já vem com o Python
#   2. Externos    → instalados via pip
#   3. Próprios    → criados por você mesmo
# ?────────────────────────────────────────────────


# * ─────────────────────────────────────────────
# * FORMA 1: import <módulo>
# * インポートの方法１
# * ─────────────────────────────────────────────
import math
import random
import datetime

# Usando com o nome do módulo na frente
raiz = math.sqrt(25)          # √25 = 5.0
pi   = math.pi                # 3.141592...
piso = math.floor(4.9)        # → 4  (arredonda pra baixo)
teto = math.ceil(4.1)         # → 5  (arredonda pra cima)

print(f"√25 = {raiz}")
print(f"PI  = {pi:.4f}")
print(f"floor(4.9) = {piso} | ceil(4.1) = {teto}")


# * ─────────────────────────────────────────────
# * FORMA 2: from <módulo> import <função>
# * インポートの方法２ — 関数を直接呼ぶ
# * ─────────────────────────────────────────────
from math import sqrt, pow, factorial

# Agora usa SEM o prefixo "math."
resultado = sqrt(144)     # → 12.0
potencia  = pow(2, 10)    # → 1024.0  (2^10)
fat       = factorial(5)  # → 120     (5! = 5×4×3×2×1)

print(f"\nsqrt(144)   = {resultado}")
print(f"2^10        = {int(potencia)}")
print(f"5!          = {fat}")


# * ─────────────────────────────────────────────
# * FORMA 3: import <módulo> as <apelido>
# * インポートの方法３ — 別名（エイリアス）
# * ─────────────────────────────────────────────
import random as rd
import datetime as dt

# "rd" e "dt" são apelidos (aliases) / エイリアス
numero_aleatorio = rd.randint(1, 10)    # número entre 1 e 10
hoje = dt.date.today()                  # data de hoje

print(f"\nNúmero aleatório: {numero_aleatorio}")
print(f"Hoje é:           {hoje}")


# * ─────────────────────────────────────────────
# * FORMA 4: from <módulo> import * (EVITAR!)
# * インポートの方法４ — 使わない方がいい！
# * ─────────────────────────────────────────────
# ! ATENÇÃO: importa TUDO do módulo — perigoso!
# ! 警告: 全部インポートする — 名前の衝突に注意！
# ! Pode sobrescrever funções existentes no código.
#
#   from math import *   ← evite isso!
#
# ! Use apenas quando tiver certeza do que está fazendo.


# ? ─────────────────────────────────────────────
# ? MÓDULO: random  /  ランダムモジュール
# ? ─────────────────────────────────────────────
print("\n── random ──")

# random.random()       → float entre 0.0 e 1.0
# random.randint(a, b)  → inteiro entre a e b (inclusive)
# random.choice(lista)  → escolhe 1 item aleatório
# random.shuffle(lista) → embaralha a lista (in-place)
# random.sample(lista, k) → k itens únicos aleatórios

frutas = ["maçã", "banana", "uva", "kiwi", "manga"]
print(f"Fruta sorteada: {random.choice(frutas)}")

random.shuffle(frutas)
print(f"Lista embaralhada: {frutas}")

amostra = random.sample(frutas, 3)
print(f"Amostra de 3: {amostra}")


# ? ─────────────────────────────────────────────
# ? MÓDULO: datetime  /  日付モジュール
# ? ─────────────────────────────────────────────
print("\n── datetime ──")

agora   = datetime.datetime.now()    # data E hora atual
hoje    = datetime.date.today()      # só a data
hora    = datetime.time(10, 30, 0)   # hora fixa: 10:30:00

# Formatação com strftime (string format time)
# 書式設定 — よく使われるコード：
#   %d → dia    %m → mês    %Y → ano (4 dígitos)
#   %H → hora   %M → minuto %S → segundo
formatado = agora.strftime("%d/%m/%Y às %H:%M")
print(f"Data formatada: {formatado}")

# Cálculo com datas / 日付の計算
intercambio = datetime.date(2029, 4, 1)     # 🎌 meta de intercâmbio!
dias_faltam = (intercambio - hoje).days
print(f"Dias para o intercâmbio no Japão: {dias_faltam} dias 🇯🇵")


# ? ─────────────────────────────────────────────
# ? MÓDULO: os  /  OSモジュール
# ? ─────────────────────────────────────────────
import os

print("\n── os ──")
diretorio_atual = os.getcwd()         # pasta atual / 現在のフォルダ
lista_arquivos  = os.listdir(".")     # lista de arquivos
sistema         = os.name             # 'nt' (Windows) ou 'posix' (Linux/Mac)

print(f"Diretório atual: {diretorio_atual}")
print(f"Sistema:         {sistema}")


# ? ─────────────────────────────────────────────
# ? MÓDULO: sys  /  SYSモジュール
# ? ─────────────────────────────────────────────
import sys

print("\n── sys ──")
print(f"Versão do Python: {sys.version[:6]}")
print(f"Plataforma:       {sys.platform}")


# * ─────────────────────────────────────────────
# * CRIANDO SEU PRÓPRIO MÓDULO
# * 自分のモジュールを作る
# * ─────────────────────────────────────────────
#
# Basta criar um arquivo .py separado, por exemplo:
#
#   ── meu_modulo.py ────────────────
#   def saudar(nome):
#       return f"Olá, {nome}! こんにちは！"
#
#   PI_PROPRIO = 3.14159
#   ─────────────────────────────────
#
# E importar no seu script principal:
#   import meu_modulo
#   print(meu_modulo.saudar("Sensei"))
#
# ou:
#   from meu_modulo import saudar
#   print(saudar("Sensei"))


# * ─────────────────────────────────────────────
# * VARIÁVEL ESPECIAL: __name__
# * 特別な変数: __name__
# * ─────────────────────────────────────────────
#
# Todo arquivo Python tem a variável __name__.
# すべてのPythonファイルに __name__ 変数があります。
#
# → Se o arquivo for executado DIRETAMENTE:
#       __name__ == "__main__"
#
# → Se for importado por outro módulo:
#       __name__ == "nome_do_arquivo"
#
# Isso permite proteger código de execução acidental:

if __name__ == "__main__":
    print("\n── Executando diretamente ──")
    print("Este bloco SÓ roda quando o script é o principal!")
    print("直接実行している場合のみ動作します！")


# * ─────────────────────────────────────────────
# * RESUMO RÁPIDO / クイックサマリー
# * ─────────────────────────────────────────────
#
#   import math                    → usa: math.sqrt()
#   from math import sqrt          → usa: sqrt()
#   from math import sqrt as raiz  → usa: raiz()
#   import math as m               → usa: m.sqrt()
#   from math import *             → usa: sqrt() ← EVITAR!
#
#   Módulos úteis da aula:
#   ┌──────────────┬──────────────────────────────┐
#   │   math       │  funções matemáticas          │
#   │   random     │  aleatoriedade                │
#   │   datetime   │  datas e horas                │
#   │   os         │  sistema operacional          │
#   │   sys        │  interpretador Python         │
#   └──────────────┴──────────────────────────────┘
#
# * がんばって！ (Ganbatte! = Boa sorte / vai com tudo!) 🎌