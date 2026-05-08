# ==================================================
# ! Desafio 09 — Tabuada
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler um número e mostrar sua tabuada
# --------------------------------------------------

# ? Entrada de dados
tabuada= int(input("Digite o valor para ver sua tabuada: "))

# ? Saida para o Usuario
print(f"Analisando o Valor, {tabuada} sua tabuada é:")
for i in range(1, 11):
    print(f"{tabuada:>4} x {i:>2} = {tabuada*i:>3}")


# NOTE:
# Nesse desafio eu usei um loop que vai de 1 a 10 para calcular a tabuada do número digitado pelo usuário. A função range(1, 11) gera uma sequência de números de 1 a 10, e dentro do loop, eu multiplico o número da tabuada pelo valor atual do loop (i) para obter o resultado da multiplicação. A formatação f-string é usada para alinhar os números na saída, tornando a tabuada mais legível.