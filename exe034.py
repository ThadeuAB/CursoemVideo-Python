print('===Exercicio 034===')
sal = float(input('Qual o salario atual? '))
if sal> 1250.00:
    print('Nesse caso o aumento sera de 10%, o novo salario sera de {:.2f} reais'.format(sal+(sal*10/100)))
else:
    print('Nesse caso o aumento sera de 15%, o novo salario sera de {:.2f} reais'.format(sal+(sal*15/100)))