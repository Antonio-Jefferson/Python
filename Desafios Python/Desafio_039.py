'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano = int(input('Digite sua data de nascimento:'))
idade = 2022 - ano 
if idade == 18: 
    print('E a hora exta de se alistar ao serviço militar')
elif idade < 18: 
    print('Você ainda é muito novo para se alistar daqui a {} anos você pode se alistar'.format((idade-18) * -1))
elif idade > 18: 
    print('Você está bem atrsado com seu alistamento, você devai ter se alistado a {} anos atrás'.format(idade - 18))


