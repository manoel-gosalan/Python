# ==================================================
# ! DESAFIO 04 — ANÁLISE DE STRING
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler qualquer valor digitado pelo usuário
# e analisar suas características
# --------------------------------------------------

# NOTE:
# input() SEMPRE retorna uma string (str)
# mesmo que o usuário digite números

algo = input("Digite algo: ")

# --------------------------------------------------
# ? Exibição principal
# --------------------------------------------------
print("Analisando o valor: '{}'".format(algo))

# --------------------------------------------------
# ? Verificações de texto
# --------------------------------------------------

# Verifica se possui apenas letras
print("isalpha()   → Só letras:                    ", algo.isalpha())

# Verifica se possui apenas números
print("isnumeric() → Apenas números:               ", algo.isnumeric())

# Verifica se possui letras e números
print("isalnum()   → Letras e números:             ", algo.isalnum())

# Verifica se contém apenas dígitos
print("isdigit()   → Apenas dígitos:               ", algo.isdigit())

# Verifica se possui somente números decimais
print("isdecimal() → Números decimais puros:       ", algo.isdecimal())

# Verifica se contém apenas espaços
print("isspace()   → Apenas espaços:               ", algo.isspace())

# Verifica se todas as letras são maiúsculas
print("isupper()   → Todas maiúsculas:             ", algo.isupper())

# Verifica se todas as letras são minúsculas
print("islower()   → Todas minúsculas:             ", algo.islower())

# Verifica se está em formato de título
print("istitle()   → Formato de título:            ", algo.istitle())

# TODO:
# Aprender type() futuramente

# FIXME:
# Estudar diferença entre:
# isnumeric()
# isdigit()
# isdecimal()