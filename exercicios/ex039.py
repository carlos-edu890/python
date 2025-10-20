'''
Exercício Python 39: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
anos = date.today().year - nascimento
if anos < 18:
    print(f'Você ainda não pode se alistar.\nFalta {18 - anos} anos.\nO seu alistamento será em {(18 - anos) + date.today().year}.')
elif anos == 18:
    print('Você já pode se alistar.')
else:
    print(f'Você tem {anos} anos. Já passou {anos - 18} anos do alistamento.\nO seu alistamento foi em {date.today().year - (anos - 18)}.')