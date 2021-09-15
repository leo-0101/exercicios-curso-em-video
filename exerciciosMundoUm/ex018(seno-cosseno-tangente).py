# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))  # pega o angulo, converte em radiano e por fim pega o seno dele
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'O ÂNGULO de {angulo} tem o seno de: {seno:.2f}')
print(f'O COSSENO de {angulo} é: {cos:.2f}')
print(f'A TANGENTE de {angulo} é: {tang:.2f}')

# math.radians()  # converte o valor em radiano (é preciso isso pq o comando so aceita valores assim.)
