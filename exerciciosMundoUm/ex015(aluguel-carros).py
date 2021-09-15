# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = int(input('Quantidade de dias alugados: '))
kmPercorrido = float(input('Informe a quantidade de Km percorridos: '))
pago = (diasAlugados * 60) + (kmPercorrido * 0.15)
print(f'Você precisa pagar: R$: {pago}.')
