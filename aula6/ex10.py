'''
Exercício 10: Escreva um programa que peça ao usuário para digitar
uma senha e continue pedindo até que o usuário digite a senha correta.
Quando a senha estiver correta, imprima uma mensagem de boas-vindas.
'''

senha = input("Defina uma senha: ")

while True:
    verif = input("Coloque a senha: ")
    
    if senha != verif:
        print("Senha incorreta!")
    else:
        print("Bem vindo!")
        break