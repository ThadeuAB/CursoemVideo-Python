print('===Exercicio 93===')
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0,tot):
    partidas.append(int(input(f'Quantos gols na {c+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=*'*30)
print(jogador)
print('=*'*30)
for k,v in jogador.items():
    print(f'O campo {k} possui valor {v}')
print('=*'*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gols.')
print(f'Total de {jogador["total"]} gols')