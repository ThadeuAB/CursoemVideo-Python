print('===Exercicio 22===')
nome=str(input('Digite o nome completo: ')).strip()
print('Maisculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))
print('Total caracteres: {}'.format(len(nome)-nome.count(' ')))
print('Total de letras no primeiro nome: {}'.format(nome.find(' ')))