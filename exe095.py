print('===Exercicio 95===')
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).upper()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f'Quantos gols na {c+1}º partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for i,j in enumerate(time):
    print(f'{i:>3} ',end='')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para sair): '))
    if busca == 999:
        print('Volte sempre!')
        break
    if busca >= len(time):
        print('Numero invalido. Digite valor mostrado na referencia "cod". ')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)