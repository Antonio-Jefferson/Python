'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
 e mostre quantos dólares ela pode comprar.'''

r = float(input('Quanto dinheiro você tem na carteira: R$ '))
dola = r / 5.57
print('Com R$ {:.2f} reais você comprar {:.2f} dólas'.format(r, dola))