'''
Exercício Python 106: Faça um mini-sistema que utilize o
Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra
‘FIM’, o programa se encerrará. Importante: use cores.
'''

def titulo(msg, cor=0):
    if cor != 0:
        print(f'{cor}=' * (len(msg) + 2))
    else:
        print('=' * (len(msg) + 2))
    print(f' {msg}')
    print('=' * (len(msg) + 2))


def pyHELP():
    while True:
        titulo('Sistema de ajuda pyHELP', '\033[1;97;43m')
        n = str(input('\033[0mFunção ou Biblioteca > '))
        if n == 'FIM' or n == 'fim':
            break
        else:
            titulo(f'Acessando o manual do comando {f'{n}'}', '\033[1;97;44m')
            print('\033[30;107m', end='')
            help(n)
    titulo('ATÉ LOGO!', '\033[97;100m')


pyHELP()