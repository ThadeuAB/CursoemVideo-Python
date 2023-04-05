print('\033[4;30;45m===Exercicio 36===\033[m')
num = int(input('Digite um numero inteiro: '))
print('===MENU===')
print('Base de conversao')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')
esc = int(input('Escolha: '))
if esc == 1:
    print(f'O numero {num} em binario e {bin(num)[2:]}')
elif esc == 2:
    print(f'O numero {num} em octal e {oct(num)[2:]}')
elif esc == 3:
    print(f'O numero {num} em hexadecimal e {hex(num)[2:]}')
else:
    print('Deves escolher uma opcao valida do Menu')