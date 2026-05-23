# * =============================================================
# * EXERCICIO 15 - MINI BANCO
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 銀行システム (ginkou shisutemu) = sistema bancario
# * =============================================================


# ? ENUNCIADO:
# Crie a simulacao de um sistema bancario simples onde o usuario
# pode realizar operacoes em uma conta ficticia.


# ! ESTADO INICIAL DO PROGRAMA:
# saldo    = R$ 1000.00
# historico = lista vazia (sem transacoes ainda)



# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------

saldo = 1000
historico = []
limite = 200
numero_saques = 0
LIMITES_SAQUES = 3




while True:
    print("\n=== Seleção de ação ===")
    print("1 - Ver Saldo ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Ver extrato ")
    print("5 - Sair ")

    escolha = input("\nEscolha: ")

    if escolha == "5":
        print(f"Saldo final: € {saldo:.2f}")
        print("Muito bom, té logo! すごくよかった、またね！")
        break
    elif escolha not in ["1", "2", "3", "4"]:
        print("Opção inválida, tente outra vez! もう一度！(mou ichido = de novo!)")
        continue

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 1 - VER SALDO
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if escolha == "1":
        print(f"Saldo atual: € {saldo:.2f}")
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 2 - DEPOSITAR
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "2":
        deposito = float(input("Digite o valor para deposito: "))

        if deposito > 0:
            saldo += deposito
            historico.append({"tipo": "Deposito", "valor": deposito})
            print(f"Depósito de {deposito:.2f} realizado. Novo saldo: {saldo:.2f}")
        else:
            print("O depósito falhou, valor deve ser maior que 0")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 3 - SACAR
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "3":
        saque = float(input("Digite o valor para saque: "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        execedeu_retiradas = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Não há saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou. Ovalor excede o limite de saque. valor deve ser € 200 ou menor.")
        elif execedeu_retiradas:
            print("Operação falhou. Número máximo de saques excedidos.")

        elif saque > 0:
            saldo -= saque
            historico.append({"tipo": "saque", "valor": saque})
            numero_saques += 1
            print(f"Saque de {saque:.2f} realizado. Novo Saldo: {saldo:.2f} ")
        else:
            print("O saque falhou, valor deve ser maior que 0")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # OPÇÃO 4 - VER EXTRATO
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    elif escolha == "4":
        print("\n ==== Extrato ==== ")
    
        if not historico:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in historico:
                if transacao["tipo"] == "Deposito":
                    print(f"  + Depósito: R$ {transacao['valor']:.2f}")
                else:
                    print(f"  - Saque:    R$ {transacao['valor']:.2f}")
    
        print(f"\n  Saldo atual: R$ {saldo:.2f}")
        print("=====================")
    
