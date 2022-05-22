'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
 Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:'''

print('=-'*20)
print(' MEDIDOR DE ÍNDICE DE MASSA COMPORAL')
print('=-'*20)

altura = float(input(' Qual é seu altura: '))
peso = float(input( 'Quanto você pesa: '))
imc = peso / (altura * altura)

#– IMC abaixo de 18,5: Abaixo do Peso
if imc < 18.5: 
    print('Seu imc deu {:.2f}, e você está ABAXO DO PESO.'.format(imc))

#– Entre 18,5 e 25: Peso Ideal
elif imc >= 18.5 and imc < 25: 
    print('Seu imc deu {:.2f}, e você está no PESO IDEAL.'.format(imc))
#– 25 até 30: Sobrepeso
elif imc >= 25 and imc < 30:
    print('Seu IMC deu {:.2f}, e você está SOBREPESO.'.format(imc))
#– 30 até 40: Obesidade
elif imc >= 30 and imc < 40: 
    print('Seu IMC deu {:.2f}, e você está COM OBESIDADE.'.format(imc))
#– Acima de 40: Obesidade Mórbida
else: 
    print('O seu IMC deu {:.2f}, você está com OBESIDADE MÓRBIDA'.format(imc))
