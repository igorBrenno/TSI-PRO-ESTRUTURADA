'''
Exercício 12: Dada a lista de frutas e a lista de cores abaixo,
utilize a função zip() e um loop "for" para imprimir cada fruta com sua respectiva cor.
'''

frutas = ['maçã', 'banana', 'laranja', 'uva']
cores = ['vermelho', 'amarelo', 'laranja', 'roxa']

juncao = zip(frutas, cores)
for i in juncao:
    print(i)