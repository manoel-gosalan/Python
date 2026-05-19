# * =============================================================
# * EXERCICIO 19 - CONVERSOR DE HORARIO (FUSOS HORARIOS)
# * Nivel: Intermediario | Linguagem: Python
# * =============================================================
# * 時間変換 (jikan henkan) = conversao de horario
# * =============================================================


# ? ENUNCIADO:
# Crie um conversor que ajude viajantes e profissionais a
# trabalhar com diferentes fusos horarios ao redor do mundo,
# tendo Brasilia como referencia.


# ! TABELA DE FUSOS HORARIOS (diferenca em relacao a Brasilia - BRT UTC-3):
# Brasilia   BRT  UTC-3   diferenca:  0h  (referencia)
# Londres    GMT  UTC+0   diferenca: +3h
# Paris      CET  UTC+1   diferenca: +4h
# Moscou     MSK  UTC+3   diferenca: +6h
# Dubai      GST  UTC+4   diferenca: +7h
# Toquio     JST  UTC+9   diferenca: +12h
# Nova York  EST  UTC-5   diferenca: -2h
# LA         PST  UTC-8   diferenca: -5h


# ! O PROGRAMA DEVE:
# TODO: 1. Pedir o horario atual em Brasilia no formato HH:MM
# TODO: 2. Validar se o formato esta correto (horas 0-23, minutos 0-59)
# TODO: 3. Exibir o horario correspondente em TODAS as cidades da tabela
# TODO: 4. Lidar com a virada do dia:
#             - Se hora calculada >= 24: exibir "(+1 dia)"  e subtrair 24
#             - Se hora calculada < 0:  exibir "(-1 dia)" e somar 24


# ? EXEMPLO DE ENTRADA E SAIDA ESPERADA:
# Input:
#   Horario em Brasilia (HH:MM): 22:30
#
# Output:
#   === Horarios pelo Mundo ===
#   Brasilia  (BRT):  22:30
#   Londres   (GMT):  01:30  (+1 dia)
#   Paris     (CET):  02:30  (+1 dia)
#   Moscou    (MSK):  04:30  (+1 dia)
#   Dubai     (GST):  05:30  (+1 dia)
#   Toquio    (JST):  10:30  (+1 dia)
#   Nova York (EST):  20:30
#   LA        (PST):  17:30


# * DICAS - ヒント (hint):
# Guarde as cidades em uma lista de tuplas ou dicionarios:
#   cidades = [
#       ("Brasilia", "BRT", 0),
#       ("Londres",  "GMT", 3),
#       ("Toquio",   "JST", 12),
#       ...
#   ]
#
# Separe hora e minuto da entrada:
#   partes = entrada.split(":")
#   hora   = int(partes[0])
#   minuto = int(partes[1])
#
# Calcule o horario convertido:
#   hora_conv = hora + diferenca
#   dia_info  = ""
#   if hora_conv >= 24:
#       hora_conv -= 24
#       dia_info = "(+1 dia)"
#   elif hora_conv < 0:
#       hora_conv += 24
#       dia_info = "(-1 dia)"
#
# Para formatar com zero a esquerda: f"{hora_conv:02d}:{minuto:02d}"


# ---------------------------------------------------------------
# SEU CODIGO COMEÇA AQUI
# ---------------------------------------------------------------
