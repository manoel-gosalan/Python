# * =============================================================
# * EXERCICIO 10 - PLAYLIST INTELIGENTE
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * 音楽リスト (ongaku risuto) = lista de musicas
# * =============================================================


# ? ENUNCIADO:
# Crie um sistema de gerenciamento de playlist de musicas.
# O usuario pode adicionar, remover, listar e buscar musicas.


# ! O PROGRAMA DEVE TER UM MENU COM AS OPCOES:
# TODO: 1. Adicionar musica  -> pede o nome e adiciona na lista
# TODO: 2. Remover musica    -> pede o nome e remove (ou avisa que nao existe)
# TODO: 3. Listar todas      -> mostra todas as musicas numeradas
# TODO: 4. Buscar musica     -> verifica se a musica existe e em qual posicao
# TODO: 5. Sair              -> encerra o programa

# ! REGRAS IMPORTANTES:
# Nao pode adicionar musica com nome vazio
# Ao remover, se a musica nao existir, avise o usuario
# A busca nao deve ser case-sensitive (maiusculas/minusculas)


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# === Playlist Manager ===
# 1 - Adicionar musica
# 2 - Remover musica
# 3 - Listar todas
# 4 - Buscar musica
# 5 - Sair
# Escolha: 1
# Nome da musica: Bohemian Rhapsody
# "Bohemian Rhapsody" adicionada com sucesso!

# Escolha: 3
# Sua Playlist:
# 1. Bohemian Rhapsody
#
# Escolha: 4
# Buscar: bohemian rhapsody
# "Bohemian Rhapsody" encontrada na posicao 1

# * DICAS - ヒント (hint):
# Use uma lista [] para guardar as musicas /// feito
# Use while True para o menu ficar em loop ate o usuario sair
# Use .lower() nas duas strings na hora de comparar (busca e remocao)
# Use enumerate() para listar com numeracao

# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------


playlist = []

while True:
    print("\n=== Playlist Manager ===")
    print("1 - Adicionar música")
    print("2 - Remover música")
    print("3 - Listar todas")
    print("4 - Buscar música")
    print("5 - Sair")

    escolha = input("\nEscolha: ")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 1 - Adicionar
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if escolha == "1":
        musica = input("Nome da música: ").strip()  # remove espaços vazios!

        if musica == "":  # nome vazio?
            print("Nome não pode ser vazio!")
        else:
            playlist.append(musica)
            print(f'"{musica}" adicionada com sucesso!')

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 2 - Remover
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "2":
        busca = input("Nome para remover: ").lower()

        # Procura na lista ignorando maiúsculas/minúsculas
        encontrada = None
        for musica in playlist:
            if musica.lower() == busca:
                encontrada = musica
                break

        if encontrada:
            playlist.remove(encontrada)
            print(f'"{encontrada}" removida!')
        else:
            print(" Música não encontrada na playlist!")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 3 - Listar
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "3":
        if not playlist:
            print("Sua playlist está vazia!")
        else:
            print("\n Sua Playlist:")
            for i, musica in enumerate(playlist, start= 1 ):
                print(f"  {i}. {musica}")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 4 - Buscar
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "4":
        busca = input("Buscar: ").lower()

        for i, musica in enumerate(playlist, start=1):
            if musica.lower() == busca:
                print(f'"{playlist}" encontrada na posição {i}!')
                break
        else:
            print("Música não encontrada!")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 5 - Sair
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "5":
        print("Até logo! さようなら！")
          # sai do while True!
        break
    else:
        print("Opção inválida! Tenta de novo.")