'''Faça um programa que leia algo pelo teclado e mostre na tela qual 
seu tipo primitivo e todas as informações possiveis sobre ela'''

v = (input('Digite algo:'))
print('O tipo primitivo desse valor é:', type(v))
print('Tem somente espaço?', v.isspace())
print('É um número?', v.isnumeric())
print('É alfabetico?', v.isalpha())
print('É alfanumerico?', v.isalnum())
print('Está em maiúsculas?', v.isupper())
print('Está em menúsculas?', v.islower())
print('Está capitalizada?', v.istitle())
