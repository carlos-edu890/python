'''
Exercício Python 15: Escreva um programa que pergunte a
quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por Km rodado.
'''

dias = int(input('A quantos dias foi alugado: '))
km = float(input('Digite a quantos km rodados: '))
print(f'O valor a pagar é R${km *0.15 + dias * 60:.2f}')