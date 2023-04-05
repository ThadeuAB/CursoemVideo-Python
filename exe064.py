print('===Exercicio 64===')
num = 0
soma = 0
count = 0
while num != 999:
    num = int(input('Digite um numero qualquer (999 para parar): '))
    soma = soma+num
    count = count+1
print(f'Voce digitou {count-1} diferentes valores, a soma destes deu {soma-999}')