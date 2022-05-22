''' : Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# 1- ESCOLHER UMNÚMERO ALEATÓRIO.
# 2- PEDIR PARA PESSOA ESCOLHER UM NÚMERO ENTRE 0 E 5.
# 3- MOSTRAR NA TELA SE ELA ACERTOU OU ERROU.

from random import randrange
from time import sleep
num = randrange(0,5) # tá sorteando o numero 
print('====== Adivinhe o número entre 0 e 5 =======')
n = int(input('Em qual número estou pensando: ')) # o jogador escolher um número.
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('Você acertou o número, PARABÉNS.') # se o jogador acertar vai digitar isso.
else:
    print('Você errou, eu estava pensando no {} e não no {}.'.format(num, n)) # se não acertar vai digitar isso.
    

print('=========== FIM ============')