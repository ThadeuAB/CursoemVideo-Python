print('===Exercicio 53===')
fra = str(input('Digite uma frase: ')).strip().upper()
pal = fra.split()
jun = ''.join(pal)
inv = ''
for letra in range(len(jun)-1,-1,-1):
    inv += jun[letra]
print(jun, inv)
if jun == inv:
    print('Temos um palindromo')
else:
    print('Nao e um palidromo')