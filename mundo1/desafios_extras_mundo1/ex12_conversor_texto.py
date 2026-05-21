# * =============================================================
# * EXERCICIO 12 - CONVERSOR DE TEXTO
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * テキスト変換 (tekisuto henkan) = conversao de texto
# * =============================================================

# ? ENUNCIADO:
# Crie um programa que funcione como uma ferramenta de transformacao
# de texto, com varios modos de conversao que o usuario pode escolher.


# ! O MENU DEVE OFERECER AS SEGUINTES CONVERSOES:
# TODO: 1. MAIUSCULAS      -> transforma todo o texto em maiusculo
# TODO: 2. minusculas      -> transforma todo o texto em minusculo
# TODO: 3. Capitalizado    -> Primeira Letra De Cada Palavra Em Maiusculo
# TODO: 4. Invertido       -> escreve o texto completamente de tras pra frente
# TODO: 5. snake_case      -> substitui espacos por underline, tudo minusculo
#                            exemplo: "meu texto aqui" -> "meu_texto_aqui"
# TODO: 6. Contar chars    -> exibe quantos caracteres o texto possui (com e sem espacos)

# ! REGRAS:
# O programa deve continuar rodando ate o usuario escolher sair
# Se o usuario digitar uma opcao invalida, avise e peca novamente


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Digite o texto: hello world python
#   Opcao: 5
#
# Output:
#   Resultado: hello_world_python
#
# Input:
#   Digite o texto: Python e demais
#   Opcao: 6
#
# Output:
#   Com espacos: 16 caracteres
#   Sem espacos: 14 caracteres


# * DICAS - ヒント (hint):
# .upper()              -> MAIUSCULAS
# .lower()              -> minusculas
# .title()              -> Capitalizado
# texto[::-1]           -> Invertido (slicing reverso)
# .replace(" ","_").lower() -> snake_case
# len(texto)            -> conta todos os chars
# len(texto.replace(" ", "")) -> conta sem espacos


# ---------------------------------------------------------------
# O SEU CÓDIGO COMEÇA AQUI
# ---------------------------------------------------------------

while True:
    print("\n=== Seleção de ação ===")
    print("1 - MAIUSCULAS")
    print("2 - minusculas")
    print("3 - Capitalizado")
    print("4 - Invertido")
    print("5 - Snake_case")
    print("6 - Contar chars")
    print("7 - Sair")

    escolha = input("\nEscolha: ")

    if escolha == "7":
        print("Muito bom, té logo! すごくよかった、またね！")
        break  # ← break SÓ AQUI, no sair

    elif escolha not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida, tente outra vez! もう一度！(mou ichido = de novo!)")
        continue  # ← pula pro próximo ciclo do loop

    # Pede o texto UMA vez, fora dos ifs
    frase = input("Digite a frase: ")

    if escolha == "1":
        print(f"Resultado: {frase.upper()}")

    elif escolha == "2":
        print(f"Resultado: {frase.lower()}")

    elif escolha == "3":
        print(f"Resultado: {frase.title()}")

    elif escolha == "4":
        print(f"Resultado: {frase[::-1]}")

    elif escolha == "5":
        print(f"Resultado: {frase.replace(' ', '_').lower()}")

    elif escolha == "6":
        sem_espaco = frase.replace(" ", "")
        print(f"Com espaços:    {len(frase)} caracteres")
        print(f"Sem espaços:    {len(sem_espaco)} caracteres")