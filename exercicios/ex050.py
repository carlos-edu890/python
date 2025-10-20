'''
Exercício Python 50: Desenvolva um programa que leia
seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

qtd = 0
soma = 0
for i in range(0,6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        qtd += 1
print(f'A soma de todos os {qtd} pares foi {soma}')