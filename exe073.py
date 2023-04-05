print('===Exercicio 73===')
print('Classificacao Campeonato Brasileiro 2007')
clas = ('São Paulo','Santos','Flamengo','Fluminense','Cruzeiro',
        'Grêmio','Palmeiras','Atlético-MG','Botafogo','Vasco','Internacional','Atlético-PR',
        'Figueirense','Sport','Náutico','Goiás','Corinthians','Juventude','Paraná Clube','América-RN')
print('MENU')
print('1 - Os 5 primeiros colocados')
print('2 - Os 4 ultimos colocados')
print('3 - Participantes em ordem alfabetica')
print('4 - Posicao do seu time')
esc = int(input('Marque a opcao: '))
while esc<1 or esc>4:
    esc = int(input('Invalido.Marque a opcao: '))
if esc==1:
    print(clas[:5])
if esc==2:
    print(clas[16:])
if esc==3:
    print(sorted(clas))
if esc==4:
    club = str(input('Qual clube deseja verificar? '))
    print(clas.index(club)+1)