print('===Exercicio 56===')
sidade = 0
velho = 0
nvelho = ''
mul = 0
for c in range(1,5):
    print(f'---{c}º PESSOA ---')
    nome = str(input('Nome: ')).strip()
    sex = str(input('Sexo (M/F): ')).upper().strip()
    idade = int(input('Idade: '))
    sidade = sidade+idade
    if sex == 'M':
        if idade > velho:
            velho = idade
            nvelho = nome
    if sex == 'F':
        if idade < 20:
            mul = mul+1
med = sidade/4
print(f'A media de idade do grupo e {med:.1f}')
if velho>0:
    print(f'O homem mais velho e {nvelho} com {velho} anos')
if mul>0:
    print(f'Existe {mul} mulheres abaixo de 20 anos')


