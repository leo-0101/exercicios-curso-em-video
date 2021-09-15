# Faça um programa que  tenha uma função chamada area() que receba as dimensões
# de um terreno retangular largura x comprimento e mostre a área do terreno

def area(larg, comp):
    area = comp * larg
    print(f'A área total do terreno de {comp}mts de frente, com {larg} de lateral é: {area:.2f}m²')


print('-' * 20)
print('Calculando valores')
print('-' * 20)
comp = float(input('Quantos metros o terreno possui de frente? '))
larg = float(input('Quantos metros o terreno possui de lado? '))

area(comp, larg)
# aqui pude usar o nome dos parâmetros da função como variáveis fora da função e não deu problemas.
