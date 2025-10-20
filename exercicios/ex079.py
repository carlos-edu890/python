'''
Exercício Python 079: Crie um programa onde o usuário
possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
'''

lista = []
while True:
    e = ''
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while e != 'S' and e != 'N':
        e = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if e == 'N':
        break
lista.sort()
print(f'Esses são os elementos {lista}')