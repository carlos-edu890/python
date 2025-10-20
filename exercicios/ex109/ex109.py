'''
Exercício Python 109: Modifique as funções que form criadas
no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''

import moeda

p = float(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'Aumentando 15%, temos: {moeda.aumentar(p, 15, True)}')
print(f'Diminuindo 20%, temos: {moeda.diminuir(p, 20)}')