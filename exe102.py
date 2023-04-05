def fatorial(n, show=False):
    """
    Calcula fatorial
    :param n: numero a ser calculada
    :param show: se deseja mostrar a conta
    :return: o resultado do fatorial
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


print('===Exercicio 102===')
print(fatorial(5))