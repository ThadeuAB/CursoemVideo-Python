print('===Exercicio 40===')
n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
med = (n1+n2)/2
if med < 5:
    print(f'Com media de {med:.1f}. Aluno esta REPROVADO.')
elif med >=7:
    print(f'Com media de {med:.1f}. Aluno esta APROVADO.')
else:
    print(f'Com media de {med:.1f}. Aluno esta em RECUPERACAO.')