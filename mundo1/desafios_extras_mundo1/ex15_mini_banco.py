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


# ! O MENU DEVE TER AS SEGUINTES OPCOES:
# TODO: 1. Ver saldo    -> exibe o saldo atual formatado
# TODO: 2. Depositar    -> pede um valor e adiciona ao saldo
# TODO: 3. Sacar        -> pede um valor e subtrai do saldo
# TODO: 4. Ver extrato  -> lista todas as transacoes com tipo e valor
# TODO: 5. Sair         -> exibe o saldo final e encerra

# ! REGRAS DE VALIDACAO (importante - nao pule isso):
# Deposito: valor deve ser maior que zero
# Saque: valor deve ser maior que zero E menor ou igual ao saldo atual
# Se a validacao falhar, exiba a mensagem de erro e nao processe


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Escolha: 2
#   Valor do deposito: 500
#   Deposito de R$ 500.00 realizado! Novo saldo: R$ 1500.00
#
# Escolha: 3
#   Valor do saque: 2000
#   Saldo insuficiente! Saldo atual: R$ 1500.00
#
# Escolha: 4
#   === Extrato ===
#   + Deposito: R$ 500.00
#   Saldo atual: R$ 1500.00


# * DICAS - ヒント (hint):
# Guarde o historico como uma lista de dicionarios:
#   historico = []
#   historico.append({"tipo": "Deposito", "valor": 500.00})
#
# Para formatar valores monetarios use: f"R$ {valor:.2f}"
#
# Para o extrato, use "+" para depositos e "-" para saques:
#   if transacao["tipo"] == "Deposito":
#       print(f'+ Deposito: R$ {transacao["valor"]:.2f}')


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
