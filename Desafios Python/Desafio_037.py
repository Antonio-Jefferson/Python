'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# 1- vou ler um numero interio 
num = int(input('Digite um número inteiro qualquuer: '))
# Escolher entre 3 opções de conversão 
print('Escolha como quer coneverter')
print('Digite 1 para BINÁRIO ')
print('Digite 2 para OCTAL ')
print('Digite 3 para HEXADECIMAL ')
opcao = int(input('Sua escolha: '))
# condições 
if opcao == 1: 
    print('{} covertido em Binário é  igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em Octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print(' {} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else: 
    print('Opção invalida. Tente novamente.')
    