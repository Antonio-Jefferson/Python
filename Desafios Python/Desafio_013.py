'''Faça um algoritmo que leia o salário
 de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Qual é o seu salário? R$ '))
aumento = (salario * 115) / 100
print('Seu salário quera de R${:.2f}, com um aumento de 15%, passou a ser R$ {:.2f}'.format(salario, aumento))