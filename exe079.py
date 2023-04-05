print('===Exercicio 79===')
print('Digite valores.Valores repetidos serao ignorados.')
cont = ''
valores = []
while cont != 'N':
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado.')
    else:
        print('Valor repetido, nao sera inserido.')
    cont = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
valores.sort()
print(f'Lista digitada em ordem: {valores}')