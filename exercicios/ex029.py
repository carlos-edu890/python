'''
Exercício Python 29: Escrava um programa que leia a velocidade de um carro.
Sa ela ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
'''

velocidade = int(input('Digite a velocidade em Km/h: '))
if velocidade > 80:
    print(f'Você foi multado em R${float((velocidade - 80)*7):.2f}')
else:
    print('Pode passar. Tome cuidado!')