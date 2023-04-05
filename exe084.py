print('===Exercicio 84===')
grupo = []
dado = []
maior = 0
menor = 0
cont = ''
while cont != 'N':
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso(kg): ')))
    if len(grupo) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    grupo.append(dado[:])
    dado.clear()
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('=*'*40)
print(f'Ao todo voce cadastrou {len(grupo)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ',end='')
for c in grupo:
    if c[1] == maior:
        print(f'{c[0]}, ',end='')
print(f'\nO menor peso foi de {menor}kg. Peso de ',end='')
for c in grupo:
    if c[1] == menor:
        print(f'{c[0]}, ',end='')