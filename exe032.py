from datetime import date
print('===Exercicio 32===')
ano = int(input('Qual ano deseja saber se e bissexto? Digite "0" para ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano%400 == 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print('{} nao e um ano bissexto'.format(ano))