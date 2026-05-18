# ============================================================
# ! DESAFIO EX06 — Validador de Senha
# ============================================================

# ? Conceitos treinados:
# ? len(), comparação

# TODO:
# Descrição:
# Valide uma senha simples.

titulo = " Validação de Senha ".center(40, "\u2550")
footer = "\u2550" * 40
separador = "─" * 40

senha = input("Digite sua senha: ")

especiais = "@!#&."
numeros = "0123456789"

tem_tamanho_minimo = len(senha) >= 8
tem_tamanho_maximo = len(senha) <= 16
tem_especial = any(c in especiais for c in senha)
tem_numero = any(c in numeros for c in senha)

print(titulo)

if tem_tamanho_minimo and tem_tamanho_maximo and tem_especial and tem_numero:
    print("Acesso Permitido")
else:
    print("Acesso Negado")
    print(separador)
    if not tem_tamanho_minimo:
        print("- Mínimo de 8 caracteres")
    if not tem_tamanho_maximo:
        print("- Maximo de 16 caracteres")
    if not tem_especial:
        print("- Precisa de um especial: @, !, #, &, .")
    if not tem_numero:
        print("- Precisa de pelo menos um número")

print(footer)
