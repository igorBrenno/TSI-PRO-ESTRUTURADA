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
        if (ord(coisa[i]) >= 65 and ord(coisa[i]) <= 90):
            maior += 1
        if (ord(coisa[i]) >= 97 and ord(coisa[i]) <= 122):
            menor += 1
    return (maior, menor)

# Crie uma função chamada len_custom que aceita um iterável (por exemplo, uma lista ou uma string) como argumento e retorna o
# número de elementos no iterável. Ela deve ter o mesmo comportamento que a função embutida len().

def len_custom(coisa):
    contador = 0
    for i in coisa:
        contador += 1
    return contador

# Crie uma função chamada sum_custom que aceita uma lista de números como argumento e retorna a soma de todos os números na lista.
# Ela deve ter o mesmo comportamento que a função embutida sum().

def sum_custom(coisa):
    contador = 0
    for i in coisa:
        contador += i
    return contador

# Crie uma função chamada max_custom que aceita uma lista de números como argumento e retorna o maior número na lista. Ela deve ter o
# mesmo comportamento que a função embutida max().

def max_custom(coisa):
    if coisa == []:
        maior = None
    maior = coisa[0]
    tm = len(coisa)
    for i in range(tm):
        if coisa[i] > maior:
            maior = coisa[i]
    return maior

# Crie uma função que aceita *args e retorna a soma de todos os números passados como argumentos.

def aceitaArgs(*args):
    soma = 0 
    for i in args:
        soma += i
    return soma

print(aceitaArgs(1, 2, 3, 4))

# Escreva uma função que recebe *args e retorna o número de argumentos passados.

def argumentoPassado(*args):
    contador = 0
    for i in args:
        contador += 1
    return contador

print(argumentoPassado(1, 4, 5, 7, 9))

# Considerando a PEP 257 que trata da convensão de docstrings em python, selecione as 3 primeiras funções desta lista e crie a documentação.

def argumentoPassado(*args):
    """
    ## Uma função que calcula a quantidade de elementos passados para a função
    - A função irá receber uma tupla de valores que vai passar por um loop for, que vai contar quantos valores foram passado
    """


    contador = 0
    for i in args:
        contador += 1
    return contador

print(argumentoPassado(1, 4, 5, 7, 9))

# Considere a função a seguir e responda: Por que o valor da variável 'temperatura' não foi alterada? De que forma podemos
#  alterar o código para que esta variável seja modificada?

temperatura = 30
def ligar_ar():
    temperatura = 20

ligar_ar()
print(temperatura)

# A função filter é uma função que aceita uma outra função como argumento e um iterável (*args). Ela filtra todos os valores
#  que são False a partir da primeira função passada, retornando uma lista de valores que retornaram True. Crie um filtro que
#  recebe uma lista de números e retorna os pares.

def funcaoPares(*args):
    
    return list(filter(lambda i : i % 2 == 0, args))
print(funcaoPares(1, 2 , 4, 5, 7, 9 , 10))

# A função map é uma função que aceita uma outra função como argumento e um iterável (*args). Ela retorna uma lista de valores
#  que passaram pela primeira função passada como argumento. Crie uma lista que formata todos os nomes passados para um valor em maiúsculo.

