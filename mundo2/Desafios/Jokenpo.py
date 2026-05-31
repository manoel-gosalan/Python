import random

opcoes = ["pedra", "papel", "tesoura"]
pontos_jogador = 0
pontos_maquina = 0

while True:
    print("\nEscolha: 0 = pedra | 1 = papel | 2 = tesoura")

    while True:
        try:
            jogador = int(input("\nSua escolha: "))
            if jogador in (0, 1, 2):
                break
            else:
                print("\nDigite apenas 0, 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida! Digite apenas números 0, 1 ou 2.")

    maquina = random.randint(0, 2)
    print(f"Você: {opcoes[jogador]} | Máquina: {opcoes[maquina]}")

    if jogador == maquina:
        print("Empate!")
    elif (jogador == 0 and maquina == 2) or \
        (jogador == 1 and maquina == 0) or \
        (jogador == 2 and maquina == 1):
        print("Você venceu!")
        pontos_jogador += 1
    else:
        print("Máquina venceu!")
        pontos_maquina += 1

    print(f"Placar: você {pontos_jogador} x {pontos_maquina} máquina")

    while True:
        continuar = input("\nJogar de novo? (s/n): ").strip().lower()
        if continuar in ("s", "n"):
            break
        else:
            print("\nDigite apenas 's' para sim ou 'n' para não.")

    if continuar == "n":
        print("\nJogo encerrado. Obrigado por jogar!")
        break