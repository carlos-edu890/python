'''
Exercício Python 70: Crie um programa que leia o nome
e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

print('-' * 30, '\n    LOJA DO ATACADÃO')
print('-' * 30)
total_gasto = qtd = 0
barato_preco = 0
barato_nome = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('O Preço do produto: R$'))
    while preco < 1:
        preco = float(input('O Preço do produto: R$'))
    print('-' * 30)
    total_gasto += preco
    if barato_preco > preco or barato_preco == 0:
        barato_preco = preco
        barato_nome = nome
    if preco > 1000:
        qtd += 1
    e = ' '
    while e not in 'SN':
        e = str(input('Quer Continuar? [S/N] ')).upper()[0].strip()
    if e == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'Total gasto: R${total_gasto:.2f}')
print(f'Temos {qtd} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato_nome} que custa R${barato_preco:.2f}')