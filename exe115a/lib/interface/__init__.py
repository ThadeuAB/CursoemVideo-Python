def linha(tam = 42):
    return '-' * tam


def header(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    header('MENU PRINICIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('Sua Opcao: ')
    return opc


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite numero inteiro valido.\033[m')
            continue
        else:
            return a