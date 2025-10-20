'''
Exercício Python 64: Crie um programa que leia vários
números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)
'''

n = int(input('Digite o valor[999 para parar]: '))
i = 0
soma = 0
while n != 999:
    soma += n
    n = int(input('Digite o valor[999 para parar]: '))
    i += 1
print(f'Você digitou {i} vezes e a soma dos números foi {soma}')