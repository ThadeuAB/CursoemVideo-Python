from random import randrange
from emoji import emojize
from time import sleep
print('===Exercicio 45===')
print('='*20)
print('-J-O-K-E-N-P-O')
print('='*20)
comp = randrange(3)
print('0 - PEDRA')
print('1 - PAPEL')
print('2 - TESOURA')
play = int(input('Escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if play == 0:
    print(emojize('Voce escolheu :oncoming_fist:'))
    if comp == 0:
        print(emojize('O computador escolheu :oncoming_fist: .EMPATE'))
    elif comp == 1:
        print(emojize('O computador escolheu :waving_hand: .VOCE PERDEU'))
    elif comp == 2:
        print(emojize('O computador escolheu :victory_hand: .VOCE GANHOU'))
elif play == 1:
    print(emojize('Voce escolheu :waving_hand:'))
    if comp == 0:
        print(emojize('O computador escolheu :oncoming_fist: .VOCE GANHOU'))
    elif comp == 1:
        print(emojize('O computador escolheu :waving_hand: .EMPATE'))
    elif comp == 2:
        print(emojize('O computador escolheu :victory_hand: .VOCE PERDEU'))
elif play == 2:
    print(emojize('Voce escolheu :victory_hand:'))
    if comp == 0:
        print(emojize('O computador escolheu :oncoming_fist: .VOCE PERDEU'))
    elif comp == 1:
        print(emojize('O computador escolheu :waving_hand: .VOCE GANHOU'))
    elif comp == 2:
        print(emojize('O computador escolheu :victory_hand: .EMPATE'))
else:
    print('Escolha uma opcao valida')
