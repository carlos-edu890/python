'''
Nessa aula, vamos aprender como utilizar estruturas condcionais simples e
compostas nos seus programas em Python.
'''

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
m = (n1+n2) / 2
if m >= 6:
    print('\033[1:30:42mVocê passou!')
else:
    print('Você foi reprovado!')