print('===Exercicio 71===')
print('/'*30)
print('B A N C O P A T I N H A S')
print('/'*30)
saque = int(input('Qual valor deseja sacar? R$ '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total ==0:
            break
print('/'*30)
print('Obrigado! Volte sempre.')