'''
Exercício Python 077: Crie um programa que tenha
uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais.
'''

tupla = (
    'Bola', 'Celular', 'Fone', 'Rede', 'Coisa', 'Lapis', 'Ninja'
)

for i in tupla:
    e = ''
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for e in i:
        if e.upper() in 'AEIOU':
            print(e.lower(), end=' ')