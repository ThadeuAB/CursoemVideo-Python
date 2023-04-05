from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'arq115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    res = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if res == 1:
       lerArquivo(arq)
    elif res == 2:
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif res == 3:
        header('Volte sempre!')
        break
    else:
        print('\033[0;31mEscolha uma opcao valida.\033[m')
    sleep(2)