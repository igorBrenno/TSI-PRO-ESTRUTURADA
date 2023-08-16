"""
Escreva um programa que solicite ao usuário o raio de um círculo e
calcule a área e o perímetro desse círculo. Imprima os resultados formatados.
"""

import math
raio = int(input("Diga um raio: "))

area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print(f"Area do circulo: {area:.2f}")
print(f"Perimetro do circulo: {perimetro:.2f}")