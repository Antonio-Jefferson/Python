'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
num = float(input('Digite o valor do cateto aposto: '))
num2 = float(input('Digite o valor do cateto adjacente: '))
raiz = hypot(num, num2)
print('{:.2f}'.format(raiz))

