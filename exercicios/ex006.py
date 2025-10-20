'''
Exercício Python 006: Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
'''

import math

number = int(input('Digite um valor: '))
print(f'O seu dobro é {number*2}\nSeu tripo é {number*3}\nSua raiz quadrada é {math.sqrt(number):.2f}')
# para a raiz quadrada number**(1/2)