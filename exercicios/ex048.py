'''
Exercício Python 48: Faça um programa que calcule a soma
entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
'''

soma = 0
qtd = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        qtd += 1
print(f'A soma de todos os {qtd} ímpares é {soma}')
