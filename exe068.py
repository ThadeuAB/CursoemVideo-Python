from random import randint
print('===Exercicio 68===')
print('***Par ou Impar***')
print('Digite um valor de 0 a 10 que sera somado a um valor escolhido pelo computador')
print('=-'*20)
vit = 0
while True:
    comp = randint(0,10)
    play = int(input('Digite um valor: '))
    res = ''
    guess = str(input('PAR OU IMPAR [P/I]: ')).upper().strip()[0]
    while guess not in 'PI':
        guess = str(input('Deves digitar apenas P ou I: ')).upper().strip()[0]
    if guess == 'P':
        guess = 'PAR'
    elif guess == 'I':
        guess = 'IMPAR'
    if (comp+play)%2== 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Voce jogou {play}, o computador jogou {comp}. Total de {play+comp} deu {res}')
    print('-'*20)
    if guess == res:
        vit = vit+1
        print('Voce Venceu! Vamos de novo.')
        print('-'*20)
    elif guess != res:
        print('Voce perdeu!')
        break
print('=-'*20)
print(f'GAME OVER! Voce Venceu {vit} vezes.')


