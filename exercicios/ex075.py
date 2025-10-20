'''
Exercício Python 075: Desenvolva um programa que leia
quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

Aula Anterior

'''

n1 = int(input('Digite o valor 1°: '))
n2 = int(input('Digite o valor 2°: '))
n3 = int(input('Digite o valor 3°: '))
n4 = int(input('Digite o valor 4°: '))
tupla = (n1, n2, n3, n4)
'''
Ou tupla = (
    int(input('Digite o valor 1°: ')), int(input('Digite o valor 2°: ')),
    int(input('Digite o valor 3°: ')), int(input('Digite o valor 4°: '))
)
'''


qtd = tupla.count(9)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {qtd} vezes')

try:
    print(f'O valor 3 apareceu na {tupla.index(3)}° posição')
except ValueError:
    print('O valor 3 não foi digitado em nenhuma posição')
# ou poderia usar if 3 in tupla:

print(f'Os valores pares digitados foram ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')