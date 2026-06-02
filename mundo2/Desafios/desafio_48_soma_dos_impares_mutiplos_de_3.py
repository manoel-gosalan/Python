# * =============================================================
# * DESAFIO 048 - SOMA DOS ÍMPARES MÚLTIPLOS DE 3
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 奇数 (kisuu) = número ímpar
# * 倍数 (baisuu) = múltiplo
# * =============================================================


# ? ENUNCIADO

# * Faça um programa que calcule a soma de todos os números
# * ímpares que são múltiplos de 3 e que se encontram
# * no intervalo de 1 até 500.

# TODO Percorrer os números de 1 a 500.
# TODO Identificar os ímpares.
# TODO Identificar os múltiplos de 3.
# TODO Somar os valores encontrados.
# TODO Mostrar o resultado final.

titulo = " Soma dos impares multiplos de 3 ".center(50, "\u2550")
fim = "\u2550" * 50
resultado_final = 0
valores = []  

for m in range(1, 500):
    if m % 3 == 0 and m % 2 != 0:
        resultado_final += m
        valores.append(m) 

print(f"\n{titulo}")
print(f"\nResultado: \033[1m{resultado_final}\033[0m")
while True:
    print("\n1 - ver todos os valores")
    print("2 - sair")
    escolha = input("\nEscolha: ")

    if escolha == "1":
        for indice, m in enumerate(valores, start=1):
            print(f"{indice:>3}: {m:>5}")
        
    elif escolha == "2":
        print("Até logo! またね！")
        break
print(fim)