'''
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

c1 = float(input('Digite o comprimento: '))
c2 = float(input('Digite o comprimento: '))
c3 = float(input('Digite o comprimento: '))

if c1+c2 > c3 and c1+c3 > c2 and c2+c3 > c1:
    print('Pode formar um triangulo.')
else:
    print('Não pode formar um triangulo.')