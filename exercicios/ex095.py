'''
Exercício Python 095: Aprimore o desafio 93 para que ele
funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
lista_jogador = []

while True:
    print('—='*30)
    jogador['nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    soma = 0
    for i in range(0, n):
        jogador['gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))
        soma += jogador['gols'][i]
    jogador['total'] = soma
    lista_jogador.append(jogador.copy())
    e = ''
    while e != 'S' and e != 'N':
        e = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if e == 'N':
        break
print('—='*30)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":<15}')
print('—'*60)
for n, jogador in enumerate(lista_jogador):
    print(f'{n:<5}', end='')
    for d in jogador.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('—' * 60)
    n = int(input('Mostrar dados de qual jogador [999 para parar]? '))
    if n >= 0 and n <= len(lista_jogador) - 1:
        print(f'LEVANTAMENTO DO JOGADOR {lista_jogador[n]["nome"]}:')
        for i, v in enumerate(lista_jogador[n]["gols"]):
            print(f'{'=>':>5} Na partida {i + 1}, fez {v} gols.')
    elif n == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com código {n}.')
print('<<< VOLTE SEMPRE >>>')