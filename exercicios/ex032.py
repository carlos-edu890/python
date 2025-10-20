'''
Exercício Python 32: Faça um programa que leia um ano qualquer a mostra se ala é BISSEXTO.
'''

from calendar import isleap
ano = int(input('Digite o ano: '))
if isleap(ano):
    print('O ano {}, é bissexto.'.format(ano))
else:
    print('O ano {}, não é bissexto.'.format(ano))