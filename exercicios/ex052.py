'''
Exercício Python 52: Faça um programa que leia um
número inteiro e diga se ele é ou não um número primo.
'''

n = int(input('Digite o valor: '))
qtd = 0
for i in range(1, n+1):
    if n % i == 0:
        print(f'\033[1:32m{i}', end=' ')
        qtd += 1
    else:
        print(f'\033[1:31m{i}', end=' ')
if qtd == 2:
    print('\n\033[mO número {} é primo'.format(n))
else:
    print('\n\033[mO número {} não é primo'.format(n))