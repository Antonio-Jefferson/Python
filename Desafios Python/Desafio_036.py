'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
 o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não 
 pode exceder 30% do salário ou então o empréstimo será negado.'''


casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em qunatos anos quer pagar: '))
prestacao = casa / (12 * anos)
minimo = salario * 30 / 100
print('Para comprar uma casa de R${} em {} anos com um salário de R${} com uma pretação de R${}'.format(casa, anos, salario, prestacao))
if prestacao <= minimo:
    print('O seu emprestimos foi APROVADO!')
else: 
    print('O seu emprestimo foi NEGADO!')