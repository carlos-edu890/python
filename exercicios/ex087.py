'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.
'''

lista = []
dado = []
for p in range(0, 3):
    n1 = int(input(f'Digite um valor [{p}, 0]: '))
    dado.append(n1)
    n2 = int(input(f'Digite outro valor [{p}, 1]: '))
    dado.append(n2)
    n3 = int(input(f'Digite mais um valor [{p}, 2]: '))
    dado.append(n3)
    lista.append(dado[:])
    dado.clear()
somaPar = somaCol3 = maiorLin2 = 0
for i in range (0, len(lista)):
    for j in range (0, len(lista[i])):
        print(f'[{lista[i][j]:^5}]', end='')
        if lista[i][j] % 2 == 0:
            somaPar += lista[i][j]
        if j == 2:
            somaCol3 += lista[i][j]
        if i == 1 and lista[i][j] > maiorLin2:
            maiorLin2 = lista[i][j]
    print()
print(f'A soma dos pares foi {somaPar}')
print(f'A soma da coluna 3 foi {somaCol3}')
print(f'O maior valor da linha 2 foi {maiorLin2}')