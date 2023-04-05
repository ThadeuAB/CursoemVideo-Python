print('===Exercicio 67===')
print('***TABUADA***')
while True:
    n = int(input('Qual valor deseja verificar a tabuada? (Valores negativos serao desconsiderados) '))
    print('=*' * 10)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('=*'*10)
print('Valores negativos nao sao considerados')