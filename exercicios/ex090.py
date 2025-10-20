'''
Exercício Python 090: Faça um programa que leia nome e
média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do {aluno['nome']}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
print(f'O nome é {aluno['nome']}.')
print(f'A média é {aluno['media']}.')
print(f'A situação é {aluno['situacao']}.')