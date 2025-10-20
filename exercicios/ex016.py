'''
Exercício Python 16: Crie um programa que leia um
número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

n = float(input('Digite um valor: '))
print(f'Parte inteira: {int(n)}')
# ou use o pacote math e use a função floor()