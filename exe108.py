import uteis

print('===Exercicio 108===')
val = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {uteis.moeda(val)} e R$ {uteis.moeda(uteis.metade(val))}')
print(f'O dobro de R$ {uteis.moeda(val)} e R$ {uteis.moeda(uteis.dobro(val))}')
print(f'Aumentando 10%, temos R$ {uteis.moeda(uteis.dezpct(val))}')