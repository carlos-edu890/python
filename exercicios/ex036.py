'''
Exercício Python 36: Escreva um programa para aprovar o
empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor = float(input('Digite o valor da casa R$'))
salario = float(input('Digite o salário do comprador R$'))
anos = int(input('Digite os anos que vai pagar: '))
prestacao = valor / (anos * 12)
if prestacao < (salario * 0.3):
    print(f'O emprestimo foi aprovado!\nA Prestação foi de R${prestacao:.2f}')
else:
    print('Emprestimo foi negado!\nA prestação excedeu R${:.2f} o salário R${:.2f}'.format(prestacao,salario*0.3))
print('Tenha um bom dia!')