print('===Exercicio 90===')
classe = dict()
sit = ''
classe['Nome'] = str(input('Nome: '))
med = float(input(f'Media de {classe["Nome"]}: '))
classe['Media'] = med
if med >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
classe['Situacao'] = sit
for k,v in classe.items():
    print(f'{k} e igual a {v}')