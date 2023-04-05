print('===Exercicio 77===')
grupo = ('VILA VELHA', 'VITORIA', 'SERRA', 'CARIACICA', 'GUARAPARI', 'VIANA','COLATINA')
for c in grupo:
    print(f'\nNa palavra {c} temos ',end='')
    for l in c:
        if l.upper() in 'AEIOU':
            print(l,end=' ')