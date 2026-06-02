# * =============================================================
# * DESAFIO 050 - SOMA DOS PARES
# * Nível: Intermediário
# * Linguagem: Python
# * =============================================================
# * 合計 (goukei) = soma total
# * =============================================================

# ? ENUNCIADO

# * Desenvolva um programa que leia seis números inteiros.
# *
# * Ao final, mostre a soma apenas dos valores pares
# * digitados pelo usuário.

# TODO Ler 6 números.
# TODO Verificar quais são pares.
# TODO Somar somente os pares.
# TODO Exibir o resultado.

titulo = " Soma dos pares ".center(30, "\u2550")
fim = "\u2550" * 30
separador = "─" * 30

contador = 0
resultado_final = 0
soma_total = 0
input_usuario = []
valores = []



print(titulo)
while contador < 6:
    usuario = int(input(f"\nValor {contador+1} de 6:\n→ "))
    soma_total += usuario
    input_usuario.append(usuario)
    
    if usuario % 2 == 0:
        resultado_final += usuario
        valores.append(usuario)
    
    contador += 1

print(f"A soma dos Pares = {resultado_final}")
    

while True:
    print("\n1 - ver todos os valores")
    print("2 - sair")
    escolha = input("\nEscolha: ")

    if escolha == "1":
        print("Valores pares:")
        for indice, v in enumerate(valores, start=1):
            print(f"{indice:>3}. {v:>2}")
        print(f"{resultado_final:>5}")
        print(separador)
        print("Todos os valores:")
        for indice, t in enumerate((input_usuario), start=1):
            print(f"{indice:>3}. {t:>2}")
        print(f"{soma_total:>5}")
        print(separador)
    elif escolha == "2":
        print("Até logo! またね！")
        break
print(fim)