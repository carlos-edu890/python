'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o
primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
'''

a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
i = 0
c = a1
while i < 10:
    print(f'{c} -> ', end='')
    c += razao
    i += 1
print('ACABOU!')