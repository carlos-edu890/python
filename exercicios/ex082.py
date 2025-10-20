'''
Exercício Python 082: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
while True:
    n = ''
    while not n.isnumeric():
        n = input('Digite um valor: ')
    e = ''
    while e != 'N' and e != 'S':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    lista.append(int(n))
    if e == 'N':
        break
pares = []
impares = []
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')