"""
Escreva um programa em Python que solicite ao usuário dois números inteiros
e troque os valores das variáveis. Em seguida, imprima os valores atualizados.
"""
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))

n1, n2 = n2, n1
print(f"{n1}, {n2}")