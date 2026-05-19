
# ============================================================
# ! DESAFIO EX04 — Analisador de Nome
# ============================================================

# ? Conceitos treinados:
# ? len(), upper(), lower()

# TODO:
# Descrição:
# Analise um nome completo.
import time

titulo = " Analisador de Nome ".center(40, "\u2550")
separador = "─" * 40
footer = "\u2550" * 40

nome = str(input("Digite seu nome: "))

print(titulo)
print(f'{nome}')
print(f"Analisando seu nome:")
time.sleep(3)
print(separador)
print(f'O seu nome tem: {len(nome)} letas.')
print(f'Em maiúsculo é: {nome.upper()}. ')
print(f'Em minúsculo é: {nome.lower()}' )
print(f'Ele ao contrario é: {nome[::-1].capitalize()}')