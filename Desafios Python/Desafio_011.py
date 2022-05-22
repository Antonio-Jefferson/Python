'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

l = float(input('Quantos metros tem de largura?: '))
a = float(input('Quantos metros tem a altura?: '))
area = l * a 
litros_de_tinta = area / 2 
print('Você vai precisar de {} litros de tinta para pintar uma área {}m²'.format(litros_de_tinta, area))
