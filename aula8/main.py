import random
'''
1- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
Leia um número do teclado
Compare se este número está na lista
'''
def q1():
    lista = []
    for i in range(5):
        lista.append(int(input("Digite um valor: ")))
    valor = int(input("Digite o valor procurado: "))
    contador = 0
    if (valor in lista):
        for i in lista:
            if (valor != i):
                contador += 1
            else:
                break
    else:
        contador = -1
    return print(contador)



'''
2 - Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.

Crie uma lista com tamanho 50 e armazene nesta lista valores gerados aleatóriamente
Faça uma iteração na lista para verificar quantos destes números são iguais à 6
'''
def dado():

    lista = []
    contador = 0

    for i in range(50):
        lista.append(random.randrange(1, 7))

    for i in lista:
        if (i == 6):
            contador += 1
    print(lista)
    return print(contador)


'''
3- Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma: cada célulaé a soma dela mesma e das células anteriores. Imprima o vetor antes e depois da manipulação. Exemplo:

Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]
'''

def q3():
    lista = [2, 1, 20,5, 17,19,14,4, 18,2]
    listam = []
    # for i in range(10):
    #     lista.append(random.randrange(0, 21))
    
    listam.append(lista[0])
    for j in range(1, len(lista)):
        print(j)
        listam.append(lista[j-1]+lista[j])
    print(lista)
    print(listam)
q3()
