'''
Exercício Python 074: Crie um programa que vai
gerar cinco números aleatórios e colocar em
uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o
maior valor que estão na tupla.
'''

from random import randint

tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))

print('Os valores sorteados foram: ', end='')
for valor in tupla:
    print(valor, end=' ')
print(f'\nO menor número sorteado foi: {min(tupla)}')
print(f'O maior número sorteado foi: {max(tupla)}')