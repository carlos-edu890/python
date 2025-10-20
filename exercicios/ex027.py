'''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = input('Digite seu nome: ')
print(nome.split()[0])
print(nome.split()[len(nome.split())-1])