def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite numero inteiro valido.\033[m')
            continue
        else:
            return a


def leiaReal(msg):
    while True:
        try:
            b = float(input(msg))
        except:
            print('\033[0;31mERRO! Digite numero real valido.\033[m')
            continue
        else:
            return b


a = leiaInt('Digite um numero inteiro: ')
b = leiaReal('Digite um numero real: ')
print(f'Numero inteiro foi {a} e numero real foi {b}')