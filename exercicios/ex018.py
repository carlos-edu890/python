'''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import cos, sin, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
print(f'O Cosseno: {cos(radians(angulo)):.2}\nO Seno: {sin(radians(angulo)):.2f}\nA Tangente: {tan(radians(angulo)):.2f}')