'''
Exercício Python 093: Crie um programa que gerencie o
aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
soma = 0
for i in range(0, n):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    soma += jogador['gols'][i]
jogador['total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'{'=>':>5} Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')