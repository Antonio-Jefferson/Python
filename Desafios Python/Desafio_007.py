'''Desenvolva um programa que leia as duas
 notas de um aluno, calcule e mostre a sua média.'''

# 1- pedir as notas.

nota1 = float(input('Digite sua primeira nota: ')) 
nota2 = float(input('Digite sua segunda nota: '))

# 2- calcular a média.

media = (nota1 + nota2) / 2 

# 3- mostrar o resultado na tela.

print('A média da sua nota é, {}'.format(media))