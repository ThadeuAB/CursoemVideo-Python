from utilidadesCeV import moeda, dado

print('===Exercicio 112===')
v = dado.leiaDinheiro('Digite o preco: R$ ')
a = float(input('Qual adicional de taxa: '))
d = float(input('Qual reducao de taxa: '))
moeda.resumo(v,a,d)