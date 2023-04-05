import uteis109

print('===Exercicio 109===')
val = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {uteis109.moeda(val)} e R$ {uteis109.metade(val, True)}')
print(f'O dobro de R$ {uteis109.moeda(val)} e R$ {uteis109.dobro(val, True)}')
print(f'Aumentando 10%, temos R$ {uteis109.dezpct(val,10, True)}')