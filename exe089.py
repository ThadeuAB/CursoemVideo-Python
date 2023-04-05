print('===Exercicio 89===')
boletim = list()
cont = ''
while cont != 'N':
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    boletim.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('=*'*45)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for c,v in enumerate(boletim):
    print(f'{c:<4} {v[0]:<10} {v[2]:>8.1f}')
while True:
    print('='*45)
    opc = int(input('Mostrar nota de qual aluno? (999 para interromper): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} sao {boletim[opc][1]}')
    else:
        print('Digite uma opcao valida.')
print('<<<VOLTE SEMPRE>>>')