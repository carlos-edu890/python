'''
Exercício Python 060: Faça um programa que leia um número
qualquer e mostre o seu fatorial. Exemplo
'''

n = int(input('Digite o valor: '))
i = n
fatorial = 1
print(f'O fatorial de {n}! = ', end='')
while i >= 0:
    if i > 0:
        print(f'{i} ', end='')
        fatorial *= i
        if i != 1:
            print(f'x ', end='')
        elif n > 1:
            print(f'= {fatorial}', end='')
    elif n == 0:
        print('1')
    i -= 1