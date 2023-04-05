print('===Exercicio 50===')
s = 0
con = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º valor: '))
    if n%2==0:
        s=s+n
        con=con+1
print(f'Voce informou {con} numeros pares, a soma destes foi de {s}')