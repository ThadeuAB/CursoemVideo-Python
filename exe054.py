from datetime import date
print('===Exercicio 54===')
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if atual - ano >=21:
        maior += 1
    else:
        menor += 1
print(f'{maior} candidatos sao maior de idade')
print(f'{menor} candidatos sao menor de idade')