print('===Exercicio 61===')
print('Progressao Aritmetica')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
t = int(input('Quantos termos da PA deseja ver? '))
count = 1
while count <= t:
    print(f'{n}',end=' → ')
    n = n+r
    count += 1
print('Acabou')