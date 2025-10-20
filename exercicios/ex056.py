'''
Exercício Python 56: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, mostre: a
média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
'''

media = 0
idade_velho = 0
homem_velho = ''
qtd_mulheres = 0
for i in range(4):
    print('-='*20)
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).upper().strip()
    print('-='*20, '\n')
    media += idade
    if idade_velho < idade and sexo == 'M':
        idade_velho = idade
        homem_velho = nome
    if idade < 20 and sexo == 'F':
        qtd_mulheres += 1
media /= 4
print(f'A média de idade é {media:.1f} anos.\nO homem mais velho é {homem_velho}, com a idade {idade_velho} anos.\nA quantidade de mulheres menores de 20 anos é {qtd_mulheres}.')