print('===Exercicio 75===')
tup = (int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
    int(input('Digite o ultimo numero: ')))

print(f'Voce digitou os valores {tup}')
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3) + 1}º posicao')
else:
    print('O valor 3 nao foi digitado nenhuma vez')
print('Os valores pares digitados foram ',end=' ')
for c in range(0,4):
    if tup[c]%2==0:
        print(tup[c],end=' ')
