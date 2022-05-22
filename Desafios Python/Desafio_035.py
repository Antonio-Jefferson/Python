'''Desenvolva um programa que leia o comprimento de 
três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulos')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulos')

print('-='*20)