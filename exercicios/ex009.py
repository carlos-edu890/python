'''
Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e
mostre na tela a sua tabuada.
'''

number = int(input('Digite um valor: '))
for i in range(1, 11):
    print(f'{number} x {i} = {number*i}')