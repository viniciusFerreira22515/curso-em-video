print('{}Desafio 012{}'.format('=' * 5, '=' * 5))
p = float(input('Digite o preço: R$'))
np = p - (p*5/100)
print('Preço com desconto de 5%: R${:.2f}'.format(np))
