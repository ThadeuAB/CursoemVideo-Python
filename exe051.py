print('===Exercicio 51===')
print('===10 primeiros termos de uma Progressao Aritmetica===')
n = int(input('Qual o primeiro termo? '))
r = int(input('Qual e a razao? '))
for c in range(n,n+(10*r),r):
    print(c,end=' → ')
print('ACABOU')