import uteis

print('===Exercicio 107===')
val = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {val:.2f} e R$ {uteis.metade(val):.2f}')
print(f'O dobro de R$ {val:.2f} e R$ {uteis.dobro(val):.2f}')
print(f'Aumentando 10%, temos R$ {uteis.dezpct(val):.2f}')