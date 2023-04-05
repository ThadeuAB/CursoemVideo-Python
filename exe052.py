print('===Exercicio 52===')
n = int(input('Digite o valor que deseja saber se e um numero primo: '))
pr = 0
for c in range(1,n+1):
    if n%c==0:
       print('\033[33m', end='')
       pr += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO numero {n} foi divisivel {pr} vezes.')
if pr==2:
    print(f'O numero {n} e primo')
else:
    print(f'O numero {n} nao e primo')