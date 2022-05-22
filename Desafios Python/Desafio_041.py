''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date

# ler o  ano de nascimento 
ano = int(input('Em qual ano você nasceu: '))
atual = date.today().year
idade = atual - ano 
# se ele é mirim 
if idade <= 9: 
    print(' Você tem {} ano e está na categoria MIRIM.'.format(idade))
# infantil
elif idade > 9 and idade <= 14: 
    print('Você tem {} ano e está na categoria INFANTIL.'.format(idade))
# junior 
elif idade > 14 and idade <= 19: 
    print('Você tem {} e está na categoria JÚNIOR.'.format(idade))
# senior 
elif idade > 19 and idade <= 25: 
    print('Você tem {} anos e está na categoria SÊNIOR'.format(idade))
# MASTER
else: 
    print('Você tem {} ano e está na categoria MASTER'.format(idade))
