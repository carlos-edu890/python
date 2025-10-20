'''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''

from time import sleep
from random import choice

jogadas = ['tesoura','papel','pedra']
jogada = input('Pedra, Papel ou Tesoura: ').lower()
print('JO-', end='')
sleep(1)
print('KEN-', end='')
sleep(1)
print('PÔ!!!')
escolha = choice(jogadas)

print(f'\033[3;32mVOCÊ ESCOLHEU {jogada.upper()} e CPU ESCOLHEU {escolha.upper()}.', end=' ')
if jogada == escolha:
    print('EMPATE!')
elif jogada == 'tesoura' and escolha == 'papel':
    print('VOCÊ VENCEU!')
elif jogada == 'pedra' and escolha == 'tesoura':
    print('VOCÊ VENCEU!')
elif jogada == 'papel' and escolha == 'pedra':
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')