'''
Exercício Python 11: Faça um programa que leia a largura e a altura
de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
print(f'A área da parede é {largura*altura}m\nA quantidade de tinta para pintar é {(altura*largura)/2:.2f} litros.')