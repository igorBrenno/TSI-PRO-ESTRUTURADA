'''
Exercício 4: Escreva um programa que utilize um loop "for" para
calcular a soma de todos os números ímpares de 1 a 100.
'''

soma = 0
for i in range(100):
    if i % 2 == 0:
        soma = soma
    else:
        soma += i

print(soma)