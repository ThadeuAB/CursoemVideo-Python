from exe115a.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        header('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo cadastro de {nome} adicionado.')
            a.close()