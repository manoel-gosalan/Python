# ==================================================
# ! DESAFIO 02 — DATA DE NASCIMENTO
# ==================================================

# --------------------------------------------------
# ? Entrada de dados
# --------------------------------------------------
usuario = input("Digite seu nome: ")

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

# --------------------------------------------------
# ? Saída formatada
# --------------------------------------------------
print(
    "Olá {}, você nasceu em {}/{}/{}!".format(
        usuario,
        dia,
        mes,
        ano
    )
)

# NOTE:
# int() converte texto para número inteiro

# TODO:
# Aprender f-string futuramente