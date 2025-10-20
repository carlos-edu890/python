'''
Exercício Python 55: Faça um programa que leia o peso de
cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

menor_peso = 0
maior_peso = 0
for i in range(5):
    peso = float(input('Digite o seu peso: '))
    if i == 0:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f'Maior peso: {maior_peso:.2f}Kg\nMenor peso: {menor_peso:.2f}Kg')