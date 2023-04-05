print('===Exercicio 86===')
matriz =[[],[],[]]
for c in range(0,3):
    matriz[0].append(int(input(f'Digite um valor para [0,{c}]: ')))
for c in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para [1,{c}]: ')))
for c in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para [2,{c}]: ')))
print('=*'*40)
print(f'{matriz[0][0]:^5}  {matriz[0][1]:^5}  {matriz[0][2]:^5}')
print(f'{matriz[1][0]:^5}  {matriz[1][1]:^5}  {matriz[1][2]:^5}')
print(f'{matriz[2][0]:^5}  {matriz[2][1]:^5}  {matriz[2][2]:^5}')