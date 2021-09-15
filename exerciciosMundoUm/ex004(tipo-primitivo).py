a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
# a variável seguida de '.isnumeric()'  # verifica se ela é numérica, isso vale para as outros testes.
print('É alfabético?', a.isalpha())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print(f'É numérico? {a.isnumeric()}')
print(f'Está capitalizada? {a.istitle()}')
#  formatação nas duas últimas aplicando o .format, que é o novo padrão do Python.
