# ==================================================
# ! Desafio 06 — Dobro, Triplo e Raiz Quadrada
# ==================================================

# --------------------------------------------------
# ? Objetivo
# Ler um número e mostrar seu dobro, triplo e raiz quadrada
# --------------------------------------------------

from math import sqrt

numero = int(input("Digite um numero: "))

# ? Mostrando entrada de dados
print(f"Analisando o valor {numero}")

# ? Mostrando o dobro do valor 
print(f"O dobro de {numero} é: {numero*2}")

# ? Mostrando o seu triplo
print(f"O triplo de {numero} é: {numero*3}")

# ? Mostrando a raiz quadrada
print(f"A raiz quadrada de {numero} é: {sqrt(numero)}")



# NOTE:
# pode usar bibliotecas matemáticas, como math.sqrt() para calcular a raiz quadrada apos ler m pouco a documentação da biblioteca math podemos notar que é a melhor opção para calcular a raiz quadrada, pois é uma função otimizada e fácil de usar. Para calcular o dobro e o triplo, basta multiplicar o número por 2 e 3, respectivamente. Aqui está um exemplo de como resolver o desafio:


