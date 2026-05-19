# * =============================================================
# * EXERCICIO 16 - SIMULADOR DE LOGIN
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * ログインシステム (roguin shisutemu) = sistema de login
# * =============================================================


# ? ENUNCIADO:
# Crie um sistema de autenticacao simulado com usuarios pre-cadastrados.
# O programa deve verificar login e senha com limite de tentativas.


# ! USUARIOS PRE-CADASTRADOS (defina voce mesmo no codigo):
# Cadastre pelo menos 3 usuarios com nome e senha
# Exemplo de estrutura: {"admin": "admin123", "user1": "senha1", "joao": "py2024"}


# ! O PROGRAMA DEVE:
# TODO: 1. Pedir USUARIO e SENHA para efetuar o login
# TODO: 2. Permitir no maximo 3 TENTATIVAS antes de bloquear o acesso
# TODO: 3. Apos login bem-sucedido, exibir mensagem de boas-vindas personalizada
# TODO: 4. Apos login, exibir um MENU INTERNO com as opcoes:
#             - Ver meu perfil (exibe nome do usuario logado)
#             - Cadastrar novo usuario (adiciona ao dicionario)
#             - Sair (encerra o programa)

# ! REGRAS DE SEGURANCA:
# Nunca exiba a senha em nenhum momento (nem nas mensagens de erro)
# Ao bloquear, exiba mensagem clara de acesso bloqueado
# O cadastro de novo usuario nao pode sobrescrever um usuario existente


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Usuario: admin
# Senha: 1234
#   Senha incorreta. Tentativas restantes: 2
#
# Usuario: admin
# Senha: admin123
#   Bem-vindo, admin!
#
# === Menu Interno ===
# 1 - Ver meu perfil
# 2 - Cadastrar novo usuario
# 3 - Sair
#
# Escolha: 2
#   Novo usuario: joao
#   Nova senha: python99
#   Usuario "joao" cadastrado com sucesso!


# * DICAS - ヒント (hint):
# Use um dicionario para os usuarios:
#   usuarios = {"admin": "admin123", "user1": "senha1"}
#
# Controle as tentativas com um contador:
#   tentativas = 0
#   while tentativas < 3:
#       ...
#       tentativas += 1
#
# Para verificar login: if usuarios.get(nome_usuario) == senha_digitada


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
