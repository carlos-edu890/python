'''
Exercício Python 63: Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''

from math import floor

n = int(input('Digite um valor: '))
i = 0
c = m = 0
while i < n:
    c = (((1 + 5**(1/2))/2)**m - ((1 - 5**(1/2))/2)**m)/5**(1/2)
    print(f'{floor(c)} -> ', end='')
    m += 1
    i += 1
print('ACABOU!')