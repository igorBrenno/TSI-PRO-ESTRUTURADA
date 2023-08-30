'''
Exercício 5: Escreva um programa que peça ao
usuário para digitar uma frase e, em seguida,
conte quantas vogais 
(a, e, i, o, u) existem na frase utilizando um loop "for".
'''

escreva = input("Digite uma frase: ")

vog = 0
for i in escreva:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vog += 1

print(vog)