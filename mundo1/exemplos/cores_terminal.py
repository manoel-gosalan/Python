# * ============================================================
# * AULA 11 — CORES NO TERMINAL
# * ターミナルの色 (Tāminaru no Iro)
# * Prof. Gustavo Guanabara | Curso em Vídeo
# * ============================================================


# ? ─────────────────────────────────────────────
# ? O QUE SÃO ANSI ESCAPE CODES?
# ? ANSIエスケープコードとは？
# ? ─────────────────────────────────────────────
#
# ? ANSI Escape Codes são códigos especiais usados
# ? para alterar cores e estilos no terminal.
# ?
# ? Eles permitem:
# ? - mudar cor do texto
# ? - mudar cor do fundo
# ? - aplicar estilos (bold, underline...)
# ?
# ? ANSIコードでターミナルの色やスタイルを変更できます。
#
# Estrutura:
#
# \033[style;text;backgroundm
#
# Onde:
#   style      -> estilo do texto
#   text       -> cor da fonte
#   background -> cor de fundo
#
# Exemplo:
# \033[1;31;43m
#
#   1  -> bold
#   31 -> vermelho
#   43 -> fundo amarelo


# * ─────────────────────────────────────────────
# * RESETANDO A COR
# * リセット
# * ─────────────────────────────────────────────
#
# Para voltar ao normal:
#
# \033[m
#
# ou:
#
# \033[0;0;0m

print("\033[31mTexto Vermelho\033[m")
print("Texto normal")


# ? ─────────────────────────────────────────────
# ? ESTILOS DE TEXTO
# ? テキストスタイル
# ? ─────────────────────────────────────────────
#
# Código | Estilo
# ─────────────────
#   0    | none/reset
#   1    | bold
#   4    | underline
#   7    | negative/invertido

print("\033[1mTexto Bold\033[m")
print("\033[4mTexto Sublinhado\033[m")
print("\033[7mTexto Invertido\033[m")


# * ─────────────────────────────────────────────
# * CORES DE TEXTO
# * 文字色
# * ─────────────────────────────────────────────
#
# Código | Cor
# ─────────────────
#   30    | branco/cinza
#   31    | vermelho
#   32    | verde
#   33    | amarelo
#   34    | azul
#   35    | roxo
#   36    | ciano
#   37    | branco

print("\033[31mVermelho\033[m")
print("\033[32mVerde\033[m")
print("\033[34mAzul\033[m")


# ? ─────────────────────────────────────────────
# ? CORES DE FUNDO
# ? 背景色
# ? ─────────────────────────────────────────────
#
# Código | Fundo
# ─────────────────
#   40    | branco/preto
#   41    | vermelho
#   42    | verde
#   43    | amarelo
#   44    | azul
#   45    | roxo
#   46    | ciano
#   47    | branco

print("\033[30;41mTexto Preto Fundo Vermelho\033[m")
print("\033[33;44mTexto Amarelo Fundo Azul\033[m")


# * ─────────────────────────────────────────────
# * COMBINANDO ESTILOS E CORES
# * 組み合わせ
# * ─────────────────────────────────────────────

print("\033[1;32;40mTexto Verde Bold\033[m")
print("\033[4;35;47mTexto Roxo Sublinhado\033[m")


# ? ─────────────────────────────────────────────
# ? USANDO COM f-strings
# ? f文字列で使う
# ? ─────────────────────────────────────────────

nome = "Gosalan"

print(f"\033[1;34mPrazer em te conhecer, {nome}!\033[m")


# * ─────────────────────────────────────────────
# * DICIONÁRIO DE CORES
# * 色辞書
# * ─────────────────────────────────────────────
#
# Técnica MUITO usada para organizar cores.

cores = {
    "limpa": "\033[m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "bold": "\033[1m"
}

print(f"{cores['verde']}Texto Verde{cores['limpa']}")
print(f"{cores['bold']}Texto Bold{cores['limpa']}")


# ? ─────────────────────────────────────────────
# ? EXEMPLO PRÁTICO
# ? 実用例
# ? ─────────────────────────────────────────────

nome = "Sensei"

print(f"\033[1;32mOlá, {nome}!\033[m")
print(f"\033[1;31mErro encontrado!\033[m")
print(f"\033[1;33mAviso importante!\033[m")


# * ─────────────────────────────────────────────
# * OBSERVAÇÃO IMPORTANTE
# * 重要な注意
# * ─────────────────────────────────────────────
#
# Alguns terminais antigos podem não interpretar
# ANSI corretamente.
#
# Hoje:
# ✔ VS Code Terminal
# ✔ Linux
# ✔ MacOS
# ✔ Windows Terminal
#
# funcionam normalmente.


# ? ─────────────────────────────────────────────
# ? BIBLIOTECA COLORAMA
# ? Coloramaライブラリ
# ? ─────────────────────────────────────────────
#
# Biblioteca MUITO usada no mercado para cores.
#
# Instalação:
#
# pip install colorama
#
# Exemplo:

# from colorama import Fore, Style
#
# print(Fore.RED + "Texto vermelho")
# print(Style.RESET_ALL)

# NOTE:
# Colorama melhora compatibilidade no Windows.


# * ─────────────────────────────────────────────
# * CASOS REAIS NO MERCADO
# * 実際の使用例
# * ─────────────────────────────────────────────
#
# Cores são usadas para:
#
# ✔ Logs
# ✔ CLIs
# ✔ Scripts DevOps
# ✔ Ferramentas backend
# ✔ Monitoramento
# ✔ Mensagens de erro
# ✔ Sistemas de deploy
#
# Exemplos:
#
# Verde   -> sucesso
# Vermelho -> erro
# Amarelo -> alerta
# Azul -> informação


# ? ─────────────────────────────────────────────
# ? RESUMO RÁPIDO / クイックサマリー
# ? ─────────────────────────────────────────────
#
# Estrutura ANSI:
#
# \033[style;text;backgroundm
#
# RESET:
# \033[m
#
# Estilos:
#   0 -> reset
#   1 -> bold
#   4 -> underline
#   7 -> invertido
#
# Texto:
#   30-37
#
# Fundo:
#   40-47
#
# Exemplo:
#
# \033[1;31;43m
#
# 1  -> bold
# 31 -> vermelho
# 43 -> fundo amarelo
#
# Colorama:
# pip install colorama
#
# * がんばって！ (Ganbatte!) 🎌
