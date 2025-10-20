'''
Exercício Python 44: Elabore um programa que calcule o valor a
ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
'''

preco = float(input('Digite o preço do produto: R$'))
print('='*40)
print('QUAL A FORMA DE PAGAMENTO')
escolha = input('Dinheiro ou cheque\nNo cartão\nNo cartão 2x\nNo cartão 3x ou mais\nEscolha: ').lower()
print('='*40)

if escolha == 'cheque' or escolha == 'dinheiro':
    print(f'Preço normal: R${preco:.2f}\nCom desconto de 10%: R${preco - preco * 0.1:.2f}')
elif escolha == 'cartão' or escolha == 'cartao':
    print(f'Preço normal: R${preco:.2f}\nCom desconto de 5%: R${preco - preco * 0.05:.2f}')
elif escolha == 'cartão 2x' or escolha == 'cartao 2x':
    print(f'Preço normal: R${preco:.2f}\nCom 2x no cartão: R${preco / 2:.2f}')
elif escolha == 'cartão 3x' or escolha == 'cartao 3x':
    print(f'Preço normal: R${preco:.2f}\nCom juros de 20%: R${preco + preco * 0.2:.2f}')