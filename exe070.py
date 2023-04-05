print('===Exercicio 70===')
c = 0
nmenor = ''
menor = 0
mil = 0
tot = 0
print('-*'*15)
print('LOJA DE GRATIS')
print('-*'*15)
while True:
    c += 1
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preco: R$ '))
    tot += preco
    if c == 1:
        nmenor = nome
        menor = preco
    if preco > 1000.00:
        mil += 1
    if preco < menor:
        menor = preco
        nmenor = nome
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('---FIM DO PROGRAMA---')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nmenor} que custa R${menor:.2f}')

