'''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for i in range(a1, a1 + (10 - 1) * razao + razao, razao):
    print(f'{i} -> ', end='')
print('ACABOU!')