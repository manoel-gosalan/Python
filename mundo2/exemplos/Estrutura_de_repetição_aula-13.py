# * =============================================================
# * AULA 13 - ESTRUTURA DE REPETIÇÃO FOR
# * Curso em Vídeo - Python Mundo 2
# * Professor: Gustavo Guanabara
# * =============================================================
# * 繰り返し (kurikaeshi) = repetição
# * ループ (ruupu) = loop
# * 回数 (kaisuu) = quantidade de vezes
# * 範囲 (hani) = intervalo/faixa
# * =============================================================

# ? O QUE É O FOR?

# * A estrutura FOR é usada quando sabemos quantas vezes
# * uma ação deverá ser repetida.

# * Exemplo:
# * "Mostre uma mensagem 10 vezes"
# * "Conte de 1 até 100"
# * "Percorra uma sequência"

# =============================================================
# ? SINTAXE BÁSICA
# =============================================================

for c in range(1, 6):
    print("Olá")

# * Saída:
# * Olá
# * Olá
# * Olá
# * Olá
# * Olá

# ! O último número não é incluído.
# * range(1, 6) -> vai de 1 até 5

# =============================================================
# ? FUNCIONAMENTO DO RANGE()
# =============================================================

# * range(inicio, fim)

for c in range(1, 6):
    print(c)

# * Resultado:
# * 1
# * 2
# * 3
# * 4
# * 5

# -------------------------------------------------------------

# * range(0, 5)

for c in range(0, 5):
    print(c)

# * Resultado:
# * 0 1 2 3 4

# -------------------------------------------------------------

# * range(6, 0, -1)

for c in range(6, 0, -1):
    print(c)

# * Resultado:
# * 6 5 4 3 2 1

# * O terceiro parâmetro define o passo.

# -------------------------------------------------------------

# * range(0, 11, 2)

for c in range(0, 11, 2):
    print(c)

# * Resultado:
# * 0 2 4 6 8 10

# =============================================================
# ? CONTAGEM REGRESSIVA
# =============================================================

for c in range(10, 0, -1):
    print(c)

print("BUM! BUM! POOOW!")

# * Muito usado para cronômetros e contagens regressivas.

# =============================================================
# ? USANDO INPUT DENTRO DO FOR
# =============================================================

n = int(input("Digite um número: "))

for c in range(0, n + 1):
    print(c)

# * O usuário escolhe até onde a repetição vai.

# =============================================================
# ? SOMANDO VALORES
# =============================================================

soma = 0

for c in range(1, 6):
    n = int(input("Digite um valor: "))
    soma += n

print(f"A soma foi {soma}")

# * Muito usado para acumular resultados.

# =============================================================
# ? CONTADOR E ACUMULADOR
# =============================================================

# * CONTADOR
# * Conta quantas vezes algo aconteceu.

contador = 0

for c in range(5):
    numero = int(input("Número: "))

    if numero % 2 == 0:
        contador += 1

print(contador)

# -------------------------------------------------------------

# * ACUMULADOR
# * Guarda e soma valores.

acumulador = 0

for c in range(5):
    valor = int(input("Valor: "))
    acumulador += valor

print(acumulador)

# =============================================================
# ? PRINCIPAIS CONCEITOS DA AULA
# =============================================================

# TODO Aprender a usar FOR para repetições controladas.
# TODO Entender o funcionamento do range().
# TODO Fazer contagens crescentes.
# TODO Fazer contagens regressivas.
# TODO Utilizar passo positivo e negativo.
# TODO Receber valores durante a repetição.
# TODO Criar acumuladores.
# TODO Criar contadores.
# TODO Resolver problemas matemáticos usando laços.

# =============================================================
# ? MACETE DE DEV
# =============================================================

# * Sempre leia o range() assim:

# * range(inicio, fim, passo)

# * Exemplo:
# * range(1, 11, 1)

# * Tradução:
# * Comece em 1
# * Vá até antes do 11
# * Pulando de 1 em 1

# =============================================================
# ? RESUMO DO SENSEI
# =============================================================

# * FOR = repetir um número conhecido de vezes.
# * RANGE = define o intervalo da repetição.
# * PASSO = controla o tamanho do salto.
# * CONTADOR = conta ocorrências.
# * ACUMULADOR = soma ou acumula valores.
# * FOR + RANGE é uma das combinações mais usadas
# * em Python e aparece constantemente em lógica,
# * algoritmos, automação e desenvolvimento profissional.

# =============================================================