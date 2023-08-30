'''
Exercício 6: Escreva um programa que peça ao usuário
para digitar uma palavra e, em seguida,
imprima a palavra ao contrário utilizando um loop "for".
'''

escreva = input("Digite uma palavra: ")

escreva = reversed(escreva)

for i in escreva:
    print(i)