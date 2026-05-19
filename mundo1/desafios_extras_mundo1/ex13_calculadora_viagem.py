# * =============================================================
# * EXERCICIO 13 - CALCULADORA DE VIAGEM
# * Nivel: Iniciante | Linguagem: Python
# * =============================================================
# * 旅行計算機 (ryokou keisanki) = calculadora de viagem
# * =============================================================


# ? ENUNCIADO:
# Crie uma calculadora que ajude o usuario a planejar os custos
# e o tempo de uma viagem de carro.


# ! O PROGRAMA DEVE PEDIR AO USUARIO:
# TODO: 1. A DISTANCIA da viagem em km
# TODO: 2. O CONSUMO MEDIO do carro em km/litro
# TODO: 3. O PRECO DO COMBUSTIVEL por litro em reais
# TODO: 4. A VELOCIDADE MEDIA que sera mantida em km/h
# TODO: 5. O ORCAMENTO disponivel para combustivel (em reais)

# ! O PROGRAMA DEVE CALCULAR E EXIBIR:
# - Quantos LITROS de combustivel serao necessarios
# - O CUSTO TOTAL da viagem em reais
# - O TEMPO ESTIMADO de viagem (separado em horas e minutos)
# - Se o orcamento informado e SUFICIENTE ou nao, e quanto falta (ou sobra)

# ! REGRAS DE VALIDACAO:
# Nenhum valor pode ser zero ou negativo
# Se o usuario digitar algo invalido, avise e peca novamente


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Distancia (km): 350
#   Consumo do carro (km/l): 12
#   Preco do combustivel (R$/l): 5.89
#   Velocidade media (km/h): 80
#   Seu orcamento para combustivel (R$): 150
#
# Output:
#   === Resultado ===
#   Combustivel necessario: 29.17 litros
#   Custo total: R$ 171.77
#   Tempo de viagem: 4 horas e 22 minutos
#   Orcamento INSUFICIENTE. Faltam R$ 21.77


# * FORMULAS - ヒント (hint):
# litros_necessarios = distancia / consumo
# custo_total        = litros_necessarios * preco_combustivel
# tempo_total_horas  = distancia / velocidade
# horas              = int(tempo_total_horas)
# minutos            = int((tempo_total_horas - horas) * 60)


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
