'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

i = 0
while True:
    n = int(input('Digite um valor: '))
    o = randint(0, 10)
    p = str(input('Par ou Ímpar? [P/I] ')).upper()[0].strip()
    while p not in 'PI':
        p = str(input('Par ou Ímpar? [P/I] ')).upper()[0].strip()
    print(f'Você jogou {n} e o computador jogou {o}. ', end='')
    if p == 'P':
        if (n + o) % 2 == 0:
            print(f'Total deu {n + o} DEU PAR')
            print('Você VENCEU!\nVamos jogar novamente...')
            i += 1
        else:
            print(f'Total deu {n + o} DEU ÍMPAR')
            break
    elif p == 'I':
        if (n + o) % 2 == 1:
            print(f'Total deu {n + o} DEU ÍMPAR')
            print('Você VENCEU!\nVamos jogar novamente...')
            i += 1
        else:
            print(f'Total deu {n + o} DEU PAR')
            break
print('Você PERDEU!\n', f'\nGAME OVER! Você venceu {i} vezes.')