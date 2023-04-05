print('===Exercicio 72===')
ext = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze',
       'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um numero entre 0 e 20: '))
while num<0 or num>20:
    num=int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {ext[num]}.')