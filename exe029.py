print('===Exercicio 29===')
vel = float(input('Qual a velocidade que o carro estava? '))
if vel <= 80:
    print('Velocidade dentro do permitido')
else:
    print('Nesse caso a multa sera de {} reais'.format((vel-80)*7))