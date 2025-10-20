'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

c1 = float(input('Digite o comprimento: '))
c2 = float(input('Digite o comprimento: '))
c3 = float(input('Digite o comprimento: '))

if c1+c2 > c3 and c1+c3 > c2 and c2+c3 > c1:
    print('Pode formar um triangulo.')
    if c1 == c2 == c3:
        print('O triângulo que será formado é um Equilátero.')
    elif c1 == c2 or c2 == c3 or c3 == c1:
        print('O triângulo que será formado é um Isósceles.')
    else:
        print('O triângulo que será formado é um Escaleno.')
else:
    print('Não pode formar um triangulo.')