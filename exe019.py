from random import choice
print('===Exercicio 19===')
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
lista = [al1,al2,al3,al4]
print('O aluno sorteado para apagar o quadro foi {}'.format(choice(lista)))