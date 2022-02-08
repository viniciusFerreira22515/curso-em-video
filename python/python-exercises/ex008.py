#km hm dam m dm cm mm
print('{}Desafio 008{}'.format('=' * 5, '=' * 5))
m = float(input('Valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000
print('Quilômetros: {}\nHecâmetros: {}\nDecâmetros: {}'.format(km, hm, dam))
print('Metros: {}\nDecímetro: {}\nCentímetros: {:.0f}\nMilímetros: {:.0f}'.format(m, dm, c, mm))
