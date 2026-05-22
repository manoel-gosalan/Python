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
separador = "─" * 40
fim = "\u2250" * 40

distancia = float(input("Digite a distancia que deseja percorrer: "))
consumo = float(input("Digite a distancia media que seu carro faz por litro: "))
valor_combustivel = float(input("Valor atual do combustivel: "))
velocidade_media = int(input("Velocidade media: "))
orcamento_final = float(input("Digite o valor do seu orçamento final: "))

if distancia <= 0:
    print("A distancia não pode ser zero ou negativa.")
elif consumo <= 0:
    print("O consumo não pode ser zero ou negativo.")
elif valor_combustivel <= 0:
    print("O valor do combustivel não pode ser zero ou negativo.")
elif velocidade_media <= 0:
    print("A velocidade não pode ser zero ou negativa.")
elif orcamento_final <= 0:
    print("O orçamento não pode ser zero ou negativo.")
else:

    litros_nescessario = distancia / consumo
    custo_total = litros_nescessario * valor_combustivel
    tempo_total_horas = distancia / velocidade_media
    horas = int(tempo_total_horas)
    minutos = int((tempo_total_horas - horas) * 60)

    print(f"\n{'=== Resultado ==='}")
    print(f"Combustivel nescessario : {litros_nescessario:.2f} litros")
    print(f"Custo total da viagem: € {custo_total:.2f}")
    print(f"Tempo de viagem: {horas} hora e {minutos} minutos")

    if custo_total < orcamento_final:
        print(f"Sobra um total de € {(orcamento_final - custo_total):.2f}")
    else:
        print(f"Falta € {(orcamento_final - custo_total):.2f}")
