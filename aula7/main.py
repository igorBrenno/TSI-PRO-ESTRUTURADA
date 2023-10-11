# Escreva uma função chamada saudacao que aceita um nome como argumento e imprime "Olá, [nome]!".

def saudacao(nome):
    return f"Olá, {nome}!"

# Crie uma função dobro que aceita um número como argumento e retorna o dobro desse número.

def dobro(num):
    return num * 2

# Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma
#  como argumentos. O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.

def saudacao_personalizada(nome, idioma = "inglês"):
    match idioma:
        case "inglês":
            return f"Hello, {nome}!"
        case "espanhol":
            return f"Hola, {nome}!"
        case "francês":
            return f"Bonjour, {nome}!"
        case _:
            return f"Hello, {nome}!"

# Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente

def potencia(base, exp = 2):
    return base ** exp

# Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.


def idade_valida(idade):
    if idade >= 0 and idade <= 150:
        return True
    else:
        return False

# Implemente uma função validar_email que verifica se uma string fornecida como argumento representa um endereço de e-mail válido.
#  Considere que um email válido não deve ter espaços, deve conter 01 arroba e terminar com .com


def validar_email(email):
    if "@" in email:
       separada = email.split("@")
       match separada[1]:
            case "gmail.com":
               return True
            case "hotmail.com":
               return True
            case "email.com":
               return True
            case "academico.ifpb.edu.br":
               return True
            case _:
               return False
    else:
        return False

# Escreva uma função calcular_pagamento que aceita os parâmetros nomeados horas_trabalhadas e taxa_hora e retorna o pagamento total.

def calcular_pagamento(horas_trabalhadas, taxa_hora):
    return horas_trabalhadas * taxa_hora

# Crie uma função que retorne o maior número dentre 3 elementos.

def maior_numero(a, b, c):

    maior = a

    if b > maior:
        maior = b
    
    if c > maior:
        maior = c
    
    return maior

# Escreva uma função em Python function que aceita uma string e retorna a quantidade de letras maiúsculas e minúsculas.

def contagem_letras(coisa):
    tm = len(coisa)
    maior = 0
    menor = 0
    for i in range(tm):
        if ord(coisa[i]) >= 65 or ord(coisa[i]) <= 90:
            maior += 1
        if ord(coisa[i]) >= 97 or ord(coisa[i]) <= 122:
            menor += 1
    return (maior, menor)
