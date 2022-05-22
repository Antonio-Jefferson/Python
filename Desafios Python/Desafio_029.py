'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.'''

v = int(input('Qual é a velocidade do seu carro: ')) # pedindo a velocidade do carro 
if v <= 80:
    print('Tenha um bom dia. Dirija com cuidado!')
else:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
m = ( v - 80 ) * 7                            # calculo de quando a multa vai ser
print('Você pagara um multa de R${}'.format(m))
print('Dirija com cuidado, tenha um bom dia.')   