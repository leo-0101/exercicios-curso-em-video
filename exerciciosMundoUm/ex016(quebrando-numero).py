# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

from math import trunc  # importa um comando expecífico da biblioteca 'math'

num = float(input('Insira um número: '))
print(f'O valor informado foi {num} e sua parte inteira é: {trunc(num)}')
# o comando vai 'truncar', isto é, vai nos mostrar somente o valor inteiro.
print(f'O valor informado foi {num} e sua parte inteira é: {int(num)}')
#  também vai nos mostrar somente a porção inteira

