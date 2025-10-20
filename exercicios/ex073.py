'''
Exercício Python 73: Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Bragantino.
'''

tabela_brasileirao = (
    'Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo',
    'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Internacional',
    'Ceará SC', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Vasco da Gama',
    'Santos', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife'
)
print('-='*30)
print(f'Os 5 primeiros times do Brasileirão:\n{tabela_brasileirao[:5]}')
print('-='*30)
print(f'Os 4 últimos times do Brasileirão:\n{tabela_brasileirao[16:]}')
print('-='*30)
print(f'Os times em ordem alfabética:\n{sorted(tabela_brasileirao)}')
print('-='*30)
print(f'O Bragantino está na {tabela_brasileirao.index('Bragantino') + 1}° posição.')