'''
Exercício Python 096: Faça um programa que tenha uma
função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(a, b):
    print(f'A área de um terreno de {a:.1f}x{b:.1f} é de {a*b:.1f}m².')


print('Controle de Terrenos')
print('-'*30)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))