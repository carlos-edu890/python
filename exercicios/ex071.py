'''
Exercício Python 071: Crie um programa que simule o
funcionamento de um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''


n = int(input('Qual o Valor a ser sacado? R$'))
cd_50 = cd_20 = cd_10 = cd_1 = 0
while True:
    if n == 0:
        break
    if n // 50 > 0:
        n -= 50
        cd_50 += 1
    elif n // 20 > 0:
        n -= 20
        cd_20 += 1
    elif n // 10 > 0:
        n -= 10
        cd_10 += 1
    elif n // 1 > 0:
        n -= 1
        cd_1 += 1
if cd_50 > 0:
    print(f'Total de {cd_50} cédulas de R$50')
if cd_20 > 0:
    print(f'Total de {cd_20} cédulas de R$20')
if cd_10 > 0:
    print(f'Total de {cd_10} cédulas de R$10')
if cd_1 > 0:
    print(f'Total de {cd_1} cédulas de R$1')
print('=' * 30, '\nVolte sempre! Tenha um bom dia!')