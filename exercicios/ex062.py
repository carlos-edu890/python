'''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o
usuário se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos.
'''

a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
i = 10
c = a1
o = 0
while i > 0:
    print(f'{c} -> ', end='')
    c += razao
    i -= 1
    o += 1
    if i == 0:
        print('ACABOU!\n')
        i = int(input('Quer mostrar mais quantos termos? '))
print('A progressão foi encerrada com {} termos.'.format(o))