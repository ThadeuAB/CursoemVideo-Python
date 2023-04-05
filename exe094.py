print('===Exercicio 94===')
dados = dict()
galera = list()
cont = ''
soma = media = 0
while cont != 'N':
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    sex = str(input('Sexo[M/F]: ')).upper().strip()[0]
    while sex not in 'MF':
        print('ERRO! Valor deve ser M ou F.')
        sex = str(input('Sexo[M/F]: ')).upper().strip()[0]
    dados['sexo'] = sex
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        print('ERRO! Valor deve ser S ou N!')
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade foi de {media:5.2f} anos')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ',end=' ')
print()
print('Lista de pessoas com idade acima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('  ',end='')
        for k,v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('ENCERRADO')