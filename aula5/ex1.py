'''
Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.
'''

num = int(input("Digite um numero: "))

resp = ""
if num == 0:
    resp = "Numero é igual a zero"
elif num > 0:
    resp = "Numero é positivo"
elif num < 0:
    resp = "Numero é negativo"

print(resp)