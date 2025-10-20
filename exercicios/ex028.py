'''
Exercício Python 28: Escrava um programa que faça o computador "pansar" am um número inteiro entre
0 a 5 a paça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se O usuário venceu ou perdeu
'''

from random import randint
n = int(input('Adivinhe o valor: '))
r = randint(0, 5)
if n == r:
    print(f'Você acertou!\nO número era {r}')
else:
    print(f'Você errou!\nO número era {r}')