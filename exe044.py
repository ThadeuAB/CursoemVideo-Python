print('===Exercicio 44===')
val = float(input('Digite o preco do produto: '))
print('===Escolha a Forma de Pagamento===')
print('1 - A vista(Dinheiro/Cheque)')
print('2 - A vista(Cartao)')
print('3 - Parcelado em 2x')
print('4 - Parcelado em 3x ou mais')
esc = int(input('Opcao: '))
if esc == 1:
    print(f'O valor a ser pago sera de {val-(val*10/100):.2f}')
elif esc == 2:
    print(f'O valor a ser pago sera de {val-(val*5/100):.2f}')
elif esc == 3:
    print(f'O valor a ser pago sera de {val:.2f} em 2x de {val/2:.2f}')
elif esc == 4:
    par = int(input('Digite a quantidade de parcelas: '))
    print(f'O valor a ser pago sera de {val+(val*20/100):.2f} em {par}x de {(val+(val*20/100))/par:.2f}')
else:
    print('Escolha uma opcao valida')
