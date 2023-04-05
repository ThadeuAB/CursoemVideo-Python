def notas(*n,sit=False):
    """
    FUncao para analisar notas
    :param n: quantiade de notas
    :param sit: se deseja ver situacao (opcional)
    :return: maior nota, menor nota, qtde de notas, media e situacao se incluido
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situacao'] = 'APROVADO'
        elif r['Media'] >= 5:
            r['Situacao'] = 'RECUPERACAO'
        else:
            r['Situacao'] = 'REPROVADO'
    return r


print('===Exercicio 105===')
resp = notas(5.5,8.5,2.5,2.5,sit=True)
print(resp)