'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulos')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
         print('ESCALENO')
    else: 
        print('ISÓSCELES')     
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulos')

print('-='*20)