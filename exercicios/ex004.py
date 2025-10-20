'''
Exercício Python 4: Faça um programa que leia algo pelo teclado e
mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

pl = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(pl))
print('Só tem espaços? ', pl.isspace())
print('É um numero? ', pl.isnumeric())
print('É alfabetico? ', pl.isalpha())
print('É alfanúmerico? ', pl.isalnum())
print('Está em maiusculo? ', pl.isupper())
print('Está em minusculo? ', pl.islower())
print('Está capitalizada? ', pl.isprintable())