"""faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informações sobre ele"""

algo = input("Digite algo: ")

print("Analisando '{}':".format(algo))
print("isalpha()    → só letras:                      ", algo.isalpha())
print("isnumeric()  → só numéricos (inclui ², ½):     ", algo.isnumeric())
print("isalnum()    → letras e/ou números:             ", algo.isalnum())
print("isdigit()    → só dígitos (inclui ², mas não ½):", algo.isdigit())
print("isdecimal()  → só dígitos decimais puros 0-9:  ", algo.isdecimal())
print("isspace()    → só espaços/tabs/newline:         ", algo.isspace())
print("isupper()    → todas letras maiúsculas:         ", algo.isupper())
print("islower()    → todas letras minúsculas:         ", algo.islower())
print("istitle()    → formato Título Assim:            ", algo.istitle())