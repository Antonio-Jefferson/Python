'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
 superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

s = float(input('Qual é seu salário:'))
# calculando o novo salário
a1 = (s * 110) / 100
a = (s * 115) / 100
# condição para o aumneto de 15% ou 10%
if s <= 1250.00:
    print('Seu novo salário sera de {}'.format(a))
else: 
    print('Seu novo salário sera de {}'.format(a1)) 
