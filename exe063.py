print('===Exercicio 63===')
n = int(input('Quantos numeros da sequencia de Fibonacci deseja ver? '))
v1 = 0
v2 = 1
v3 = 0
c = 1
print('0 → ',end='')
while c != n:
    print(f'{v2}',end=' → ')
    c = c+1
    v3 = v1+v2
    v1 = v2
    v2 = v3
print('Acabou')