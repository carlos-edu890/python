'''
Exercício Python 078: Faça um programa que
leia 5 valores numéricos e guarde-os em
uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior número é {maior} na posição ', end='')
for pos, c in enumerate(lista):
    if c == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor número é {menor} na posição ', end='')
for pos, c in enumerate(lista):
    if c == menor:
        print(f'{pos}...', end=' ')