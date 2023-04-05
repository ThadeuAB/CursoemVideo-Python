print('===Exercicio 69===')
man = 0
wmenor = 0
maior = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sex == 'M':
        man +=1
    if sex == 'F' and idade < 20:
        wmenor += 1
    print('-'*20)
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-'*20)
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('===FIM DO PROGRAMA===')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo foram cadastrados {man} homens')
print(f'E temos {wmenor} mulheres com menos de 20 anos')