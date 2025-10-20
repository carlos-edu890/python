'''
Exercício Python 38: Escreva um programa que leia
dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite o valor: '))
n2 = int(input('Digite o valor: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
else:
    print(f'{n1} e {n2} são iguais')