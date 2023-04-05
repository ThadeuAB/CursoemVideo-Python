from random import randint
from time import sleep
print('===Exercicio 88===')
jog = int(input('Quantos jogos deseja? '))
pal = []
dado = []
for c in range(0,jog):
    cont = 0
    while True:
        n = randint(1,60)
        if n not in dado:
            dado.append(n)
            cont += 1
        if cont >= 6:
           break
    dado.sort()
    pal.append(dado[:])
    dado.clear()
for v,c in enumerate(pal):
    print(f'Jogo {v+1}: {c}')
    sleep(1)
print('Boa sorte!!')
