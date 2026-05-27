# * =============================================================
# * AULA 12 — CONDIÇÕES ANINHADAS
# * Curso de Python Mundo 2 — Gustavo Guanabara
# * =============================================================
# * 条件分岐 (jouken bunki) = Estruturas Condicionais
# * =============================================================

# ? INTRODUÇÃO
# Nessa aula aprendemos como o Python toma decisões.
#
# O programa pode seguir caminhos diferentes dependendo
# das condições definidas pelo desenvolvedor.
#
# Isso é extremamente importante em sistemas reais:
#
# - Login
# - Validação de idade
# - Sistemas bancários
# - Jogos
# - Inteligência artificial
# - APIs
# - Segurança
#
# Basicamente:
# Sem condições -> o programa seria apenas linear.

# * =============================================================
# * ESTRUTURA DAS CONDIÇÕES
# * =============================================================

# ? O Python trabalha com:
#
# if    -> se
# elif  -> senão se
# else  -> senão

# ? ESTRUTURA BASE:

# if condição:
#     bloco de código

# elif outra_condição:
#     outro bloco

# else:
#     bloco final

# ! IMPORTANTE:
# O Python lê de cima para baixo.
#
# Quando encontra uma condição verdadeira:
# -> ele EXECUTA
# -> e IGNORA o restante.

# * =============================================================
# * EXEMPLO 1 — SISTEMA DE NOTAS
# * =============================================================

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aluno aprovado!")

elif nota >= 5:
    print("Aluno em recuperação!")

else:
    print("Aluno reprovado!")

# ? EXPLICAÇÃO DETALHADA
#
# Se a nota for:
#
# >= 7
# -> aprovado
#
# >= 5 e < 7
# -> recuperação
#
# menor que 5
# -> reprovado

# ! OBSERVAÇÃO IMPORTANTE:
# O elif só é verificado caso o if seja falso.

# * =============================================================
# * FLUXO DE EXECUÇÃO
# * =============================================================

# ? Imagine:
#
# nota = 8
#
# O Python faz:
#
# if nota >= 7
# -> True
#
# Resultado:
# -> executa o print
# -> encerra a estrutura

# ! O elif e o else nem serão lidos nesse caso.

# * =============================================================
# * EXEMPLO 2 — CLASSIFICAÇÃO DE IDADE
# * =============================================================

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")

else:
    print("Idoso")

# ? EXPLICAÇÃO
#
# idade = 15
#
# Verificações:
#
# idade < 12
# -> False
#
# idade < 18
# -> True
#
# Resultado:
# -> Adolescente

# ! O restante será ignorado.

# * =============================================================
# * COMPARADORES LÓGICOS
# * =============================================================

# ==  -> igual
# !=  -> diferente
# >   -> maior
# <   -> menor
# >=  -> maior ou igual
# <=  -> menor ou igual

# ? EXEMPLOS:

numero = 10

print(numero == 10)
print(numero > 5)
print(numero != 7)

# * =============================================================
# * OPERADORES LÓGICOS
# * =============================================================

# and -> ambas precisam ser verdadeiras
# or  -> apenas uma precisa ser verdadeira
# not -> inverte o valor lógico

# * =============================================================
# * EXEMPLO COM AND
# * =============================================================

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado!")

else:
    print("Dados incorretos!")

# ? EXPLICAÇÃO
#
# O login só acontece se:
#
# usuario == "admin"
# E
# senha == "1234"

# ! As duas precisam ser verdadeiras.

# * =============================================================
# * EXEMPLO COM OR
# * =============================================================

dia = input("Digite o dia: ")

if dia == "sábado" or dia == "domingo":
    print("Final de semana!")

else:
    print("Dia útil!")

# ? EXPLICAÇÃO
#
# Basta UMA condição ser verdadeira.

# * =============================================================
# * EXEMPLO COM NOT
# * =============================================================

logado = False

if not logado:
    print("Usuário não autenticado!")

# ? EXPLICAÇÃO
#
# not False
# -> True

# * =============================================================
# * CONDIÇÕES ANINHADAS
# * =============================================================

# ? Condição aninhada:
# É quando existe um if dentro de outro if.

# * EXEMPLO:

idade = int(input("Digite sua idade: "))

if idade >= 18:

    print("Maior de idade")

    if idade >= 65:
        print("Idoso")

    else:
        print("Adulto")

else:
    print("Menor de idade")

# ? FLUXO
#
# Primeiro:
# -> verifica se é maior de idade
#
# Depois:
# -> verifica se é idoso

# ! Isso cria múltiplos níveis de decisão.

# * =============================================================
# * ERROS COMUNS
# * =============================================================

# ! 1 -> Esquecer os :
#
# if idade >= 18
#     print("Erro")

# ! Correto:
#
# if idade >= 18:
#     print("Correto")

# -------------------------------------------------------------

# ! 2 -> Erro de indentação
#
# Python usa indentação para organizar blocos.

# ERRADO:
#
# if True:
# print("Erro")

# CORRETO:
#
# if True:
#     print("Certo")

# -------------------------------------------------------------

# ! 3 -> Ordem errada das condições

idade = 20

# ERRADO:

if idade >= 0:
    print("Pessoa existente")

elif idade >= 18:
    print("Adulto")

# ? O elif nunca será executado
# porque a primeira condição já captura tudo.

# * =============================================================
# * BOAS PRÁTICAS
# * =============================================================

# ! Escreva condições simples
# ! Evite código duplicado
# ! Organize as verificações em ordem lógica
# ! Use nomes claros nas variáveis
# ! Evite muitos níveis de if

# * =============================================================
# * RESUMO DA AULA
# * =============================================================

# ? Você aprendeu:
#
# - Estruturas condicionais
# - if / elif / else
# - Fluxo de execução
# - Operadores relacionais
# - Operadores lógicos
# - Condições aninhadas
# - Indentação
# - Boas práticas
