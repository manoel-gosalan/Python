# * ============================================================
# * DESAFIO 35 — ANALISANDO TRIÂNGULO v1.0
# * 三角形分析 (Sankakkei Bunseki)
# * Curso em Vídeo | Gustavo Guanabara
# * ============================================================

# ? ─────────────────────────────────────────────
# ? Desenvolva um programa que leia o comprimento
# ? de três retas.
# ?
# ? O programa deve analisar se essas retas
# ? podem formar um triângulo.
# ? ─────────────────────────────────────────────
titulo    = " Analisando Triangulo v1.0 ".center(40, "\u2550")
separador = "─" * 40
footer    = "\u2550" * 40

primeiro_segmento = float(input("Primeiro Segmento: "))
segundo_segmento  = float(input("Segundo Segmento: "))
terceiro_segmento = float(input("Terceiro Segmento: "))

print(f'\n{titulo}')
if primeiro_segmento < segundo_segmento + terceiro_segmento and segundo_segmento < primeiro_segmento + terceiro_segmento and terceiro_segmento < primeiro_segmento + segundo_segmento:
    print(f"Após Analisarmos os valor dos segmentos: ")
    print(separador)
    print(f"{'Primeiro Segmento  :':<20} {primeiro_segmento}")
    print(f"{'Segundo Segmento   :':<20} {segundo_segmento}" )
    print(f"{'Terceiro Segmento  :':<20} {terceiro_segmento}")
    print(separador)
    print("Eles formam um Triângulo")
else:
    print(f"Após Analisarmos os valor dos segmentos: ")
    print(separador)
    print(f"{'Primeiro Segmento:':<20} {primeiro_segmento}")
    print(f"{'Segundo Segmento:' :<20} {segundo_segmento}" )
    print(f"{'Terceiro Segmento:':<20} {terceiro_segmento}")
    print(separador)
    print("Eles não formam um triângulo")

print(footer)