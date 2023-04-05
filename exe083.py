print('===Exercicio 83===')
pilha = []
pare = 0
exp = (str(input('Digite uma expressao: ')))
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')