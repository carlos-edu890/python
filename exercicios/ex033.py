'''
Exercício Pyhton 33: Faça um programa que leia três números e
mostra qual é o maior e qual é o menor.
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'O maior valor é {n1} e o menor é {n3}.')
    else:
        print(f'O maior valor é {n1} e o menor é {n2}.')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'O maior valor é {n2} e o menor é {n3}.')
    else:
        print(f'O maior valor é {n2} e o menor é {n1}.')
else:
    if n1 > n2:
        print(f'O maior valor é {n3} e o menor é {n2}.')
    else:
        print(f'O maior valor é {n3} e o menor é {n1}.')