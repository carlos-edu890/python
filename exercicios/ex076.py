'''
Exercício Python 076: Crie um programa que tenha
uma tupla única com nomes de produtos e
seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''

tupla = (
    'Borracha', 0.50, 'Caneta', 0.75, 'Livro', 15, 'Faca', 20
)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for i in tupla:
    if tupla.index(i) % 2 == 0:
        print(f'{i:.<30}', end='')
    else:
        print(f'R${i:>7.2f}')
print('-'*40)