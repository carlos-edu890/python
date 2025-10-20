'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o
computador vai “pensar” em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.
'''

from random import randint
n = int(input('Acabei de escolher um número entre 0 e 10\nSerá que você consegue adivinhar?\nQual número você acha que foi: '))
r = randint(0, 10)
qtd = 1
while n != r:
    if r > n:
        n = int(input('Maior... Tente novamente.\nQual número você acha que foi: '))
    else:
        n = int(input('Menor... Tente novamente.\nQual número você acha que foi: '))
    qtd += 1
print(f'Você acertou!\nO número era {r}\nAcertou com {qtd} tentativas')