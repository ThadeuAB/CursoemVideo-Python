from time import sleep

def maior(*num):
    cont = maior = 0
    print('=*'*30)
    print('Analisando valores...')
    for v in num:
        print(f'{v} ',end='')
        sleep(0.2)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'Maior valor informado foi {maior}')


print('===Exercicio 99===')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()