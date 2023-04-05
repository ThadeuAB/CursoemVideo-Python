from random import randint
from time import sleep

def sorteio(lst):
    for c in range(0,6):
        n = randint(1,10)
        lst.append(n)
        print(f'{n} ',end='')
        sleep(0.2)
    print('Pronto!!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores PARES foi {soma}')


print('===Exercicio 100===')
num = list()
sorteio(num)
somaPar(num)