
# * =============================================================
# * DESAFIO 037 - CONVERSOR DE BASES NUMÉRICAS
# * =============================================================

# ? ENUNCIADO:
# Leia um número inteiro e peça para o usuário escolher:
#
# [1] binário
# [2] octal
# [3] hexadecimal

numero = int(input("Digite um número inteiro: "))

print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])
else:
    print("❌ Opção inválida")
