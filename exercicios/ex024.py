'''
Exercício Python 24: Crie um programa que leia o nome de
uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

nome = input('Digite seu nome: ')
print('SANTO' in nome.split()[0].upper())