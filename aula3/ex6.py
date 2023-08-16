"""
Escreva um programa que solicite ao usuário um número e verifique
se ele é par ou ímpar. Imprima uma mensagem informando o resultado.
"""

numero = int(input("Digite um numero para verificar: "))

resul = ""
if numero % 2 == 0:
    resul = "Par"
else:
    resul = "Impar"

print("O numero é ", resul)