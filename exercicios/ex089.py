'''
Exercício Python 089: Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

lista = []
nome = []
notas = []
while True:
    nome.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Digite a nota 1° do aluno: ')))
    notas.append(float(input('Digite a nota 2° do aluno: ')))
    nome.append(notas[:])
    media = sum(notas) / len(notas)
    nome.append(media)
    lista.append(nome[:])
    notas.clear()
    nome.clear()
    e = ''
    while e != 'S' and e != 'N':
        e = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if e == 'N':
        print('-='*30)
        print(f'No. {'NOME':<10}',f'{'MÉDIA':>5}')
        print('-'*25)
        for pos, i in enumerate(lista):
            print(f'{pos}  {i[0]:<10}', f'{i[2]:>5.1f}')
            #print(f'{pos}  {i[0]:<10}', f'{(i[1][0] + i[1][1]) / 2:>5.1f}')
        print('-'*25)
        break
while True:
    pos = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    if pos == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    elif pos <= len(lista) - 1:
        for a, i in enumerate(lista):
            if pos == a:
                print(f'Notas de {i[0]} são {i[1]}')
                print('-'*25)
                break
'''
nome.append(str(input('Nome: ')))
notas.append(float(input('Digite a nota 1° do aluno: ')))
notas.append(float(input('Digite a nota 2° do aluno: ')))
nome.append(notas[:])
lista.append(nome[:])
print(f'aluno: {nome[1][1]}')'''