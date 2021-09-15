larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
litros = area / 2  # a cada 2m², preciso de 1l de tinta #
print(f'Sua parede tem as dimensões de {larg} x {alt} e uma área de {area}m².')
print(f'Você precisará de {litros}l de tinta.')
