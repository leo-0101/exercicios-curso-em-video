# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. #

preco = float(input('Preço do produto: '))
desconto = preco - (preco * 0.05)

print(f'O preço do produto com desconto é: R$: {desconto:.2f}.')
