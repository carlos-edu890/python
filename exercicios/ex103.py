'''
Exercício Python 103: Faça um programa que tenha uma função
chamada ficha(), que receba dois parâmetros opcionais: o nome
de um jogador e quantos gols ele marcou. O programa deverá ser
capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome='<desconhecido>', idade='0'):
    if nome == '':
        nome = '<desconhecido>'
    if idade == '':
        idade = '0'
    return f'O jogador {nome} fez {idade} gol(s) no campeonato.'


print('-'*40)
print(ficha(input('Nome do jogador: '), input('Idade do jogador: ')))