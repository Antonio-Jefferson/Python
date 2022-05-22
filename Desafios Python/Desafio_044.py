'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
 normal e condição de pagamento:'''


produto = float(input('Digite o valor do produto: R$ '))
print('--- ESCOLHA UMA FORMA DE PAGAMENTO ABAIXO ---')
print('''
[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão ''')
opção = int(input('Sua opção: '))
# desconto de 10%
desconto = produto * 90 / 100
desconto2 = produto * 95 / 100
juro = produto * 120 / 100

# à vista dinheiro/cheque: 10% de desconto
if opção == 1: 
    print('Você pagando a vista em dinheiro/ cheque você tem 10% de desconto')
    print('Você pagarar {} com o desconto de 10%.'.format(desconto))
# à vista no cartão: 5% de desconto
elif opção == 2:
    print('Você pagando á vista no cartão tem um desconto de 5%')
    print('Você pagarar R${} com o desconto de 5%'.format(desconto2))
# em até 2x no cartão: preço formal 
elif opção == 3:
    print(' Você pagando em até 2x no cartão fica o preço formal de R${} do produto'.format(produto))

# 3x ou mais no cartão: 20% de juros
elif opção == 4: 
    print(' Pangando em até 3x no cartão tem um juros de 20%')
    print('Com o juros de 20% você pagara R${} agora'.format(juro))
else: 
    print('OPÇÃO ÍNVALIDA')
    print('POR FAVOR ESCOLHAR UMA OPÇÃO SUJERIDA ACIMA.')