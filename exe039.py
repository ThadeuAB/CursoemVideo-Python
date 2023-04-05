from datetime import date
print('===Exercicio 39===')
nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
if idade < 18:
    print(f'Idade: {idade}. Ainda nao e hora de se alistar. Falta {18 - idade} anos.')
elif idade == 18:
    print(f'Idade: {idade}. Hora de se alistar.')
else:
    print(f'Idade: {idade}.Passou do tempo do alistamento por {idade - 18} anos')