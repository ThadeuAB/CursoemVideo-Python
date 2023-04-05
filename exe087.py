print('===Exercicio 87===')
matriz =[[],[],[]]
par = 0
maior = 0
for c in range(0,3):
    n = (int(input(f'Digite um valor para [0,{c}]: ')))
    matriz[0].append(n)
    if n%2 == 0:
        par = par+n
for c in range(0,3):
    n = (int(input(f'Digite um valor para [1,{c}]: ')))
    matriz[1].append(n)
    if n > maior:
        maior = n
    if n%2 == 0:
        par = par+n
for c in range(0,3):
    n=(int(input(f'Digite um valor para [2,{c}]: ')))
    matriz[2].append(n)
    if n%2 == 0:
        par = par+n
col = matriz[0][2]+matriz[1][2]+matriz[2][2]

print('=*'*40)
print(f'{matriz[0][0]}  {matriz[0][1]}  {matriz[0][2]}')
print(f'{matriz[1][0]}  {matriz[1][1]}  {matriz[1][2]}')
print(f'{matriz[2][0]}  {matriz[2][1]}  {matriz[2][2]}')
print('=*'*40)
print(f'A soma dos valores pares e {par}')
print(f'A soma dos valores da segunda coluna e de {col}')
print(f'O maior valor da segunda linha e {maior}')