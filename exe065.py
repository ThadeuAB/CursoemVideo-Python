print('===Exercicio 65===')
count = 0
soma = 0
esc = 'B'
maior = 0
menor = 0
num = 0
while esc != 'N':
    num = int(input('Digite um valor: '))
    soma = soma+num
    count = count+1
    if count == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    esc = str(input('Deseja digitar outro numero? [S/N] ')).upper()
    while esc != 'S' and esc != 'N':
        print('OPCAO INVALIDA!')
        esc = str(input('Deseja digitar outro numero? [S/N]')).upper()
print(f'Foram digitados {count} valores. A media dos valores foi de {soma/count:.1f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')