'''
Exercício Python 17: Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot

catopos =  float(input('Digite o valor do cateto: '))
catadj = float(input('Digite o valor do cateto: '))
print(f'A Hipotenusa é: {hypot(catopos, catadj):.2f}')