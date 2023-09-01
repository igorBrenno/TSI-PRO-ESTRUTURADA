'''
Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.
'''

num = int(input("Digite um numero: "))

resp = ""

if num % 2 == 0:
    resp = "Numero é par"

else:
    resp = "Numero é impar"
print(resp)