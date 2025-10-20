'''
Exercício Python 088: Faça um programa que ajude um jogador
da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

n = int(input('Quantos jogos você que gerar: '))
lista = []
lista2 = []
print(f' SORTEANDO {n} JOGOS '.center(40,  '='))
for c in range(1, n+1):
    while len(lista2) < 6:
        i = randint(1, 60)
        if i not in lista2:
            lista2.append(i)
    sleep(1)
    lista.append(lista2[:])
    lista[c-1].sort()
    print(f'Jogo {c}: {lista[c-1]}')
    lista2.clear()
print(f' < BOA SORTE! > '.center(40, '='))