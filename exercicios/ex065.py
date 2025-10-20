'''
Exercício Python 65: Crie um programa que leia vários
números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
'''

n = int(input('Digite o valor: '))
media = n
i = 1
maior = menor = n
p = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
if p == 'S':
    while p == 'S':
        n = int(input('Digite o valor: '))
        media += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        i += 1
        p = str(input('Deseja continuar? [S/N] : ')).upper().strip()[0]
print(f'A média foi {media / i:.2f}\nO maior número foi {maior} e o menor foi {menor}')