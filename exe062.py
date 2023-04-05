print('===Exercicio 62===')
print('Progressao Aritmetica')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
t = int(input('Quantos termos da PA deseja ver? '))
count = 1
orig = n
total = 0
while t !=0:
    total = total+t
    while count <= total:
        print(f'{n}',end=' → ')
        n = n+r
        count += 1
    print('Pausa')
    t = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'PA finalizada com {total} termos mostrados.')