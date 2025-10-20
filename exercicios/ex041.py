'''
Exercício Python 041: A Confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''

from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está na categoria INFANTIL!')
elif idade <= 19:
    print('Você está na categoria JUNIOR!')
elif idade <= 25:
    print('Você está na categoria SENIOR!')
else:
    print('Você está na categoria MASTER!')
