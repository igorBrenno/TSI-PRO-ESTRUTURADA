'''
Exercício 9: Escreva um programa que peça ao usuário para digitar uma série de números
(um por linha) e pare quando o usuário digitar um número negativo. Em seguida, calcule
e imprima a média dos números digitados.
'''

lista = []
media = 0
soma = 0
while True:
    num = int(input("digite um numero: "))
    
    if num < 0:
        break
    else:
        lista.append(num)
        
for i in lista:
    soma += i
media = soma / len(lista)
print(media)
