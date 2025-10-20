'''
Exercício Python 13: Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Digite O salario: '))
print(f'Salario com 15% de aumento: R${salario+(salario*0.15):.2f}')