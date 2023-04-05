from time import sleep


def contador(i,f,p):
    print('-='*20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.2)
            cont -= p
        print('FIM!')


print('===Exercicio 98===')
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Sua vez...')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)