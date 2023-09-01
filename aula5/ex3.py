'''
Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.
'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

soma = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("O resultado da soma é", soma, "\nO resultado da subtração é" , sub, "\nO resultado da multiplicação é", mul, "\nO resultado da divisão é", div)