'''Crie um program que leia um número e mostre na tela
 o seu dobro, triplo e a raiz quadrada desse numero.'''

# 1- Pedi um número
n = int (input('Digite um número: '))
# 2- Fazendo os calculos 
d = n * 2
t = n * 3 
r = n ** (1/2)
# 3- Mostrando os resultados 
print ('O dobro de {} é {}'.format(n, d))
print ('O tripo de {} é {}'.format(n, t))
print ('A raiz quadrada de {} é igual a {}'.format(n, r))
