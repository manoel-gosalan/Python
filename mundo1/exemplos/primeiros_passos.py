# * ============================================================
# * PRIMEIROS PASSOS COM PYTHON
# * Python基礎 (Python Kiso)
# * ============================================================


# ? ─────────────────────────────────────────────
# ? PRINT E TIPOS BÁSICOS
# ? ─────────────────────────────────────────────
#
# Tudo entre aspas é STRING.
# Fora das aspas o Python interpreta como código.

print('Olá Mundo')     # string
print(7 + 4)           # soma matemática
print('7' + '4')       # concatenação


# * ─────────────────────────────────────────────
# * CONCATENAÇÃO
# * ─────────────────────────────────────────────
#
# String + String = concatenação

print('Curso' + 'Python')

# Com vírgula o Python separa automaticamente
print('Curso', 'Python')


# ? ─────────────────────────────────────────────
# ? VARIÁVEIS
# ? ─────────────────────────────────────────────
#
# Variáveis armazenam dados na memória.

nome = 'Gosalan'
idade = 28
peso = 106.3

print(nome, idade, peso)


# * ─────────────────────────────────────────────
# * INPUT()
# * ─────────────────────────────────────────────
#
# input() permite receber dados do usuário.
#
# IMPORTANTE:
# input() SEMPRE retorna string.

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print(nome, idade)


# ? ─────────────────────────────────────────────
# ? CONVERSÃO DE TIPOS
# ? ─────────────────────────────────────────────
#
# Para fazer cálculos é necessário converter.

idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))

print(type(idade))
print(type(peso))