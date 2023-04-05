print('===Exercicio 43===')
pes = float(input('Digite o peso: '))
alt = float(input('Digite a altura: '))
imc = pes/alt**2
if imc < 18.5:
    print(f'Com IMC de {imc:.2f}, voce esta abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'Com IMC de {imc:.2f}, voce esta no peso ideal')
elif imc > 25 and imc <= 30:
    print(f'Com IMC de {imc:.2f}, voce esta com sobrepeso.')
elif imc > 30 and imc<=40:
    print(f'Com IMC de {imc:.2f}, voce esta com obesidade.')
else:
    print(f'com IMC de {imc:.2f}, voce esta com obesidade morbida.')
