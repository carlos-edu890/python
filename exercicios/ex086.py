'''
Exercício Python 086: Crie um programa que declare uma matriz de
dimensão 3×3 e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.
'''

lista = [[], [], []]
#dado = []
for p in range(0, 3):
    n1 = int(input(f'Digite um valor [{p}, 0]: '))
    lista[p].append(n1)
    #dado.append(n1)
    n2 = int(input(f'Digite um valor [{p}, 1]: '))
    lista[p].append(n2)
    #dado.append(n2)
    n3 = int(input(f'Digite um valor [{p}, 2]: '))
    lista[p].append(n3)
    #dado.append(n3)
    #lista.append(dado[:])
    #dado.clear()
for i in range (0, len(lista)):
    for j in range (0, len(lista[i])):
        print(f'[{lista[i][j]:^5}]', end='')
    print()