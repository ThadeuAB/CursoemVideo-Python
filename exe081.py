print('===Exercicio 81===')
lista = []
cont = ''
while cont != 'N':
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} elementos')
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')