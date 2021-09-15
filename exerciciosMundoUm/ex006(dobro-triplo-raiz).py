valorUm = int(input('Digite um valor: '))

resultadoDobro = valorUm * 2
resultadoTriplo = valorUm * 3
raizQuadrada = valorUm ** (1/2)  # pow(n, (1/2)) <= também funciona com a função #

print(f'O dobro de {valorUm} é: {resultadoDobro}')
print(f'O triplo de {valorUm} é: {resultadoTriplo}')
print(f'Por fim, a raiz quadrada de {valorUm} é: {raizQuadrada:.2f}.')
