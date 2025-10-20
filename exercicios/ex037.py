'''
Exercício Python 37: Escreva um programa em Python que leia um
número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

n = int(input('Digite o valor: '))
e = int(input('ESCOLHA A COONVERSÃO\n1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\nQUAL A ESCOLHA: '))
if e == 1:
    print(f'Em binário é {bin(n)[2:]}')
elif e == 2:
    print(f'Em octal é {oct(n)[2:]}')
elif e == 3:
    print(f'Em hexadecimal é {hex(n)[2:]}')
else:
    print('Digitou uma tecla errada!')