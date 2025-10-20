'''
Exercício Python 26: Faça um programa que leia uma frase
pelo teclado e mostre quantas vezes aparece a letra “A”, em que
posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

nome = input('Nome Completo: ').lower().strip()
print(f'A letra "a" aparece {nome.count('a')} vezes')
print(f'Apareceu na primeira vez na posição {nome.find('a') + 1}')
print(f'Apareceu na ultima vez na posição {nome.rfind('a') + 1}')
