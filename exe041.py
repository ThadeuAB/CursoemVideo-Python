print('===Exercicio 41===')
age = int(input('Qual a idade do atleta? '))
if age <= 9:
    print(f'Com {age} anos. Esta na categoria MIRIM')
elif age <=14:
    print(f'Com {age} anos. Esta na categoria INFANTIL')
elif age <= 19:
    print(f'Com {age} anos. Esta na categoria JUNIOR')
elif age <= 25:
    print(f'Com {age} anos. Esta na categoria SENIOR')
else:
    print (f'Com {age} anos. Esta na categoria MASTER')