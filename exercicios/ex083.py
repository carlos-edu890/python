'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta.
'''

lista = []
e = input('Digite uma expressão matemática usando parênteses: ').strip()
qtdA = qtdF = 0
for c in e:
    if c == '(' or c == ')':
        lista.append(c)
for n in lista:
    if n == '(':
        qtdA += 1
    if n == ')':
        qtdF += 1
if qtdA == qtdF:
    print('A expressão está valida!')
else:
    print('A expressão não está errada!')
'''
e = input('Digite uma expressão matemática usando parênteses: ')
qtd = 0
for c in e:
    if c == '(' or c == ')':
        qtd += 1
if qtd % 2 == 0:
    print('A expressão está valida!')
else:
    print('A expressão não está valida!')
'''