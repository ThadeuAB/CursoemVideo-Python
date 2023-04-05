print('===Exercicio 48===')
soma = 0
for c in range(1,501):
    if c%3 == 0 and c%2==1:
        soma = soma+c
print(f'A soma de todos os numeros impares e multiplos de 3 entre 1 e 500 e {soma}')