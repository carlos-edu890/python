'''
Exercício Python 69: Crie um programa que leia a idade e o sexo
de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

qtd_maior = 0
qtd_homem = 0
mulher_menor = 0
while True:
    print('-' * 30, '\n    CADASTRO DE UMA PESSOA')
    print('-' * 30)
    n = int(input('Digite a idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Digite o sexo: [M/F] ')).upper()[0].strip()
    print('-' * 30)
    if n > 18:
        qtd_maior += 1
    if s == 'M':
        qtd_homem += 1
    if s == 'F':
        if n < 20:
            mulher_menor += 1
    c = ''
    while c != 'S' and c != 'N': # c not in 'SN'
        c = str(input('Quer Continuar? [S/N] ')).upper()[0].strip()
    if c == 'N':
        break
print('=' * 6, ' FIM DO PROGRAMA ', '=' * 6)
print(f'Total de pessoas com mais de 18 anos: {qtd_maior}')
print(f'Ao todo temos {qtd_homem} homens cadastrados')
print(f'Total de mulheres com menos de 20 anos: {mulher_menor}')