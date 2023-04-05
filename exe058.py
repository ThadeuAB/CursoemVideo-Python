from random import randint
print('==Exercicio 58==')
comp = randint(0,10)
chute = 1
print('***O computador escolheu um numero entre 0 e 10***')
play = int(input('Qual numero voce acha que e? '))
while play != comp:
    if play>comp:
        print('Um pouco menos')
    elif play<comp:
        print('Um pouco mais')
    chute = chute+1
    play = int(input('Errou, tente de novo: '))
print(f'Acertou! Voce precisou de {chute} chutes para acertar')
