print('===Exercicio 74===')
from random import randint
tup = ((randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)))
print('Os valores sorteados foram: ',end='')
for c in tup:
    print(f'{c}',end=' ')
print(f'\nO maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')

