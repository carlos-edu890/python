'''
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
digitação novamente até ter um valor correto.
'''

sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0].strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados Invalidos. Por favor, digite seu sexo: [M/F] ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso.')