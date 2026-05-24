import random

# =============================================================
# CORES - ANSI escape codes
# =============================================================
VERDE    = "\033[92m"   # jogador
AZUL     = "\033[94m"   # computador
AMARELO  = "\033[93m"   # vitória / números positivos
VERMELHO = "\033[91m"   # derrota / números negativos
CIANO    = "\033[96m"   # neutro / empate
RESET    = "\033[0m"    # volta ao normal — SEMPRE usar no fim!

# =============================================================

print(f"{CIANO}=== じゃんけんぽん - Pedra, Papel e Tesoura ==={RESET}")

while True:
    rodadas = int(input("Quantas rodadas deseja jogar? "))
    if rodadas >= 1:
        break
    print(f"{VERMELHO}Digite um número válido (mínimo 1).{RESET}")

opcoes = ["Pedra", "Papel", "Tesoura"]

vitorias = 0
derrotas = 0
empates  = 0

for r in range(1, rodadas + 1):
    print(f"\n{CIANO}--- Rodada {r} ---{RESET}")
    print("(1) Pedra  (2) Papel  (3) Tesoura")

    while True:
        escolha = int(input("Sua jogada: "))
        if escolha in [1, 2, 3]:
            break
        print(f"{VERMELHO}Escolha inválida. Digite 1, 2 ou 3.{RESET}")

    jogador    = opcoes[escolha - 1]
    computador = random.choice(opcoes)

    # Verde pro jogador, azul pro computador
    print(f"{VERDE}Você: {jogador}{RESET} | {AZUL}Computador: {computador}{RESET}")

    if jogador == computador:
        print(f"{CIANO}Empate!{RESET}")
        empates += 1

    elif (jogador == "Pedra"   and computador == "Tesoura") or \
         (jogador == "Tesoura" and computador == "Papel")   or \
         (jogador == "Papel"   and computador == "Pedra"):

        vitorias += 1
        print(f"{VERDE}Você ganhou! {RESET}")

        if jogador == "Pedra":
            print(f"{VERDE}Pedra quebra Tesoura!{RESET}")
        elif jogador == "Tesoura":
            print(f"{VERDE}Tesoura corta Papel!{RESET}")
        else:
            print(f"{VERDE}Papel cobre Pedra!{RESET}")

    else:
        derrotas += 1
        print(f"{VERMELHO}Computador ganhou!{RESET}")

        if computador == "Pedra":
            print(f"{VERMELHO}Pedra quebra Tesoura!{RESET}")
        elif computador == "Tesoura":
            print(f"{VERMELHO}Tesoura corta Papel!{RESET}")
        else:
            print(f"{VERMELHO}Papel cobre Pedra!{RESET}")

    # Placar: vitórias em amarelo, derrotas em vermelho
    print(f"Placar: {VERDE}Você {AMARELO}{vitorias}{RESET} x {VERMELHO}{derrotas}{RESET} {AZUL}Computador{RESET}")

# Relatório final
print(f"\n{CIANO}=== Resultado Final ==={RESET}")
print(
    f"Vitórias: {AMARELO}{vitorias}{RESET} | "
    f"Derrotas: {VERMELHO}{derrotas}{RESET} | "
    f"Empates: {CIANO}{empates}{RESET}"
)

aproveitamento = (vitorias / rodadas) * 100

# Cor do aproveitamento muda conforme o resultado
if aproveitamento >= 50:
    cor_aprov = AMARELO
else:
    cor_aprov = VERMELHO

print(f"Aproveitamento: {cor_aprov}{aproveitamento:.1f}%{RESET}")

if vitorias > derrotas:
    print(f"{VERDE}Você foi o grande vencedor! {RESET}")
elif derrotas > vitorias:
    print(f"{VERMELHO}O computador venceu! {RESET}")
else:
    print(f"{CIANO}Foi um empate geral!{RESET}")