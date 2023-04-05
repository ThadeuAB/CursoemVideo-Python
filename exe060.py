from math import factorial
print('===Exercicio 60===')
print('*****FATORIAL***')
num = int(input('Digite o numero que deseja ver o fatorial: '))
fat = factorial(num)
cont = num
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont} ', end='')
    print('x ' if cont > 1 else '= ', end='')
    cont = cont-1

print(f'{fat}')