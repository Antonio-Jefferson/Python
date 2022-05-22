'''Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import cos, tan, sin, radians
a = float(input('Digite o ângulo que você deseja: '))
print('O ãngulo de {} tem o seno de {:.2f}'.format(a, sin(radians (a))))
print('O Ângulo de {} tem o cosseno de {:.2f}'.format(a, cos(radians(a))))
print('O Ângulo de {} tem a tangente de {:.2f}'.format(a, tan(radians(a))))

