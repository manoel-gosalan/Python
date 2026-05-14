# * ============================================================
# * AULA 10 — CONDIÇÕES EM PYTHON (PARTE 1)
# * 条件文 (Jōkenbun)
# * Prof. Gustavo Guanabara | Curso em Vídeo
# * ============================================================


# ? ─────────────────────────────────────────────
# ? O QUE SÃO CONDIÇÕES? / 条件とは？
# ? ─────────────────────────────────────────────
# ? Condições permitem que o programa tome decisões.
# ? 条件によってプログラムが動作を変えます。
#
# O Python analisa se uma expressão é:
#   → True  (Verdadeiro)
#   → False (Falso)
#
# Base de praticamente TODO sistema:
#   → login
#   → permissões
#   → validações
#   → menus
#   → APIs
#   → jogos
#   → automações


# * ─────────────────────────────────────────────
# * ESTRUTURA BÁSICA DO IF
# * if文の基本構造
# * ─────────────────────────────────────────────

idade = 18

if idade >= 18:
    print("Maior de idade")

# ! IMPORTANTE:
# ! Python usa INDENTAÇÃO para definir blocos.
# ! インデントが超重要！
#
# Sem indentação correta → ERROR


# ? ─────────────────────────────────────────────
# ? OPERADORES RELACIONAIS / 比較演算子
# ? ─────────────────────────────────────────────
#
#   >    maior que
#   <    menor que
#   >=   maior ou igual
#   <=   menor ou igual
#   ==   igual
#   !=   diferente

numero = 10

print(numero > 5)     # True
print(numero < 5)     # False
print(numero == 10)   # True
print(numero != 7)    # True


# * ─────────────────────────────────────────────
# * CONDIÇÃO COM ELSE
# * else文
# * ─────────────────────────────────────────────

nota = 5.5

if nota >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

# else:
# → executa quando o if for False


# ? ─────────────────────────────────────────────
# ? CONDIÇÕES SIMPLES E COMPOSTAS
# ? 単純条件と複合条件
# ? ─────────────────────────────────────────────
#
# Condição simples:
#
#   if condição:
#       bloco
#
# Condição composta:
#
#   if condição:
#       bloco_true
#   else:
#       bloco_false


# * ─────────────────────────────────────────────
# * EXEMPLO PRÁTICO — VELOCIDADE
# * 実用例 — スピードチェック
# * ─────────────────────────────────────────────

velocidade = 85

if velocidade > 80:
    print("MULTADO! Você ultrapassou o limite.")

print("Dirija com segurança!")

# ! Mesmo que o IF não execute,
# ! o código fora dele continua normalmente.


# ? ─────────────────────────────────────────────
# ? OPERADORES LÓGICOS / 論理演算子
# ? ─────────────────────────────────────────────
#
# and → E
# or  → OU
# not → NÃO
#
# MUITO usado em backend e autenticação.

idade = 20
tem_cartao = True

if idade >= 18 and tem_cartao:
    print("Entrada permitida")


# * ─────────────────────────────────────────────
# * OPERADOR AND
# * AND演算子
# * ─────────────────────────────────────────────
#
# Só retorna True se TUDO for verdadeiro.

usuario = "gosalan"
senha = "1234"

if usuario == "gosalan" and senha == "1234":
    print("Login realizado")


# ? ─────────────────────────────────────────────
# ? OPERADOR OR
# ? OR演算子
# ? ─────────────────────────────────────────────
#
# Retorna True se PELO MENOS UM for verdadeiro.

dia = "domingo"

if dia == "sábado" or dia == "domingo":
    print("Fim de semana")


# * ─────────────────────────────────────────────
# * OPERADOR NOT
# * NOT演算子
# * ─────────────────────────────────────────────
#
# Inverte o valor lógico.

logado = False

if not logado:
    print("Usuário precisa fazer login")


# ? ─────────────────────────────────────────────
# ? CONDIÇÕES ANINHADAS (INTRODUÇÃO)
# ? ネストされた条件
# ? ─────────────────────────────────────────────
#
# Uma condição dentro da outra.

idade = 19
tem_documento = True

if idade >= 18:
    if tem_documento:
        print("Entrada autorizada")


# * ─────────────────────────────────────────────
# * VALORES BOOLEANOS / 真偽値
# * ─────────────────────────────────────────────
#
# True  → verdadeiro
# False → falso
#
# Tipo boolean:
#
#   bool

ativo = True
banido = False

print(type(ativo))   # <class 'bool'>


# ? ─────────────────────────────────────────────
# ? INPUT + CONDIÇÕES
# ? 入力と条件
# ? ─────────────────────────────────────────────

nome = input("Digite seu nome: ")

if nome == "Gosalan":
    print("Nome reconhecido!")
else:
    print("Usuário diferente")


# * ─────────────────────────────────────────────
# * CUIDADO COM INPUT()
# * input()の注意点
# * ─────────────────────────────────────────────
#
# input() SEMPRE retorna STRING.
#
# Então isso aqui:
#
#   idade = input()
#
# NÃO vira int automaticamente.
#
# Precisa converter:
#
#   idade = int(input("Idade: "))


# ? ─────────────────────────────────────────────
# ? EXPRESSÕES BOOLEANAS
# ? ブール式
# ? ─────────────────────────────────────────────

saldo = 500
saque = 200

print(saque <= saldo)  # True

# O resultado da comparação já é um boolean.


# * ─────────────────────────────────────────────
# * TERNÁRIO (INTRODUÇÃO)
# * 三項演算子
# * ─────────────────────────────────────────────
#
# Forma curta de condição:
#
# valor_true if condição else valor_false

idade = 17

status = "Maior" if idade >= 18 else "Menor"

print(status)


# ? ─────────────────────────────────────────────
# ? DICAS IMPORTANTES DA AULA
# ? 重要ポイント
# ? ─────────────────────────────────────────────
#
# ✔ Python usa indentação obrigatória
# ✔ Condições retornam True ou False
# ✔ if executa apenas se for True
# ✔ else executa quando for False
# ✔ and exige tudo verdadeiro
# ✔ or exige pelo menos um verdadeiro
# ✔ not inverte o boolean
# ✔ bool é MUITO usado em sistemas reais
#
# Exemplos reais:
#   → login
#   → autenticação JWT
#   → permissões admin
#   → validação de idade
#   → gateways de pagamento
#   → menus de sistema
#   → IA tomando decisões


# * ─────────────────────────────────────────────
# * RESUMO RÁPIDO / クイックサマリー
# * ─────────────────────────────────────────────
#
#   if condição:
#       bloco
#
#   if condição:
#       bloco_true
#   else:
#       bloco_false
#
# Operadores:
#   ┌──────────────┬────────────────────┐
#   │ ==           │ igual              │
#   │ !=           │ diferente          │
#   │ >            │ maior              │
#   │ <            │ menor              │
#   │ >=           │ maior ou igual     │
#   │ <=           │ menor ou igual     │
#   └──────────────┴────────────────────┘
#
# Operadores lógicos:
#   ┌──────────────┬────────────────────┐
#   │ and          │ E                  │
#   │ or           │ OU                 │
#   │ not          │ NÃO                │
#   └──────────────┴────────────────────┘
#
# Fluxo mental do backend:
#
#   entrada → validação → decisão → resposta
#
# Isso é literalmente a base de APIs, jogos,
# automações e sistemas profissionais.
#
# * がんばって！ (Ganbatte!) 🎌
#