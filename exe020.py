from random import shuffle
print('===Exercicio 20===')
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
lista = [al1,al2,al3,al4]
shuffle(lista)
print('A ordem de apresentacao sera {}'.format(lista))