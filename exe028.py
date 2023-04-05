from random import randrange
print('===Exercicio 28===')
num = int(randrange(6))
print('O computador pensou em um numero entre 0 e 5')
adv = int(input('Qual numero voce acha que e? '))
if adv == num:
    print('Acertou!Parabens!')
else:
    print('Errou, que pena. O computador pensou em {}'.format(num))