#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer,{}!'.format(nome))
#print('Prazer em te conhecer,{:20}!'.format(nome)) #definindo quantidade de caracteres
#print('Prazer em te conhecer,{:^20}!'.format(nome)) #definindo alinhamento
#print('Prazer em te conhecer,{:>20}!'.format(nome)) #definindo alinhamento
#print('Prazer em te conhecer,{:=^20}!'.format(nome)) #isolando com espaços

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto vale {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão inteira é {} e potência {}'.format(di, e))
#\n pula linha
#end='' indica que não haverá quebra de linhas entre prints
