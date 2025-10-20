'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
qtd = 0
while True:
    n = ''
    while not n.isnumeric():
        n = input('Digite um valor: ')
    e = ''
    while e != 'N' and e != 'S':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    lista.append(int(n))
    qtd += 1
    if e == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {qtd} elementos.')
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')