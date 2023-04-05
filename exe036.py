print('\033[2;34;41m===Exercicio 36===\033[m')
print('='*20)
print('BANCO POPULAR')
print('Emprestimo para casa')
print('='*20)
casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salario: '))
ano = int(input('Digite a quantidade de anos para pagar: '))
parc = casa/(ano*12)
pag = sal*30/100
if parc > pag:
    print(f'Emprestimo NEGADO, a parcela de {parc:.2f} excede 30% do seu salario de {sal:.2f}.')
else:
    print(f'Emprestimo APROVADO. Sera cobrado a parcela mensal de {parc:.2f} em {ano} anos')