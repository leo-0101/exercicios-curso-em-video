# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. #

sal = float(input('Qual é o seu salário atual? R$: '))
salReajustado = sal + (sal * 0.15)

print(f'Parabéns! Seu novo salário com o aumento de 15% será de: R$: {salReajustado:.2f}.')