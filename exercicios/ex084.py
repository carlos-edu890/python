'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.
'''

lista = []
pessoas = []
maior = 0
menor = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    pessoas.append(lista[:])
    lista.clear()
    e = ''
    while e != 'S' and e != 'N':
        e = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if e == 'N':
        break
print(f'Foram {len(pessoas)} pessoas cadastradas.')
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if menor == 0:
        menor = p[1]
    elif p[1] < menor:
        menor = p[1]
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')