#Crie um programa que leia um número e mostre na tela seu sucessor e antecessor.

n = int (input('Digite um número:'))
suc = n + 1
ant = n - 1
print('O sucesso do número {} é {} e o antecessor é igual a {}'.format(n, suc, ant))