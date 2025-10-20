'''
Exercício Python 099: Faça um programa que tenha uma função
chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep

def maior(* num):
    print('-=' * 30)
    print(f'Analisando os valores passados...')
    if len(num) >= 1:
        maior = num[0]
        for n in num:
            print(f'{n} ', end='')
            sleep(0.5)
            if n > maior:
                maior = n
    else:
        maior = 0
    print(f'Foram analisados no total {len(num)} valores ao todo.')
    print(f'O maior valor digitado foi {maior}.')


maior(1, 3, 4, 7, 8, 9)
maior(1, 5, 3)
maior(0)
maior()