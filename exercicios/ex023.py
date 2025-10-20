'''
Exercício Python 23: Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

n = input('Digite um valor de 0 a 9999: ')
print(f'Unidade: {int(n) // 1 % 10}\nDezena: {int(n) // 10 % 10}'
      f'\nCentena: {int(n) // 100 % 10}\nMilhar: {int(n) // 1000 % 10}')