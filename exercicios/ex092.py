'''
Exercício Python 092: Crie um programa que leia nome,
ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for
diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nasc
num_carteira = -1
while num_carteira < 0:
    num_carteira = int(input('Quantidade de carteira de trabalho [0 não tem]: '))
pessoa['carteira'] = num_carteira
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = int(input('Salario: R$ '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - nasc
print('-='*30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')