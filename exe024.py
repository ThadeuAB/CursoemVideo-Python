print('===Exercicio 24===')
cid = str(input('Digite o nome da cidade: ')).strip()
print('Contem Santo no nome: {}'.format(cid[:5].upper() == 'SANTO'))