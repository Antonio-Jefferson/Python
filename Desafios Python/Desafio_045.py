'''Crie um programa que faça o computador jogar Jokenpô com você'''

from random import randint # bibliotec para escolher um numeor aleatório
from time import sleep # biblioteca de tempo 

opções = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)  # fazendo aletória de 0 a 2 
print('-='*15)
print('---- FAÇA SUA JOGADA ----- ')
print('''
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Sua opção: '))
print('-='*14)
print('JÔ!')  
sleep(1)
print('KEN!') 
sleep(1) 
print('PÔ!')   
print('Jogador jogou {}'.format(opções[jogador]))
print('Computador jogou {}'.format(opções[computador]))

# Condições para escolher o vencedor

if computador == 0: # caso o computador jogar pedra
    if jogador == 0:
        print('EMPATE')
        print('-='*14)
    elif jogador == 1:
        print('JOGADOR VENCEU')
        print('-='*14)
    elif jogador == 2:
        print('COMPUTADOR VENCE')
        print('-='*14)
    else: 
        print('JOGADA INVALIDA')
elif computador == 1:  # caso o computador jogar papel 
        if jogador == 0:
            print('COMPUTADOR VENCE')
            print('-='*14)
        elif jogador == 1:
             print('EMPATE')
             print('-='*14)
        elif jogador == 2:
             print('JOGADOR VENCEU')
             print('-='*14)
        else: 
            print('JOGADA INVALIDA')
elif computador == 2:  # caso o computador jogar tesoura
        if jogador == 0:
            print('JOGADOR VENCEU')
            print('-='*14)
        elif jogador == 1:
            print('COMPUTADOR VENCE')
            print('-='*14)
        elif jogador == 2:
            print('EMPATE')
            print('-='*14)
        else: 
            print('JOGADA INVALIDA')
   
