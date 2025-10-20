'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a
altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite sua altura em Kg: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f}. Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.1f}. Você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.1f}. Você tem sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é {imc:.1f}. Você tem obesidade.')
else:
    print(f'Seu imc é {imc:.1f}. Você tem obesidade mórbida.')