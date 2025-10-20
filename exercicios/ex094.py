'''
Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas

B) A média de idade

C) Uma lista com as mulheres

D) Uma lista de pessoas com idade acima da média
'''

pessoa = {}
lista_pessoas = []
lista_mulher = []
lista_menor = []
media_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while True:
        if pessoa['sexo'] in 'MF':
            break
        pessoa['sexo'] = str(input('ERRO! Digite apenas [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    while True:
        if pessoa['idade'] >= 0:
            break
        pessoa['idade'] = int(input('ERRO! Digite a sua idade novamente: '))
    media_idade += pessoa['idade']
    lista_pessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        lista_mulher.append(pessoa.copy())
    e = ''
    while e != 'S' and e != 'N':
        e = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if e == 'N':
        break
media_idade = media_idade / len(lista_pessoas)
print('-='*30)
print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
print(f'A média de idade é {media_idade:.1f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in lista_mulher:
    print(f'{p['nome']} ', end='')
print()
print('Lista das pessoas que estão com a idade acima da média:')
for p in lista_pessoas:
    if p['idade'] > media_idade:
        print('\n')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('<<< PROGRAMA ENCERRADO >>>')