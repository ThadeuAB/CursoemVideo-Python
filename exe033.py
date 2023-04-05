print('===Exercicio 33===')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1>n2 and n1>n3:
    print('o maior numero e {}'.format(n1))
    if n2>n3:
        print('O menor numero e {}'.format(n3))
    else:
        print('O menor numero e {}'.format(n2))
if n2>n1 and n2>n3:
    print('O maior numero e {}'.format(n2))
    if n1>n3:
        print('O menor numero e {}'.format(n3))
    else:
        print('O menor numero e {}'.format(n1))
if n3>n2 and n3>n1:
    print('O maior numero e {}'.format(n3))
    if n2>n1:
        print('O menor numero e {}'.format(n1))
    else:
        print('O menor numero e {}'.format(n2))