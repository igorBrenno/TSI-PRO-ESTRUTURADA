'''
Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.
'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

maior = num1

if num2 > maior:
    maior = num2
elif num3 > maior: 
    maior = num3

print(maior)