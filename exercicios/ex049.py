'''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada
de um número que o usuário escolher, só que agora utilizando um laço for.
'''

number = int(input('Digite um valor: '))
for i in range(1, 11):
    print(f'{number} x {i:2} = {number*i}')