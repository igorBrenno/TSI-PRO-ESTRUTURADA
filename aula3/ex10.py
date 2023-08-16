"""
Escreva um programa que solicite ao usuário a sua idade e verifique se ele
é maior de idade (idade igual ou superior a 18 anos). Imprima uma mensagem informando o resultado.
"""
n = int(input("Digite sua idade: "))
if n >= 18:
    print("Usuario é maior de idade.")
else:
    print("Usuario é menor de idade.")