'''
Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
'''

idade = int(input("Digite sua idade: "))

resul = ""

if idade <= 12:
    resul = "Criança"
elif idade >= 13 and idade <= 19:
    resul = "Adolecente"
elif idade >= 20 and idade <= 59:
    resul = "Adulto"
elif idade >= 60:
    resul = "Idoso"
print(resul)