""" Crie um script que leia, o Dia, o Mês e o ano de uma pessoa e mostre isso com uma mensagem formatada """
usuario = input("Digite sue nome: ")
dia = int(input("Digite o dia de Nascimento: "))
mes = int(input("Digite o Mês de Nascimento: "))
ano = int(input("Digite o Ano de Aniversario: "))

print("Olá Sr.(a) {}, Você sua data de nascimento é {}/{}/{} !".format(usuario, dia, mes, ano))