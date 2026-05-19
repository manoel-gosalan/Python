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
#
# Escolha: 3
# Sua Playlist:
# 1. Bohemian Rhapsody
#
# Escolha: 4
# Buscar: bohemian rhapsody
# "Bohemian Rhapsody" encontrada na posicao 1


# * DICAS - ヒント (hint):
# Use uma lista [] para guardar as musicas
# Use while True para o menu ficar em loop ate o usuario sair
# Use .lower() nas duas strings na hora de comparar (busca e remocao)
# Use enumerate() para listar com numeracao


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
