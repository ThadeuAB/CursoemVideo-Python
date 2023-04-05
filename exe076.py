print('===Exercicio 76===')
lista=('Papel', 5.90, 'Caneta', 3.55, 'Borracha', 0.75)
print('-'*15)
print('---LISTA---')
print('-'*15)
for c in range(0,len(lista),2):
    print(f'{lista[c]:.<30} R$ ',lista[c+1])