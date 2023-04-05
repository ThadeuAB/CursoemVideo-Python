def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def metade(n):
    m = n/2
    return m


def dobro(n):
    d = n*2
    return d


def dezpct(n):
    dz = n+(n/100*10)
    return dz

def moeda(p =0, m ='R$'):
    return f'{m}{p:.2f}'.replace('.',',')