print('===Exercicio 57===')
s = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while s not in 'MmFf':
    print('Digite uma opcao valida!')
    s = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
print('Obrigado')