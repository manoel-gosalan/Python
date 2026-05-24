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
#?  - Ver meu perfil (exibe nome do usuario logado)
#?  - Cadastrar novo usuario (adiciona ao dicionario)
#?  - Sair (encerra o programa)


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
usuarios      = []
senha_acesso  = []
nomes         = []
ir_cadastrar  = False    # flag de navegação

while True:

    # Se a flag estiver levantada, pula direto pro cadastro
    # sem mostrar o menu principal
    if ir_cadastrar:
        ir_cadastrar = False   # abaixa a bandeira imediatamente
        escolha = "1"          # força a opção de cadastro
    else:
        print("\n(1) Cadastrar")
        print("(2) Login")
        print("(3) Ver usuários cadastrados")
        print("(4) Sair")
        escolha = input("\nEscolha: ")

    # ─────────────────────────
    if escolha == "4":
        print("Até logo! またね！")
        break

    elif escolha not in ["1", "2", "3"]:
        print("Opção inválida! もう一度！")
        continue

    # ─────────────────.────────
    elif escolha == "1":
        print("\n==== Cadastro ====")
        while True:
            CADASTRAR     = input("Usuário: ").strip()
            NOME_COMPLETO = input("Nome completo: ").strip()
            SENHA         = input("Senha: ")

            if len(CADASTRAR) < 3:
                print("Usuário deve ter ao menos 3 letras!")
                continue
            if len(SENHA) < 6:
                print("Senha deve ter ao menos 6 dígitos!")
                continue
            if CADASTRAR in usuarios:
                print(f"Usuário '{CADASTRAR}' já existe!")
                continue

            usuarios.append(CADASTRAR)
            senha_acesso.append(SENHA)
            nomes.append(NOME_COMPLETO)
            print(f"Usuário '{CADASTRAR}' cadastrado!")
            break

    # ─────────────────────────
    elif escolha == "2":
        tentativas = 0

        while tentativas < 3:
            login = input("Usuário: ")
            senha = input("Senha: ")

            if login in usuarios:
                indice = usuarios.index(login)   # acha a posição do usuário
                if senha_acesso[indice] == senha:
                    print(f"\nBem-vindo, {nomes[indice]}! ようこそ！")

                    # ── Menu Interno ──────────────────────
                    while True:
                        print("\n==== Menu Interno ====")
                        print("(1) Ver meu Perfil")
                        print("(2) Cadastrar novo usuário")
                        print("(3) Sair")

                        selecionar = input("\nEscolha: ")   # ← input() aqui!

                        if selecionar == "1":
                            print(f"\n==== Perfil ====")
                            print(f"  Usuário : {login}")
                            print(f"  Nome    : {nomes[indice]}")
                            # senha nunca é exibida! セキュリティ！

                        elif selecionar == "2":
                            ir_cadastrar = True    # levanta a bandeira
                            break                  # sai do menu interno

                        elif selecionar == "3":
                            print("Saindo... またね！")
                            break

                        else:
                            print("Opção inválida! もう一度！")

                    break   # sai do loop de tentativas

            tentativas += 1
            restantes = 3 - tentativas
            if restantes > 0:
                print(f" Dados incorretos. Tentativas restantes: {restantes}")
            else:
                print("Acesso bloqueado! アクセスブロック！Excedeu o numero de tentativas")

    # ─────────────────────────
    elif escolha == "3":
        if not usuarios:
            print("Não há usuários cadastrados!")
        else:
            print("\n==== Usuários Cadastrados ====")
            for i, user in enumerate(usuarios, 1):
                print(f"  {i}. {user} — {nomes[i-1]}")