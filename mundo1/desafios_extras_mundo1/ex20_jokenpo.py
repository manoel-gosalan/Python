# * =============================================================
# * EXERCICIO 20 - JOKENPO (PEDRA, PAPEL E TESOURA)
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * じゃんけんぽん (jankenpon) = pedra papel tesoura em japones!
# * =============================================================


# ? ENUNCIADO:
# Crie uma versao completa do classico jogo Pedra, Papel e Tesoura
# com placar, rodadas e relatorio de estatisticas ao final.


# ! REGRAS DO JOGO:
# Pedra   vence Tesoura
# Tesoura vence Papel
# Papel   vence Pedra
# Jogadas iguais = empate


# ! O PROGRAMA DEVE:
# TODO: 1. Perguntar quantas RODADAS serao jogadas (minimo 1)
# TODO: 2. Em cada rodada: pedir a jogada do usuario (1, 2 ou 3)
# TODO: 3. Gerar a jogada do COMPUTADOR aleatoriamente
# TODO: 4. Exibir quem ganhou a rodada e POR QUE (ex: "Pedra quebra Tesoura")
# TODO: 5. Manter e exibir o PLACAR atualizado apos cada rodada
# TODO: 6. Ao final, exibir RELATORIO COMPLETO com:
#             - Total de vitorias, derrotas e empates
#             - Percentual de aproveitamento do usuario
#             - Declarar o vencedor geral (ou empate)


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Quantas rodadas? 3
#
# --- Rodada 1 ---
# (1) Pedra  (2) Papel  (3) Tesoura: 1
# Voce: Pedra | Computador: Tesoura
# Voce ganhou! Pedra quebra Tesoura!
# Placar: Voce 1 x 0 Computador
#
# --- Rodada 2 ---
# (1) Pedra  (2) Papel  (3) Tesoura: 2
# Voce: Papel | Computador: Papel
# Empate!
# Placar: Voce 1 x 0 Computador
#
# --- Rodada 3 ---
# (1) Pedra  (2) Papel  (3) Tesoura: 3
# Voce: Tesoura | Computador: Pedra
# Computador ganhou! Pedra quebra Tesoura!
# Placar: Voce 1 x 1 Computador
#
# === Resultado Final ===
# Vitorias: 1 | Derrotas: 1 | Empates: 1
# Aproveitamento: 33.3%
# Foi um empate geral!


# * DICAS - ヒント (hint):
# import random
# opcoes = ["Pedra", "Papel", "Tesoura"]
# jogada_pc = random.choice(opcoes)
#
# Crie uma funcao para decidir o vencedor da rodada:
#   def verificar_vencedor(jogador, computador):
#       if jogador == computador:
#           return "empate"
#       vitorias = {"Pedra": "Tesoura", "Tesoura": "Papel", "Papel": "Pedra"}
#       if vitorias[jogador] == computador:
#           return "jogador"
#       return "computador"
#
# Calculo do aproveitamento:
#   aproveitamento = (vitorias / total_rodadas) * 100


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
