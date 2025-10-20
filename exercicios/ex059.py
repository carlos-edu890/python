'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('O 1° valor: '))
n2 = int(input('O 2° valor: '))
e = 0
while e != 5:
    print('--'*20)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    e = int(input('Escolha: '))
    if e == 1:
        print(f'A soma é {n1+n2}')
    elif e == 2:
        print(f'A multiplicação é {n1*n2}')
    elif e == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif e == 4:
        n1 = int(input('O 1° valor: '))
        n2 = int(input('O 2° valor: '))
    elif e > 5 or e < 1:
        print('Opcão invalida!')
    print('--' * 20, '\n')