print('===Exercicio 82===')
alist = []
blist = []
clist = []
cont = ''
while cont != 'N':
    n = (int(input('Digite um valor: ')))
    alist.append(n)
    if n%2 == 0:
        blist.append(n)
    else:
        clist.append(n)
    cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
print(f'Lista digitada: {alist}')
print(f'Lista com numeros pares: {blist}')
print(f'Lista com numeros impares: {clist}')