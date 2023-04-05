print('===Exercicio 79===')
valores = []
maior=menor=0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        maior=menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'Voce digitou os valores {valores}')
print('=-'*40)
print(f'O maior valor digitado foi {maior},nas posicoes ',end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {menor},nas posicoes ',end='')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')