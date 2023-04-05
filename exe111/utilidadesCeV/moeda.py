def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def metade(n, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def dobro(n, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def aumentar(n, p, formato=False):
    res = n+(n/100*p)
    return res if not formato else moeda(res)


def diminuir(n, p, formato=False):
    res = n-(n/100*p)
    return res if not formato else moeda(res)


def moeda(n=0, m ='R$'):
    return f'{m}{n:.2f}'.replace('.',',')

def resumo(n=0, ta=10, td=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preco analisado: {moeda(n)}')
    print(f'Dobro do valor: {dobro(n,True)}')
    print(f'Metade do valor: {metade(n,True)}')
    print(f'Com {ta}% de aumento: {aumentar(n,ta,True)}')
    print(f'Com {td}% de reducao: {diminuir(n,td,True)}')
    print('-'*30)