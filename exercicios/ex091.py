'''
Exercício Python 091: Crie um programa onde 4 jogadores
joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

dic = {}
print('Valores sorteados:')
for i in range(0,4):
    dic[f'jogador{i+1}'] = randint(1,6)
    print(f'{'O':>5} jogador{i+1} tirou {dic[f'jogador{i+1}']}')
print('Ranking dos jogadores:')
i = 1
dic_ord = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
for k, v in dic_ord.items():
    print(f'{i:>5}° lugar: {k} com {v}')
    i += 1