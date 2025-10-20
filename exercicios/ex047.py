'''
Exercício Python 47: Crie um programa que mostre na tela
todos os números pares que estão no intervalo entre 1 e 50.
'''

for i in range(1, 51, 1):
    if i % 2 == 0:
        print(f'{i}', end=' ')
print('Acabou!')

'''
é posivel reduzir usando range(2, 51, 2)
'''