# * ============================================================
# * DESAFIO 26 — Primeira e Última Ocorrência
# * 最初と最後の出現 (Saisho to Saigo no Shutsugen)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Faça um programa que leia uma frase pelo teclado
# ? e mostre:
# ?
# ? - Quantas vezes aparece a letra "A"
# ? - Em que posição ela aparece a primeira vez
# ? - Em que posição ela aparece a última vez
# ? ─────────────────────────────────────────────

frase = str(input('Digite uma frase: ')).upper().strip()

titulo  = " Primeira e Ultima Ocorrencia ".center(55, '\u2550')
titulo2 = " Em contagem Humana contanto a partir do 1 ".center(55, "\u2550")
separador = '─' * 55

print(f'\n{titulo}')
print(f"  {'Frase analisada':<20}: {frase}")
print(separador)
print(f"  {'Ocorrencias de A':<20}: {frase.count('A')} vezes")
print(f"  {'Primeira posicao':<20}: {frase.find('A')}")
print(f"  {'Ultima posicao':<20}: {frase.rfind('A')}")
print(separador)
print(titulo2)
print(f"  {'Frase analisada':<20}: {frase}")
print(separador)
print(f"  {'Ocorrencias de A':<20}: {frase.count('A')} vezes")
print(f"  {'Primeira posicao':<20}: {frase.find('A') + 1}")
print(f"  {'Ultima posicao':<20}: {frase.rfind('A') + 1}")
print(separador)
