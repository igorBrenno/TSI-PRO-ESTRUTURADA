"""
Solicite ao usuário o primeiro número inteiro e armazene-o em uma variável chamada numero1. Solicite ao usuário o segundo
número inteiro e armazene-o em uma variável chamada numero2. Troque os valores das variáveis
numero1 e numero2 utilizando atribuição múltipla. Imprima os valores atualizados das variáveis utilizando a função print().
"""

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))

numero1 = numero1 + numero2
numero2 = numero1 - numero2
numero1 = numero1 - numero2

print("Numero1: ", numero1)
print("Numero2: ", numero2)