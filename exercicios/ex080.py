'''
Exercício Python 080: Crie um programa onde o
usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        j = 0
        while j < len(lista) and lista[j] < n:
            j += 1
        lista.insert(j, n)
        print(f'Adicionado na posição {j} da lista...')
print(f'O valores da lista em ordem são {lista}')