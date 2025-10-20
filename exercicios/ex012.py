'''
Exercício Python 12: Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Digite o valor: '))
print(f'Preço com 5% de desconto: R${preco-(preco*0.05):.2f}')