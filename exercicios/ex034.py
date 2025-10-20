'''
Exercicio Python 34:
Escreva um programa que pergunte o salário de um Funcionário a calcula o valor do seu aumento.
Para salários superiores a R$1.250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o salario: '))
if salario > 1.250:
    print(f'O seu aumento com 10% é R${salario + salario*0.10:.2f}')
else:
    print(f'O seu aumento de 15% é R${salario + salario*0.15:.2f}')