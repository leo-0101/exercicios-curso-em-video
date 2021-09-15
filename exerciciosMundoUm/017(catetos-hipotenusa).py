# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
hipo = hypot(co, ca)  # importando da biblioteca fica assim: só precisando informar os dois valores

print(f'A hipotenusa vai medir: {hi:.2f}')
print(f'A hipotenusa vai medir (com o math): {hipo:.2f}')
