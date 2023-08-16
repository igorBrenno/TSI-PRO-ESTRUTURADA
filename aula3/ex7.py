"""
Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e 
armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" 
entre essas variáveis e imprima os resultados.
"""

v1 = bool(input("Digite um valor true ou false: "))
v2 = bool(input("Digite um valor true ou false: "))


print("Em and: ", v1 and v2)
print("Em or: ", v1 or v2)
print("Em not para valor1 : ", not v1)
print("Em not para valor2 : ", not v2)