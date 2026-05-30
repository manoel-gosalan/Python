# * =============================================================
# * DESAFIO 43 - CURSO EM VÍDEO
# * Mundo 2 - Python
# * =============================================================

# ? ENUNCIADO:
# faça um script que leia a altura e peso de uma pessoa e calcule o IMC e classifique o resultado.
## ! CLASSIFICAÇÃO (tabela da OMS):
# IMC < 18.5          -> "Abaixo do peso"
# 18.5 <= IMC < 25.0  -> "Peso normal"
# 25.0 <= IMC < 30.0  -> "Sobrepeso"
# 30.0 <= IMC < 35.0  -> "Obesidade grau I"
# 35.0 <= IMC < 40.0  -> "Obesidade grau II"
# IMC >= 40.0         -> "Obesidade grau III (mórbida)"

# * O programa deve:
# 1. Pedir o peso (kg) e a altura (m)
# 2. Validar os valores (ambos devem ser maiores que zero)
#    -> Se inválido    : "Valores inválidos."
# 3. Calcular o IMC (com 2 casas decimais)
# 4. Exibir o IMC e a classificação

#
# TODO:
# Implemente a lógica completa do exercício.


titulo = "Calculadora de IMC".center(40, "\u2550")
separador = "─"*40
fim = "\u2550" * 40

nome = input("Informe o seu nome: ").capitalize()
altura = float(input("Informe a sua Altura (ex 1.73): "))
peso = float(input("Informe o seu peso (ex 103.03): "))
IMC = peso / (altura ** 2 )
txt_usuario = f"Olá \033[0m{nome}\033[1m bem vindo ao seu calculador de IMC."
txt_imc = f"O seu IMC atual é de \033[0m{IMC:.2f}\033[1m de acordo com a OMS você está: "

print(f"\n{titulo}")

if altura < 0 or peso < 10:
    print("Valores invalidos tente novamente.")

# Calcula a classificação primeiro
if IMC < 18.5:
    classificacao = "Abaixo do peso ideal"
elif IMC < 25.5:
    classificacao = "No peso ideal"
elif IMC < 30.0:
    classificacao = "Sobrepeso. Comece uma academia!"
elif IMC < 35.0:
    classificacao = "Obesidade Grau 1. Dieta + academia."
elif IMC < 40.0:
    classificacao = "Obesidade Grau 2. Procure um personal e nutricionista."
else:
    classificacao = "\033[0mObesidade Grau 3 (MÓRBIDA)\033[1m. Procure um médico imediatamente."

# Imprime UMA vez só
print(txt_usuario)
print(separador)
print(txt_imc)
print(classificacao)
print(fim)

