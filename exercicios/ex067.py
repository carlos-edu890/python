'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo
'''

while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n >= 0:
        i = 1
        while i <= 10:
            print(f'{n} x {i:2} = {n * i}')
            i += 1
        i = 1
    else:
        break
print('O PROGRAMA FOI ENCERRADO. VOLTE SEMPRE!')