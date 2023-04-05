print('===Exercicio 59===')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
esc = 1
while esc != 5:
    print('=*'*20)
    print('****M E N U****')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos numeros')
    print('[5] - Sair do Programa')
    esc = int(input('Qual opcao deseja: '))
    if esc == 1:
        print(f'A soma de {n1} e {n2} e igual a {n1+n2}')
    elif esc == 2:
        print(f'O produto de {n1} e {n2} e igual a {n1*n2}')
    elif esc == 3:
        if n1>n2:
            print(f'{n1} e maior que {n2}')
        elif n2>n1:
            print(f'{n2} e maior que {n1}')
        else:
            print('Os valores dados sao iguais')
    elif esc == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif esc > 5 or esc == 0:
        print('Digite uma opcao valida')
print('PROGRAMA FINALIZADO')