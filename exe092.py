from datetime import datetime
print('===Exercicio 92===')
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 se nao tem): '))
if dados['CTPS'] != 0:
    dados['Contratacao'] = int(input('Ano de contratacao: '))
    dados['Salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['Idade'] + ((dados['Contratacao'] + 35) - datetime.now().year)
print('=-'*35)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')