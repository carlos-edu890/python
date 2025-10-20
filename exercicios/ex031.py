'''
Exercício Python 31: Desenvolva um programa que pergunta a distância da uma
viagem em Km. Calcula o preço da passagem cobrando R$0.50 por Km
para viagens de até 200Km e R$0.45 para viagens mais longas.
'''

distancia = int(input('Distância da viagem: '))
if distancia <= 200:
    print(f'O preço da passagem é R${distancia*0.50:.2f}.')
else:
    print(f'O preço da passagem é R${distancia*0.45:.2f}.')