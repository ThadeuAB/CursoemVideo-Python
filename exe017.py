from math import hypot
print('===Exercicio 17===')
print('---Calculo da Hipotenusa---')
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento da cateto adjacente: '))
print('Considerando o cateto oposto de {} e o cateto adjacente de {}, a hipotenusa e de {:.2f}'.format(cato,cata,hypot(cato,cata)))