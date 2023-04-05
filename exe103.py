def ficha(name='<desconhecido>',score=0):
    print(f'O jogador {name} fez {score} gols no campeonato')

print('===Exercicio 103===')
nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols marcou: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(score=gols)
else:
    ficha(nome,gols)