''' Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
 até 200Km e R$0,45 parta viagens mais longas.'''

d = float(input('Qual é a distância da viagem?: '))
valor1 = d * 0.50
valor2 = d * 0.45
if d <= 200:
    print('A viagem de {}km vai custar R${}'.format(d, valor1))
else:
    print('A viagem de {}km vai custar apenas R${}.'.format(d, valor2))
print('Tenha uma boa viagem!')   