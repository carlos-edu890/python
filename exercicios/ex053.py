'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
'''

frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
print(f'A frase: {frase} invertida é ', end='')
count = 0
for i in range(0, len(frase)):
    print(f'{frase[len(frase) - 1 - i]}', end='')
    if frase[i] == frase[len(frase) - 1 - i]:
        count += 1
    '''
    if frase[i] != frase[len(frase) - 1 - i]:
        print('Não é palindromo!')
    if i == len(frase) - 1:
        print('\nÉ palindromo!')
    '''
if count == len(frase):
    print('\nA frase é um palindromo!')
else:
    print('\nA frase não é um palindromo!')