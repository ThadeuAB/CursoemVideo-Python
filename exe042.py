print('===Exercicio 42===')
print('E possivel formar um triangulo? ')
l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))
if l1+l2 > l3 and l2+l3 > l1 and l1+l3 > l2:
    if l1 == l2 and l2 == l3:
        print('Forma triangulo EQUILATERO.')
    elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
        print('Forma um triangulo ISOSCELES.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Forma um triangulo ESCALENO.')
else:
    print('Nao forma triangulo')