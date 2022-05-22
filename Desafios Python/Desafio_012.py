'''Faça um algoritmo que leia o preço
 de um produto e mostre seu novo preço, com 5% de desconto.'''

produto = float(input('Quanto custa o produto?: '))
desconto = (95 * produto) / 100
print('Com o desconto de 5%, o produto que era R$ {:.2f} ficou por R$ {:.2f}'.format(produto, desconto))