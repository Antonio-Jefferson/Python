''' Escreva um programa que leia um valor em metros
 e o exiba convertido em centímetros e milímetros.'''

m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 1000
print('{}m equivalem a {}cm'.format(m, cm))
print('{}m equivalem a {}mm'.format(m, mm))
