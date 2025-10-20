'''
Exercício Python 54: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''

from datetime import date

qtd_maioridade = 0
qtd_menoridade = 0
for i in range(7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nascimento
    if idade < 18:
        qtd_menoridade += 1
    else:
        qtd_maioridade += 1
print(f'Maiores de idade: {qtd_maioridade}\nMenores de idade: {qtd_menoridade}')