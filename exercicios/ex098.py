'''
Exercício Python 098: Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1

b) de 10 até 0, de 2 em 2

c) uma contagem personalizada
'''

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i} ', end='')
            sleep(0.5)
    elif inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            sleep(0.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Digite o inicio: ')), int(input('Digite fim: ')), int(input('Digite passo: ')))