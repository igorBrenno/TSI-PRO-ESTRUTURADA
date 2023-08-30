'''
Exercício 8: Escreva um programa que peça ao usuário para
adivinhar um número secreto entre 1 e 100. O programa deve
informar se o palpite é muito alto, muito baixo ou correto.
Continue pedindo ao usuário para adivinhar até que ele acerte
o número utilizando um loop "while".
'''

import random
ram = random.randint(1, 100)


while True:
    num = int(input("Digite um numero: "))
    if  num == ram:
        print("Você acertou o valor era" , ram)
        break
    elif num > ram:
        print("Maior que o valor")
    elif num < ram:
        print("Menor que o valor")
        
