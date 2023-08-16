"""
Escreva um programa que solicite ao usuário uma temperatura em graus Celsius 
e converta-a para Fahrenheit. Imprima o resultado formatado.
"""

cel = float(input("Digite um valor de celsius: "))

fai = cel * 9/5 + 32

print(f"Valor convertido em Fahrenheit: {fai}")