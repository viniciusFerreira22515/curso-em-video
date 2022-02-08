#Tinta: 1L = 2m²
print('{}Desafio 011{}'.format('=' * 5, '=' * 5))
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
ar = l*a
t = ar / 2
print('Área: {:.2f}m²\nQuantidade de tinta: {:.2f}L'.format(ar, t))
