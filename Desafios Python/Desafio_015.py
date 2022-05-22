'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos quilometros percorrido?: '))
dias = int(input('Quantos dias percorridos?: '))
preço = (km * 0.15) + (dias * 60)
print(' você vai precisar pagar {:.2f}, por {:.2f}km rodados e {} dia'.format(preço, km, dias) )