from datetime import date


def voto(age):
    age = idade
    if age < 16:
        return print(f'Com {idade} anos, NAO VOTA!')
    elif age >=16 and age <18 or age >=65:
        return print(f'Com {idade} anos, VOTO OPCIONAL!')
    elif age >=18 and age <65:
        return print(f'Com {idade} anos, VOTO OBRIGATORIO!')


print('===Exercicio 101===')
ano = int(input('Digite o ano de nascimento: '))
idade = (date.today().year) - ano
voto(idade)