nome = input('Aluno, qual é o seu nome? ')
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda] nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é: {media}')

if media >= 5:
    print(f'Parabéns, {nome}! Você passou de ano!')
elif media == 5:
    print(f'{nome}, você está de recuperação, que vergonha hein.')
else:
    print(f'Poxa, {nome}! Você reprovou esse bimestre. Estude mais no próximo!')
input()