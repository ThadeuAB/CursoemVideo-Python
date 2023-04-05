print('===Exercicio 31===')
km = float(input('Qual a distancia em km da viagem? '))
if km <= 200:
    print('A passagem ira custar {:.2f} reais'.format(km*0.50))
else:
    print('A passagem ira custar {:.2f} reais'.format(km*0.45))